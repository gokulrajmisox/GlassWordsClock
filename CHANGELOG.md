# Changelog

All notable changes to the **Apple Liquid Glass Desktop Clock for Rainmeter** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1] - 2026-11-19

### Changed
- **Removed Top Eyebrow Header:** Completely removed `LOCAL TIME / INDIA` and `[MeterHeader]` for a significantly cleaner, ultra-minimalist layout.
- **Fixed Date Separator Mojibake Encoding:**
  - Removed corrupted ANSI glyph `Â€¢` caused by non-BOM UTF-8 interpretation.
  - Converted date format to clean, standard English: `THURSDAY, 19 NOVEMBER`.
  - Added configurable `#DateFormat#` variable supporting comma (`%A, %#d %B`) or space-only (`%A %#d %B`).
  - Saved `GlassWordsClock.ini` as native **UTF-16 LE with BOM**, ensuring zero encoding artifacts across all Windows language locales.
- **Refined Vertical Geometry:**
  - Tuned height to `150px` for optimal vertical proportions.
  - Centered centerpiece words (`Y=44`) with increased font size (`21pt`).
  - Re-anchored subtle hairline separator (`Y=94`) and date subtitle (`Y=105`).

---

## [1.0.0] - 2026-11-19

### Added
- Initial production release of Apple Liquid Glass Desktop Clock.
