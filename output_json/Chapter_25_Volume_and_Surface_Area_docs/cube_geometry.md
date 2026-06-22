# Cube Geometry

## Overview
These questions involve a cube, a 3D shape where all edges are equal. The central idea is to always find the edge length ($a$) first, as all other properties (volume, surface area, diagonal) depend solely on this single value.

---

## Recognition Clues
* **Keywords:** "Cube", "edge", "diagonal", "surface area", "volume", "melted", "immersed".
* **Given:** Diagonal ($a\sqrt{3}$), Surface Area ($6a^2$), or Volume ($a^3$).
* **Asked:** Find the missing property (Volume, Surface Area, or edge length).
* **Context:** Objects being "melted and recast" (Volume is constant) or "immersed in water" (Volume of object = Volume of displaced water).

---

## Key Formulas

### Cube Properties
$$
\text{Diagonal} = a\sqrt{3}, \quad \text{Surface Area} = 6a^2, \quad \text{Volume} = a^3
$$
**Variables:** $a$ = edge length.
**When to use:** When given one property and asked for another.
**Worked example:** If diagonal is $6\sqrt{3}$, then $a\sqrt{3} = 6\sqrt{3} \Rightarrow a = 6$. Volume = $6^3 = 216$.

### Volume Conservation
$$
V_{new} = V_1 + V_2 + V_3
$$
**Variables:** $V$ = volume of cubes.
**When to use:** When multiple cubes are melted to form one new cube.
**Worked example:** Cubes of side 1, 6, 8. $V_{new} = 1^3 + 6^3 + 8^3 = 1 + 216 + 512 = 729$. New edge $a = \sqrt[3]{729} = 9$.

---

## Solution Framework
1. **Identify the target:** Determine which property ($a$, $V$, or $SA$) is given and which is required.
2. **Isolate the edge ($a$):** Use the given formula to solve for $a$ (e.g., if $SA=6a^2$, then $a = \sqrt{SA/6}$).
3. **Apply the conversion:** Use the calculated $a$ to find the requested value using the appropriate formula.
4. **Handle special cases:** If "melted," sum the volumes first; if "immersed," equate cube volume to (Base Area $\times$ Rise in height).

---

## Shortcut Tricks
* **Trick:** If edge increases by $x\%$, the new surface area increases by $(1 + \frac{x}{100})^2 - 1$.
* **Why it works:** Surface area is proportional to $a^2$.
* **Example:** Edge increases by 50% ($1.5$ times). New area factor is $1.5^2 = 2.25$. Increase is $2.25 - 1 = 1.25$ or $125\%$.

---

## Common Mistakes
* **Mistake:** Adding side lengths instead of volumes when melting cubes.
    * **Fix:** Always convert sides to volumes ($a^3$) before adding.
* **Mistake:** Forgetting to divide by 6 before taking the square root of surface area.
    * **Fix:** $a = \sqrt{\text{Surface Area} / 6}$.
* **Mistake:** Confusing the ratio of edges with the ratio of surface areas.
    * **Fix:** If ratio of edges is $x:y$, ratio of areas is $x^2:y^2$.

---

## Worked Example (Step-by-Step)

**Question:** Two cubes have their volumes in the ratio 1 : 27. Find the ratio of their surface areas.

**Solution:**
1. **Identify:** Given ratio of volumes $V_1:V_2 = 1:27$.
2. **Find edge ratio:** Since $V = a^3$, the ratio of edges is the cube root of the volume ratio: $\sqrt[3]{1}:\sqrt[3]{27} = 1:3$.
3. **Find area ratio:** Surface area is proportional to $a^2$. Square the edge ratio: $1^2:3^2 = 1:9$.

**Answer:** 1 : 9.

---

## Similar Patterns
**Cuboid Geometry:** Distinguish by checking if dimensions are different ($l \neq b \neq h$). If all dimensions are equal, it is a Cube.

---

## Revision Summary
* **Key formula:** $a\sqrt{3}$ (diag), $6a^2$ (SA), $a^3$ (Vol).
* **Spot it by:** Keywords "cube", "melted", or "immersed".
* **First move:** Always find the edge length $a$ first.
* **Fastest method:** Use ratios for percentage/ratio questions ($a^2$ for area, $a^3$ for volume).
* **Biggest trap:** Adding side lengths instead of volumes when melting.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Cube root:** Finding a number that multiplied by itself three times equals the target.
* **Volume displacement:** An object submerged in a liquid displaces a volume of liquid equal to its own volume.
* **Percentage increase:** $\frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100$.

### Terms Used In This Pattern
* **Edge ($a$):** The length of one side of the cube.
* **Surface Area:** The total area of all 6 faces of the cube ($6a^2$).
* **Diagonal:** The line segment connecting two opposite corners of the cube ($a\sqrt{3}$).