# Pyramid Geometry

## Overview
This pattern involves calculating the volume or surface area of a pyramid. The central idea is to identify the shape of the base, calculate its area, and then apply the standard pyramid volume formula.

---

## Recognition Clues
* **Keywords:** "Pyramid", "Base", "Height", "Slant edge", "Volume", "Surface area".
* **Given:** Base shape (square, triangle, hexagon), side length of base, and vertical height.
* **Asked:** Volume or Total Surface Area.

---

## Key Formulas

### [Volume of a Pyramid]
$$
\text{Volume} = \frac{1}{3} \times \text{Area of base} \times \text{Height}
$$

**Variables:**
- $\text{Area of base}$ = The surface area of the bottom face.
- $\text{Height}$ = The perpendicular distance from the apex to the base.

**When to use:** Whenever the question asks for the capacity or volume of the pyramid.

**Worked example:** Base area = $25\text{ cm}^2$, Height = $9\text{ cm}$. Volume = $\frac{1}{3} \times 25 \times 9 = 75\text{ cm}^3$.

### [Total Surface Area]
$$
\text{Total Surface Area} = \text{Base Area} + \text{Lateral Surface Area}
$$

**Variables:**
- $\text{Base Area}$ = Area of the bottom polygon.
- $\text{Lateral Surface Area}$ = Sum of the areas of all triangular side faces.

**When to use:** When the question asks for the "whole surface area".

**Worked example:** Base area = $\frac{\sqrt{3}}{4}$, Lateral area = $3 \times \frac{\sqrt{35}}{4}$. Total = $\frac{\sqrt{3} + 3\sqrt{35}}{4}$.

---

## Solution Framework

**Step 1: Identify the base shape** — Determine if the base is a square, triangle, or hexagon to select the correct area formula.
**Step 2: Calculate Base Area** — Compute the area using the side length provided.
**Step 3: Apply Volume Formula** — Multiply the Base Area by the Height and divide by 3.
**Step 4: Calculate Lateral Area (if needed)** — Use Heron's formula or triangle area formulas for side faces if "Total Surface Area" is requested.
**Step 5: Sum areas** — Add the Base Area and Lateral Area for the final surface area result.

---

## Shortcut Tricks
* **Trick:** For volume, always divide by 3 first.
* **Why it works:** Multiplication is commutative; $\frac{1}{3} \times (\text{Area} \times \text{Height})$ is the same as $(\text{Area} \times \frac{\text{Height}}{3})$.
* **When to use:** When the height is a multiple of 3.
* **Example:** Height = $30$, Base Area = $64$. Calculate $\frac{30}{3} = 10$, then $64 \times 10 = 640$.

---

## Common Mistakes
* **Mistake:** Using side length instead of base area in the volume formula.
    * **Fix:** Always calculate the area of the base polygon first.
* **Mistake:** Forgetting to divide by 3.
    * **Fix:** Remember that a pyramid is exactly $1/3$ of a prism.
* **Mistake:** Assuming lateral faces are equilateral.
    * **Fix:** Use the slant edge and base side to find the actual dimensions of the triangular faces.

---

## Worked Example (Step-by-Step)

**Question:** A right pyramid is on a regular hexagonal base. Each side of the base is $10\text{ m}$ and the height is $60\text{ m}$. The volume of the pyramid is?

**Solution:**
1. **Identify Base:** The base is a regular hexagon.
2. **Calculate Base Area:** Area $= \frac{3\sqrt{3}}{2} \times (\text{side})^2 = \frac{3\sqrt{3}}{2} \times 100 = 150\sqrt{3}\text{ m}^2$.
3. **Apply Volume Formula:** Volume $= \frac{1}{3} \times (150\sqrt{3}) \times 60$.
4. **Simplify:** $\frac{1}{3} \times 60 = 20$. Then $150\sqrt{3} \times 20 = 3000\sqrt{3}$.
5. **Final Calculation:** $3000 \times 1.732 = 5196$.

**Answer:** $5196\text{ m}^3$.

---

## Similar Patterns
**Prism Geometry:** Distinguish by the volume formula; prisms do not have the $1/3$ factor (Volume = Base Area $\times$ Height).

---

## Revision Summary
* **Key formula:** $\text{Volume} = \frac{1}{3} \times \text{Base Area} \times \text{Height}$.
* **Spot it by:** Looking for "pyramid" and base shape descriptions.
* **First move:** Calculate the area of the base polygon.
* **Fastest method:** Divide height by 3 before multiplying by base area.
* **Biggest trap:** Forgetting the $1/3$ factor or using side length instead of area.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Area of Square** — $a^2$ where $a$ is the side.
* **Area of Equilateral Triangle** — $\frac{\sqrt{3}}{4}a^2$.
* **Area of Regular Hexagon** — $\frac{3\sqrt{3}}{2}a^2$.
* **Heron's Formula** — $\sqrt{s(s-a)(s-b)(s-c)}$ for the area of a triangle with sides $a, b, c$ and semi-perimeter $s = \frac{a+b+c}{2}$.

### Formulas You Must Know First
* **Semi-perimeter** — $s = \frac{a+b+c}{2}$.

### Terms Used In This Pattern
* **Apex** — The top point of the pyramid.
* **Slant edge** — The distance from the apex to a corner of the base.
* **Lateral face** — The triangular sides of the pyramid.