# Composite Solid Surface Area

## Overview
This pattern involves finding the total surface area of a solid formed by joining multiple basic shapes (e.g., a cylinder with hemispherical ends). The central idea is to sum the **curved** surface areas of the individual components while ignoring the faces that are hidden inside the joint.

---

## Recognition Clues
* **Keywords:** "Solid in the form of...", "hemispherical ends", "total length of the solid".
* **Given:** Total length of the composite object and a ratio relating dimensions (e.g., diameter to height).
* **Asked:** Total surface area of the resulting solid.

---

## Key Formulas

### [Total Surface Area of Composite Solid]
$$
\text{TSA} = \text{Sum of exposed curved surface areas}
$$

**Variables:**
- $r$ = radius of the cylinder/hemisphere
- $h$ = height of the cylindrical part

**When to use:** When a solid is composed of multiple parts joined together.

**Worked example:** For a cylinder with two hemispherical ends:
$\text{TSA} = (2\pi rh) + 2(2\pi r^2) = 2\pi rh + 4\pi r^2$.
Given $r=3.5$ and $h=28$:
$\text{TSA} = 2 \times \frac{22}{7} \times 3.5 \times 28 + 4 \times \frac{22}{7} \times 3.5^2 = 616 + 154 = 770 \text{ cm}^2$.

---

## Solution Framework

1. **Define variables:** Assign $r$ as the radius for all components (since they must match at the joints).
2. **Express dimensions in terms of $r$:** Use the given ratios to write the cylinder height $h$ in terms of $r$.
3. **Solve for $r$:** Use the "Total Length" equation (e.g., $h + 2r = \text{Total Length}$) to find the numerical value of $r$.
4. **Calculate Area:** Plug $r$ and $h$ into the sum of the curved surface areas formula.

---

## Shortcut Tricks

* **Trick:** Factor out common terms before calculating.
* **Why it works:** It reduces the number of multiplications involving $\pi$ and decimals.
* **When to use it:** Always, when the formula is $2\pi rh + 4\pi r^2$.
* **Example:** $2\pi r(h + 2r)$. With $r=3.5, h=28$: $2 \times \frac{22}{7} \times 3.5 \times (28 + 7) = 22 \times 35 = 770$.

---

## Common Mistakes

* **Mistake:** Including the flat circular bases of the cylinder in the total area.
* **Why it happens:** Forgetting that these faces are "internal" and not part of the *surface* of the solid.
* **Fix:** Only add the curved surface areas of the components.
* **Mistake:** Miscalculating total length.
* **Why it happens:** Forgetting to add the radius of *both* hemispherical ends ($h + r + r$).
* **Fix:** Always draw a quick sketch to visualize the total length.

---

## Worked Example (Step-by-Step)

**Question:** A solid is in the form of a right circular cylinder with hemispherical ends. The total length of the solid is 35 cm. The diameter of the cylinder is $\frac{1}{4}$ of its height. The surface area of the solid is?

**Solution:**
1. **Define variables:** Let radius be $r$. Diameter $d = 2r$.
2. **Express dimensions:** Given $2r = \frac{1}{4}h \Rightarrow h = 8r$.
3. **Solve for $r$:** Total length $= h + r + r = 8r + 2r = 10r$. Given $10r = 35 \Rightarrow r = 3.5$.
4. **Calculate Area:** $\text{TSA} = 2\pi rh + 4\pi r^2 = 2\pi r(8r) + 4\pi r^2 = 20\pi r^2$.
   $\text{TSA} = 20 \times \frac{22}{7} \times 3.5 \times 3.5 = 770 \text{ cm}^2$.

**Answer:** 770 cm$^2$.

---

## Similar Patterns
**Volume of Composite Solids:** Distinguish by checking if the question asks for "Surface Area" (use curved areas) or "Volume" (use $\pi r^2h + \frac{4}{3}\pi r^3$).

---

## Revision Summary
* **Key formula:** $\text{TSA} = \sum \text{Curved Surface Areas}$.
* **Spot it by:** "Solid with hemispherical ends" and "Total length".
* **First move:** Express all dimensions in terms of $r$.
* **Fastest method:** Factor out $2\pi r$ before substituting values.
* **Biggest trap:** Adding the internal circular faces of the cylinder.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Curved Surface Area (Cylinder):** $2\pi rh$.
* **Curved Surface Area (Hemisphere):** $2\pi r^2$.
* **Algebraic Substitution:** Replacing $h$ with $8r$ to solve for a single variable.

### Formulas You Must Know First
* **Diameter to Radius:** $r = \frac{d}{2}$.

### Terms Used In This Pattern
* **Composite Solid:** A shape made by combining two or more standard geometric solids.
* **Right Circular Cylinder:** A cylinder where the base is perpendicular to the height.