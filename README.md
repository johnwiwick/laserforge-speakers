# LaserForge Speaker Catalog

John Wick Studio's editable driver data and browser parts guide for LaserForge.

**[Parts guide](https://johnwiwick.github.io/laserforge-speakers/) · [No-code model editor](https://johnwiwick.github.io/laserforge-speakers/editor.html)**

## Update without programming

1. Open the model editor, select a model, and edit the labeled form.
2. Keep changes and download the catalog update ZIP.
3. On GitHub choose **Add file → Upload files**, unzip the downloaded update, drop in its three files (`models.csv`, `catalog.json`, `app-catalog.json`), and commit.
4. Wait for GitHub Pages to finish rebuilding (usually about a minute). The browser form and desktop importer both validate the data.
5. In LaserForge click **Update supported models**. Existing projects preserve their selected specification snapshots; reselect a model to use a revised record. A corrected mounting dimension blocks new cuts until the model is reselected and fit checked. Older remote/cache revisions cannot silently replace newer bundled data.

For developer-managed bulk edits you can also open `models.csv` in Numbers or Excel, edit cells, export CSV, and run `python3 scripts/build.py` before uploading the generated JSON files. The browser editor is the programming-free path. Do not rename the columns. Numeric fields use the units in the browser form. Upload illustrations and dimension drawings into `assets/` before enabling a new model. Use original source links for manufacturer photographs and PDFs if redistribution permission is uncertain. Saved SVG images are original schematic illustrations. All six original manufacturer PDF specification/dimension sheets and their PNG previews are also preserved in assets/; source-document hashes are recorded in source-documents.json. Product photographs remain linked to their manufacturer source.

## Data quality

- Six exact models have manufacturer T/S parameters and physical reference dimensions. Good/Better/Best are budget tiers within full-range and subwoofer use, not measured listening rankings.
- No design is physically tested yet. `tested` remains false; a complete, measured speaker design needs its own documented build revision, not a driver-level checkbox.
- `displacement` is an explicitly estimated solid driver allowance. Published swept volume Vd is NOT occupied cabinet volume. Confirm the actual driver and fit template before production.
- DCS165-4 uses drawing dimensions 167/143/89.3 mm because the product-page inch dimensions disagree. PS95-8 uses the drawing's 98.2 mm flange envelope and a 77.5 mm nominal cutout from Parts Express's 3.05 inch specification. The manufacturer product page erroneously lists the magnet diameter (69.8 mm) as cutout and the basket diameter (76.8 mm) as outside flange. A fit template remains mandatory.
- Manufacturer sealed/vented volume guidance is recorded where available. PS95 sealed 1.5 L and DCS165 sealed 3.636 L / vented 10 L are authored model targets. Port tunings are authored starting alignments, not claimed manufacturer-approved complete systems. Bandpass uses generated 1.25× sealed rear and 1.2× rear front air targets and checks physical clearance. A gasketed FRONT service cover carries the port; its structural front-frame window air volume is included. The driver is serviced from its front flange. Slot end correction is approximate. All require prototype measurements.
- RMS rating is a thermal limit, not a safe low-frequency power setting. The app models excursion and port speed at a specified voltage-equivalent input and assumed high-pass filter.

## Files

- `models.csv`: owner-editable source of truth.
- `scripts/build.py`: developer bulk-edit validator; validates source and creates the guide/desktop JSON files.
- `catalog.json`: browser guide including Amazon destinations, forced to `johnwickstu04-20`.
- `app-catalog.json`: desktop technical data; no Amazon links or Associate tag.
- `assets/`: saved original illustrations and dimensional reference SVGs.
- `research/source-links.json`: preserved original 32 supplied links, expanded identities and tagged destinations; these are unreviewed, not supported models.

Five exact Amazon listing identities have been verified directly. PS220-8 and RSS210HF-4 showed Currently unavailable on October 21, 2026. DCS205-4 retains an exact-model search because no matching listing was verified. Never substitute a guessed ASIN. MSRP is a dated manufacturer reference, never presented as an Amazon price. Replace a search with a verified exact-variant Amazon product URL in the form when available; the build enforces the owner's tag.

## Future John Wick Studio speaker line

Protected original complete speaker designs, measured responses, approved customization bounds, revisioned production files, and direct-to-consumer store links will live separately from third-party driver records. Do not publish protected production files, license signing keys, customer data or proprietary crossovers into this public catalog. This repository holds public model specifications and the guide only.

## Sources and rights

Each record retains manufacturer product, specification/drawing PDF and product-photo references, checked October 21, 2026. Manufacturer content remains the manufacturer's property. Original schematic SVGs may be used with LaserForge. They are explicitly labeled reference illustrations, not photographs or screw-drilling templates.

As an Amazon Associate, John Wick Studio earns from qualifying purchases. Add the published guide URL to your Associates account's approved website list before using it commercially. The guide is substantive model information and requires a deliberate user click to visit Amazon; it is not an automatic redirect. The desktop app opens only the guide.

Automatic CSV-only regeneration is prepared in `scripts/examples/catalog-workflow.yml` but not enabled: the current GitHub OAuth login does not have workflow scope. Normal owner updates use the validated browser bundle and need no additional permission.
