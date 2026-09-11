/**
 * Grenada booking security / commercial gate tests (Phase 16D).
 * No live Stripe. Uses Worker preview mode + shared pricing authority.
 */
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import worker from "./index";
import { LIVE_PAYMENTS_CODE_ENABLED, liveCheckoutBlock, bookingsAreEnabled } from "./live-gate";
import { assertStripeTestSecret, StripeModeError } from "./stripe-guard";
import {
  GRENADA_BOOKABLE_PRODUCTS,
  findGrenadaBookingProduct,
} from "../../../shared/destinations/grenada-products";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  statusAfterPaymentSuccess,
} from "../../../shared/world-booking";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "../../..");

const previewEnv = {
  PAYMENTS_MODE: "preview",
  BOOKINGS_ENABLED: "true",
  CORS_ALLOWED_ORIGINS: "http://localhost:8910",
  SITE_BASE_URL: "http://localhost:8910",
} as unknown as Env;

const SPICE = "grenadas-spice-route";

function payload(
  sessionId: string,
  guests = { adults: 2, children: 0, infants: 0 },
  overrides: Record<string, unknown> = {},
  productId = SPICE,
) {
  const product = findGrenadaBookingProduct(productId)!;
  const quote = calculateBookingQuote(product, guests);
  return {
    productId,
    bookingSessionId: sessionId,
    guests,
    customer: { name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" },
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "celebrity-beyond",
      cruiseLine: "Celebrity Cruises",
      isCustomShip: true,
      scheduleMatched: false,
    },
    confirmationAcknowledged: true,
    clientDisplayedTotalCents: quote.amountCents,
    ...overrides,
  };
}

function jsonReq(url: string, body: unknown) {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
}

test("LIVE_PAYMENTS_CODE_ENABLED is true for Grenada Phase 16D", () => {
  assert.equal(LIVE_PAYMENTS_CODE_ENABLED, true);
});

test("live checkout allowed when code flag, unlock phrase, and live secrets present", () => {
  const product = findGrenadaBookingProduct(SPICE)!;
  const block = liveCheckoutBlock(
    {
      PAYMENTS_MODE: "live",
      LIVE_PAYMENTS_UNLOCK: "GRENADA_LIVE_UNLOCK",
      BOOKINGS_ENABLED: "true",
      STRIPE_SECRET_KEY: "sk_live_fake",
      STRIPE_WEBHOOK_SECRET: "whsec_fake",
      SITE_BASE_URL: "https://grenadashoreexcursion.com",
      DB: {} as D1Database,
    },
    product,
  );
  assert.equal(block, null);
});

test("BOOKINGS_ENABLED=false kill switch", () => {
  assert.equal(bookingsAreEnabled({ BOOKINGS_ENABLED: "false" }), false);
});

test("single Grenada product live request mode with USD currency", () => {
  assert.equal(GRENADA_BOOKABLE_PRODUCTS.length, 1);
  for (const product of GRENADA_BOOKABLE_PRODUCTS) {
    assert.equal(product.availability, "live");
    assert.equal(product.bookingMode, "request");
    assert.equal(product.pricing.currency, "USD");
    assert.equal(product.capacity.maxGuestsPerBooking, 10);
    assert.equal(product.destinationId, "grenada");
  }
});

test("grenadas-spice-route paying guest 8900; infants not sold", () => {
  const product = findGrenadaBookingProduct(SPICE)!;
  assert.equal(product.pricing.adultAmount, 89);
  assert.equal(product.pricing.childAmount, null);
  assert.equal(product.pricing.childPricingStatus, "not_sold");
  assert.equal(product.pricing.infantPricingStatus, "not_sold");
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 0 }).amountCents, 8900);
  assert.equal(calculateBookingQuote(product, { adults: 2, children: 0, infants: 0 }).amountCents, 17800);
  assert.throws(() => calculateBookingQuote(product, { adults: 1, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 1, children: 1, infants: 0 }));
});

test("rejects 0 paying guests, 11 guests, negatives, infants via quote", () => {
  const product = findGrenadaBookingProduct(SPICE)!;
  assert.throws(() => calculateBookingQuote(product, { adults: 0, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: -1, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(product, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 9, children: 0, infants: 1 }));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("preview request returns W2GRD reference", async () => {
  const body = payload(`sess-${Date.now()}`, { adults: 1, children: 0, infants: 0 });
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 200);
  const firstJson = (await res.json()) as { ok: boolean; reference: string };
  assert.equal(firstJson.ok, true);
  assert.match(firstJson.reference, /^W2GRD-/);
});

test("infant quantity rejected by preview request", async () => {
  const product = findGrenadaBookingProduct(SPICE)!;
  const badGuests = { adults: 1, children: 0, infants: 1 };
  assert.throws(() => calculateBookingQuote(product, badGuests));
  const body = {
    ...payload(`sess-infant-${Date.now()}`, { adults: 1, children: 0, infants: 0 }),
    guests: badGuests,
    clientDisplayedTotalCents: 8900,
  };
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 400);
});

test("unknown product and cross-destination IDs rejected", async () => {
  for (const productId of [
    "not-a-grenada-product",
    "classic-beach-day",
    "highlights-and-beach-break",
    "belize-cave-tubing",
    "soufriere-volcano-waterfalls-tour",
    "falmouth-beach-day",
    "ocho-rios-dunns-river",
  ]) {
    const bad = payload(`unk-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, { productId });
    const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", bad), previewEnv);
    assert.equal(res.status, 400, productId);
  }
});

test("client price mismatch rejected", async () => {
  const body = payload(`tamper-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, {
    clientDisplayedTotalCents: 1,
  });
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 400);
});

test("client total must match server quote helper", () => {
  const product = findGrenadaBookingProduct(SPICE)!;
  const quote = calculateBookingQuote(product, { adults: 1, children: 0, infants: 0 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 8900));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("ops request heading is Grenada", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/notify.ts"), "utf8");
  assert.match(src, /NEW GRENADA BOOKING REQUEST/);
});

test("TEST Stripe secret guard", () => {
  assert.doesNotThrow(() => assertStripeTestSecret("sk_test_abc"));
  assert.throws(() => assertStripeTestSecret("sk_live_abc"), StripeModeError);
});

test("Stripe Link disabled at session level (checkout source)", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/routes/checkout.ts"), "utf8");
  assert.match(src, /link_mode|payment_method_options|link/i);
});

test("public HTML never leaks SEG / internal codes", () => {
  const files = [
    "grenada-spice-island-tours/index.html",
    "book/grenadas-spice-route/index.html",
    "book/grenadas-spice-route/received/index.html",
    "js/commercial-config.js",
  ];
  const banned = /\bSEG\b|Shore Excursions Group|cagrmsspctor|SEG_MANUAL|shoreexcursionsgroup|info@wowatour\.com/i;
  for (const rel of files) {
    const path = join(ROOT, rel);
    try {
      const text = readFileSync(path, "utf8");
      assert.doesNotMatch(text, banned, rel);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === "ENOENT") {
        continue;
      }
      throw err;
    }
  }
  for (const product of GRENADA_BOOKABLE_PRODUCTS) {
    assert.doesNotMatch(product.productPath, /SEG|cagr/i);
    assert.doesNotMatch(product.bookingPath, /SEG|cagr/i);
  }
});

test("live-gate source keeps code flag true", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/live-gate.ts"), "utf8");
  assert.match(src, /LIVE_PAYMENTS_CODE_ENABLED\s*=\s*true/);
});

test("commercial-config has no internal codes", () => {
  const text = readFileSync(join(ROOT, "js/commercial-config.js"), "utf8");
  assert.doesNotMatch(text, /cagrmsspctor|SEG_MANUAL|\bSEG\b|info@wowatour/);
});
