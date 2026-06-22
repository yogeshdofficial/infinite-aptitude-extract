# Time Variation

## Overview
This pattern involves scenarios where a change in speed results in a predictable change in the time taken to cover a fixed distance. The central idea is to equate the distance ($D = \text{Speed} \times \text{Time}$) for both scenarios to solve for the unknown variable.

---

## Recognition Clues
* **Keywords:** "late," "early," "less time," "more time," "usual speed," "accident," "reduced speed."
* **Given:** Two different speeds and the resulting time difference (or a ratio of speeds and the time difference).
* **Asked:** Usually the distance, the usual time, or the original speed.
* **Scan for:** A fixed distance being covered at two different rates, leading to a specific time gap.

---

## Key Formulas

### [Distance from Time Difference]
$$
D = \frac{v_1 \times v_2}{|v_1 - v_2|} \times \Delta t
$$

**Variables:**
- $v_1, v_2$ = the two different speeds
- $\Delta t$ = the difference in time (must be in hours)

**When to use:** When you have two speeds and the total time difference (e.g., "late" vs "early").

**Worked example:** If a person travels at $3$ km/hr and $4$ km/hr with a total time difference of $70$ minutes ($7/6$ hours):
$D = \frac{3 \times 4}{4 - 3} \times \frac{7}{6} = 12 \times \frac{7}{6} = 14$ km.

---

## Solution Framework

1. **Step 1: Standardize Units** — Convert all time values into hours (e.g., $40$ min $= 40/60 = 2/3$ hr).
2. **Step 2: Define Variables** — Assign $x$ to the unknown (usually speed or distance) based on the question.
3. **Step 3: Set up the Equation** — Use the logic $\frac{D}{v_{slow}} - \frac{D}{v_{fast}} = \text{Time Difference}$.
4. **Step 4: Solve for $x$** — Clear denominators by multiplying by the common factor and solve the resulting algebraic equation.

---

## Shortcut Tricks

* **Trick:** If speed ratio is $a:b$, time ratio is $b:a$.
* **Why it works:** Since $D = S \times T$, if $D$ is constant, $S$ and $T$ are inversely proportional.
* **When to use:** When the problem gives a fraction of the usual speed (e.g., $3/4$ of usual speed).
* **Example:** Speed becomes $3/4$ of usual $\rightarrow$ Time becomes $4/3$ of usual. If $4/3T - T = 20$ min, then $1/3T = 20 \rightarrow T = 60$ min.

---

## Common Mistakes

* **Mistake:** Subtracting "late" and "early" times (e.g., $40 - 30$).
    * **Fix:** Always **add** them ($40 + 30 = 70$ min) because one is before the target and one is after.
* **Mistake:** Forgetting to convert minutes to hours.
    * **Fix:** Always divide minutes by $60$ before plugging into the speed formula.
* **Mistake:** Mixing up the denominator in the time fraction.
    * **Fix:** The larger time (smaller speed) must be the first term in the subtraction: $\frac{D}{v_{small}} - \frac{D}{v_{large}} = \Delta t$.

---

## Worked Example (Step-by-Step)

**Question:** A person reaches his destination $40$ minutes late if his speed is $3$ km/hr, and reaches $30$ minutes before time if his speed is $4$ km/hr. Find the distance.

**Solution:**
1. **Standardize:** Late $40$ min $= 2/3$ hr; Early $30$ min $= 1/2$ hr. Total time difference $= 2/3 + 1/2 = 7/6$ hr.
2. **Define:** Let distance be $D$.
3. **Equation:** $\frac{D}{3} - \frac{D}{4} = \frac{7}{6}$.
4. **Solve:** $\frac{4D - 3D}{12} = \frac{7}{6} \rightarrow \frac{D}{12} = \frac{7}{6} \rightarrow D = 14$ km.

**Answer:** $14$ km.

---

## Similar Patterns
* **Average Speed Problems:** These involve total distance/total time; distinguish by checking if the *time difference* is given (Time Variation) or if the *total time* is given (Average Speed).

---

## Revision Summary
* **Key formula:** $D = \frac{v_1 v_2}{\Delta v} \times \Delta t$.
* **Spot it by:** "Late/Early" keywords and two different speeds.
* **First move:** Convert all time units to hours.
* **Fastest method:** Use the ratio trick for speed fractions or the formula for speed values.
* **Biggest trap:** Subtracting instead of adding "late" and "early" times.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Algebraic Fractions** — Solving equations like $\frac{x}{a} - \frac{x}{b} = c$.
* **Inverse Proportion** — If distance is constant, speed and time are inversely related.

### Formulas You Must Know First
$$
\text{Distance} = \text{Speed} \times \text{Time}
$$
**What it means:** The fundamental relationship between motion variables.

### Terms Used In This Pattern
* **Usual Time:** The scheduled time to reach a destination.
* **Relative Speed:** The difference between two speeds when moving in the same direction.