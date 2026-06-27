# Surds and Roots

## Overview
This pattern involves simplifying complex radical expressions, comparing the magnitude of different surds, or solving equations involving nested roots. The central idea is to transform expressions into a common format—either by rationalizing denominators, using algebraic identities, or converting roots to a common index.

---

## Recognition Clues
* **Nested radicals:** Expressions like $\sqrt{3 + \sqrt{5}}$ or $\sqrt{x} - \frac{1}{\sqrt{x}}$.
* **Comparing surds:** Multiple terms with different roots (e.g., $\sqrt[4]{6}, \sqrt{2}, \sqrt[3]{4}$).
* **Algebraic structures:** Expressions that look like $(a-b)(a^3+a^2+a+1)$ or $t^3 - 6t^2 + 6t - 2$.
* **Given:** A value for $x$ or $t$ involving roots; **Asked:** A simplified numerical value or a larger/smaller comparison.

---

## Key Formulas

### Difference of Squares
$$
(a - b)(a + b) = a^2 - b^2
$$
**When to use:** Simplifying products of binomials involving roots.
**Example:** $(2^{1/4} - 1)(2^{1/4} + 1) = (2^{1/4})^2 - 1^2 = 2^{1/2} - 1$.

### Perfect Square Binomial
$$
a^2 + 2ab + b^2 = (a + b)^2
$$
**When to use:** Simplifying nested square roots (e.g., $\sqrt{3 + \sqrt{5}}$).
**Example:** $\sqrt{3 + \sqrt{5}} = \sqrt{\frac{6 + 2\sqrt{5}}{2}} = \frac{\sqrt{(\sqrt{5}+1)^2}}{\sqrt{2}} = \frac{\sqrt{5}+1}{\sqrt{2}}$.

### Cube of a Binomial
$$
(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3
$$
**When to use:** Eliminating cube roots when given an equation like $t = \sqrt[3]{4} + \sqrt[3]{2} + 2$.

---

## Solution Framework

1. **Identify the Goal:** Determine if you are simplifying, comparing, or solving for a variable.
2. **Standardize Indices:** For comparison, find the LCM of the root orders and convert all to the same index.
3. **Rationalize/Factor:** Use $(a-b)(a+b)$ or $(a+b)^2$ to remove radicals from denominators or simplify nested roots.
4. **Substitute:** If given a complex expression, replace the radical part with a variable (e.g., $x = 2^{1/4}$) to reveal hidden algebraic identities.
5. **Isolate and Power:** If solving for $t$, isolate the radical terms and raise both sides to the power of the root (cube or square) to eliminate them.

---

## Shortcut Tricks
* **Comparison Trick:** To compare $\sqrt[n]{a}$ and $\sqrt[m]{b}$, raise both to the power of $LCM(n, m)$.
    * *Example:* $\sqrt[4]{6}$ vs $\sqrt[3]{4} \rightarrow 6^{1/4}$ vs $4^{1/3} \rightarrow 6^3$ vs $4^4 \rightarrow 216$ vs $256$. $256$ is larger, so $\sqrt[3]{4}$ is larger.
* **Rationalization Shortcut:** If $x = a + \sqrt{b}$ and $a^2 - b = 1$, then $\frac{1}{x} = a - \sqrt{b}$.

---

## Common Mistakes
* **Order Confusion:** Thinking $\sqrt[3]{5}$ has order $1/3$ instead of $3$.
* **Algebraic Neglect:** Forgetting the $-2ab$ term when expanding $(\sqrt{x} - \frac{1}{\sqrt{x}})^2$.
* **LCM Error:** Failing to multiply the exponent by the correct factor when normalizing indices.

---

## Worked Example (Step-by-Step)

**Question:** Find the largest among $\sqrt[4]{6}$, $\sqrt{2}$, and $\sqrt[3]{4}$.

**Solution:**
1. **Identify Indices:** The indices are 4, 2, and 3.
2. **Find LCM:** $LCM(4, 2, 3) = 12$.
3. **Convert to common index 12:**
   * $\sqrt[4]{6} = 6^{1/4} = 6^{3/12} = (6^3)^{1/12} = 216^{1/12}$
   * $\sqrt{2} = 2^{1/2} = 2^{6/12} = (2^6)^{1/12} = 64^{1/12}$
   * $\sqrt[3]{4} = 4^{1/3} = 4^{4/12} = (4^4)^{1/12} = 256^{1/12}$
4. **Compare:** $256 > 216 > 64$.

**Answer:** $\sqrt[3]{4}$ is the largest.

---

## Similar Patterns
* **Indices and Exponents:** Distinguished by the absence of roots; focuses on $a^m \times a^n = a^{m+n}$.

---

## Revision Summary
* **Key formula:** $(a-b)(a+b) = a^2-b^2$ and $(a+b)^2 = a^2+2ab+b^2$.
* **Spot it by:** Nested roots or comparing different root orders.
* **First move:** Find LCM of indices for comparison or substitute $x$ for complex roots.
* **Fastest method:** Use the LCM power trick for comparisons.
* **Biggest trap:** Forgetting to multiply the radicand by the power needed to match the LCM index.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Laws of Indices:** $a^m \cdot a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$.
* **Rationalization:** Multiplying the numerator and denominator by the conjugate to remove roots from the denominator.

### Formulas You Must Know First
* **Difference of Squares:** $a^2 - b^2 = (a-b)(a+b)$.
* **Square of Binomial:** $(a+b)^2 = a^2 + 2ab + b^2$.

### Terms Used In This Pattern
* **Surd:** An irrational root of a rational number.
* **Order:** The index $n$ of the root $\sqrt[n]{a}$.
* **Radicand:** The number inside the root symbol.