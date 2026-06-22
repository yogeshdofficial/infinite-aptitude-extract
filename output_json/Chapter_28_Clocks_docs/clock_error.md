# Clock Error

## Overview
This pattern involves clocks that run faster or slower than the standard time. The central idea is to establish a ratio between the "faulty clock time" and "correct clock time" to determine the actual time elapsed.

---

## Recognition Clues
* **Keywords:** "gains," "loses," "slow," "fast," "uniformly," "true time," "correct time."
* **Given:** Initial error (e.g., 5 min slow), final error (e.g., 5 min 48 sec fast), and the total time elapsed.
* **Asked:** When the clock was correct, or the true time corresponding to a faulty clock reading.

---

## Key Formulas

### [True Time Calculation]
$$
\text{True Time} = \text{Faulty Time} \times \frac{24}{24 \pm \text{Error per 24h}}
$$

**Variables:**
- $\text{Faulty Time}$ = Total duration shown by the faulty clock.
- $\text{Error}$ = Gain (+) or Loss (-) in 24 hours.

**When to use:** When you need to find the actual time elapsed based on a clock that gains or loses time.

**Worked example:** If a clock loses 16 min in 24h and shows 89 hours, $\text{True Time} = 89 \times \frac{24}{24 - 16/60} = 89 \times \frac{24}{23.733} = 90$ hours.

### [Time to Correct]
$$
\text{Time to Correct} = \text{Total Time} \times \frac{\text{Initial Error}}{\text{Total Error}}
$$

**Variables:**
- $\text{Total Time}$ = Total duration between the two observations.
- $\text{Initial Error}$ = The amount the clock was slow/fast at the start.
- $\text{Total Error}$ = Sum of initial slow and final fast (or vice versa).

**When to use:** To find exactly when a clock showed the correct time.

---

## Solution Framework

1. **Calculate Total Elapsed Time:** Find the total hours between the two given timestamps.
2. **Calculate Total Error:** Add the initial error and final error (if one is slow and one is fast, add them; if both are fast/slow, subtract them).
3. **Determine Ratio:** Establish the relationship: $\text{Total Error}$ occurs in $\text{Total Elapsed Time}$.
4. **Find Correction Point:** Use the ratio to find when the clock gained/lost exactly the amount of the "Initial Error."
5. **Add to Start Time:** Add this duration to the starting timestamp to get the exact time the clock was correct.

---

## Shortcut Tricks

* **Trick:** Use the ratio $\frac{\text{Initial Error}}{\text{Total Error}}$ directly against the total elapsed time.
* **Why it works:** It uses the property of uniform gain/loss to interpolate the exact moment the error was zero.
* **When to use:** When asked "When was the clock correct?"
* **Example:** If 5 min slow and 5.8 min fast over 180 hours, $\text{Time} = 180 \times \frac{5}{5+5.8} = 180 \times \frac{5}{10.8} = 83.33$ hours.

---

## Common Mistakes

* **Mistake:** Forgetting to convert minutes to hours when calculating ratios.
* **Why it happens:** Mixing units (minutes vs. hours) in the same equation.
* **Fix:** Always convert all time components to a single unit (hours) before dividing.
* **Mistake:** Subtracting errors when they should be added.
* **Why it happens:** Assuming "slow" and "fast" always mean subtraction.
* **Fix:** If a clock goes from "slow" to "fast," the total error is the sum of the two.

---

## Worked Example (Step-by-Step)

**Question:** A watch is 5 min slow at 8 a.m. Sunday and 5 min 48 sec fast at 8 p.m. the following Sunday. When was it correct?

**Solution:**
1. **Total Time:** 8 a.m. Sunday to 8 p.m. next Sunday = 7 days + 12 hours = 180 hours.
2. **Total Error:** 5 min (slow) + 5.8 min (fast) = 10.8 min.
3. **Ratio:** The watch gains 10.8 min in 180 hours.
4. **Correction Point:** To be correct, it must gain the initial 5 min. Time = $180 \times \frac{5}{10.8} = 83.33$ hours.
5. **Convert:** 83 hours 20 minutes = 3 days, 11 hours, 20 minutes.
6. **Add:** 8 a.m. Sunday + 3 days 11h 20m = 7:20 p.m. Wednesday.

**Answer:** 7:20 p.m. Wednesday.

---

## Similar Patterns
* **Relative Speed Problems:** These involve two objects moving at different speeds; distinguish by checking if the "gain" is constant (clock) or variable (distance/speed).

---

## Revision Summary
* **Key formula:** $\text{Time} = \text{Total Time} \times \frac{\text{Initial Error}}{\text{Total Error}}$.
* **Spot it by:** "Gains/Loses" and "Correct time" keywords.
* **First move:** Calculate total elapsed hours and total error magnitude.
* **Fastest method:** Use the ratio of initial error to total error.
* **Biggest trap:** Mixing up units (minutes vs hours) in the ratio.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Unit Conversion** — Converting minutes to fractions of an hour ($min/60$).
* **Time Addition** — Adding hours/days to a specific clock time.

### Formulas You Must Know First
* **Total Time** = $(\text{Days} \times 24) + \text{Remaining Hours}$.

### Terms Used In This Pattern
* **Uniform Gain/Loss** — The clock error increases at a constant rate per hour.
* **Faulty Clock** — A clock that does not track time at the standard rate.