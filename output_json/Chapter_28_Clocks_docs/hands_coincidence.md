# Hands Coincidence

## Overview
This pattern involves finding the exact time when clock hands reach a specific relative position (coinciding, at right angles, or a set distance apart). The central idea is that the minute hand must "gain" a specific number of minute spaces over the hour hand to reach the target configuration.

---

## Recognition Clues
* **Keywords:** "together," "right angle," "straight line," "apart," "between X and Y o'clock."
* **Given:** The starting hour (e.g., "between 4 and 5").
* **Asked:** The exact time (minutes past the hour).
* **Visual:** The hands are moving; you are calculating the moment the gap between them matches a specific condition.

---

## Key Formulas

### Time to Gain Gap
$$
\text{Time} = \frac{60}{55} \times \text{Gap} = \frac{12}{11} \times \text{Gap}
$$

**Variables:**
- $\text{Gap}$ = The number of minute spaces the minute hand must cover to reach the target position.
- $\frac{12}{11}$ = The constant multiplier derived from the relative speed of the hands.

**When to use:** Every time you need to find the exact minute past the hour.

**Worked example:** To find when hands coincide at 2 o'clock, the gap is 10 spaces. Time = $\frac{12}{11} \times 10 = 10\frac{10}{11}$ minutes past 2.

---

## Solution Framework

1. **Identify Initial Gap:** Determine the distance (in minute spaces) between the hands at the start hour (e.g., at 4 o'clock, the gap is 20 spaces).
2. **Determine Target Gap:** Identify the required distance for the specific condition (0 for together, 15 for right angles, 30 for straight lines).
3. **Calculate Required Gain:** Subtract or add the target gap from the initial gap to find how many spaces the minute hand must "gain" to reach the target.
4. **Apply Formula:** Multiply the required gain by $\frac{12}{11}$ to get the exact minutes past the hour.

---

## Shortcut Tricks

* **Trick:** Always use the multiplier $\frac{12}{11}$.
* **Why it works:** The minute hand moves 60 spaces while the hour hand moves 5, meaning the minute hand gains 55 spaces every 60 minutes ($\frac{60}{55} = \frac{12}{11}$).
* **When to use:** Any problem involving clock hand positions.
* **Example:** For 5 minutes gain, $5 \times \frac{12}{11} = \frac{60}{11} = 5\frac{5}{11}$ minutes.

---

## Common Mistakes

* **Mistake:** Using 60 instead of 55 in the denominator. **Fix:** Always use $\frac{12}{11}$ as your multiplier.
* **Mistake:** Forgetting there are two cases for right angles or "apart" questions. **Fix:** Check both (Initial Gap - Target) and (Initial Gap + Target).
* **Mistake:** Calculating time past the wrong hour. **Fix:** Always calculate minutes past the *starting* hour (e.g., "past 4" for "between 4 and 5").

---

## Worked Example (Step-by-Step)

**Question:** At what time between 4 and 5 o’clock will the hands of a clock be at a right angle?

**Solution:**
1. **Initial Gap:** At 4 o'clock, the minute hand is at 12 and the hour hand is at 4 (20 minute spaces apart).
2. **Target Gap:** Right angle = 15 minute spaces.
3. **Calculate Gain:**
   - Case I: $20 - 15 = 5$ spaces.
   - Case II: $20 + 15 = 35$ spaces.
4. **Apply Formula:**
   - Case I: $\frac{12}{11} \times 5 = \frac{60}{11} = 5\frac{5}{11}$ minutes past 4.
   - Case II: $\frac{12}{11} \times 35 = \frac{420}{11} = 38\frac{2}{11}$ minutes past 4.

**Answer:** $5\frac{5}{11}$ minutes past 4 and $38\frac{2}{11}$ minutes past 4.

---

## Similar Patterns
**Angle Calculation:** If asked for the angle at a specific time (e.g., 3:25), use the formula $\theta = |30H - 5.5M|$ instead of the "gain" method.

---

## Revision Summary
* **Key formula:** $\text{Time} = \frac{12}{11} \times \text{Gap}$.
* **Spot it by:** Looking for "together," "right angle," or "straight line" between two hours.
* **First move:** Find the initial minute-space gap at the start hour.
* **Fastest method:** Multiply the required gain by $\frac{12}{11}$.
* **Biggest trap:** Forgetting to calculate both cases for right angles or "apart" conditions.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Minute Spaces:** The clock face is divided into 60 parts; each hour represents 5 minute spaces.
* **Relative Speed:** The minute hand moves 12 times faster than the hour hand.

### Formulas You Must Know First
* No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Coincide:** Hands are together (0 minute spaces apart).
* **Right Angle:** Hands are 15 minute spaces apart.
* **Straight Line:** Hands are 30 minute spaces apart (opposite).