/**
 * Shared booking engine tests — Grenada Phase 16D (Grenada's Spice Route only).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  GRENADA_BOOKABLE_PRODUCTS,
  GRENADA_CANCELLATION_COPY,
  findGrenadaBookingProduct,
} from "../destinations/grenada-products";
import { grenadaBookingCore } from "../destinations/grenada";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(grenadaBookingCore);
const spice = findGrenadaBookingProduct("grenadas-spice-route");
assert.ok(spice);

test("single Grenada product ID present", () => {
  assert.equal(GRENADA_BOOKABLE_PRODUCTS.length, 1);
  assert.equal(GRENADA_BOOKABLE_PRODUCTS[0]!.id, "grenadas-spice-route");
});

test("spice route paying guest 89; ages 0-2 not sold; no child discount", () => {
  assert.equal(spice!.pricing.adultAmount, 89);
  assert.equal(spice!.pricing.childAmount, null);
  assert.equal(spice!.pricing.childPricingStatus, "not_sold");
  assert.equal(spice!.pricing.infantAmount, null);
  assert.equal(spice!.pricing.infantPricingStatus, "not_sold");
  assert.equal(calculateBookingQuote(spice!, { adults: 1, children: 0, infants: 0 }).amountCents, 8900);
  assert.equal(calculateBookingQuote(spice!, { adults: 2, children: 0, infants: 0 }).amountCents, 17800);
  assert.throws(() => calculateBookingQuote(spice!, { adults: 1, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(spice!, { adults: 1, children: 1, infants: 0 }));
  assert.throws(() => calculateBookingQuote(spice!, { adults: 0, children: 0, infants: 0 }));
});

test("max 10 guests; 11 rejected; infants rejected (not sold)", () => {
  assert.equal(spice!.capacity.maxGuestsPerBooking, 10);
  assert.doesNotThrow(() => calculateBookingQuote(spice!, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(spice!, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(spice!, { adults: 9, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(spice!, { adults: -1, children: 0, infants: 0 }));
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(spice!, { adults: 1, children: 0, infants: 0 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 8900));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Grenada W2GRD prefix", () => {
  assert.match(createBookingReference(grenadaBookingCore), /^W2GRD-/);
  assert.equal(grenadaBookingCore.bookingRefPrefix, "W2GRD");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(GRENADA_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(GRENADA_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(GRENADA_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(GRENADA_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: spice!,
    reference: "W2GRD-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $89.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|cagrmsspctor|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: spice!,
    reference: "W2GRD-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $89.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    destinationLabel: "Grenada Shore Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /cagrmsspctor|SEG_MANUAL/i);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findGrenadaBookingProduct("classic-beach-day"), null);
  assert.equal(findGrenadaBookingProduct("belize-cave-tubing"), null);
  assert.equal(findGrenadaBookingProduct("highlights-and-beach-break"), null);
  assert.equal(findGrenadaBookingProduct("soufriere-volcano-waterfalls-tour"), null);
});
