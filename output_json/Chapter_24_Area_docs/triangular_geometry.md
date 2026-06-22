# Triangular Geometry

## Overview
This pattern involves calculating the area of complex fields or triangles. The central idea is to decompose complex shapes into simpler triangles and trapezoids or to use side-length properties when the height is unknown.

---

## Recognition Clues
* **Keywords:** "Area of the field," "triangular field," "sides measure," "hypotenuse," "cultivating the field."
* **Given:** Three sides of a triangle, or a combination of base/height segments, or cost/rate of cultivation.
* **Asked:** Total area of the shape or specific dimensions (base/height).

---

## Key Formulas

### [Area of Triangle (Base-Height)]
$$
\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}
$$
**Variables:** $b$ = base, $h$ = perpendicular height.
**When to use:** When the base and perpendicular height are known or can be derived.
**Worked example:** For $\Delta BFE$ with base $48$ and height $24$: $\text{Area} = \frac{1}{2} \times 48 \times 24 = 576$.

### [Heron’s Formula]
$$
\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}
$$
**Variables:** $s = \frac{a+b+c}{2}$ (semi-perimeter), $a, b, c$ = sides of the triangle.
**When to use:** When all three side lengths are provided.
**Worked example:** Sides $15, 16, 17 \implies s=24$. $\text{Area} = \sqrt{24(9)(8)(7)} = 24\sqrt{21}$.

### [Pythagorean Theorem]
$$
a^2 + b^2 = c^2
$$
**Variables:** $c$ = hypotenuse, $a, b$ = legs of a right triangle.
**When to use:** To find a missing side in a right-angled triangle.
**Worked example:** Hypotenuse $65$, side $25 \implies b^2 = 65^2 - 25^2 = 3600 \implies b=60$.

---

## Solution Framework
1. **Identify the shape:** Determine if it is a single triangle or a composite figure.
2. **Extract dimensions:** List all given lengths; calculate missing segments using subtraction or Pythagoras.
3. **Select formula:** Use Heron’s if 3 sides are known; use $\frac{1}{2}bh$ if base/height are known.
4. **Calculate components:** Solve for individual areas of triangles/trapezoids.
5. **Sum/Finalize:** Add individual areas or solve for the unknown variable using the total area.

---

## Shortcut Tricks
* **Trick:** Use Pythagorean triples (e.g., 3-4-5, 5-12-13) to find missing sides instantly.
* **Why it works:** It eliminates the need to calculate squares and square roots.
* **When to use:** When the triangle is right-angled and sides are multiples of common triples.
* **Example:** If hypotenuse is $65$ ($13 \times 5$) and side is $25$ ($5 \times 5$), the other side is $12 \times 5 = 60$.

---

## Common Mistakes
* **Mistake:** Using the hypotenuse as the height in $\frac{1}{2}bh$.
    * **Fix:** Only use the two sides forming the $90^\circ$ angle as base and height.
* **Mistake:** Forgetting to convert units (e.g., hectares to $m^2$).
    * **Fix:** Always convert to the same unit before calculating area ($1 \text{ hectare} = 10,000 \text{ m}^2$).
* **Mistake:** Calculating perimeter instead of semi-perimeter ($s$) in Heron's formula.
    * **Fix:** Always divide the sum of sides by $2$ first.

---

## Worked Example (Step-by-Step)

**Question:** Find the area of a right–angled triangle with hypotenuse $65$ cm and one side $25$ cm.

**Solution:**
1. **Identify:** It is a right-angled triangle.
2. **Extract:** Hypotenuse $c=65$, side $a=25$.
3. **Calculate missing side:** $b = \sqrt{65^2 - 25^2} = \sqrt{4225 - 625} = \sqrt{3600} = 60$.
4. **Apply Formula:** $\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 25 \times 60$.
5. **Finalize:** $25 \times 30 = 750$.

**Answer:** $750 \text{ cm}^2$.

---

## Similar Patterns
**Quadrilateral Geometry:** Distinguish by counting sides; if the shape has four sides, use the trapezoid or parallelogram area formulas instead of triangle formulas.

---

## Revision Summary
* **Key formula:** $\text{Area} = \frac{1}{2}bh$ or $\sqrt{s(s-a)(s-b)(s-c)}$.
* **Spot it by:** Looking for "triangular field" or "three sides given."
* **First move:** Identify if you have base/height or three sides.
* **Fastest method:** Use Pythagorean triples for right triangles.
* **Biggest trap:** Using the hypotenuse as a base/height in $\frac{1}{2}bh$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Right-angled triangle** — A triangle where one angle is $90^\circ$.
* **Trapezoid** — A quadrilateral with at least one pair of parallel sides; $\text{Area} = \frac{1}{2}(a+b)h$.
* **Semi-perimeter** — Half the perimeter of a triangle, $s = \frac{a+b+c}{2}$.

### Formulas You Must Know First
* **Pythagoras:** $a^2 + b^2 = c^2$.
* **Unit Conversion:** $1 \text{ hectare} = 10,000 \text{ m}^2$.

### Terms Used In This Pattern
* **Hypotenuse** — The longest side of a right-angled triangle, opposite the $90^\circ$ angle.
* **Altitude** — The perpendicular height of a triangle from a vertex to the opposite side.