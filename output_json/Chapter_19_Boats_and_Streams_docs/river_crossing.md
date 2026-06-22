# River Crossing

## Overview
This pattern involves a person or boat attempting to cross a river along the shortest path (perpendicular to the banks). The central idea is that the swimming speed, current speed, and effective speed form a right-angled triangle, allowing the use of the Pythagorean theorem.

---

## Recognition Clues
* **Keywords:** "cross the river perpendicularly," "straight," "shortest path," "width of the river."
* **Given:** Swimming speed in still water ($u$), current speed ($v$), and river width ($w$).
* **Asked:** Time taken to cross or the velocity of the current.

---

## Key Formulas

### [Effective Speed for Perpendicular Crossing]
$$
v_{eff} = \sqrt{u^2 - v^2}
$$

**Variables:**
- $v_{eff}$ = effective speed across the river
- $u$ = swimming speed in still water
- $v$ = current speed

**When to use:** When you need to find the actual speed at which the person moves from one bank to the other while the current is pushing them.

**Worked example:** If $u = 25$ m/min and $v = 15$ m/min, then $v_{eff} = \sqrt{25^2 - 15^2} = \sqrt{625 - 225} = \sqrt{400} = 20$ m/min.

---

## Solution Framework

1. **Identify $u$ and $v$:** Extract the swimming speed in still water and the current speed from the question.
2. **Calculate $v_{eff}$:** Use the Pythagorean formula $v_{eff} = \sqrt{u^2 - v^2}$ to find the net speed perpendicular to the bank.
3. **Calculate Time:** Use $\text{Time} = \frac{\text{Width}}{v_{eff}}$.
4. **Unit Conversion:** Ensure time units (hours/minutes) match the speed units (km/hr or m/min).

---

## Shortcut Tricks

* **Trick:** If given time in still water ($t_1$) and time in flowing water ($t_2$) for the same width ($w$), use $v = \sqrt{(\frac{w}{t_2})^2 - (\frac{w}{t_1})^2}$.
* **Why it works:** It directly relates the two scenarios using the Pythagorean relationship without calculating $u$ and $v_{eff}$ separately.
* **When to use:** When the question provides two different times for the same distance.
* **Example:** $w=100, t_1=4, t_2=5$. $v = \sqrt{(100/5)^2 - (100/4)^2}$ is incorrect; use $v = \sqrt{u^2 - v_{eff}^2} = \sqrt{25^2 - 20^2} = 15$.

---

## Common Mistakes

* **Mistake:** Adding or subtracting speeds ($u+v$ or $u-v$).
    * **Why it happens:** Confusing "downstream/upstream" travel with "perpendicular" crossing.
    * **Fix:** Use the Pythagorean theorem for perpendicular paths.
* **Mistake:** Forgetting to convert units.
    * **Why it happens:** Speed is in km/hr but time is asked in minutes.
    * **Fix:** Always check if distance/speed units match time units.

---

## Worked Example (Step-by-Step)

**Question:** A man wishes to cross a river perpendicularly. In still water he takes 4 minutes to cross the river, but in a flowing river he takes 5 minutes. If the river is 100 metres wide, the velocity of the flowing water is?

**Solution:**
1. **Find $u$:** In still water, $u = \frac{\text{Distance}}{\text{Time}} = \frac{100}{4} = 25$ m/min.
2. **Find $v_{eff}$:** In flowing water, $v_{eff} = \frac{\text{Distance}}{\text{Time}} = \frac{100}{5} = 20$ m/min.
3. **Apply Formula:** $v_{eff} = \sqrt{u^2 - v^2} \Rightarrow 20 = \sqrt{25^2 - v^2}$.
4. **Solve for $v$:** $400 = 625 - v^2 \Rightarrow v^2 = 225 \Rightarrow v = 15$ m/min.

**Answer:** 15 m/min.

---

## Similar Patterns

**Downstream/Upstream:** Distinguish by the phrase "along the stream" or "against the stream" versus "perpendicularly" or "straight across."

---

## Revision Summary

* **Key formula:** $v_{eff} = \sqrt{u^2 - v^2}$.
* **Spot it by:** "Cross perpendicularly" or "shortest path."
* **First move:** Calculate $u$ and $v_{eff}$ from distance/time if not given.
* **Fastest method:** Use the Pythagorean relationship between $u, v,$ and $v_{eff}$.
* **Biggest trap:** Using $u+v$ or $u-v$ instead of the square root formula.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Pythagorean Theorem:** In a right triangle, $a^2 + b^2 = c^2$, where $c$ is the hypotenuse.
* **Basic Kinematics:** $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$.

### Formulas You Must Know First
* $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$: Used to derive $u$ and $v_{eff}$ from given data.

### Terms Used In This Pattern
* **Still Water:** Speed of the swimmer without any current influence.
* **Current:** The speed of the flowing water.
* **Perpendicularly:** Crossing at a 90-degree angle to the river bank.