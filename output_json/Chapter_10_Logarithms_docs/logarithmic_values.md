# Logarithmic Values

## Overview
These questions provide specific logarithmic values (e.g., $\log 2, \log 3$) and ask you to evaluate a more complex logarithmic expression. The central idea is to decompose the target number into its prime factors or fractions of known values (like 10, 100) to apply standard log properties.

---

## Recognition Clues
* **Given:** "If $\log_{10} 2 = a$ and $\log_{10} 3 = b$..." or similar specific values.
* **Asked:** "Find the value of $\log_{10} (\text{complex number})$."
* **Keywords:** "If $\log x = \dots$, then $\log y = \dots$".
* **Structure:** The target number is usually a composite number (e.g., 50, 4.5, 360, 12).

---

## Key Formulas

### [Logarithm Properties]
$$
\log(xy) = \log x + \log y \quad | \quad \log\left(\frac{x}{y}\right) = \log x - \log y \quad | \quad \log(x^n) = n \log x
$$

**Variables:**
- $x, y$ = numbers being multiplied, divided, or raised to a power.
- $n$ = the exponent.

**When to use:** To break down complex numbers into prime factors or known values.

**Worked example:** To find $\log 4$, use $\log(2^2) = 2 \log 2$. If $\log 2 = 0.3010$, then $\log 4 = 2 \times 0.3010 = 0.6020$.

### [Change of Base Formula]
$$
\log_b a = \frac{\log_k a}{\log_k b}
$$

**Variables:**
- $a$ = the argument, $b$ = the original base, $k$ = the new base (usually 10).

**When to use:** When the base of the log is not 10 (e.g., $\log_5 12$).

**Worked example:** $\log_5 12 = \frac{\log_{10} 12}{\log_{10} 5} = \frac{\log_{10} (2^2 \times 3)}{\log_{10} (10/2)}$.

---

## Solution Framework

1. **Prime Factorization:** Break the target number into prime factors (2, 3, 5, 7).
2. **Rewrite as Fractions/Products:** If the number contains 5, rewrite it as $\frac{10}{2}$ to use $\log 10 = 1$.
3. **Apply Properties:** Expand the expression using the product, quotient, and power rules.
4. **Substitute:** Replace the log terms with the given numerical or algebraic values.
5. **Simplify:** Perform the final arithmetic or algebraic combination.

---

## Shortcut Tricks
* **Trick:** Always treat $\log 5$ as $\log (\frac{10}{2}) = 1 - \log 2$.
* **Why it works:** $\log 10$ is always 1 in base 10, eliminating the need for a $\log 5$ value.
* **When to use:** Whenever the number 5 appears in the argument.
* **Example:** $\log 50 = \log (100/2) = \log 100 - \log 2 = 2 - \log 2$.

---

## Common Mistakes
* **Mistake:** Calculating $\log 100$ as 1. **Fix:** $\log_{10} 100 = 2$ (since $10^2 = 100$).
* **Mistake:** Writing $\log(x+y) = \log x + \log y$. **Fix:** Only products $\log(xy)$ split into sums.
* **Mistake:** Forgetting to distribute a multiplier (like $1/3$) to all terms inside the log. **Fix:** Use brackets: $\frac{1}{3}(\log 7 + 2 \log 3)$.

---

## Worked Example (Step-by-Step)

**Question:** If $\log_{10} 2 = a$ and $\log_{10} 3 = b$, find $\log_5 12$.

**Solution:**
1. **Change of Base:** $\log_5 12 = \frac{\log_{10} 12}{\log_{10} 5}$.
2. **Factorize:** $12 = 2^2 \times 3$, so $\log_{10} 12 = \log_{10} (2^2 \times 3) = 2\log_{10} 2 + \log_{10} 3 = 2a + b$.
3. **Handle 5:** $\log_{10} 5 = \log_{10} (\frac{10}{2}) = \log_{10} 10 - \log_{10} 2 = 1 - a$.
4. **Substitute:** $\frac{2a + b}{1 - a}$.

**Answer:** $\frac{2a + b}{1 - a}$

---

## Similar Patterns
* **Logarithmic Equations:** These involve solving for $x$ (e.g., $\log(x^2 - 6x + 45) = 2$). Distinguish by checking if the question asks for a *value* (this pattern) or an *unknown variable* (equations).

---

## Revision Summary
* **Key formula:** $\log(x/y) = \log x - \log y$ and $\log(x^n) = n \log x$.
* **Spot it by:** Given log values and a request to find a log of a composite number.
* **First move:** Prime factorize the target number.
* **Fastest method:** Use $\log 5 = 1 - \log 2$ and $\log 10 = 1$.
* **Biggest trap:** Confusing $\log(x+y)$ with $\log x + \log y$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Factorization** — Breaking a number into a product of primes (e.g., $12 = 2^2 \times 3$).
* **Base 10 Logarithm** — $\log_{10} x$ is the power to which 10 must be raised to get $x$.

### Formulas You Must Know First
$$
\log_b (b^n) = n
$$
**What it means:** The log of a base raised to a power is just the power.
**Example:** $\log_{10} 100 = \log_{10} (10^2) = 2$.

### Terms Used In This Pattern
* **Argument** — The number inside the log function (e.g., in $\log 50$, 50 is the argument).
* **Mantissa** — The decimal part of a logarithm.