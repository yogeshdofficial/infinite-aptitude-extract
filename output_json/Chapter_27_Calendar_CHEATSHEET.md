# Calendar — Exam Cheat Sheet

## How To Solve Any Question In This Chapter

1. **Identify Scope:** Does the question ask for a specific day of a date, a future/past day, or a calendar repetition?
2. **Categorize:** Use the Quick-Recognition Table to match the question type.
3. **Calculate Odd Days:** Determine the total days elapsed and find the remainder when divided by 7 ($\text{Total days} \pmod{7}$).
4. **Apply Shift:** Add or subtract the odd days from the reference day (Forward = Add, Backward = Subtract).
5. **Verify Leap Years:** Check if the interval crosses February 29th; if yes, add an extra day.
6. **Sanity Check:** Ensure the final day is within the 7-day cycle (0=Sunday, 1=Monday, ..., 6=Saturday).

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Calendar Basics | "After X days", "Century" | Current day/Year | Day of week/Leap status |
| Calendar Repetition | "Same calendar", "Serve for" | Year | Repeating year |
| Specific Date | "What was the day", "On what dates" | Full date | Day of week |
| Yearly Shift | "Jan 1 to Jan 1", "Same date" | Two years | Day of week |

---

## Formula Bank

**[Calendar Basics]**

$$
\text{New day} = \text{Current day} + (\text{Days} \pmod{7})
$$
→ *produces: future day of the week*
→ *use when: calculating days after X*

$$
\text{Leap year} = \text{Year} \div 400 \text{ (for centuries)}
$$
→ *produces: leap year status*
→ *use when: checking century leap years*

**[Calendar Repetition]**

$$
\sum \text{Odd days} \equiv 0 \pmod{7}
$$
→ *produces: year with identical calendar*
→ *use when: finding repeating calendar years*

**[Specific Date]**

$$
\text{Total odd days} = \sum \text{odd days in years} + \sum \text{odd days in months}
$$
→ *produces: total remainder for date*
→ *use when: finding day of any date*

**[Yearly Shift]**

$$
\text{Day}_{n-1} = \text{Day}_n - \text{Odd days}
$$
→ *produces: previous year's day*
→ *use when: moving backward in time*

---

## Step Sequences

**Calendar Basics:** Identify leap status → Calculate total days → Modulo 7 → Add to current.
**Calendar Repetition:** List years → Count leap years → Sum odd days → Stop at multiple of 7.
**Specific Date:** Century code → Year code → Month code → Date → Sum and Modulo 7.
**Yearly Shift:** Identify interval → Count leap days → Add/Subtract odd days → Result.

---

## Fastest Tricks

* **Calendar Basics:** Century last days cycle: Friday(5), Wednesday(3), Monday(1), Sunday(0).
* **Calendar Repetition:** Ordinary years repeat after 6 or 11 years; leap years after 28.
* **Specific Date:** 1st March 2005 is Tuesday; use as a reference anchor.
* **Yearly Shift:** Ordinary year = 1 odd day; Leap year = 2 odd days.

---

## Trap Watch

* **Calendar Basics:** Century years not divisible by 400 are not leap years → Check 400.
* **Calendar Repetition:** Counting the target year in the sum → Stop at end of previous year.
* **Specific Date:** Forgetting Feb 29 in leap years → Check if year is leap.
* **Yearly Shift:** Moving backward across Feb 29 → Subtract 2 days.

---

## Last-Minute Reminders

* A leap year occurs every 4 years, but century years must be divisible by 400.
* The remainder 0 corresponds to Sunday, 1 to Monday, and so on up to 6 for Saturday.
* When moving backward in time, always subtract the odd days instead of adding.
* Always verify if the date provided falls after February in a leap year.
* The number of odd days in a normal year is 1, and in a leap year is 2.