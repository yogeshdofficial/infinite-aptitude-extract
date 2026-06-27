# Logarithmic Simplification

## Overview
This pattern involves simplifying complex logarithmic expressions containing multiple terms, coefficients, or varying bases. The central idea is to condense the expression into a single log term by applying standard log properties (product, quotient, and power rules) and the change-of-base formula.

---

## Recognition Clues
* **Visual:** Multiple log terms separated by $+$ or $-$ signs, or products of logs with different bases.
* **Given:** Expressions like $\log_a b \pm \log_a c$ or coefficients like $n \log a$.
* **Asked:** "Evaluate," "Simplify," or "Find the value of" a numerical expression.
* **Clue:** Presence of fractions inside logs or logs with bases that are powers of each other (e.g., 9 and 27).

---

## Key Formulas

### [Change of Base]
$$
\log_b a = \frac{\log a}{\log b}
$$
**Variables:** $a$ = argument, $b$ = base.
**When to use:** When bases are different and cannot be easily converted to a common base.
**Worked example:** $\log_5 3 \times \log_{27} 25 = \frac{\log 3}{\log 5} \times \frac{\log 25}{\log 27} = \frac{\log 3}{\log 5} \times \frac{2 \log 5}{3 \log 3} = \frac{2}{3}$.

### [Reciprocal Property]
$$
\frac{1}{\log_a b} = \log_b a
$$
**Variables:** $a$ = original base, $b$ = original argument.
**When to use:** When the log term is in the denominator of a fraction.
**Worked example:** $\frac{1}{\log_{xy} (xyz)} = \log_{xyz} (xy)$.

### [Power and Product/Quotient Rules]
$$
n \log a = \log(a^n), \quad \log a + \log b = \log(ab), \quad \log a - \log b = \log\left(\frac{a}{b}\right)
$$
**When to use:** To condense multiple terms into one single log.
**Worked example:** $2 \log 4 = \log(4^2) = \log 16$.

---

## Solution Framework

1. **Clear Coefficients:** Move any number multiplying a log inside as an exponent ($n \log a \to \log a^n$).
2. **Standardize Bases:** If bases differ, use the change-of-base formula or express bases as powers of a common number.
3. **Condense:** Use the sum/difference rules to combine all logs into one single $\log(\text{expression})$.
4. **Simplify Argument:** Perform the arithmetic inside the log to reduce the fraction or product to a simple number.
5. **Evaluate:** Solve the final log value (e.g., $\log_{10} 10 = 1$ or $\log_b 1 = 0$).

---

## Shortcut Tricks

* **Trick:** The "Chain Rule" for products: $\log_a b \times \log_b c \times \log_c a = 1$.
* **Why it works:** Bases and arguments cancel out when written as fractions: $\frac{\log b}{\log a} \times \frac{\log c}{\log b} \times \frac{\log a}{\log c} = 1$.
* **When to use:** When you see a product of logs where the argument of one is the base of the next.
* **Example:** If $\log_a b = 1/2$ and $\log_b c = 1/3$, then $\log_a c = (1/2) \times (1/3) = 1/6$.

---

## Common Mistakes

* **Mistake:** Forgetting to square/cube the fraction when moving a coefficient inside.
    * **Fix:** Always apply the exponent to the *entire* fraction: $2 \log(5/9) = \log(5/9)^2 = \log(25/81)$.
* **Mistake:** Incorrectly applying the quotient rule with a minus sign.
    * **Fix:** $\log a - \log b$ is $\log(a/b)$, not $\log(a-b)$.
* **Mistake:** Arithmetic errors in complex fraction multiplication.
    * **Fix:** Simplify individual fractions before multiplying them together.

---

## Worked Example (Step-by-Step)

**Question:** Simplify: $\log \frac{75}{16} - 2 \log \frac{5}{9} + \log \frac{32}{243}$

**Solution:**
1. **Clear Coefficients:** $2 \log \frac{5}{9} = \log (\frac{5}{9})^2 = \log \frac{25}{81}$.
2. **Condense:** Combine into one log: $\log (\frac{75}{16} \div \frac{25}{81} \times \frac{32}{243})$.
3. **Simplify Argument:** $\log (\frac{75}{16} \times \frac{81}{25} \times \frac{32}{243})$.
4. **Calculate:** $\frac{75}{25} = 3$, $\frac{32}{16} = 2$, $\frac{81}{243} = \frac{1}{3}$. So, $\log(3 \times 2 \times \frac{1}{3}) = \log 2$.

**Answer:** $\log 2$

---

## Similar Patterns
**Logarithmic Equations:** Distinguished by the presence of an equals sign and a variable (e.g., $\log x = 2$); requires solving for $x$ rather than simplifying an expression.

---

## Revision Summary
* **Key formula:** $\log a + \log b = \log(ab)$ and $\log a - \log b = \log(a/b)$.
* **Spot it by:** Multiple log terms with coefficients or different bases.
* **First move:** Move coefficients inside as exponents.
* **Fastest method:** Use the chain rule for products of logs.
* **Biggest trap:** Forgetting to apply exponents to the whole fraction.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Exponent Laws** — $a^m \times a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$.
* **Logarithm Definition** — $\log_a x = m \iff a^m = x$.

### Formulas You Must Know First
$$
\log_a a = 1, \quad \log_a 1 = 0
$$
**What it means:** The log of the base is always 1; the log of 1 is always 0.
**Example:** $\log_{10} 10 = 1$ and $\log_{10} 1 = 0$.

### Terms Used In This Pattern
* **Argument** — The number inside the log function (e.g., $x$ in $\log_a x$).
* **Base** — The subscript number $a$ in $\log_a x$.