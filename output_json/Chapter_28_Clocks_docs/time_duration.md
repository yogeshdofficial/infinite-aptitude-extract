# Time Duration

## Overview
This pattern involves calculating the elapsed time between two events or converting time across different zones. The central idea is to use "Midnight" (00:00 or 24:00) as a bridge to split the duration into two manageable segments.

---

## Recognition Clues
* **Keywords:** "behind", "ahead", "leaves at", "reaches at", "duration of the journey".
* **Given:** Two timestamps (e.g., 12:25 noon and 10:45 am) or a reference time plus a time zone offset.
* **Asked:** The total time elapsed or the target time in a different zone.

---

## Key Formulas

### [Time Zone Conversion]
$$
\text{Target Time} = \text{Reference Time} \pm \text{Offset}
$$
**Variables:**
- $\text{Reference Time}$ = The starting time provided.
- $\text{Offset}$ = The time difference (add if ahead, subtract if behind).

**When to use:** When calculating time in a different location.

**Worked example:** Delhi is 02:35, London is 5h 30m behind. $02:35 - 05:30$. Using 24-hour format: $26:35 - 05:30 = 21:05$.

### [Total Duration]
$$
\text{Duration} = (\text{Time to Midnight}) + (\text{Time from Midnight})
$$
**Variables:**
- $\text{Time to Midnight}$ = $24:00 - \text{Departure Time}$
- $\text{Time from Midnight}$ = $\text{Arrival Time} - 00:00$

**When to use:** When a journey crosses the midnight threshold.

**Worked example:** 12:25 noon to 10:45 am. Duration = $(24:00 - 12:25) + 10:45 = 11:35 + 10:45 = 22:20$.

---

## Solution Framework

1. **Standardize:** Convert all times to the 24-hour clock format to avoid AM/PM confusion.
2. **Bridge to Midnight:** If the event crosses midnight, split the calculation into "Time until 24:00" and "Time after 00:00".
3. **Calculate Segments:** Subtract the start time from 24:00 for the first part; use the arrival time for the second part.
4. **Sum and Normalize:** Add the hours and minutes separately; if minutes $\ge 60$, convert to hours (e.g., 80 min = 1h 20m).

---

## Shortcut Tricks

* **Trick:** Use the "24-hour borrow" method for subtraction.
* **Why it works:** It treats the day as a continuous 24-hour cycle, preventing negative results when subtracting across midnight.
* **When to use:** When the time to be subtracted is greater than the current time (e.g., $02:35 - 05:30$).
* **Example:** $02:35 - 05:30 \rightarrow (24 + 2):35 - 05:30 = 26:35 - 05:30 = 21:05$.

---

## Common Mistakes

* **Mistake:** Subtracting minutes as decimals (e.g., 0.30 instead of 30 minutes).
    * **Fix:** Always treat hours and minutes as separate units; 1 hour = 60 minutes.
* **Mistake:** Forgetting to carry over minutes to hours when the sum exceeds 60.
    * **Fix:** Divide total minutes by 60 to find the extra hours.
* **Mistake:** Misinterpreting "12:25 noon" as 00:25.
    * **Fix:** Noon is 12:00; midnight is 00:00 or 24:00.

---

## Worked Example (Step-by-Step)

**Question:** A bus leaves at 12.25 noon and reaches destination at 10.45 am. The duration of the journey is?

**Solution:**
1. **Standardize:** Departure = 12:25. Arrival = 10:45 (next day).
2. **Bridge to Midnight:** Time from 12:25 to 24:00 is $24:00 - 12:25 = 11$ hours $35$ minutes.
3. **Time from Midnight:** Time from 00:00 to 10:45 is $10$ hours $45$ minutes.
4. **Sum:** $11\text{h } 35\text{m} + 10\text{h } 45\text{m} = 21\text{h } 80\text{m}$.
5. **Normalize:** $80\text{m} = 1\text{h } 20\text{m}$. Total = $21\text{h} + 1\text{h } 20\text{m} = 22\text{h } 20\text{m}$.

**Answer:** 22 hours 20 minutes.

---

## Similar Patterns
**Clock Angle Problems:** These involve calculating the position of hands at a specific time, whereas Time Duration problems focus on the elapsed interval between two points in time.

---

## Revision Summary
* **Key formula:** $\text{Duration} = (\text{Time to Midnight}) + (\text{Time from Midnight})$.
* **Spot it by:** Looking for "leaves at", "reaches at", or time zone offsets.
* **First move:** Convert all times to 24-hour format.
* **Fastest method:** Use the "24-hour borrow" for subtraction and split at midnight for duration.
* **Biggest trap:** Treating 60 minutes as 100 units.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **24-Hour Clock:** A system where the day runs from 00:00 to 23:59.
* **Time Conversion:** $1 \text{ hour} = 60 \text{ minutes}$.

### Formulas You Must Know First
* No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Offset:** The difference in time between two geographical locations.
* **Elapsed Time:** The total duration between a start time and an end time.