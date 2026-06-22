# Quantity Change

## Overview
This pattern involves finding an unknown value that, when added to or subtracted from existing quantities, changes their ratio to a new, specified ratio. The central idea is to represent the initial quantities as variables (e.g., $ax, bx$) and solve the resulting algebraic equation using cross-multiplication.

---

## Recognition Clues
* **Keywords:** "What must be added/subtracted", "remaining numbers may be proportional", "dimensions increased/decreased".
* **Given:** An initial ratio (e.g., $7:11$) and a target ratio (e.g., $3:4$).
* **Asked:** The specific value ($x$) that causes the change.
* **Structure:** Two ratios linked by a common change applied to all terms.

---

## Key Formulas

### [Cross-Multiplication Property]
$$
\frac{a+x}{b+x} = \frac{c}{d} \implies d(a+x) = c(b+x)
$$

**Variables:**
- $a, b$ = initial terms of the ratio
- $x$ = the unknown value to be added/subtracted
- $c, d$ = target ratio terms

**When to use:** When a single value $x$ is added to or subtracted from two terms to reach a new ratio.

**Worked example:** For $7:11$ becoming $3:4$: $\frac{7+x}{11+x} = \frac{3}{4} \implies 4(7+x) = 3(11+x) \implies 28+4x = 33+3x \implies x=5$.

---

## Solution Framework

1. **Define Variables:** Assign $x$ to the unknown value and express initial quantities as $ax$ and $bx$.
2. **Set up Equation:** Write the ratio as a fraction, applying the change ($+x$ or $-x$) to both terms.
3. **Cross-Multiply:** Multiply the numerator of one side by the denominator of the other to eliminate fractions.
4. **Isolate $x$:** Expand the brackets, group all $x$ terms on one side, and constants on the other.
5. **Solve:** Divide to find the final value of $x$.

---

## Shortcut Tricks
* **Trick:** For $\frac{a+x}{b+x} = \frac{c}{d}$, the value $x = \frac{ad-bc}{c-d}$.
* **Why it works:** It is the algebraic result of solving the cross-multiplication equation $ad + dx = bc + cx$.
* **When to use:** When you need to solve in under 10 seconds without writing out the full expansion.
* **Example:** For $7:11$ to $3:4$, $a=7, b=11, c=3, d=4$. $x = \frac{(7 \times 4) - (11 \times 3)}{3-4} = \frac{28-33}{-1} = \frac{-5}{-1} = 5$.

---

## Common Mistakes
* **Mistake:** Adding $x$ to only one term of the ratio.
    * **Why it happens:** Misreading the instruction "added to each term".
    * **Fix:** Always write the change in both the numerator and denominator.
* **Mistake:** Sign errors during expansion (e.g., $(15-x)(38-x)$).
    * **Why it happens:** Forgetting that $(-x) \times (-x) = +x^2$.
    * **Fix:** Use FOIL (First, Outer, Inner, Last) method carefully.

---

## Worked Example (Step-by-Step)

**Question:** What must be added to each term of the ratio $7:11$ so as to make it equal to $3:4$?

**Solution:**
1. **Define:** Let the number to be added be $x$. Initial terms are $7$ and $11$.
2. **Equation:** $\frac{7+x}{11+x} = \frac{3}{4}$.
3. **Cross-Multiply:** $4(7+x) = 3(11+x)$.
4. **Isolate:** $28 + 4x = 33 + 3x \implies 4x - 3x = 33 - 28$.
5. **Solve:** $x = 5$.

**Answer:** $5$

---

## Similar Patterns
**Proportionality Problems:** If the question asks for a number to be subtracted from four numbers to make them proportional, use $\frac{a-x}{b-x} = \frac{c-x}{d-x}$. This is distinct because it involves four terms instead of two.

---

## Revision Summary
* **Key formula:** $\frac{a+x}{b+x} = \frac{c}{d} \implies ad+dx = bc+cx$.
* **Spot it by:** "Added to each term" or "proportional" keywords.
* **First move:** Write the ratio as a fraction with $+x$ or $-x$.
* **Fastest method:** Use the shortcut $x = \frac{ad-bc}{c-d}$.
* **Biggest trap:** Forgetting to apply the change to both terms of the ratio.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio:** A comparison of two quantities by division, written as $a:b$ or $\frac{a}{b}$.
* **Proportion:** The equality of two ratios, $\frac{a}{b} = \frac{c}{d}$.
* **Linear Equation:** An equation where the variable is to the power of 1, solvable by isolating the variable.

### Formulas You Must Know First
* **Cross-Multiplication:** If $\frac{a}{b} = \frac{c}{d}$, then $ad = bc$.
    * **Example:** If $\frac{x}{5} = \frac{2}{10}$, then $10x = 10 \implies x=1$.

### Terms Used In This Pattern
* **Antecedent:** The first term of a ratio.
* **Consequent:** The second term of a ratio.