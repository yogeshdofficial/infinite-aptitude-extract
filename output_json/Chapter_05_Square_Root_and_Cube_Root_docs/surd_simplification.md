# Surd Simplification

## Overview
This pattern involves simplifying complex expressions containing square roots of non-perfect squares. The central idea is to eliminate radicals from denominators using **rationalization** or to simplify terms by extracting perfect square factors.

---

## Recognition Clues
* **Visual:** Expressions containing fractions with square roots in the denominator (e.g., $\frac{1}{\sqrt{a} \pm \sqrt{b}}$).
* **Visual:** Long series of terms with alternating signs (e.g., $\frac{1}{\sqrt{100}-\sqrt{99}} - \frac{1}{\sqrt{99}-\sqrt{98}} \dots$).
* **Given:** Values for specific roots (e.g., $\sqrt{3} = 1.732$) or variables like $x = 1 + \sqrt{2}$.
* **Asked:** The simplified numerical value of the entire expression.

---

## Key Formulas

### [Difference of Squares]
$$
(a + b)(a - b) = a^2 - b^2
$$
**Variables:** $a, b$ are the terms in the binomial.
**When to use:** To rationalize a denominator of the form $(\sqrt{a} \pm \sqrt{b})$.
**Worked example:** For $\frac{1}{3+\sqrt{3}}$, multiply by $\frac{3-\sqrt{3}}{3-\sqrt{3}}$. Denominator becomes $3^2 - (\sqrt{3})^2 = 9 - 3 = 6$.

### [Radical Factoring]
$$
\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}
$$
**Variables:** $a$ is a perfect square, $b$ is the remaining factor.
**When to use:** To simplify large radicals like $\sqrt{192}$.
**Worked example:** $\sqrt{192} = \sqrt{64 \times 3} = 8\sqrt{3}$.

---

## Solution Framework

1. **Factorize:** Extract perfect squares from all radicals (e.g., $\sqrt{48} = 4\sqrt{3}$).
2. **Rationalize:** Multiply the numerator and denominator by the conjugate of the denominator (e.g., $\frac{1}{\sqrt{a}-\sqrt{b}} \times \frac{\sqrt{a}+\sqrt{b}}{\sqrt{a}+\sqrt{b}}$).
3. **Simplify Denominator:** Use $a^2 - b^2$ to turn the denominator into a simple integer.
4. **Combine:** Group like terms (e.g., all terms with $\sqrt{3}$) and perform arithmetic.
5. **Telescope:** If it is a long series, observe the cancellation pattern; usually, only the first and last terms remain.

---

## Shortcut Tricks

* **Trick:** If the denominator is $(\sqrt{n+1} - \sqrt{n})$, the rationalized form is simply $(\sqrt{n+1} + \sqrt{n})$.
* **Why it works:** Because $(\sqrt{n+1})^2 - (\sqrt{n})^2 = (n+1) - n = 1$.
* **When to use:** In series questions like Q13 where the difference between radicands is 1.
* **Example:** $\frac{1}{\sqrt{100}-\sqrt{99}} = \sqrt{100}+\sqrt{99}$.

---

## Common Mistakes

* **Sign Errors:** Forgetting to distribute a negative sign to the second term of a conjugate when subtracting fractions.
* **Partial Rationalization:** Multiplying the denominator by the conjugate but forgetting to multiply the numerator by the same value.
* **Incorrect Factoring:** Simplifying $\sqrt{48}$ as $\sqrt{24} \times \sqrt{2}$ instead of $4\sqrt{3}$.

---

## Worked Example (Step-by-Step)

**Question:** If $\sqrt{3} = 1.732$, find the value of $\sqrt{192} - \frac{1}{2}\sqrt{48} - \sqrt{75}$.

**Solution:**
1. **Factorize:**
   $\sqrt{192} = \sqrt{64 \times 3} = 8\sqrt{3}$
   $\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}$
   $\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt{3}$
2. **Substitute:**
   $8\sqrt{3} - \frac{1}{2}(4\sqrt{3}) - 5\sqrt{3}$
3. **Simplify:**
   $8\sqrt{3} - 2\sqrt{3} - 5\sqrt{3} = 1\sqrt{3}$
4. **Final Calculation:**
   $1 \times 1.732 = 1.732$

**Answer:** 1.732

---

## Similar Patterns

**Algebraic Identities:** If the question involves $x^2 + y^2$ with $x, y$ as conjugates, use $(x+y)^2 - 2xy$ instead of manual squaring.

---

## Revision Summary

* **Key formula:** $(a+b)(a-b) = a^2 - b^2$.
* **Spot it by:** Fractions with radicals in the denominator.
* **First move:** Rationalize the denominator using the conjugate.
* **Fastest method:** Recognize telescoping series to cancel intermediate terms.
* **Biggest trap:** Forgetting to distribute negative signs across the conjugate.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Conjugate** — For $\sqrt{a} + \sqrt{b}$, the conjugate is $\sqrt{a} - \sqrt{b}$.
* **Perfect Squares** — Numbers like $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$.

### Formulas You Must Know First
$$
(a \pm b)^2 = a^2 \pm 2ab + b^2
$$
**What it means:** Expansion of a binomial square.
**Example:** $(1+\sqrt{2})^2 = 1^2 + 2(1)(\sqrt{2}) + (\sqrt{2})^2 = 3 + 2\sqrt{2}$.

### Terms Used In This Pattern
* **Surd** — An irrational root of a number.
* **Rationalize** — The process of removing radicals from a denominator.