# Calendar Basics

## Overview
These questions test your ability to calculate future days, identify leap years, and determine properties of centuries using the Gregorian calendar. The central idea is the **"Odd Day"**: any remainder left after dividing a total number of days by 7.

---

## Recognition Clues
* **Keywords:** "After X days," "Last day of a century," "Not a leap year," "X weeks X days."
* **Given:** A starting day, a specific year, or a duration in weeks/days.
* **Asked:** The day of the week, the validity of a leap year, or the total count of days.

---

## Key Formulas

### Odd Day Calculation
$$
\text{Odd Days} = \text{Total Days} \pmod{7}
$$
**Variables:**
- $\text{Total Days}$ = The number of days elapsed.
- $\pmod{7}$ = The remainder when divided by 7.

**When to use:** To find the day of the week after a specific duration.
**Worked example:** For 61 days: $61 \div 7 = 8$ weeks and $5$ remainder. Odd days = $5$.

### Leap Year Condition
$$
\text{Leap Year} = \text{Year} \div 4 \text{ (if not a century)} \text{ OR } \text{Year} \div 400 \text{ (if a century)}
$$
**Variables:**
- $\text{Year}$ = The year in question.

**When to use:** To check if a year has 366 days.
**Worked example:** For 700: $700 \div 400 = 1.75$ (Not divisible, so not a leap year).

---

## Solution Framework

**Step 1: Simplify the duration** — Convert all time periods into total days or odd days (divide by 7).
**Step 2: Apply the cycle** — Add the odd days to the current day of the week to find the target day.
**Step 3: Check constraints** — For century years, ensure divisibility by 400; for general years, use 4.
**Step 4: Verify sequence** — If dealing with recurring events (like Sundays), list the dates to find the pattern.

---

## Shortcut Tricks

* **Trick:** The "Last Day of Century" cycle is always Friday, Wednesday, Monday, Sunday.
* **Why it works:** The odd days in 100-year blocks follow a repeating pattern of 5, 3, 1, 0.
* **When to use:** When asked what a century cannot end on (e.g., Tuesday, Thursday, Saturday).
* **Example:** Since the cycle is 5, 3, 1, 0, any day not in this set (like Tuesday) is impossible.

---

## Common Mistakes

* **Mistake:** Counting the current day as the first day.
    * **Fix:** Always add the odd days to the *current* day (e.g., if today is Monday, +1 is Tuesday).
* **Mistake:** Assuming every 100th year is a leap year.
    * **Fix:** Only century years divisible by 400 are leap years.
* **Mistake:** Miscalculating $x$ weeks $x$ days.
    * **Fix:** Remember $x$ weeks = $7x$ days, so total = $7x + x = 8x$.

---

## Worked Example (Step-by-Step)

**Question:** Today is Monday. After 61 days, it will be?

**Solution:**
1. **Simplify:** Divide 61 by 7. $61 = (7 \times 8) + 5$.
2. **Identify Odd Days:** The remainder is 5.
3. **Apply:** Count 5 days forward from Monday: Tuesday (1), Wednesday (2), Thursday (3), Friday (4), Saturday (5).

**Answer:** Saturday.

---

## Similar Patterns
**Clock Problems:** These involve angles and time intervals; distinguish them by looking for "degrees" or "hands of the clock" rather than "days" or "years."

---

## Revision Summary
* **Key formula:** $\text{Odd Days} = \text{Total Days} \pmod{7}$.
* **Spot it by:** Keywords like "leap year," "century," or "after X days."
* **First move:** Convert all durations into odd days by dividing by 7.
* **Fastest method:** Use the 5-3-1-0 odd day cycle for century calculations.
* **Biggest trap:** Forgetting that century years must be divisible by 400 to be leap years.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Divisibility Rule for 4** — A number is divisible by 4 if its last two digits are divisible by 4.
* **Modular Arithmetic** — The concept of finding the remainder after division.

### Formulas You Must Know First
$$
\text{Total Days} = (\text{Weeks} \times 7) + \text{Extra Days}
$$
**What it means:** Converts a duration into a single unit of days.

### Terms Used In This Pattern
* **Leap Year** — A year with 366 days (February has 29 days).
* **Ordinary Year** — A year with 365 days (February has 28 days).
* **Century Year** — A year ending in "00" (e.g., 1900, 2000).