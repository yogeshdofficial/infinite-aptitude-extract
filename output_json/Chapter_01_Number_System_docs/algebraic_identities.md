# Algebraic Identities

## Overview
These questions involve complex-looking arithmetic expressions that are actually standard algebraic forms in disguise. The central idea is to replace large, repetitive numbers with variables ($a, b, c$) to reveal a simplified identity, allowing you to solve the problem in seconds without manual calculation.

---

## Recognition Clues
* **Repeated numbers:** You see the same two or three numbers multiplied by themselves multiple times (e.g., $789 \times 789 \times 789$).
* **Standard structures:** The expression contains squares ($a^2$), cubes ($a^3$), or products ($2ab$ or $ab$).
* **Given:** A long string of arithmetic operations involving large numbers.
* **Asked:** The simplified numerical value of the entire expression.

---

## Key Formulas

### [Sum/Difference of Cubes]
$$
\frac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b
$$
**Variables:** $a, b$ = the two distinct numbers in the expression.
**When to use:** When the expression is a fraction with cubes in the numerator and a quadratic form in the denominator.
**Worked example:** For $\frac{789^3 + 211^3}{789^2 - 789 \times 211 + 211^2}$, let $a=789, b=211$. Result: $789 + 211 = 1000$.

### [Square of a Binomial]
$$
a^2 \pm 2ab + b^2 = (a \pm b)^2
$$
**Variables:** $a, b$ = the two numbers being squared.
**When to use:** When you see two squares and a middle term that is twice the product of the roots.
**Worked example:** For $387^2 + 113^2 + 2(387)(113)$, let $a=387, b=113$. Result: $(387+113)^2 = 500^2 = 250,000$.

### [Difference of Squares]
$$
a^2 - b^2 = (a + b)(a - b)
$$
**Variables:** $a, b$ = the numbers being squared.
**When to use:** When you see two perfect squares being subtracted.
**Worked example:** For $796^2 - 204^2$, let $a=796, b=204$. Result: $(796+204)(796-204) = 1000 \times 592 = 592,000$.

---

## Solution Framework
1. **Identify variables:** Assign $a, b$ (and $c$ if needed) to the distinct numbers present.
2. **Map to identity:** Rewrite the expression using $a, b, c$ to see which algebraic identity fits.
3. **Simplify the identity:** Reduce the algebraic form (e.g., $\frac{a^3+b^3}{a^2-ab+b^2}$ becomes $a+b$).
4. **Substitute and solve:** Plug the original numbers back into the simplified form to get the final answer.

---

## Shortcut Tricks
* **Trick:** For expressions like $\frac{(a+b)^2 - (a-b)^2}{ab}$, the answer is always $4$.
* **Why it works:** $(a^2+2ab+b^2) - (a^2-2ab+b^2) = 4ab$. Dividing by $ab$ leaves $4$.
* **When to use:** Whenever you see the specific structure $(a+b)^2 - (a-b)^2$ in the numerator.

---

## Common Mistakes
* **Mistake:** Calculating large squares manually. **Fix:** Always look for the identity first; the numbers are chosen to cancel out.
* **Mistake:** Confusing $(a+b)^2$ with $a^2+b^2$. **Fix:** Remember the middle term $2ab$ is essential for the identity.
* **Mistake:** Incorrect sign in the denominator of cube identities. **Fix:** If the numerator is $a^3+b^3$, the denominator must have $-ab$.

---

## Worked Example (Step-by-Step)

**Question:** Simplify: $\frac{658 \times 658 \times 658 - 328 \times 328 \times 328}{658 \times 658 + 658 \times 328 + 328 \times 328}$

**Solution:**
1. **Identify variables:** Let $a = 658$ and $b = 328$.
2. **Map to identity:** The expression is $\frac{a^3 - b^3}{a^2 + ab + b^2}$.
3. **Simplify:** We know $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$. Thus, the expression simplifies to $(a - b)$.
4. **Substitute:** $658 - 328 = 330$.

**Answer:** 330

---

## Similar Patterns
* **Simplification/BODMAS:** If the numbers are small or don't form a clear algebraic pattern, it is a standard BODMAS problem, not an identity problem.

---

## Revision Summary
* **Key formula:** Recognize $a^3 \pm b^3$ and $a^2 \pm b^2$ patterns.
* **Spot it by:** Look for repeated large numbers and squares/cubes.
* **First move:** Assign $a$ and $b$ to the numbers and rewrite the expression.
* **Fastest method:** Use the simplified identity result (e.g., $a+b$ or $a-b$) immediately.
* **Biggest trap:** Trying to perform the actual multiplication of large numbers.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Algebraic Expansion** — Knowing that $(a+b)^2 = a^2 + 2ab + b^2$ and $(a-b)^2 = a^2 - 2ab + b^2$.
* **Cube Identities** — Knowing that $a^3+b^3 = (a+b)(a^2-ab+b^2)$ and $a^3-b^3 = (a-b)(a^2+ab+b^2)$.

### Formulas You Must Know First
* **Square of a Trinomial** — $(a+b+c)^2 = a^2+b^2+c^2+2ab+2bc+2ca$.

### Terms Used In This Pattern
* **Identity** — An equation that is true for all values of the variables involved.
* **Variable** — A letter (like $a$ or $b$) used to represent a number in an expression.