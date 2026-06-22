# Square Properties

## Overview
These questions involve calculating dimensions, areas, or perimeters of squares based on given geometric properties. The central idea is that all square properties (area, diagonal, perimeter) are derived from a single variable: the side length $a$.

---

## Recognition Clues
* **Keywords:** "Square", "Perimeter", "Area", "Diagonal", "Percentage change", "Ratio".
* **Given:** Perimeter, Area, or Diagonal of one or more squares.
* **Asked:** Perimeter, Area, or Diagonal of a related square, or percentage change in area.

---

## Key Formulas

### [Area from Side]
$$
\text{Area} = a^2
$$
**Variables:** $a$ = side length.
**When to use:** When side length is known or easily derived from perimeter ($a = \frac{P}{4}$).
**Example:** If side $a = 10$, Area $= 10^2 = 100$.

### [Area from Diagonal]
$$
\text{Area} = \frac{1}{2} \times d^2
$$
**Variables:** $d$ = diagonal length.
**When to use:** When the diagonal is given directly.
**Example:** If diagonal $d = 3.8$, Area $= 0.5 \times (3.8)^2 = 7.22$.

### [Diagonal from Side]
$$
d = a\sqrt{2}
$$
**Variables:** $a$ = side length, $d$ = diagonal.
**When to use:** To find the longest straight line (bamboo) that fits in a square.
**Example:** If side $a = 10$, $d = 10\sqrt{2} \approx 14.14$.

---

## Solution Framework
1. **Identify the target:** Determine if you need side, area, or diagonal.
2. **Standardize:** Convert all given values (perimeter/diagonal) into the side length $a$ or diagonal $d$.
3. **Apply Formula:** Use the relevant formula to find the missing property.
4. **Final Conversion:** If the question asks for perimeter, multiply the final side by 4. If it asks for percentage change, use $\frac{\text{New} - \text{Old}}{\text{Old}} \times 100$.

---

## Shortcut Tricks
* **Trick:** For percentage change in area, if side changes by $x\%$, area changes by $(2x + \frac{x^2}{100})\%$.
* **Why it works:** Derived from $(1 + \frac{x}{100})^2 = 1 + \frac{2x}{100} + \frac{x^2}{10000}$.
* **When to use:** When side length increases or decreases by a percentage.
* **Example:** Side increases by 25%: $2(25) + \frac{25^2}{100} = 50 + 6.25 = 56.25\%$.

---

## Common Mistakes
* **Mistake:** Subtracting perimeters instead of areas. **Fix:** Always convert to area first, perform the operation, then convert back to side/perimeter.
* **Mistake:** Adding percentages directly (e.g., 25% + 25% = 50%). **Fix:** Use the $(2x + \frac{x^2}{100})$ formula for area changes.
* **Mistake:** Forgetting to divide by 2 when using the diagonal formula for area. **Fix:** Remember Area $= 0.5 \times d^2$.

---

## Worked Example (Step-by-Step)

**Question:** The perimeters of two squares are 40 cm and 32 cm. Find the perimeter of a third square whose area is equal to the difference of the areas of the two squares.

**Solution:**
1. **Standardize:** Side 1 $= \frac{40}{4} = 10$. Side 2 $= \frac{32}{4} = 8$.
2. **Calculate Areas:** Area 1 $= 10^2 = 100$. Area 2 $= 8^2 = 64$.
3. **Difference:** Area 3 $= 100 - 64 = 36$.
4. **Find Side 3:** Side 3 $= \sqrt{36} = 6$.
5. **Final Conversion:** Perimeter 3 $= 6 \times 4 = 24$ cm.

**Answer:** 24 cm.

---

## Similar Patterns
* **Rectangle Properties:** Distinguished by having length $\neq$ breadth; requires two variables ($l$ and $b$) instead of one ($a$).

---

## Revision Summary
* **Key formula:** Area $= a^2$ or $0.5 \times d^2$.
* **Spot it by:** Keywords "Square", "Area", "Diagonal".
* **First move:** Convert given perimeter/diagonal to side length $a$.
* **Fastest method:** Use $(2x + \frac{x^2}{100})\%$ for percentage area changes.
* **Biggest trap:** Subtracting perimeters instead of areas.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Square:** A quadrilateral with four equal sides and $90^\circ$ angles.
* **Pythagorean Theorem:** $a^2 + b^2 = c^2$; used to derive $d = a\sqrt{2}$.
* **Percentage Change:** $\frac{\text{New Value} - \text{Original Value}}{\text{Original Value}} \times 100$.

### Formulas You Must Know First
* **Perimeter of Square:** $P = 4a$.
* **Area of Square:** $A = a^2$.

### Terms Used In This Pattern
* **Diagonal:** The line segment connecting opposite corners of the square.
* **Perimeter:** The total length of the boundary of the square.