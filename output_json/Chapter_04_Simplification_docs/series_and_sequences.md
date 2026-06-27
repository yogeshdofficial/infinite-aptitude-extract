# Series and Sequences

## Overview
This pattern involves long chains of products or sums where intermediate terms cancel out, leaving only the first and last components. The central idea is to simplify each term into a form that allows for "telescoping"—where the end of one term eliminates the beginning of the next.

---

## Recognition Clues
* **Product chains:** Look for a series of parentheses like $(1 - \frac{1}{x})(1 - \frac{1}{y})\dots$
* **Sum of fractions:** Look for denominators that are products of consecutive integers, e.g., $\frac{1}{2\times3} + \frac{1}{3\times4} + \dots$
* **Patterned denominators:** The second factor of one denominator is the first factor of the next (e.g., $n(n+1)$ followed by $(n+1)(n+2)$).
* **Goal:** You are asked to find the "value" or "sum" of the entire sequence.

---

## Key Formulas

### Telescoping Product Property
$$
\left(1 - \frac{1}{n}\right) = \frac{n-1}{n} \quad \text{or} \quad \left(1 + \frac{1}{n}\right) = \frac{n+1}{n}
$$
**When to use:** When the question is a product of terms in parentheses.
**Worked example:** For $(1-\frac{1}{3})(1-\frac{1}{4})$, this becomes $\frac{2}{3} \times \frac{3}{4}$. The $3$s cancel, leaving $\frac{2}{4} = \frac{1}{2}$.

### Partial Fraction Decomposition
$$
\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}
$$
**When to use:** When the question is a sum of fractions with product-form denominators.
**Worked example:** For $\frac{1}{2\times3} + \frac{1}{3\times4}$, this becomes $(\frac{1}{2} - \frac{1}{3}) + (\frac{1}{3} - \frac{1}{4})$. The $-\frac{1}{3}$ and $+\frac{1}{3}$ cancel, leaving $\frac{1}{2} - \frac{1}{4} = \frac{1}{4}$.

---

## Solution Framework

1. **Simplify individual terms:** Convert each bracketed term into a single fraction or a difference of two fractions.
2. **Write the sequence:** Write out the first two and last two terms to visualize the cancellation pattern.
3. **Identify the survivors:** Determine which terms do not have a "partner" to cancel with (usually the first numerator/denominator and the last numerator/denominator).
4. **Perform final arithmetic:** Calculate the value of the remaining fractions to get the final answer.

---

## Shortcut Tricks

* **Trick:** In a product series, the result is always $\frac{\text{First Numerator}}{\text{Last Denominator}}$ (or vice versa).
* **Why it works:** Every intermediate numerator cancels with the preceding denominator.
* **When to use:** Only for product series like $(1-\frac{1}{3})(1-\frac{1}{4})\dots(1-\frac{1}{100})$.
* **Example:** For $(1-\frac{1}{3})\dots(1-\frac{1}{100})$, the first numerator is $2$ and the last denominator is $100$. Result: $\frac{2}{100} = \frac{1}{50}$.

---

## Common Mistakes

* **Mistake:** Trying to find a common denominator for the whole series.
    * **Fix:** Always use the telescoping property to break terms apart first.
* **Mistake:** Canceling the wrong terms in a product.
    * **Fix:** Write out the first three terms to see the diagonal cancellation pattern clearly.
* **Mistake:** Forgetting the sign in partial fractions.
    * **Fix:** Always write $(\frac{1}{n} - \frac{1}{n+1})$ and ensure the middle terms have opposite signs.

---

## Worked Example (Step-by-Step)

**Question:** Find the value of $\frac{1}{2\times3} + \frac{1}{3\times4} + \dots + \frac{1}{9\times10}$.

**Solution:**
1. **Simplify:** Use $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$.
2. **Expand:** $(\frac{1}{2} - \frac{1}{3}) + (\frac{1}{3} - \frac{1}{4}) + (\frac{1}{4} - \frac{1}{5}) + \dots + (\frac{1}{9} - \frac{1}{10})$.
3. **Cancel:** The $-\frac{1}{3}$ cancels with $+\frac{1}{3}$, $-\frac{1}{4}$ with $+\frac{1}{4}$, etc.
4. **Survivors:** Only the first term ($\frac{1}{2}$) and the last term ($-\frac{1}{10}$) remain.
5. **Calculate:** $\frac{1}{2} - \frac{1}{10} = \frac{5}{10} - \frac{1}{10} = \frac{4}{10} = \frac{2}{5}$.

**Answer:** $\frac{2}{5}$

---

## Similar Patterns
**Arithmetic Progressions:** Distinguished by the presence of a common difference rather than a telescoping cancellation pattern.

---

## Revision Summary
* **Key formula:** $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$ for sums; $\frac{n-1}{n}$ for products.
* **Spot it by:** Denominators that are products of consecutive numbers.
* **First move:** Expand the first two and last two terms to see what cancels.
* **Fastest method:** Identify the "survivors" (first and last terms) and ignore the middle.
* **Biggest trap:** Attempting to add/multiply all fractions without canceling.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fraction Subtraction** — Finding a common denominator to subtract two fractions: $\frac{a}{b} - \frac{c}{d} = \frac{ad-bc}{bd}$.
* **Factorization** — Recognizing that numbers like $30, 42, 56$ are products of consecutive integers ($5\times6, 6\times7, 7\times8$).

### Formulas You Must Know First
* **Basic Fraction Arithmetic:** $\frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}$.

### Terms Used In This Pattern
* **Telescoping:** A series where most terms cancel out, leaving only a few.
* **Partial Fraction:** Breaking a complex fraction into a sum or difference of simpler fractions.