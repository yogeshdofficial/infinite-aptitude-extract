# Calendar — Chapter Overview

## What This Chapter Is About

This chapter deals with the mathematical structure of the Gregorian calendar and the cyclical nature of days, weeks, and years. The central quantity that governs all calculations here is the "odd day," which represents the remainder of time after accounting for complete seven-day weeks. By mastering how these odd days accumulate over years and months, you will be able to determine the day of the week for any historical or future date and identify when calendar cycles repeat.

---

## Core Concepts

**[Odd Days]** — This is the fundamental unit of measurement in calendar problems. Since a week always has 7 days, any number of days can be divided by 7; the remainder is the "odd day." For example, 10 days is 1 week and 3 odd days, meaning the day of the week shifts by 3 positions.

**[Leap Year Logic]** — A leap year contains 366 days instead of 365 because of an extra day in February. A year is a leap year if it is divisible by 4, unless it is a century year (like 1900), which must be divisible by 400 to qualify. For example, 2000 is a leap year, but 2100 is not.

**[Yearly Shift]** — Because an ordinary year has 365 days (52 weeks + 1 odd day), the calendar shifts forward by exactly one day each year. In a leap year, the shift is two days. This concept allows us to calculate the day of the week for a date in a future year without counting every single day in between.

**[Century Cycles]** — The calendar repeats its pattern of odd days every 400 years. Because of the leap year rules, 100 years contain 5 odd days, 200 years contain 3, 300 years contain 1, and 400 years contain 0. This cycle is the "anchor" for calculating dates across long spans of time.

---

## Key Terms Glossary

**Ordinary Year** — A year consisting of 365 days, having 1 odd day.

**Leap Year** — A year consisting of 366 days, having 2 odd days.

**Century Year** — A year that is a multiple of 100 (e.g., 1700, 1800, 2000). These are only leap years if they are divisible by 400.

**Odd Day** — The remainder obtained after dividing the total number of days by 7.

---

## Pattern Map

**Calendar Basics** (5 questions) — Focuses on identifying leap years and calculating odd days for small, fixed time intervals.

**Yearly Shift** (6 questions) — Focuses on calculating the change in the day of the week as you move forward or backward across full years.

**Specific Date** (9 questions) — The most comprehensive pattern; requires calculating the total odd days from a reference point (like 0001 AD) to a precise calendar date.

**Calendar Repetition** (3 questions) — Focuses on finding a future year that has the exact same calendar (same days on same dates) as a given year, requiring the Yearly Shift concept.

---

## Core Formulas

### Odd Day Calculation
$$
\text{Odd Days} = \text{Total Days} \pmod{7}
$$

**Variables:**
- $\text{Total Days}$ = The number of days in the period being analyzed.

**When to use:** Whenever you need to convert a large number of days into a manageable shift in the day of the week.

**Key insight:** If the remainder is 0, the day of the week is the same as the starting point.

**Worked example:** 15 days $\div$ 7 = 2 weeks with a remainder of 1. Thus, 15 days = 1 odd day.

### Yearly Shift Calculation
$$
\text{Total Shift} = (\text{Number of Years}) + (\text{Number of Leap Years})
$$

**Variables:**
- $\text{Number of Years}$ = The count of years elapsed.
- $\text{Number of Leap Years}$ = The count of February 29ths that occurred in that span.

**When to use:** To find the day of the week for the same date in a different year.

**Key insight:** You must count the leap years carefully; if the date is before February 29th, that year's leap day might not be included.

**Worked example:** From Jan 1, 2001 to Jan 1, 2005 is 4 years. There is 1 leap year (2004). Total shift = 4 + 1 = 5 days.

---

## Suggested Study Order

1. **Calendar Basics** — Start here to master the definition of odd days and the leap year rule, which are the building blocks for everything else.
2. **Yearly Shift** — Study next to understand how time moves forward year-by-year without needing to calculate full dates.
3. **Specific Date** — Study this third as it combines the century cycle, yearly shifts, and monthly day-counting into one complete process.
4. **Calendar Repetition** — Study last, as it requires you to apply the Yearly Shift logic to find when the cycle resets to zero odd days.

---

## Chapter-Wide Traps

**Century Leap Year Confusion:** Treating every year divisible by 4 as a leap year (e.g., 1900 is not a leap year) → Always check if a century year is divisible by 400.

**The "Inclusive" Counting Error:** Adding the current year and the target year incorrectly when calculating shifts → Always calculate the difference between the years ($Year_2 - Year_1$) to find the number of elapsed years.

**Month-End Calculation:** Miscounting the number of days in months (especially February) → Always verify the month length before summing days for a specific date.