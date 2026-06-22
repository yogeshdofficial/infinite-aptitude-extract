# Rectangle Basics

## Overview
This pattern involves calculating dimensions, area, perimeter, or diagonal length of a rectangle. The central idea is to relate the two dimensions (length $l$ and breadth $b$) using the given constraints (area, perimeter, or diagonal) and algebraic identities.

---

## Recognition Clues
* **Keywords:** "rectangular field," "lawn," "carpet," "diagonal," "fencing," "cost per square metre."
* **Given:** Area, perimeter, diagonal, or ratio of sides.
* **Asked:** Dimensions ($l, b$), diagonal length, or total cost of covering/fencing.
* **Units:** Watch for mixed units (e.g., cm vs m) or area units (hectares vs $m^2$).

---

## Key Formulas

### Area and Perimeter
$$
\text{Area} = l \times b, \quad \text{Perimeter} = 2(l + b)
$$
**Variables:** $l$ = length, $b$ = breadth.
**When to use:** When dimensions are given or needed to find total coverage/boundary.
**Example:** If $l=15, b=8$, Area = $15 \times 8 = 120$ $m^2$.

### Diagonal Relationship
$$
d^2 = l^2 + b^2
$$
**Variables:** $d$ = diagonal, $l$ = length, $b$ = breadth.
**When to use:** When the diagonal is given or required.
**Example:** If $l=15, b=8$, $d = \sqrt{15^2 + 8^2} = \sqrt{289} = 17$ m.

### Algebraic Identity
$$
(l + b)^2 = (l^2 + b^2) + 2lb
$$
**When to use:** When you have Area ($lb$) and Diagonal ($l^2+b^2$) but need Perimeter ($2(l+b)$).

---

## Solution Framework
1. **Define variables:** Assign $l$ and $b$ to the dimensions.
2. **Translate constraints:** Write equations for the given values (e.g., $lb = \text{Area}$, $2(l+b) = \text{Perimeter}$).
3. **Solve for unknowns:** Use substitution or algebraic identities to find $l$ and $b$ or the required perimeter/diagonal.
4. **Unit conversion:** Ensure all units match (e.g., convert hectares to $m^2$, cm to m) before calculating.
5. **Final Calculation:** Multiply by the rate if a cost is requested.

---

## Shortcut Tricks
* **Trick:** If given Area ($A$) and Perimeter ($P$), then $l+b = P/2$ and $lb = A$. The dimensions are roots of $x^2 - (P/2)x + A = 0$.
* **Why it works:** This is the standard quadratic form for two numbers given their sum and product.
* **Example:** $P=46, A=120$. $P/2 = 23$. Solve $x^2 - 23x + 120 = 0 \implies (x-15)(x-8)=0$. Dimensions are 15 and 8.

---

## Common Mistakes
* **Mistake:** Confusing linear metres (perimeter) with square metres (area).
    * **Fix:** Always check if the rate is per metre (fencing) or per square metre (carpeting).
* **Mistake:** Forgetting to divide perimeter by 2.
    * **Fix:** Remember $P = 2(l+b)$, so $l+b = P/2$.
* **Mistake:** Using diagonal as a side.
    * **Fix:** Diagonal is always the hypotenuse; use Pythagoras.

---

## Worked Example (Step-by-Step)

**Question:** The diagonal of a rectangular field is 15 m and its area is 108 sq. m. What will be the total expenditure in fencing the field at the rate of ₹ 5 per metre?

**Solution:**
1. **Identify:** $d = 15$, $Area (lb) = 108$.
2. **Relate:** $l^2 + b^2 = d^2 = 15^2 = 225$.
3. **Identity:** $(l+b)^2 = (l^2 + b^2) + 2lb = 225 + 2(108) = 225 + 216 = 441$.
4. **Perimeter:** $l+b = \sqrt{441} = 21$. Perimeter $= 2(l+b) = 2 \times 21 = 42$ m.
5. **Cost:** $42 \times 5 = 210$.

**Answer:** ₹ 210.

---

## Similar Patterns
**Square Basics:** Distinguished by the clue "all sides are equal," simplifying $l=b=a$, so $Area = a^2$ and $Diagonal = a\sqrt{2}$.

---

## Revision Summary
* **Key formula:** $d^2 = l^2 + b^2$ and $(l+b)^2 = l^2+b^2+2lb$.
* **Spot it by:** Keywords like "diagonal," "fencing," or "area."
* **First move:** Write down $l$ and $b$ and translate given values into equations.
* **Fastest method:** Use the quadratic $x^2 - (P/2)x + A = 0$ if $P$ and $A$ are known.
* **Biggest trap:** Forgetting to convert units (e.g., cm to m) or confusing $P$ with $P/2$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Pythagorean Theorem:** In a right triangle, $a^2 + b^2 = c^2$.
* **Quadratic Factoring:** Solving $ax^2 + bx + c = 0$ by splitting the middle term.
* **Unit Conversion:** $1 \text{ hectare} = 10,000 \text{ m}^2$; $100 \text{ cm} = 1 \text{ m}$.

### Formulas You Must Know First
* **Perimeter of Rectangle:** $2(l+b)$.
* **Area of Rectangle:** $l \times b$.

### Terms Used In This Pattern
* **Diagonal:** The line segment connecting opposite corners of the rectangle.
* **Fencing:** Refers to the perimeter of the field.
* **Carpeting:** Refers to the area of the floor.