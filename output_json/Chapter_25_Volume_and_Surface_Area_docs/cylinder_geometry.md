# Cylinder Geometry

## Overview
This pattern involves problems featuring cylindrical objects like tanks, pipes, wires, or wells. The central idea is to relate the physical dimensions (radius $r$ and height $h$) to the volume or surface area using standard geometric formulas.

---

## Recognition Clues
* **Keywords:** "Cylindrical," "tank," "pipe," "wire," "well," "embankment," "iron rod."
* **Given:** Diameter or radius, height or length, and sometimes total volume.
* **Asked:** Volume, surface area, depth/height, or the number of items that can be formed from a total volume.

---

## Key Formulas

### Cylinder Volume
$$
V = \pi r^2 h
$$
**Variables:** $r$ = radius, $h$ = height/depth.
**When to use:** To find capacity or when converting material from one shape to another.
**Example:** $r=7, h=10 \implies V = \frac{22}{7} \times 7^2 \times 10 = 1540$.

### Curved Surface Area (CSA)
$$
CSA = 2\pi rh
$$
**Variables:** $r$ = radius, $h$ = height.
**When to use:** To find the area of the side wall (excluding top/bottom).
**Example:** $r=3.5, h=40 \implies CSA = 2 \times \frac{22}{7} \times 3.5 \times 40 = 880$.

### Total Surface Area (TSA)
$$
TSA = 2\pi r(h + r)
$$
**Variables:** $r$ = radius, $h$ = height.
**When to use:** To find the total material needed for the entire cylinder.
**Example:** $r=3.5, h=40 \implies TSA = 2 \times \frac{22}{7} \times 3.5 \times (40 + 3.5) = 957$.

---

## Solution Framework
1. **Standardize Units:** Convert all dimensions to the same unit (e.g., cm to m) before calculating.
2. **Find Radius:** If diameter is given, divide by 2 immediately ($r = \frac{d}{2}$).
3. **Identify Goal:** Determine if you need Volume ($V$), CSA, or TSA.
4. **Apply Formula:** Substitute $r$ and $h$ into the relevant formula.
5. **Solve for Unknown:** If $V$ is given, rearrange the formula to solve for $h$ or $r$.

---

## Shortcut Tricks
* **Trick:** When finding the number of items, use $\frac{\text{Total Volume}}{\text{Volume of one item}}$.
* **Why it works:** It avoids calculating intermediate values twice.
* **When to use:** Questions asking "How many rods/bricks can be made?"
* **Example:** Total volume $0.88$, one rod volume $0.0022 \implies \frac{0.88}{0.0022} = 400$.

---

## Common Mistakes
* **Mistake:** Using diameter instead of radius in $\pi r^2 h$.
    * **Fix:** Always divide diameter by 2 before squaring.
* **Mistake:** Mixing units (e.g., cm and m).
    * **Fix:** Convert everything to meters or centimeters at the very start.
* **Mistake:** Forgetting to add the area of the two circular bases for TSA.
    * **Fix:** Use $2\pi r(h+r)$ instead of just $2\pi rh$.

---

## Worked Example (Step-by-Step)

**Question:** A well with 14 m inside diameter is dug 10 m deep. Earth taken out is spread around it to a width of 21 m to form an embankment. Find the height of the embankment.

**Solution:**
1. **Find Volume of Earth:** $r = \frac{14}{2} = 7$ m. $V = \frac{22}{7} \times 7^2 \times 10 = 1540$ m$^3$.
2. **Find Embankment Area:** It is a ring. Inner radius $r_1 = 7$ m, Outer radius $r_2 = 7 + 21 = 28$ m. Area $= \pi(r_2^2 - r_1^2) = \frac{22}{7} \times (28^2 - 7^2) = 2310$ m$^2$.
3. **Calculate Height:** Volume = Area $\times$ Height $\implies 1540 = 2310 \times H$.
4. **Solve:** $H = \frac{1540}{2310} = \frac{2}{3}$ m.

**Answer:** $\frac{2}{3}$ m.

---

## Similar Patterns
* **Cone Geometry:** Distinguish by the presence of "slant height" ($l$) or "conical" shape.
* **Cuboid Geometry:** Distinguish by "length, breadth, height" keywords instead of "radius/diameter."

---

## Revision Summary
* **Key formula:** $V = \pi r^2 h$.
* **Spot it by:** Keywords like "cylinder," "pipe," or "well."
* **First move:** Convert diameter to radius ($r = d/2$) and standardize units.
* **Fastest method:** Use the ratio of volumes for "how many" questions.
* **Biggest trap:** Forgetting to convert units (e.g., cm to m) before calculating.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Circle Area:** $\pi r^2$.
* **Ring Area:** $\pi(R^2 - r^2)$.
* **Unit Conversion:** $1 \text{ m} = 100 \text{ cm}$, $1 \text{ dm} = 0.1 \text{ m}$.

### Terms Used In This Pattern
* **Radius ($r$):** Distance from the center of the circular base to the edge.
* **Diameter ($d$):** The full width of the circular base ($d = 2r$).
* **Embankment:** A raised structure formed by spreading earth around a hole.