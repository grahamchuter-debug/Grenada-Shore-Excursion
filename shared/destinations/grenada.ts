/**
 * Grenada destination booking core.
 * Product catalogue: shared/destinations/grenada-products.ts
 * Public editorial: scripts/build-grenada-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const grenadaBookingCore = {
  id: "grenada",
  siteName: "Grenada Shore Excursions",
  siteHostname: "grenadashoreexcursion.com",
  siteUrl: "https://grenadashoreexcursion.com",
  bookingEmail: "hello@grenadashoreexcursion.com",
  originatingSite: "grenadashoreexcursion.com",
  originatingPort: "St George's, Grenada",
  bookingRefPrefix: "W2GRD",
  sessionKeyPrefix: "w2-grd-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Grenada schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "grenada",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
