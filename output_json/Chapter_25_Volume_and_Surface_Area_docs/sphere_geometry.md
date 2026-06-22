# Sphere Geometry

## Overview
These questions involve calculating volumes or surface areas of spheres and hemispheres, or converting one shape into another (e.g., melting a sphere into a wire). The central idea is the **Conservation of Volume**: the total volume of material remains constant during shape transformation.

---

## Recognition Clues
* **Keywords:** "Sphere," "Hemisphere," "Melted," "Drawn into a wire," "Filled into bottles."
* **Given:** Radius ($r$) or diameter ($d$) of the sphere/hemisphere.
* **Asked:** Volume, surface area, or the number of smaller objects (bottles/wires) that can be formed.

---

## Key Formulas

### Volume of Sphere
$$
V = \frac{4}{3}\pi r^3
$$
**Variables:** $r$ = radius.
**When to use:** Finding the capacity of a full sphere.
**Example:** $r=9 \Rightarrow V = \frac{4}{3} \times \pi \times 9^3 = 972\pi$.

### Volume of Hemisphere
$$
V = \frac{2}{3}\pi r^3
$$
**Variables:** $r$ = radius.
**When to use:** Finding the capacity of a bowl or half-sphere.
**Example:** $r=9 \Rightarrow V = \frac{2}{3} \times \pi \times 9^3 = 486\pi$.

### Surface Areas of Hemisphere
$$
\text{CSA} = 2\pi r^2, \quad \text{TSA} = 3\pi r^2
$$
**Variables:** $r$ = radius.
**When to use:** CSA for the curved part only; TSA if the flat circular top is included.

---

## Solution Framework
1. **Standardize Units:** Convert all dimensions (mm, cm, m) to the same unit (usually cm) before calculating.
2. **Find Radius:** If diameter is given, divide by 2 ($r = \frac{d}{2}$).
3. **Calculate Volume:** Apply the relevant formula ($\frac{4}{3}\pi r^3$ or $\frac{2}{3}\pi r^3$).
4. **Equate/Divide:** If melting/filling, set $\text{Total Volume} = n \times \text{Volume of one small object}$ and solve for $n$ or the missing dimension.

---

## Shortcut Tricks
* **Trick:** Cancel $\pi$ early.
* **Why it works:** $\pi$ appears on both sides of the equation in transformation problems.
* **When to use:** Whenever you are equating two volumes (e.g., sphere to wire).
* **Example:** $972\pi = \pi \times r^2 \times h \Rightarrow 972 = r^2 \times h$.

---

## Common Mistakes
* **Mistake:** Using diameter instead of radius in formulas.
    * **Fix:** Always divide diameter by 2 immediately.
* **Mistake:** Forgetting the circular base in Hemisphere TSA.
    * **Fix:** Remember TSA = CSA ($2\pi r^2$) + Base ($\pi r^2$) = $3\pi r^2$.
* **Mistake:** Unit mismatch (e.g., mm vs cm).
    * **Fix:** Convert everything to cm at the start.

---

## Worked Example (Step-by-Step)

**Question:** A hemispherical bowl of internal radius 9 cm contains a liquid. This liquid is to be filled into cylindrical shaped small bottles of diameter 3 cm and height 4 cm. How many bottles will be needed?

**Solution:**
1. **Find Radius:** Bowl $r = 9$ cm. Bottle $r = \frac{3}{2} = 1.5$ cm.
2. **Volume of Bowl:** $V_{bowl} = \frac{2}{3} \pi (9)^3 = \frac{2}{3} \pi (729) = 486\pi$ cm$^3$.
3. **Volume of Bottle:** $V_{bottle} = \pi (1.5)^2 (4) = \pi (2.25)(4) = 9\pi$ cm$^3$.
4. **Divide:** Number of bottles = $\frac{486\pi}{9\pi} = 54$.

**Answer:** 54 bottles.

---

## Similar Patterns
* **Cylinder/Cone Geometry:** Distinguish by the shape description; spheres have a constant radius in all directions, while cylinders/cones have a distinct height ($h$).

---

## Revision Summary
* **Key formula:** Sphere $V = \frac{4}{3}\pi r^3$; Hemisphere $V = \frac{2}{3}\pi r^3$.
* **Spot it by:** "Melted," "Sphere," or "Hemisphere" in the question.
* **First move:** Convert all units to cm and find the radius.
* **Fastest method:** Cancel $\pi$ from both sides before calculating.
* **Biggest trap:** Using diameter instead of radius.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Radius vs Diameter:** $r = \frac{d}{2}$.
* **Volume of Cylinder:** $V = \pi r^2 h$.
* **Unit Conversion:** $1 \text{ cm} = 10 \text{ mm}$; $1 \text{ m} = 100 \text{ cm}$.

### Formulas You Must Know First
* **Volume of Cylinder:** $V = \pi r^2 h$.
    * **What it means:** The space inside a circular tube.
    * **Example:** $r=2, h=10 \Rightarrow V = \pi(4)(10) = 40\pi$.

### Terms Used In This Pattern
* **Hemisphere:** Half of a sphere.
* **CSA (Curved Surface Area):** Area of the rounded surface only.
* **TSA (Total Surface Area):** Area of the rounded surface plus the flat base.