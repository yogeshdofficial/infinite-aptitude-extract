# Calendar Repetition

## Overview
This pattern involves identifying the next year that will have an identical calendar to a given year. The central idea is that a calendar repeats when the total number of "odd days" accumulated between the start of the given year and the start of the target year equals a multiple of 7.

---

## Recognition Clues
* **Keywords:** "calendar for the year... will be the same for the year", "will serve for the year".
* **Given:** A specific starting year (e.g., 2003, 2007, 2009).
* **Asked:** The next year that shares the same calendar.

---

## Key Formulas

### [Cumulative Odd Days]
$$
\sum (\text{Odd days per year}) \equiv 0 \pmod{7}
$$

**Variables:**
- $\text{Odd days per year}$ = 1 for an ordinary year (365 days), 2 for a leap year (366 days).
- $\equiv 0 \pmod{7}$ = The sum must be a multiple of 7 (7, 14, 21, etc.).

**When to use:** To find the target year by adding odd days year-by-year until the sum hits a multiple of 7.

**Worked example:** For 2007: 2007(1) + 2008(2) + 2009(1) + 2010(1) + 2011(1) + 2012(2) + 2013(1) + 2014(1) + 2015(1) + 2016(2) + 2017(1) = 14. Since 14 is a multiple of 7, the next year, 2018, has the same calendar.

---

## Solution Framework

**Step 1: Identify the starting year** — Note if it is an ordinary year (1 odd day) or a leap year (2 odd days).
**Step 2: List subsequent years** — Write down the years following the start year.
**Step 3: Assign odd days** — Assign 2 to leap years and 1 to ordinary years.
**Step 4: Calculate cumulative sum** — Keep adding the odd days until the total sum is exactly 7 or 14.
**Step 5: Identify the target** — The year *following* the one that completes the sum is the answer.

---

## Shortcut Tricks

* **Trick:** For an ordinary year, if the previous year was a leap year, the calendar repeats in 6 years; otherwise, it repeats in 11 years.
* **Why it works:** The accumulation of odd days hits a multiple of 7 faster or slower based on the placement of leap years.
* **When to use:** When you need to save time on simple, non-century years.
* **Example:** 2009 follows 2008 (leap). $2009+6 = 2015$. (Matches Q18).

---

## Common Mistakes

* **Mistake:** Counting the leap year incorrectly.
    * **Why it happens:** Forgetting that a leap year occurs every 4 years.
    * **Fix:** Always check if the year is divisible by 4.
* **Mistake:** Stopping the sum at the year that makes the total 7.
    * **Why it happens:** Confusing the "summing year" with the "repeating year."
    * **Fix:** The repeating year is the one *after* the sum reaches 7.
* **Mistake:** Miscounting the interval.
    * **Why it happens:** Including the start year in the odd day count.
    * **Fix:** Only count odd days *between* the years.

---

## Worked Example (Step-by-Step)

**Question:** The calendar for the year 2009 will be the same as that of the year?

**Solution:**
1. **Step 1:** 2009 is an ordinary year.
2. **Step 2 & 3:** List years and odd days: 2009(1), 2010(1), 2011(1), 2012(2), 2013(1), 2014(1).
3. **Step 4:** Sum: $1 + 1 + 1 + 2 + 1 + 1 = 7$.
4. **Step 5:** The sum reaches 7 at the end of 2014. Therefore, the next year, 2015, has the same calendar.

**Answer:** 2015

---

## Similar Patterns
* **Day of the Week Calculation:** Distinguished by the question asking for a specific day (e.g., "What was the day on 15th Aug 1947?") rather than a repeating calendar year.

---

## Revision Summary
* **Key formula:** $\sum \text{Odd days} = 7n$.
* **Spot it by:** "Calendar for the year X will be the same for..."
* **First move:** List years and assign 1 for ordinary, 2 for leap.
* **Fastest method:** Use the 6/11 year rule for non-century years.
* **Biggest trap:** Stopping the count at the year that completes the sum of 7.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Odd Days** — The remainder when the total number of days is divided by 7.
* **Leap Year** — A year divisible by 4 (e.g., 2004, 2008) having 366 days (2 odd days).
* **Ordinary Year** — A year not divisible by 4 having 365 days (1 odd day).

### Formulas You Must Know First
$$
\text{Total Days} \pmod{7} = \text{Odd Days}
$$
**What it means:** Any number of days divided by 7 leaves a remainder of 0 to 6.
**Example:** 365 days / 7 = 52 weeks and 1 day remainder (1 odd day).

### Terms Used In This Pattern
* **Calendar Repetition** — When two years have the same sequence of days and dates.