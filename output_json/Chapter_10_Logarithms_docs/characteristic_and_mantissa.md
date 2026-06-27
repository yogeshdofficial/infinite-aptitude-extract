# Characteristic and Mantissa

## Overview
This pattern involves finding the number of digits in a large power (e.g., $2^{56}$) or decomposing a negative logarithm into its integer and decimal parts. The central idea is that the number of digits in a number $x$ is determined by the integer part (characteristic) of its common logarithm ($\log_{10} x$).

---

## Recognition Clues
* **Keywords:** "number of digits in", "characteristic and mantissa", "logarithm of a number is".
* **Given:** A large power (e.g., $2^{64}$, $4^{50}$) or a negative decimal value.
* **Asked:** The count of digits in the result or the specific characteristic/mantissa values.
* **Scan for:** $\log 2$ or $\log 3$ values provided in the question stem.

---

## Key Formulas

### [Number of Digits]
$$
\text{Digits} = \lfloor \log_{10} x \rfloor + 1
$$
**Variables:** $\lfloor \log_{10} x \rfloor$ is the characteristic (integer part) of the log.
**When to use:** When asked for the number of digits in a large power.
**Example:** For $2^{56}$, $\log(2^{56}) = 56 \times 0.30103 = 16.85768$. Characteristic is $16$. Digits = $16 + 1 = 17$.

### [Characteristic and Mantissa Decomposition]
$$
\log x = \text{Characteristic} + \text{Mantissa} \quad (\text{where } 0 \le \text{Mantissa} < 1)
$$
**Variables:** Characteristic is an integer; Mantissa is a non-negative decimal.
**When to use:** When given a negative logarithm (e.g., $-3.153$).
**Example:** For $-3.153$, write as $-3 - 0.153$. Subtract $1$ and add $1$: $(-3-1) + (1-0.153) = -4 + 0.847$. Characteristic is $-4$, Mantissa is $0.847$.

---

## Solution Framework

1. **Step 1: Apply Logarithm:** Take $\log_{10}$ of the given power using $\log(a^n) = n \log a$.
2. **Step 2: Simplify Base:** If the base is not $2$ or $3$, convert it (e.g., $4 = 2^2$, $5 = \frac{10}{2}$).
3. **Step 3: Calculate Value:** Multiply the exponent by the given log value to get the decimal result.
4. **Step 4: Identify Characteristic:** Extract the integer part (the number before the decimal).
5. **Step 5: Add One:** Add $1$ to the characteristic to get the final digit count.

---

## Shortcut Tricks
* **Trick:** For $5^n$, use $\log 5 = (1 - \log 2) \approx 0.699$.
* **Why it works:** $5 = \frac{10}{2}$, so $\log 5 = \log 10 - \log 2 = 1 - \log 2$.
* **When to use:** Whenever the base is $5$.
* **Example:** For $5^{20}$, $\log(5^{20}) = 20(1 - 0.3010) = 20(0.699) = 13.98$. Digits = $13+1 = 14$.

---

## Common Mistakes
* **Mistake:** Taking the characteristic as the final answer. **Fix:** Always add $1$.
* **Mistake:** Treating the mantissa as negative. **Fix:** Always ensure the decimal part is positive by borrowing $1$ from the integer.
* **Mistake:** Using $\ln$ (natural log) instead of $\log_{10}$. **Fix:** Only use the provided $\log 2$ or $\log 3$ values.

---

## Worked Example (Step-by-Step)

**Question:** If $\log 2 = 0.30103$, find the number of digits in $4^{50}$.

**Solution:**
1. **Apply Log:** $\log(4^{50}) = 50 \log 4$.
2. **Simplify Base:** $50 \log(2^2) = 50 \times 2 \log 2 = 100 \log 2$.
3. **Calculate:** $100 \times 0.30103 = 30.103$.
4. **Identify Characteristic:** The integer part is $30$.
5. **Add One:** $30 + 1 = 31$.

**Answer:** 31 digits.

---

## Similar Patterns
* **Logarithmic Equations:** These involve solving for $x$ (e.g., $\log(x^2-6x+45)=2$). Distinguish by checking if the question asks for a *value* of $x$ (Equation) or a *count of digits* (Characteristic).

---

## Revision Summary
* **Key formula:** $\text{Digits} = \lfloor \log_{10} x \rfloor + 1$.
* **Spot it by:** Large powers or negative log values.
* **First move:** Apply $\log$ and use power/product rules.
* **Fastest method:** Convert all bases to $2, 3,$ or $10$.
* **Biggest trap:** Forgetting to add $1$ to the characteristic.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Logarithm Power Rule:** $\log(a^n) = n \log a$.
* **Logarithm Product Rule:** $\log(ab) = \log a + \log b$.
* **Logarithm Quotient Rule:** $\log(\frac{a}{b}) = \log a - \log b$.

### Formulas You Must Know First
* $\log_{10} 10 = 1$
* $\log_{10} 1 = 0$

### Terms Used In This Pattern
* **Characteristic:** The integer part of a logarithm.
* **Mantissa:** The positive decimal part of a logarithm.