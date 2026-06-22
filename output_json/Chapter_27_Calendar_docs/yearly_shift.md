# Yearly Shift

## Overview
This pattern involves finding the day of the week for a specific date in a different year. The central idea is to calculate the total number of "odd days" between the two dates and shift the starting day of the week forward or backward accordingly.

---

## Recognition Clues
* **Keywords:** "What day of the week lies on...", "What was the day of the week on..."
* **Given:** A specific date and its corresponding day of the week.
* **Asked:** The day of the week for the same date in a different year.
* **Timeframe:** The gap is usually a small number of years (e.g., 2006 to 2010).

---

## Key Formulas

### [Odd Day Shift]
$$
\text{Target Day} = \text{Given Day} \pm (\text{Total Odd Days} \pmod{7})
$$

**Variables:**
- $\text{Target Day}$ = The day of the week we are solving for.
- $\text{Given Day}$ = The starting day provided in the question.
- $\text{Total Odd Days}$ = The sum of odd days for each year in the interval.

**When to use:** To find the day of the week after calculating the total shift. Use $+$ when moving forward in time, and $-$ when moving backward.

**Worked example:** From Jan 1, 2006 (Sunday) to Jan 1, 2010. Total odd days = $1+1+2+1 = 5$. Target = $\text{Sunday} + 5 = \text{Friday}$.

---

## Solution Framework

**Step 1: Identify the interval** — Determine the number of years between the given date and the target date.

**Step 2: Count odd days per year** — Assign 1 odd day for an ordinary year (365 days) and 2 odd days for a leap year (366 days).

**Step 3: Check for leap years** — A year is a leap year if it is divisible by 4 (e.g., 2004, 2008). Ensure you include the leap day (Feb 29) if it falls within your specific date range.

**Step 4: Sum and Modulo** — Add all odd days and find the remainder when divided by 7.

**Step 5: Shift the day** — Move forward in the week if the target year is later, or backward if the target year is earlier.

---

## Shortcut Tricks

* **Trick:** Leap year check.
* **Why it works:** A leap year adds an extra day to the calendar, shifting the day of the week by 2 instead of 1.
* **When to use it:** Always check if the interval includes February 29th.
* **Example:** Moving from March 2004 to March 2005 crosses Feb 29, 2004, so add 2 days. Moving from Jan 2004 to Jan 2005 also crosses Feb 29, 2004, so add 2 days.

---

## Common Mistakes

* **Mistake:** Counting the final year as a full year.
    * **Why it happens:** Misinterpreting the range (e.g., 2006 to 2010 is 4 years, not 5).
    * **Fix:** Only count the years *between* the two dates.
* **Mistake:** Forgetting to subtract when moving backward.
    * **Why it happens:** Habitually adding odd days.
    * **Fix:** If the target year is earlier than the given year, subtract the odd days.
* **Mistake:** Misidentifying leap years.
    * **Why it happens:** Assuming every 4th year is a leap year without checking the specific date range.
    * **Fix:** Verify if Feb 29 is actually included in the period.

---

## Worked Example (Step-by-Step)

**Question:** It was Sunday on Jan 1, 2006. What was the day of the week on Jan 1, 2010?

**Solution:**
1. **Identify interval:** 2006 to 2010.
2. **Count odd days:**
   - 2006 (Ordinary): 1 odd day.
   - 2007 (Ordinary): 1 odd day.
   - 2008 (Leap): 2 odd days.
   - 2009 (Ordinary): 1 odd day.
3. **Sum:** $1 + 1 + 2 + 1 = 5$ odd days.
4. **Shift:** Sunday + 5 days = Monday (1), Tuesday (2), Wednesday (3), Thursday (4), Friday (5).

**Answer:** Friday.

---

## Similar Patterns
**Calendar Date Calculation:** This requires finding the day for a date in a different month or century, which involves calculating odd days for months and centuries, not just yearly shifts.

---

## Revision Summary
* **Key formula:** $\text{Target} = \text{Given} \pm \text{Total Odd Days}$.
* **Spot it by:** Same date, different year.
* **First move:** Count years and identify leap years.
* **Fastest method:** Sum odd days ($1$ for ordinary, $2$ for leap) and shift.
* **Biggest trap:** Forgetting to subtract when moving backward in time.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Odd Days** — The remainder when the total number of days is divided by 7.
* **Leap Year** — A year with 366 days; occurs every 4 years (divisible by 4).

### Formulas You Must Know First
$$
\text{Odd Days} = \text{Total Days} \pmod{7}
$$
**What it means:** Dividing the total days by 7 gives the number of full weeks; the remainder is the "odd day" count.

### Terms Used In This Pattern
* **Ordinary Year** — A year with 365 days (1 odd day).
* **Leap Year** — A year with 366 days (2 odd days).