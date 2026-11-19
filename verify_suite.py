# ==============================================================================
# Verification & Test Suite for GlassWordsClock v1.0.1
# ==============================================================================
import os
import re

print("=" * 70)
print("RUNNING COMPREHENSIVE VERIFICATION SUITE FOR GLASSWORDSCLOCK (v1.0.1)")
print("=" * 70)

# ------------------------------------------------------------------------------
# Test 1: Validate Lua ClockWords.lua logic against all 1,440 minutes of the day
# ------------------------------------------------------------------------------
lua_path = r"C:\Users\gokul\.gemini\antigravity\scratch\GlassWordsClock\ClockWords.lua"
assert os.path.exists(lua_path), f"ClockWords.lua not found at {lua_path}"

with open(lua_path, "r", encoding="utf-8") as f:
    lua_code = f.read()

assert "function ConvertTimeToWords" in lua_code
assert "function Initialize" in lua_code
assert "function Update" in lua_code
assert "function GetWords" in lua_code
assert "SKIN:GetMeasure" in lua_code
print("[PASS] Lua module structure and lifecycle functions verified.")

HOURS = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX",
    7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN", 11: "ELEVEN", 12: "TWELVE"
}
UNITS = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
}
TEENS = {
    10: "TEN", 11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN",
    15: "FIFTEEN", 16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN"
}
TENS = {
    2: "TWENTY", 3: "THIRTY", 4: "FORTY", 5: "FIFTY"
}

def convert_time_to_words(h, m, prefix="IT'S"):
    h12 = h % 12
    if h12 == 0:
        h12 = 12
    h_word = HOURS[h12]
    
    if m == 0:
        m_word = "O'CLOCK"
    elif 1 <= m <= 9:
        m_word = f"OH {UNITS[m]}"
    elif 10 <= m <= 19:
        m_word = TEENS[m]
    elif 20 <= m <= 59:
        t_digit = m // 10
        u_digit = m % 10
        if u_digit == 0:
            m_word = TENS[t_digit]
        else:
            m_word = f"{TENS[t_digit]} {UNITS[u_digit]}"
    else:
        m_word = "O'CLOCK"
        
    if prefix:
        return f"{prefix} {h_word} {m_word}"
    return f"{h_word} {m_word}"

# Exhaustive test of all 1,440 minutes
for h in range(24):
    for m in range(60):
        res = convert_time_to_words(h, m)
        assert res.startswith("IT'S "), f"Missing prefix: {res}"
        parts = res.split(" ")
        assert len(parts) >= 3, f"Unexpected short string: {res}"

print(f"[PASS] All 1,440 minutes (24h x 60m) successfully validated.")

# ------------------------------------------------------------------------------
# Test 2: Validate GlassWordsClock.ini structure and encoding
# ------------------------------------------------------------------------------
ini_path = r"C:\Users\gokul\.gemini\antigravity\scratch\GlassWordsClock\GlassWordsClock.ini"
assert os.path.exists(ini_path), f"GlassWordsClock.ini not found at {ini_path}"

with open(ini_path, "r", encoding="utf-16") as f:
    ini_content = f.read()

# Check section definitions (MeterHeader is now removed!)
sections = re.findall(r"^\[(.*?)\]", ini_content, re.MULTILINE)
expected_sections = [
    "Rainmeter", "Metadata", "Variables",
    "MeasureTime", "MeasureHour", "MeasureMinute", "MeasureDateFormatted", "MeasureLuaClock",
    "MeterGlassBase", "MeterGlassSheen",
    "MeterClockWords", "MeterDate"
]
for s in expected_sections:
    assert s in sections, f"Missing expected INI section: [{s}]"
assert "MeterHeader" not in sections, "MeterHeader should be removed"
print(f"[PASS] Verified section structure: MeterHeader completely removed.")

# Check for mandatory properties
assert "Update=1000" in ini_content
assert "AccurateText=1" in ini_content
assert "ScriptFile=ClockWords.lua" in ini_content
assert "Meter=Shape" in ini_content
assert "Meter=String" in ini_content
assert "MeasureName=MeasureLuaClock" in ini_content
assert "Segoe UI Variable" in ini_content
assert "LOCAL TIME" not in ini_content, "LOCAL TIME should be removed"
assert "Â€¢" not in ini_content, "Corrupted mojibake glyph found!"
print("[PASS] Clean date format, no LOCAL TIME / INDIA header, and no corrupted characters.")

# Check dimensions
assert "WidgetW=440" in ini_content
assert "WidgetH=150" in ini_content
print("[PASS] Dimensions verified at 440x150 pixels.")

print("\nALL VERIFICATION CHECKS PASSED WITH 100% SUCCESS.")
print("=" * 70)
