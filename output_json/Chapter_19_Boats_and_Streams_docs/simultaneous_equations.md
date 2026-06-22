# Simultaneous Equations (Boats and Streams)

## Overview
This pattern involves problems where a boat covers two different sets of upstream and downstream distances in two different total times. The central idea is to treat the reciprocal of speeds ($1/u$ and $1/v$) as variables to form a system of linear equations that can be solved via elimination.

---

## Recognition Clues
* **Keywords:** "Upstream", "Downstream", "Total time", "Still water", "Speed of current".
* **Given:** Two distinct scenarios, each providing a distance upstream, a distance downstream, and the total time taken for that trip.
* **Asked:** Speed of the boat in still water ($u$) or speed of the current ($v$).
* **Visual cue:** Look for two equations of the form $\frac{D_1}{u} + \frac{D_2}{v} = T$.

---

## Key Formulas

### [Still Water Speed]
$$
\text{Still Water Speed} = \frac{v + u}{2}
$$
**Variables:** $v$ = downstream speed, $u$ = upstream speed.
**When to use:** When the question asks for the boat's speed in still water after finding $u$ and $v$.
**Example:** If $v=11$ and $u=5$, Still Water Speed = $\frac{11+5}{2} = 8$ km/hr.

### [Current Speed]
$$
\text{Current Speed} = \frac{v - u}{2}
$$
**Variables:** $v$ = downstream speed, $u$ = upstream speed.
**When to use:** When the question asks for the speed of the stream/current.
**Example:** If $v=11$ and $u=5$, Current Speed = $\frac{11-5}{2} = 3$ km/hr.

---

## Solution Framework
1. **Define Variables:** Let $u$ = upstream speed and $v$ = downstream speed.
2. **Set Equations:** Write two equations using $\frac{\text{Distance}}{\text{Speed}} = \text{Time}$.
3. **Simplify:** Divide equations by common factors to make coefficients smaller.
4. **Eliminate:** Multiply equations to make the coefficients of $1/u$ or $1/v$ identical, then subtract.
5. **Solve:** Find $u$ and $v$, then apply the Still Water or Current speed formulas.

---

## Shortcut Tricks
* **Trick:** If the distances are multiples, simplify the equations by dividing by the greatest common divisor (GCD) before solving.
* **Why it works:** It reduces the magnitude of numbers, minimizing arithmetic errors during the elimination step.
* **When to use:** Always, when the distances and time share a common factor (e.g., $24/u + 36/v = 6$ becomes $4/u + 6/v = 1$).

---

## Common Mistakes
* **Mistake:** Forgetting to divide by 2 when calculating still water or current speed.
* **Why it happens:** Rushing to the final answer after finding $u$ and $v$.
* **Fix:** Always write the final formula $\frac{v \pm u}{2}$ clearly on your scratchpad.
* **Mistake:** Confusing $u$ (upstream) and $v$ (downstream) in the equations.
* **Why it happens:** Upstream is always slower ($u < v$); if your calculation shows $u > v$, you have swapped them.

---

## Worked Example (Q9)
**Question:** A man can row 40 km upstream and 55 km downstream in 13 hours. Also, he can row 30 km upstream and 44 km downstream in 10 hours. Find the speed of the man in still water and the speed of the current.

**Solution:**
1. **Equations:** $\frac{40}{u} + \frac{55}{v} = 13$ (i) and $\frac{30}{u} + \frac{44}{v} = 10$ (ii).
2. **Eliminate $1/u$:** Multiply (i) by 3 and (ii) by 4:
   $\frac{120}{u} + \frac{165}{v} = 39$
   $\frac{120}{u} + \frac{176}{v} = 40$
3. **Subtract:** $(\frac{176}{v} - \frac{165}{v}) = 40 - 39 \implies \frac{11}{v} = 1 \implies v = 11$.
4. **Solve for $u$:** Substitute $v=11$ into (i): $\frac{40}{u} + \frac{55}{11} = 13 \implies \frac{40}{u} + 5 = 13 \implies \frac{40}{u} = 8 \implies u = 5$.
5. **Final:** Still water = $\frac{11+5}{2} = 8$ km/hr; Current = $\frac{11-5}{2} = 3$ km/hr.

**Answer:** Still water speed = 8 km/hr, Current speed = 3 km/hr.

---

## Similar Patterns
* **Work and Wages:** Distinguished by the absence of "upstream/downstream" and the use of "man-days" instead of "distance/speed".

---

## Revision Summary
* **Key formula:** $u = \text{upstream speed}$, $v = \text{downstream speed}$.
* **Spot it by:** Two scenarios with total time for upstream and downstream distances.
* **First move:** Set up two equations: $\frac{D_1}{u} + \frac{D_2}{v} = T$.
* **Fastest method:** Simplify equations by dividing by common factors first.
* **Biggest trap:** Forgetting to divide by 2 for final speed calculations.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Upstream:** Speed of boat minus speed of current ($u - v$).
* **Downstream:** Speed of boat plus speed of current ($u + v$).
* **Time-Distance:** $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$.

### Formulas You Must Know First
* **Speed in still water:** $\frac{1}{2}(\text{Downstream} + \text{Upstream})$.
* **Speed of current:** $\frac{1}{2}(\text{Downstream} - \text{Upstream})$.

### Terms Used In This Pattern
* **Still Water:** The speed of the boat if the water were not moving.
* **Current/Stream:** The speed of the water flow.