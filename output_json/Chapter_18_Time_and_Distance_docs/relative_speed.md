# Relative Speed

## Overview
This pattern involves two objects moving simultaneously. You solve it by calculating a single "Relative Speed" and treating the problem as if one object is stationary while the other moves at that combined rate.

---

## Recognition Clues
* **Keywords:** "moving in the same direction," "moving towards each other," "catches up," "overtaken," "meet."
* **Given:** Two speeds ($S_1, S_2$) and either a distance gap or a total distance.
* **Asked:** Time taken to meet, distance covered until meeting, or the speed of one object.

---

## Key Formulas

### [Relative Speed: Opposite Direction]
$$
S_{rel} = S_1 + S_2
$$
**When to use:** When two objects move towards each other.
**Example:** Q22: $S_1 = 65, S_2 = 35$. $S_{rel} = 65 + 35 = 100$ kmph.

### [Relative Speed: Same Direction]
$$
S_{rel} = S_1 - S_2 \quad (\text{where } S_1 > S_2)
$$
**When to use:** When one object chases another or moves in the same direction.
**Example:** Q24: $S_1 = 10, S_2 = 8$. $S_{rel} = 10 - 8 = 2$ kmph.

---

## Solution Framework

1. **Identify Direction:** Determine if speeds should be added (opposite) or subtracted (same).
2. **Adjust for Time Lag:** If one object starts earlier, calculate the distance it covered alone and subtract it from the total distance.
3. **Calculate Relative Speed:** Use the formulas above to find the effective speed.
4. **Apply Time Formula:** Use $T = \frac{\text{Distance}}{\text{Relative Speed}}$ to find the time taken to meet.
5. **Final Calculation:** If asked for distance, multiply the time found in Step 4 by the individual speed of the relevant object.

---

## Shortcut Tricks

* **Trick:** For two objects meeting, $T = \frac{\text{Initial Gap}}{S_{rel}}$.
* **Why it works:** It bypasses complex algebraic equations by focusing only on the gap that needs to be closed.
* **When to use:** When you need the time to "catch up" or "meet."
* **Example:** Q24: Gap = 0.1 km, $S_{rel} = 2$ kmph. $T = \frac{0.1}{2} = 0.05$ hours.

---

## Common Mistakes

* **Mistake:** Forgetting to adjust for the "head start" time.
    * **Fix:** Calculate the distance covered by the first object during the time gap before applying relative speed.
* **Mistake:** Using $S_1 + S_2$ for same-direction problems.
    * **Fix:** Always subtract speeds when moving in the same direction.
* **Mistake:** Mixing units (e.g., kmph with metres).
    * **Fix:** Convert all units to km/hr and km, or m/sec and metres before calculating.

---

## Worked Example (Step-by-Step)

**Question:** A thief is spotted by a policeman from 100m away. Thief speed = 8 km/hr, Policeman speed = 10 km/hr. How far will the thief have run before being overtaken?

**Solution:**
1. **Identify Direction:** Same direction (chase).
2. **Relative Speed:** $10 - 8 = 2$ km/hr.
3. **Time to catch:** Gap is 100m = 0.1 km. $T = \frac{0.1}{2} = 0.05$ hours.
4. **Thief's distance:** Distance = Speed $\times$ Time = $8 \text{ km/hr} \times 0.05 \text{ hr} = 0.4$ km.
5. **Convert:** $0.4 \text{ km} = 400$ metres.

**Answer:** 400 metres.

---

## Similar Patterns
* **Average Speed:** Confused when the question asks for the average of the whole trip rather than the meeting point; look for "total distance / total time" instead of relative speed.

---

## Revision Summary
* **Key formula:** $S_{rel} = S_1 \pm S_2$.
* **Spot it by:** "Same direction" or "Opposite direction" keywords.
* **First move:** Calculate the gap distance and relative speed.
* **Fastest method:** $T = \frac{\text{Gap}}{S_{rel}}$.
* **Biggest trap:** Forgetting to convert units (m to km) or ignoring the head-start time.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Basic Algebra** — Solving linear equations like $ax + b = c$.
* **Unit Conversion** — Converting km/hr to m/sec by multiplying by $\frac{5}{18}$.

### Formulas You Must Know First
$$
\text{Distance} = \text{Speed} \times \text{Time}
$$
**What it means:** The fundamental relationship between motion variables.
**Example:** If speed is 60 kmph and time is 2 hours, distance is 120 km.

### Terms Used In This Pattern
* **Relative Speed** — The speed of one object as observed from the other.
* **Overtake** — To catch up with and pass an object moving in the same direction.