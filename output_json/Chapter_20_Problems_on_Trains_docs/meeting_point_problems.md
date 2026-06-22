# Meeting Point Problems

## Overview
These problems involve two objects moving towards each other from different starting points. The central idea is that the total distance covered by both objects at the moment they meet equals the initial distance between the two starting points.

---

## Recognition Clues
* **Keywords:** "towards each other," "meet at," "cross each other," "distance between two stations."
* **Given:** Speeds of two objects, starting times (sometimes different), and either total distance or a difference in distance covered.
* **Asked:** Time of meeting or total distance between points.

---

## Key Formulas

### Relative Speed (Opposite Direction)
$$
\text{Relative Speed} = S_1 + S_2
$$
**Variables:** $S_1, S_2$ = speeds of the two objects.
**When to use:** When both objects are moving towards each other.
**Worked example:** Train A (20 kmph) and Train B (25 kmph) moving towards each other: $20 + 25 = 45$ kmph.

### Distance at Meeting
$$
D = (S_1 \times t) + (S_2 \times t)
$$
**Variables:** $D$ = total distance, $t$ = time elapsed until meeting.
**When to use:** When both start at the same time and meet at time $t$.
**Worked example:** If $t=2$ hours, $S_1=20, S_2=25$: $D = (20 \times 2) + (25 \times 2) = 90$ km.

---

## Solution Framework
1. **Normalize Start Times:** If start times differ, calculate the distance covered by the first object during the time gap and subtract it from the total distance.
2. **Determine Relative Speed:** Add the speeds of the two objects since they move in opposite directions.
3. **Calculate Time to Meet:** Divide the remaining distance by the relative speed ($t = \frac{\text{Remaining Distance}}{\text{Relative Speed}}$).
4. **Find Meeting Time/Distance:** Add $t$ to the start time of the second object or use $t$ to find individual distances covered.

---

## Shortcut Tricks
* **Trick:** If two objects start at the same time and meet, the ratio of distances covered is equal to the ratio of their speeds ($D_1 : D_2 = S_1 : S_2$).
* **Why it works:** Since time is constant, $D = S \times t \implies \frac{D_1}{D_2} = \frac{S_1 \times t}{S_2 \times t} = \frac{S_1}{S_2}$.
* **When to use:** When you are given the difference in distance covered and need the total distance.
* **Example:** $S_1=75, S_2=50$. Ratio $D_1:D_2 = 3:2$. Difference is 1 part. If 1 part = 175 km, total distance (5 parts) = $5 \times 175 = 875$ km.

---

## Common Mistakes
* **Mistake:** Using total distance when start times are different. **Fix:** Subtract the distance covered by the first object before the second starts.
* **Mistake:** Forgetting to add the time $t$ to the start time of the second object. **Fix:** Always add $t$ to the time the *second* object began moving.
* **Mistake:** Confusing "difference in distance" with "total distance." **Fix:** Use the ratio of speeds to find individual distances first, then sum them.

---

## Worked Example (Step-by-Step)

**Question:** Two stations A and B are 110 km apart. Train A starts at 7 a.m. (20 kmph). Train B starts at 8 a.m. (25 kmph). When will they meet?

**Solution:**
1. **Normalize:** Train A travels alone from 7 to 8 a.m. Distance = $20 \times 1 = 20$ km.
2. **Remaining Distance:** $110 - 20 = 90$ km.
3. **Relative Speed:** $20 + 25 = 45$ kmph.
4. **Time to Meet:** $t = \frac{90}{45} = 2$ hours.
5. **Meeting Time:** 8 a.m. + 2 hours = 10 a.m.

**Answer:** 10 a.m.

---

## Similar Patterns
**Relative Speed (Same Direction):** Distinguished by the phrase "moving in the same direction," where you subtract speeds ($S_1 - S_2$) instead of adding them.

---

## Revision Summary
* **Key formula:** $\text{Relative Speed} = S_1 + S_2$.
* **Spot it by:** "Towards each other" or "meet at."
* **First move:** Adjust for different start times by subtracting the solo distance.
* **Fastest method:** Use the ratio of speeds to find distance proportions.
* **Biggest trap:** Using the full distance when start times are staggered.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Speed-Distance-Time:** The fundamental relationship $\text{Distance} = \text{Speed} \times \text{Time}$.
* **Ratios:** Understanding that if $t$ is constant, $D \propto S$.

### Formulas You Must Know First
$$
\text{Time} = \frac{\text{Distance}}{\text{Speed}}
$$
**What it means:** Time taken is the total path length divided by the rate of travel.

### Terms Used In This Pattern
* **Relative Speed:** The speed of one object as observed from the other.
* **EMU:** Electric Multiple Unit (a type of train).