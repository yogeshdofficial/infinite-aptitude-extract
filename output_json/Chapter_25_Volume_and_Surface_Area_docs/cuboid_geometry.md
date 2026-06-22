# Cuboid Geometry

## Overview
These questions involve calculating the physical properties (volume, surface area, or diagonal) of a rectangular block or room. The central idea is to identify the three dimensions—length ($l$), breadth ($b$), and height ($h$)—and apply the appropriate geometric formula.

---

## Recognition Clues
* **Keywords:** "rectangular block," "room," "wall," "tray," "open box," "bamboo pole," "dimensions."
* **Given:** Length, breadth, and height (or ratios/relationships between them).
* **Asked:** Volume, surface area, length of the longest object (diagonal), or weight (volume $\times$ density).
* **Visual:** Look for 3D objects where the base and height are distinct.

---

## Key Formulas

### [Volume of a Cuboid]
$$
V = l \times b \times h
$$
**Variables:** $l$ = length, $b$ = breadth, $h$ = height.
**When to use:** When asked for capacity or total space occupied.
**Worked example:** $l=16, b=14, h=7 \implies V = 16 \times 14 \times 7 = 1568 \text{ m}^3$.

### [Surface Area of a Cuboid]
$$
SA = 2(lb + bh + lh)
$$
**Variables:** $l, b, h$ as defined above.
**When to use:** When asked for the total area of all six faces.
**Worked example:** $l=16, b=14, h=7 \implies SA = 2(224 + 98 + 112) = 868 \text{ m}^2$.

### [Space Diagonal]
$$
d = \sqrt{l^2 + b^2 + h^2}
$$
**Variables:** $d$ = length of the longest object (e.g., bamboo pole).
**When to use:** When asked for the longest straight line that fits inside the cuboid.
**Worked example:** $l=12, b=9, h=8 \implies d = \sqrt{144 + 81 + 64} = \sqrt{289} = 17 \text{ m}$.

---

## Solution Framework
1. **Identify Dimensions:** Extract $l, b, h$ from the text. If given as ratios, assign $x$ (e.g., $l=40x, b=x, h=5x$).
2. **Adjust for Modifications:** If corners are cut or thickness is involved, subtract the change from the original dimensions (e.g., $l_{new} = l - 2 \times \text{thickness}$).
3. **Select Formula:** Choose Volume, Surface Area, or Diagonal based on the question.
4. **Calculate:** Perform the arithmetic, ensuring units are consistent (e.g., convert all to cm or m).
5. **Final Conversion:** If the question asks for weight or a specific unit, multiply/divide by the given conversion factor.

---

## Shortcut Tricks
* **No shortcut faster than the standard framework:** The geometry of a cuboid is rigid; always define your $l, b, h$ clearly first to avoid errors.

---

## Common Mistakes
* **Mistake:** Subtracting thickness from height twice in an "open box."
    * **Fix:** For an open box, subtract thickness only once from height (the bottom).
* **Mistake:** Forgetting to subtract the cut-out square from *both* ends of the length/breadth.
    * **Fix:** Always subtract $2 \times \text{side}$ from the original dimension.
* **Mistake:** Confusing units (e.g., meters vs. centimeters).
    * **Fix:** Convert all dimensions to the same unit *before* calculating volume.

---

## Worked Example (Step-by-Step)

**Question:** A rectangular sheet of paper, 10 cm long and 8 cm wide has squares of side 2 cm cut from each of its corners. The sheet is then folded to form a tray of depth 2 cm. Find the volume of this tray.

**Solution:**
1. **Identify Dimensions:** Original $l=10, b=8$.
2. **Adjust for Modifications:** Cutting 2 cm squares from corners reduces length and breadth by $2 \times 2 = 4$ cm.
   - New $l = 10 - 4 = 6$ cm.
   - New $b = 8 - 4 = 4$ cm.
   - Depth ($h$) = 2 cm.
3. **Select Formula:** $V = l \times b \times h$.
4. **Calculate:** $V = 6 \times 4 \times 2 = 48 \text{ cm}^3$.

**Answer:** $48 \text{ cm}^3$.

---

## Similar Patterns
**Cube Geometry:** Distinguish by checking if all dimensions are equal ($l=b=h=a$). If they are, use $V=a^3$ and $SA=6a^2$.

---

## Revision Summary
* **Key formula:** $V=lbh$, $SA=2(lb+bh+lh)$, $d=\sqrt{l^2+b^2+h^2}$.
* **Spot it by:** Looking for 3D rectangular objects and dimensions.
* **First move:** Clearly list $l, b, h$ and adjust for any cut-outs or thickness.
* **Fastest method:** Direct substitution into the relevant formula.
* **Biggest trap:** Forgetting to subtract thickness/cut-outs from both sides of the dimension.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Pythagorean Theorem** — In a right-angled triangle, $a^2 + b^2 = c^2$.
* **Volume** — The amount of 3D space an object occupies.
* **Surface Area** — The sum of the areas of all faces of a 3D object.

### Formulas You Must Know First
* **Area of a Rectangle** = $l \times b$.
* **Density/Weight relationship** = $\text{Weight} = \text{Volume} \times \text{Density}$.

### Terms Used In This Pattern
* **Cuboid** — A 3D box with 6 rectangular faces.
* **Diagonal** — The longest distance between two opposite corners of a cuboid.
* **Thickness** — The width of the material forming the walls of a box.