# Infinite Series Roots

## Overview
This pattern involves expressions where a square root contains itself infinitely (e.g., $\sqrt{n + \sqrt{n + \dots}}$). The central idea is to recognize that the entire infinite expression is equal to a variable $x$, allowing you to replace the nested part with $x$ to form a solvable quadratic equation.

---

## Recognition Clues
* **Visual:** Look for a nested square root pattern ending with "..." or "$\infty$".
* **Given:** A constant number $n$ inside a repeating radical structure.
* **Asked:** The value of the entire expression.
* **Keywords:** "Find the value of", "is equal to", "positive value of $x$".

---

## Key Formulas

### [Quadratic Setup]
$$
x^2 - x - n = 0
$$

**Variables:**
- $x$ = the value of the infinite expression
- $n$ = the constant number inside the radical

**When to use:** When the expression is in the form $\sqrt{n + \sqrt{n + \dots}}$.

**Worked example:** For $\sqrt{6 + \sqrt{6 + \dots}}$, $n=6$. Equation: $x^2 - x - 6 = 0$. Factoring gives $(x-3)(x+2)=0$, so $x=3$.

---

## Solution Framework

1. **Assign Variable:** Set the entire expression equal to $x$.
2. **Substitute:** Replace the first nested radical with $x$ (e.g., $\sqrt{n+x} = x$).
3. **Square:** Square both sides to eliminate the outermost radical ($n+x = x^2$).
4. **Rearrange:** Move all terms to one side to form a standard quadratic equation ($x^2 - x - n = 0$).
5. **Solve:** Use factoring or the quadratic formula to find $x$.
6. **Select Root:** Discard negative results, as the principal square root of a positive number is always positive.

---

## Shortcut Tricks

* **Trick:** If $n$ can be expressed as the product of two consecutive integers $a \times (a+1)$, the answer is the larger integer $(a+1)$.
* **Why it works:** The quadratic $x^2 - x - (a^2+a) = 0$ factors into $(x - (a+1))(x + a) = 0$.
* **When to use:** When $n$ is a "pronic" number (e.g., 2, 6, 12, 20, 30).
* **Example:** For $\sqrt{6 + \dots}$, $6 = 2 \times 3$. The answer is $3$.

---

## Common Mistakes

* **Mistake:** Including the negative root as a solution.
    * **Why it happens:** Quadratic equations naturally yield two roots.
    * **Fix:** Always check if the result is positive; square roots cannot be negative.
* **Mistake:** Squaring only the first term instead of the whole side.
    * **Why it happens:** Forgetting that $(\sqrt{n+x})^2 = n+x$.
    * **Fix:** Always square the entire side: $x^2 = n+x$.
* **Mistake:** Misapplying the quadratic formula.
    * **Why it happens:** Sign errors with $b^2 - 4ac$.
    * **Fix:** Carefully identify $a=1, b=-1, c=-n$.

---

## Worked Example (Step-by-Step)

**Question:** If $a = \sqrt{3+\sqrt{3+\sqrt{3+\dots}}}$, then which of the following is true?

**Solution:**
1. **Assign:** $a = \sqrt{3+a}$.
2. **Square:** $a^2 = 3+a$.
3. **Rearrange:** $a^2 - a - 3 = 0$.
4. **Solve:** Use $a = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ with $a=1, b=-1, c=-3$.
   $a = \frac{1 \pm \sqrt{1 - 4(1)(-3)}}{2} = \frac{1 \pm \sqrt{13}}{2}$.
5. **Select:** Since $a > 0$, $a = \frac{1 + \sqrt{13}}{2}$.
6. **Estimate:** $\sqrt{13}$ is between $3$ and $4$ ($3.6$ approx). $a \approx \frac{1+3.6}{2} = 2.3$. Thus, $2 < a < 3$.

**Answer:** $2 < a < 3$

---

## Similar Patterns
**Finite Radical Chains:** If the expression does NOT have "..." or "$\infty$", it is a finite calculation (work from the innermost root outward).

---

## Revision Summary
* **Key formula:** $x^2 - x - n = 0$.
* **Spot it by:** Infinite nested radicals with "..." at the end.
* **First move:** Set the expression to $x$ and square both sides.
* **Fastest method:** If $n = a(a+1)$, answer is $a+1$.
* **Biggest trap:** Selecting the negative root from the quadratic solution.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Quadratic Equation** — An equation of the form $ax^2 + bx + c = 0$.
* **Factoring** — Breaking a quadratic into $(x-p)(x-q) = 0$.
* **Quadratic Formula** — $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

### Formulas You Must Know First
$$
(a+b)^2 = a^2 + 2ab + b^2
$$
**What it means:** The expansion of a squared binomial.

### Terms Used In This Pattern
* **Radical** — The symbol $\sqrt{}$ used to denote a root.
* **Infinite Series** — A sequence that continues without end, denoted by "...".