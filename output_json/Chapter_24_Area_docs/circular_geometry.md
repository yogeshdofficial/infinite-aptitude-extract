# Geometry of Rectangles and Circles

## Overview
This pattern involves calculating dimensions, areas, and perimeters of rectangles and circles. The central idea is to identify the geometric shape, select the appropriate formula for the requested property (diagonal, area, or circumference), and solve for the unknown variable.

---

## Recognition Clues
* **Keywords:** "rectangular garden," "circular field," "diagonal," "perimeter," "area," "fencing," "rope," "tethered."
* **Given:** Length/breadth of a rectangle, area of a circle, or ratios of dimensions/circumferences.
* **Asked:** Maximum distance (diagonal), length of a rope (radius), cost of fencing (circumference), or ratio of areas.

---

## Key Formulas

### [Diagonal of a Rectangle]
$$
d = \sqrt{l^2 + b^2}
$$
**Variables:** $d$ = diagonal, $l$ = length, $b$ = breadth.
**When to use:** Finding the maximum distance between two points on a rectangular perimeter.
**Worked example:** $l=100, b=50 \implies d = \sqrt{100^2 + 50^2} = \sqrt{12500} \approx 111.8$ m.

### [Circle Properties]
$$
\text{Area} = \pi R^2, \quad \text{Circumference} = 2\pi R
$$
**Variables:** $R$ = radius, $\pi \approx \frac{22}{7}$.
**When to use:** Finding the grazing area (radius) or fencing cost (circumference).
**Worked example:** Area = $9856 \implies R^2 = 9856 \times \frac{7}{22} = 3136 \implies R = 56$ m.

---

## Solution Framework
1. **Identify the shape:** Determine if the problem involves a rectangle or a circle.
2. **Extract given values:** Note the dimensions, area, or ratios provided.
3. **Convert units:** Ensure all units match (e.g., convert hectares to $m^2$ by multiplying by $10,000$).
4. **Apply the formula:** Use the relevant formula to isolate the unknown variable.
5. **Calculate final result:** Perform the arithmetic to find the requested value (cost, ratio, or length).

---

## Shortcut Tricks
* **Trick:** If the ratio of circumferences of two circles is $a:b$, the ratio of their areas is $a^2:b^2$.
* **Why it works:** Area is proportional to the square of the radius ($R^2$), and circumference is proportional to the radius ($R$).
* **When to use:** When comparing two circles without needing to calculate their actual radii.
* **Example:** Circumference ratio $2:3 \implies$ Area ratio $2^2:3^2 = 4:9$.

---

## Common Mistakes
* **Mistake:** Using diameter instead of radius in circle formulas.
    * **Why it happens:** Forgetting that $R$ in $\pi R^2$ is radius. **Fix:** Always divide diameter by 2 first.
* **Mistake:** Forgetting unit conversions (hectares to $m^2$).
    * **Why it happens:** Overlooking the unit mismatch. **Fix:** Check units before starting calculations.
* **Mistake:** Confusing perimeter with diagonal.
    * **Why it happens:** Misreading "maximum distance" as "boundary length." **Fix:** Remember "maximum distance" in a rectangle is always the diagonal.

---

## Worked Example (Step-by-Step)

**Question:** The area of a circular field is 13.86 hectares. Find the cost of fencing it at the rate of ₹ 4.40 per metre.

**Solution:**
1. **Convert units:** $13.86 \text{ hectares} = 13.86 \times 10,000 = 138,600 \text{ m}^2$.
2. **Find Radius:** $\pi R^2 = 138,600 \implies R^2 = 138,600 \times \frac{7}{22} = 44,100 \implies R = 210 \text{ m}$.
3. **Find Circumference:** $2\pi R = 2 \times \frac{22}{7} \times 210 = 1,320 \text{ m}$.
4. **Calculate Cost:** $1,320 \text{ m} \times ₹ 4.40/\text{m} = ₹ 5,808$.

**Answer:** ₹ 5,808.

---

## Similar Patterns
**Polygon Geometry:** Distinguish by the number of sides; rectangles have 4 sides and specific diagonal rules, while circles rely on $\pi$ and radius.

---

## Revision Summary
* **Key formula:** $d = \sqrt{l^2+b^2}$ (rectangle) and $A = \pi R^2$ (circle).
* **Spot it by:** Keywords like "diagonal," "fencing," or "grazing area."
* **First move:** Convert all units to standard (metres/square metres).
* **Fastest method:** Use the square of the ratio for area comparisons.
* **Biggest trap:** Using diameter instead of radius for circle calculations.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Pythagorean Theorem** — In a right triangle, $a^2 + b^2 = c^2$.
* **Unit Conversion** — $1 \text{ hectare} = 10,000 \text{ m}^2$.
* **Ratios** — Understanding that if $x:y = a:b$, then $x^2:y^2 = a^2:b^2$.

### Formulas You Must Know First
$$
a^2 + b^2 = c^2
$$
**What it means:** The square of the hypotenuse equals the sum of the squares of the other two sides.

### Terms Used In This Pattern
* **Diagonal** — The line segment connecting two non-adjacent corners of a rectangle.
* **Circumference** — The perimeter of a circle.
* **Radius** — The distance from the center of a circle to its edge.