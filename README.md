# LaserForge Speaker Catalog

John Wick Studio's editable driver data and browser parts guide for LaserForge.

**[Parts guide](https://johnwiwick.github.io/laserforge-speakers/) · [No-code model editor](https://johnwiwick.github.io/laserforge-speakers/editor.html)**

## Update without programming

1. Open the model editor, select a model, and edit the labeled form.
2. Keep changes and download `models.csv`.
3. On GitHub choose **Add file → Upload files**, drop in `models.csv`, and commit.
4. Wait for **Actions → Validate catalog and publish guide** to finish green.
5. In LaserForge click **Update supported models**. Existing projects preserve their selected specification snapshots; reselect a model to use a revised record.

You can also open `models.csv` in Numbers or Excel, edit cells, and export CSV. Do not rename the columns. Numeric fields use the units in the browser form. Upload illustrations and dimension drawings into `assets/` before enabling a new model. Use original source links for manufacturer photographs and PDFs if redistribution permission is uncertain. Current saved SVG images are original schematic illustrations, not manufacturer photos or complete mounting drawings.

## Data quality

- Six exact models have manufacturer T/S parameters and physical reference dimensions. Good/Better/Best are budget tiers within full-range and subwoofer use, not measured listening rankings.
- No design is physically tested yet. `tested` remains false; a complete, measured speaker design needs its own documented build revision, not a driver-level checkbox.
- `displacement` is an explicitly estimated solid driver allowance. Published swept volume Vd is NOT occupied cabinet volume. Confirm the actual driver and fit template before production.
- DCS165-4 uses drawing dimensions 167/143/89.3 mm because the product-page inch dimensions disagree. PS95-8 reserves a conservative 100 mm flange envelope for its square mounting ears; the product page's 76.8 mm diameter alone is not a complete flange envelope.
- Manufacturer sealed/vented volume guidance is recorded where available. PS95 sealed 1.5 L and DCS165 sealed 3.636 L / vented 10 L are authored model targets. Port tunings are authored starting alignments, not claimed manufacturer-approved complete systems. Bandpass uses generated 1.25× sealed rear and 1.2× rear front air targets and checks physical clearance. Slot end correction is approximate. All require prototype measurements.
- RMS rating is a thermal limit, not a safe low-frequency power setting. The app models excursion and port speed at a specified voltage-equivalent input and assumed high-pass filter.

## Files

- `models.csv`: owner-editable source of truth.
- `scripts/build.py`: validates source and creates the guide/desktop JSON files.
- `catalog.json`: browser guide including Amazon destinations, forced to `johnwickstu04-20`.
- `app-catalog.json`: desktop technical data; no Amazon links or Associate tag.
- `assets/`: saved original illustrations and dimensional reference SVGs.
- `research/source-links.json`: preserved original 32 supplied links, expanded identities and tagged destinations; these are unreviewed, not supported models.

The initial Amazon destinations use exact-model searches because direct listing identities, live prices and stock could not be verified. Never substitute a guessed ASIN. MSRP is a dated manufacturer reference, never presented as an Amazon price. Replace a search with a verified exact-variant Amazon product URL in the form when available; the build enforces the owner's tag.

## Future John Wick Studio speaker line

Protected original complete speaker designs, measured responses, approved customization bounds, revisioned production files, and direct-to-consumer store links will live separately from third-party driver records. Do not publish protected production files, license signing keys, customer data or proprietary crossovers into this public catalog. This repository holds public model specifications and the guide only.

## Sources and rights

Each record retains manufacturer product, specification/drawing PDF and product-photo references, checked October 21, 2026. Manufacturer content remains the manufacturer's property. Original schematic SVGs may be used with LaserForge. They are explicitly labeled reference illustrations, not photographs or screw-drilling templates.

As an Amazon Associate, John Wick Studio earns from qualifying purchases. Add the published guide URL to your Associates account's approved website list before using it commercially. The guide is substantive model information and requires a deliberate user click to visit Amazon; it is not an automatic redirect. The desktop app opens only the guide.
