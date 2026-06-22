# Rectangle Area and Dimension Variations

## Overview
These questions involve calculating changes in the area of a rectangle when its length or breadth is modified, or finding dimensions when cross-roads are cut through a field. The central idea is to set up an algebraic equation based on the fundamental formula $\text{Area} = \text{Length} \times \text{Breadth}$.

---

## Recognition Clues
* **Keywords:** "increased by", "decreased by", "percent", "cross roads", "rectangular field".
* **Given:** Relationships between length and breadth (e.g., $L=2B$), percentage changes, or total area of paths.
* **Asked:** Original dimensions, new dimensions, or percentage error in area.

---

## Key Formulas

### [Area of Rectangle]
$$
A = L \times B
$$
**Variables:** $A$ = Area, $L$ = Length, $B$ = Breadth.
**When to use:** To establish the baseline area before any changes occur.
**Example:** If $L=40$ and $B=20$, $A = 40 \times 20 = 800$.

### [Area of Perpendicular Cross Roads]
$$
A_{roads} = x(L + B - x)
$$
**Variables:** $x$ = width of road, $L$ = length of field, $B$ = breadth of field.
**When to use:** When two roads of equal width $x$ cross at the center of a rectangle.
**Example:** $L=80, B=60, x=5 \implies A = 5(80+60-5) = 5(135) = 675$.

---

## Solution Framework

1. **Define Variables:** Assign $x$ to the unknown dimension (usually breadth) and express the other in terms of $x$.
2. **Calculate Initial Area:** Write the expression for the original area ($L \times B$).
3. **Calculate New Area:** Write the expression for the area after the stated changes (e.g., $(L \pm \Delta L)(B \pm \Delta B)$).
4. **Set up Equation:** Equate the difference between the new and old area to the given change value.
5. **Solve for $x$:** Use algebraic expansion or quadratic factoring to find the value of $x$.

---

## Shortcut Tricks

* **Trick (Percentage Error):** For small percentage changes $x\%$ and $y\%$, the net change in area is $x + y + \frac{xy}{100}$.
* **Why it works:** This is the standard formula for successive percentage changes.
* **When to use:** When both dimensions are changed by a percentage (e.g., Q8).
* **Example:** $5\%$ excess ($+5$) and $6\%$ deficit ($-6$): $5 - 6 + \frac{5 \times (-6)}{100} = -1 - 0.3 = -1.3\%$. (The $1.3\%$ magnitude is the error).

---

## Common Mistakes

* **Mistake:** Adding/subtracting percentages directly (e.g., $5\% - 6\% = -1\%$).
    * **Fix:** Always use the product of the modified dimensions $(1+x)(1+y)$.
* **Mistake:** Forgetting to subtract the intersection area ($x^2$) in cross-road problems.
    * **Fix:** Remember that the central square is counted twice; subtract it once.
* **Mistake:** Choosing the wrong root in a quadratic equation.
    * **Fix:** Discard any root that exceeds the physical dimensions of the field.

---

## Worked Example (Step-by-Step)

**Question:** The length of a rectangle is twice its breadth. If its length is decreased by 5 cm and breadth is increased by 5 cm, the area is increased by 75 sq. cm. Find the length.

**Solution:**
1. **Define:** Let breadth $= x$. Then length $= 2x$.
2. **Initial Area:** $A_1 = 2x \times x = 2x^2$.
3. **New Area:** $A_2 = (2x - 5)(x + 5) = 2x^2 + 10x - 5x - 25 = 2x^2 + 5x - 25$.
4. **Equation:** $A_2 - A_1 = 75 \implies (2x^2 + 5x - 25) - 2x^2 = 75$.
5. **Solve:** $5x - 25 = 75 \implies 5x = 100 \implies x = 20$.
6. **Final:** Length $= 2x = 2(20) = 40$ cm.

**Answer:** 40 cm.

---

## Similar Patterns
* **Successive Percentage Change:** If the question asks for the *net* change in area after two percentage modifications, use the shortcut trick instead of full algebraic expansion.

---

## Revision Summary
* **Key formula:** $A = L \times B$ or $A_{roads} = x(L+B-x)$.
* **Spot it by:** "Increased/decreased by" or "cross roads" in a rectangle.
* **First move:** Assign $x$ to the breadth and express length in terms of $x$.
* **Fastest method:** Use the net change formula ($x+y+\frac{xy}{100}$) for percentage problems.
* **Biggest trap:** Forgetting to subtract the intersection area $x^2$ in cross-road problems.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Algebraic Expansion:** $(a+b)(c+d) = ac + ad + bc + bd$.
* **Quadratic Equations:** Solving $ax^2 + bx + c = 0$ via factoring.
* **Percentage Basics:** $x\%$ of $y = \frac{x}{100} \times y$.

### Formulas You Must Know First
* **Area of Rectangle:** $A = L \times B$.
* **Perimeter of Rectangle:** $P = 2(L+B)$.

### Terms Used In This Pattern
* **Excess:** An increase in measurement.
* **Deficit:** A decrease in measurement.
* **Cross roads:** Two perpendicular paths intersecting inside a field.