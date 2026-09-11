/**
 * Public commercial status for Grenada Shore Excursions (Phase 16D).
 * Internal supply references must never appear on customer pages.
 *
 * Gate values:
 * - PRODUCTION_READY_LOCKED — journey visible; live Pay & request disabled
 * - BOOKING_ENABLED — live checkout allowed (requires Worker LIVE unlock too)
 */
window.GRD_COMMERCIAL = {
  bookingsApiUrl: "https://grenada-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@grenadashoreexcursion.com",
  siteName: "Grenada Shore Excursions",
  defaultPublicBookingStatus: "BOOKING_ENABLED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details. Departure is from the cruise ship pier.",
  overTenGuidance:
    "For groups larger than 10, email hello@grenadashoreexcursion.com before requesting.",
  products: {
    "grenadas-spice-route": {
      productId: "grenadas-spice-route",
      slug: "grenadas-spice-route",
      name: "Grenada's Spice Route",
      shortTitle: "Spice Route",
      productPath: "/grenada-spice-island-tours",
      bookingPath: "/book/grenadas-spice-route",
      receivedPath: "/book/grenadas-spice-route/received",
      adultUsd: 89,
      childUsd: null,
      infantUsd: null,
      guestModel: "ages3_plus_only",
      durationLabel: "4 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Guests (ages 3+) $89 · Ages 0–2 not permitted",
    },
  },
};
