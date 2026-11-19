# Apple Liquid Glass Desktop Clock for Rainmeter

A sophisticated, minimalist Apple Liquid Glass desktop word clock designed specifically for **Windows 11** and **Rainmeter 4.5+**.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    IT'S ELEVEN FIFTY TWO                    │
│                                                             │
│                    THURSDAY, 19 NOVEMBER                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Overview & Visual Design

The **Apple Liquid Glass Desktop Clock** brings the frosted glass, optical refraction, and typographic elegance of Apple macOS widgets to Windows 11 with pure minimalism.

### Key Visual Characteristics

* **Translucent Frosted-Glass Substrate:** Multi-layer tinted glass backplate (`rgba(24, 28, 38, 195)` to `rgba(12, 14, 20, 225)`) that naturally samples and diffuses background desktop wallpapers while maintaining contrast.
* **3D Prismatic Rim (Bevel):** An angled linear gradient stroke (`135°` light vector) with a luminous top-left specular rim (`rgba(255, 255, 255, 155)`) and dark grounded bottom-right edge.
* **Secondary Inset Reflection:** A 1px inset refraction bevel creating the signature double-surface reflection found on physical curved glass hardware.
* **Convex Specular Highlight (Liquid Sheen):** A subtle, curved light sheen across the upper 40% of the widget that gently intensifies upon cursor hover.
* **Layered Ambient Contact Shadow:** Multi-step diffuse shadow layers beneath the widget, floating the glass cleanly above light or dark wallpapers without GPU blur plugins.
* **Windows 11 Native Typography:** DirectWrite rendering with subpixel anti-aliasing using the **Segoe UI Variable** font family (`Display` and `Text`). Saved with UTF-16LE Unicode for zero character corruption.

---

## 2. Clock Functionality

The widget converts Windows local system time into English words dynamically:

| Actual Time | Display Output | Description |
|---|---|---|
| `11:14` | `IT'S ELEVEN FOURTEEN` | Standard hour and minute |
| `11:05` | `IT'S ELEVEN OH FIVE` | Single-digit minute with "OH" |
| `11:00` | `IT'S ELEVEN O'CLOCK` | Exact hour mark |
| `12:30` | `IT'S TWELVE THIRTY` | Noon/midnight 12-hour formatting |
| `01:45` | `IT'S ONE FORTY FIVE` | Standard compound tens and units |
| `09:09` | `IT'S NINE OH NINE` | Compound single-digit format |
| `00:00` | `IT'S TWELVE O'CLOCK` | Midnight 12-hour conversion |
| `12:00` | `IT'S TWELVE O'CLOCK` | Noon 12-hour conversion |

### Technical Highlights

* **100% Native:** Built purely with native Rainmeter Shape meters, String meters, Time measures, and standard embedded Lua 5.1.
* **Zero External Plugins:** No third-party DLLs, no external dependencies, no paid tools.
* **Zero Internet / Network Overhead:** 100% offline, local Windows time execution.
* **Ultra-Low CPU Usage:** Updates on a strict 1-second cadence (`Update=1000`) with lightweight arithmetic mapping. Consumes `< 0.05%` CPU.

---

## 3. Widget Layout & Dimensions

* **Dimensions:** `440 × 150` pixels.
* **Default Position:** Top-right corner of the primary display with a `30px` margin from screen edges (`X = #SCREENAREAWIDTH# - 470`, `Y = 30`).
* **Interaction:** Draggable anywhere on the desktop. Rainmeter automatically saves and remembers your custom position.

### Visual Hierarchy

1. **Centerpiece:** `IT'S ELEVEN FIFTY TWO`  
   * Font: *Segoe UI Variable Display*, 21pt, Bold, crisp white (`rgba(255, 255, 255, 248)`) with soft optical drop shadow.
2. **Hairline Separator:** Subtle centered glass groove with bidirectional alpha fade.
3. **Bottom Subtitle:** `THURSDAY, 19 NOVEMBER`  
   * Font: *Segoe UI Variable Text*, 10.5pt, Semibold/Bold, uppercase (`rgba(255, 255, 255, 175)`).

---

## 4. Project Structure

```
GlassWordsClock/
├── GlassWordsClock.ini    # Rainmeter skin definition, shape styling, DirectWrite meters (UTF-16 LE)
├── ClockWords.lua         # Standalone Lua 5.1 dynamic time-to-words engine
├── README.md              # Documentation, setup guide, and technical reference
├── CHANGELOG.md           # Version release history and updates
├── GlassWordsClock.zip    # Portable ZIP distribution archive
├── GlassWordsClock.rmskin # One-click Rainmeter skin installer
└── verify_suite.py        # Automated test suite verifying all 1,440 day minutes
```

---

## 5. Customization & Date Formatting

To personalize the skin, right-click the widget on your desktop and select **Edit Configuration**:

```ini
[Variables]
; Date formatting options:
;   DateFormat=%A, %#d %B   ->  THURSDAY, 19 NOVEMBER (Standard comma)
;   DateFormat=%A %#d %B    ->  THURSDAY 19 NOVEMBER  (Space only)
DateFormat=%A, %#d %B

; Change the centerpiece prefix (or set to empty: Prefix=)
Prefix=IT'S

; Adjust typography sizes
FontSizeCenter=21
FontSizeBottom=10.5

; Adjust glass corner radius (default 26px)
CornerR=26
```

After modifying variables, save the file, right-click the widget, and choose **Refresh Clock**.
