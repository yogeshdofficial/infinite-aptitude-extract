# Basic Speed Calculation

## Overview
This pattern involves calculating the speed of a boat in still water and the speed of the stream when downstream and upstream speeds are either given or can be derived from distance and time. The central idea is that downstream speed is the sum of the boat and stream speeds, while upstream speed is their difference.

---

## Recognition Clues
* **Keywords:** "downstream," "upstream," "still water," "speed of the stream," "row a boat."
* **Given:** Distance and time for both directions, or direct speed values in km/hr.
* **Asked:** Speed of the boat in still water ($u$) or speed of the stream ($v$).
* **Time units:** Look for mixed units (e.g., "3 hours 45 minutes") that require conversion to hours.

---

## Key Formulas

### [Boat Speed in Still Water]
$$
u = \frac{1}{2}(\text{Downstream Speed} + \text{Upstream Speed})
$$
**Variables:** $u$ = speed in still water; Downstream Speed = $u+v$; Upstream Speed = $u-v$.
**When to use:** When you have both directional speeds and need the boat's base speed.
**Worked example:** If downstream = 11 km/hr and upstream = 5 km/hr, $u = \frac{1}{2}(11+5) = 8$ km/hr.

### [Stream Speed]
$$
v = \frac{1}{2}(\text{Downstream Speed} - \text{Upstream Speed})
$$
**Variables:** $v$ = speed of the stream.
**When to use:** When you have both directional speeds and need the current's speed.
**Worked example:** If downstream = 32 km/hr and upstream = 28 km/hr, $v = \frac{1}{2}(32-28) = 2$ km/hr.

---

## Solution Framework
1. **Convert units:** Ensure all times are in hours (e.g., 45 mins = $0.75$ hours) and distances in km.
2. **Calculate speeds:** Use $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$ to find the downstream and upstream speeds if not provided.
3. **Apply formula:** Use the sum formula for boat speed or the difference formula for stream speed.
4. **Divide by 2:** Always divide the result of the addition or subtraction by 2 to isolate the variable.

---

## Shortcut Tricks
* **Trick:** If distance is the same for both directions, the average speed is $\frac{2 \times \text{Downstream} \times \text{Upstream}}{\text{Downstream} + \text{Upstream}}$.
* **Why it works:** This is the harmonic mean of the two speeds, representing the effective speed over a round trip.
* **When to use:** When the question asks for the average speed of a round trip.
* **Example:** For speeds 14 km/hr and 6 km/hr, Average = $\frac{2 \times 14 \times 6}{14+6} = \frac{168}{20} = 8.4$ km/hr.

---

## Common Mistakes
* **Mistake:** Using minutes directly in the speed formula. **Fix:** Always convert minutes to hours by dividing by 60.
* **Mistake:** Forgetting to divide by 2. **Fix:** Remember that the difference between downstream and upstream is $2v$, not $v$.
* **Mistake:** Adding speeds to find the stream speed. **Fix:** Stream speed is always the difference divided by 2.

---

## Worked Example (Step-by-Step)

**Question:** A man takes 3 hours 45 minutes to row 15 km downstream and 2 hours 30 minutes to row 5 km upstream. Find the speed of the current.

**Solution:**
1. **Convert time:** 
   - Downstream: $3 \text{ hrs } 45 \text{ mins} = 3 + \frac{45}{60} = 3.75 \text{ or } \frac{15}{4} \text{ hours}$.
   - Upstream: $2 \text{ hrs } 30 \text{ mins} = 2 + \frac{30}{60} = 2.5 \text{ or } \frac{5}{2} \text{ hours}$.
2. **Calculate speeds:**
   - Downstream speed = $\frac{15}{15/4} = 15 \times \frac{4}{15} = 4$ km/hr.
   - Upstream speed = $\frac{5}{5/2} = 5 \times \frac{2}{5} = 2$ km/hr.
3. **Apply formula:** Current speed $v = \frac{1}{2}(4 - 2) = 1$ km/hr.

**Answer:** 1 km/hr.

---

## Similar Patterns
* **Average Speed Problems:** These involve total distance/total time; distinguish by checking if the question asks for a specific component (boat/stream) or the overall average.

---

## Revision Summary
* **Key formula:** $v = \frac{1}{2}(\text{Downstream} - \text{Upstream})$.
* **Spot it by:** Looking for "downstream" and "upstream" keywords.
* **First move:** Convert all time units to hours.
* **Fastest method:** Calculate individual speeds first, then apply the $\frac{1}{2}$ sum/diff rule.
* **Biggest trap:** Forgetting to divide the difference by 2.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Speed-Distance-Time:** $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$.
* **Fractional Time:** Converting minutes to hours by dividing by 60.

### Formulas You Must Know First
$$
\text{Speed} = \frac{\text{Distance}}{\text{Time}}
$$
**What it means:** The rate at which distance is covered over time.
**Example:** 10 km in 2 hours = 5 km/hr.

### Terms Used In This Pattern
* **Downstream:** Moving in the same direction as the current ($u+v$).
* **Upstream:** Moving against the current ($u-v$).
* **Still Water:** The speed of the boat without any current influence ($u$).