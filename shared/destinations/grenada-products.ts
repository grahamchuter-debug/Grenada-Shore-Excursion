import { grenadaBookingCore } from "./grenada";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle / boat capacity. */
const GRD_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/**
 * Phase 16D Graham-approved:
 * Ages 0–2 NOT PERMITTED (infant band not_sold — reject).
 * Ages 3+ paying guest USD 89 (no invented child discount).
 * Guests under 16 must travel with a responsible adult (customer acknowledgement).
 */
const PAYING_NO_INFANT_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Guests (ages 3+)", minAge: 3, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children", minAge: 3, maxAge: 11, pricingStatus: "not_sold" },
  { id: "infant", label: "Infants (0–2)", minAge: 0, maxAge: 2, pricingStatus: "not_sold" },
];

function payingGuestNoInfantUsd(payingAmount: number): ProductPricing {
  return {
    model: "adult_child",
    currency: "USD",
    adultAmount: payingAmount,
    childAmount: null,
    childPricingStatus: "not_sold",
    infantAmount: null,
    infantPricingStatus: "not_sold",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: cruise ship pier; exact instructions after confirmation.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 guests per booking (Graham online limit — not supplier capacity).",
  "At least one paying guest (ages 3+) required.",
  "Ages 0–2 NOT PERMITTED.",
  "Guests under 16 must travel with a responsible adult in the party.",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const GRENADA_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details. Departure is from the cruise ship pier.",
  overTenGuidance: "For groups larger than 10, email hello@grenadashoreexcursion.com before requesting.",
} as const;

const SPICE_ROUTE: BookableProductConfig = {
  id: "grenadas-spice-route",
  destinationId: grenadaBookingCore.id,
  slug: "grenadas-spice-route",
  name: "Grenada's Spice Route",
  durationLabel: "4 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/grenadas-spice-route",
  receivedPath: "/book/grenadas-spice-route/received",
  confirmedPath: "/book/grenadas-spice-route/received",
  productPath: "/grenada-spice-island-tours",
  pricing: payingGuestNoInfantUsd(89),
  ageBands: PAYING_NO_INFANT_BANDS,
  capacity: GRD_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "grenada",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Paying guest USD 89 (ages 3+) · Ages 0–2 not permitted · require ≥1 paying guest",
    "Concord Falls · Gouyave · traditional spice estate · Grand Etang rainforest / crater lake · mona monkey context",
    "Food and beverages NOT included · optional spice purchases at own cost",
    "Moderate activity · walking over paved, gravel and packed dirt surfaces, many on inclines",
    "Do NOT claim Annandale, Fort George, Fort Frederick, monkey guarantees, or return-to-ship guarantees",
    "Do not invent estate legal name — prefer 'traditional spice estate'",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · cagrmsspctor",
    "INTERNAL CODE: cagrmsspctor",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Paying guest USD 89 (ages 3+) · Ages 0–2 NOT PERMITTED.",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const GRENADA_BOOKABLE_PRODUCTS: readonly BookableProductConfig[] = [SPICE_ROUTE];

export function findGrenadaBookingProduct(productId: string): BookableProductConfig | null {
  return GRENADA_BOOKABLE_PRODUCTS.find((p) => p.id === productId) ?? null;
}

export function listGrenadaBookingProducts(): readonly BookableProductConfig[] {
  return GRENADA_BOOKABLE_PRODUCTS;
}
