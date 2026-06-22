# Specific Date

## Overview
This pattern involves determining the day of the week for any given calendar date. The central idea is to calculate the total number of "odd days" (remainder when total days are divided by 7) from a fixed reference point (e.g., 0001 AD) up to the target date.

---

## Recognition Clues
* **Keywords:** "What was the day of the week on...", "On what dates of [Month] did [Day] fall?"
* **Given:** A specific calendar date (Day, Month, Year).
* **Asked:** The corresponding day of the week (Monday, Tuesday, etc.).
* **Variation:** Finding all dates in a month that fall on a specific day (e.g., all Fridays in March).

---

## Key Formulas

### Odd Days Calculation
$$
\text{Odd Days} = \text{Total Days} \pmod{7}
$$

**Variables:**
- $\text{Total Days}$ = Sum of days from the reference point to the target date.
- $\pmod{7}$ = The remainder after dividing by 7.

**When to use:** To convert any duration of time into a day of the week.

**Worked example:** For 198 days, $198 \div 7 = 28$ weeks with a remainder of 2. Thus, 2 odd days.

---

## Solution Framework

**Step 1: Split the date** into (Completed Years) + (Days elapsed in the current year).
**Step 2: Calculate odd days for completed years** by breaking them into centuries (400 years = 0 odd days) and remaining years.
**Step 3: Calculate odd days for the current year** by summing the days of each completed month plus the days in the current month.
**Step 4: Sum all odd days** and find the final remainder when divided by 7.
**Step 5: Map the remainder** to the day (0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat).

---

## Shortcut Tricks

* **Trick:** Century multiples of 400 (1600, 2000, 2400) always have 0 odd days.
* **Why it works:** The calendar cycle repeats perfectly every 400 years.
* **When to use:** Whenever the year is $\ge 1600$.
* **Example:** For 2002, treat 2000 as 0 odd days, leaving only 2 years to calculate.

---

## Common Mistakes

* **Mistake:** Treating a non-leap year as a leap year (e.g., 1900, 2100).
    * **Fix:** A century year is only a leap year if divisible by 400.
* **Mistake:** Forgetting to add the current month's days.
    * **Fix:** Always include the days elapsed in the target month.
* **Mistake:** Incorrectly mapping the remainder to the day.
    * **Fix:** Use the standard mapping: 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat.

---

## Worked Example (Step-by-Step)

**Question:** What was the day of the week on 15th August, 1947?

**Solution:**
1. **Split:** 1946 complete years + days in 1947 up to Aug 15.
2. **Years:** 1600 (0) + 300 (1) + 46 years. 46 years = 11 leap + 35 ordinary = $(11 \times 2) + (35 \times 1) = 57$ days. $57 \pmod{7} = 1$ odd day. Total for 1946 years = $0 + 1 + 1 = 2$ odd days.
3. **Months:** Jan(31), Feb(28), Mar(31), Apr(30), May(31), Jun(30), Jul(31), Aug(15) = 227 days.
4. **Sum:** $227 \pmod{7} = 3$ odd days. Total = $2 + 3 = 5$ odd days.
5. **Map:** 5 corresponds to Friday.

**Answer:** Friday.

---

## Similar Patterns
* **Calendar Repetition:** Questions asking "Which year will have the same calendar as 2003?" — Solve by finding the year where the total odd days between them equals 0.

---

## Revision Summary
* **Key formula:** $\text{Total Days} \pmod{7}$.
* **Spot it by:** "What was the day on [Date]".
* **First move:** Split into completed years and current year days.
* **Fastest method:** Use 400-year cycle (0 odd days) to reduce the year count.
* **Biggest trap:** Miscounting February in leap years.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Leap Year** — A year divisible by 4 (unless it is a century not divisible by 400).
* **Odd Days** — The remainder after dividing the total number of days by 7.

### Formulas You Must Know First
* **Leap Year Count** = $\lfloor \frac{\text{Years}}{4} \rfloor$.

### Terms Used In This Pattern
* **Ordinary Year** — 365 days (1 odd day).
* **Leap Year** — 366 days (2 odd days).