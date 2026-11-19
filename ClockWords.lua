-- ==============================================================================
-- Apple Liquid Glass Desktop Clock for Rainmeter
-- File: ClockWords.lua
-- Description: Dynamic 12-hour local time to English words conversion engine.
-- Architecture: High-performance Lua 5.1 module for Rainmeter DirectWrite rendering.
-- ==============================================================================

local measureHour = nil
local measureMinute = nil

-- Word mapping dictionaries
local HOURS = {
    [1]  = "ONE",
    [2]  = "TWO",
    [3]  = "THREE",
    [4]  = "FOUR",
    [5]  = "FIVE",
    [6]  = "SIX",
    [7]  = "SEVEN",
    [8]  = "EIGHT",
    [9]  = "NINE",
    [10] = "TEN",
    [11] = "ELEVEN",
    [12] = "TWELVE"
}

local UNITS = {
    [1] = "ONE",
    [2] = "TWO",
    [3] = "THREE",
    [4] = "FOUR",
    [5] = "FIVE",
    [6] = "SIX",
    [7] = "SEVEN",
    [8] = "EIGHT",
    [9] = "NINE"
}

local TEENS = {
    [10] = "TEN",
    [11] = "ELEVEN",
    [12] = "TWELVE",
    [13] = "THIRTEEN",
    [14] = "FOURTEEN",
    [15] = "FIFTEEN",
    [16] = "SIXTEEN",
    [17] = "SEVENTEEN",
    [18] = "EIGHTEEN",
    [19] = "NINETEEN"
}

local TENS = {
    [2] = "TWENTY",
    [3] = "THIRTY",
    [4] = "FORTY",
    [5] = "FIFTY"
}

--- Converts a 24-hour hour (0..23) and minute (0..59) into English word display.
-- @param h number: Hour (0 to 23)
-- @param m number: Minute (0 to 59)
-- @param prefix string (optional): Defaults to "IT'S"
-- @return string: Formatted uppercase words e.g. "IT'S ELEVEN FOURTEEN"
function ConvertTimeToWords(h, m, prefix)
    prefix = prefix or "IT'S"

    -- Sanitize input to integers
    h = math.floor(tonumber(h) or 0)
    m = math.floor(tonumber(m) or 0)

    -- Normalize hour to 12-hour format:
    -- 0 (midnight) -> 12, 12 (noon) -> 12, 13 -> 1, 23 -> 11
    local h12 = h % 12
    if h12 == 0 then
        h12 = 12
    end

    local hWord = HOURS[h12] or "TWELVE"

    -- Convert minutes to natural English words
    local mWord = ""
    if m == 0 then
        mWord = "O'CLOCK"
    elseif m >= 1 and m <= 9 then
        mWord = "OH " .. (UNITS[m] or "")
    elseif m >= 10 and m <= 19 then
        mWord = TEENS[m] or ""
    elseif m >= 20 and m <= 59 then
        local tensDigit = math.floor(m / 10)
        local unitDigit = m % 10
        local tensWord = TENS[tensDigit] or ""

        if unitDigit == 0 then
            mWord = tensWord
        else
            mWord = tensWord .. " " .. (UNITS[unitDigit] or "")
        end
    else
        -- Fallback safety for out-of-range minutes
        mWord = "O'CLOCK"
    end

    -- Combine into centerpiece string
    if prefix and prefix ~= "" then
        return prefix .. " " .. hWord .. " " .. mWord
    else
        return hWord .. " " .. mWord
    end
end

--- Rainmeter standard lifecycle: called once when the measure initializes.
function Initialize()
    measureHour = SKIN:GetMeasure("MeasureHour")
    measureMinute = SKIN:GetMeasure("MeasureMinute")
end

--- Rainmeter standard lifecycle: called on each update cycle of the measure.
-- @return string: The text value for the meter bound to this measure.
function Update()
    local h, m

    -- Query Rainmeter time measures first
    if measureHour and measureMinute then
        local rawH = measureHour:GetValue()
        local rawM = measureMinute:GetValue()
        if rawH and rawM and rawH >= 0 and rawM >= 0 then
            h = math.floor(rawH)
            m = math.floor(rawM)
        end
    end

    -- Resilient fallback: use system clock if Rainmeter measures are unready
    if not h or not m then
        local sysTime = os.date("*t")
        h = sysTime.hour
        m = sysTime.min
    end

    -- Retrieve optional prefix variable from skin (defaults to "IT'S")
    local prefix = SKIN:GetVariable("Prefix", "IT'S")

    return ConvertTimeToWords(h, m, prefix)
end

--- Public helper to query time conversion for custom/test values.
-- Useful for debugging or custom external calls: [!CommandMeasure MeasureLuaClock "GetWords(11, 14)"]
function GetWords(h, m, customPrefix)
    return ConvertTimeToWords(h, m, customPrefix or "IT'S")
end
