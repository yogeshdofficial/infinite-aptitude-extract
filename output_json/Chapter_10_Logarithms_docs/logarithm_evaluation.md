# Logarithm Evaluation

## Overview
This pattern involves evaluating logarithmic expressions by converting them into exponential form or using power-based properties. The central idea is to express both the base and the argument as powers of the same prime number to simplify the expression into a basic numerical value.

---

## Recognition Clues
* **Keywords:** "Evaluate", "The value of", "log".
* **Given:** A logarithmic expression like $\log_b a$ or a combination of logs.
* **Asked:** A single numerical value.
* **Visual cue:** The base and the argument are often powers of the same small integer (e.g., 2, 3, 5, 7).

---

## Key Formulas

### [Power Rule for Base and Argument]
$$
\log_{b^n} (a^m) = \frac{m}{n} \log_b a
$$
**Variables:**
- $b$ = common base
- $n$ = exponent of the base
- $a$ = argument
- $m$ = exponent of the argument

**When to use:** When both the base and the argument can be written as powers of the same number.

**Worked example:** $\log_8 128 = \log_{2^3} (2^7) = \frac{7}{3} \log_2 2 = \frac{7}{3}$.

### [Logarithm Identity]
$$
b^{\log_b x} = x
$$
**Variables:**
- $b$ = base
- $x$ = argument

**When to use:** When the expression is in the form of a base raised to a logarithmic power.

**Worked example:** $36^{\log_6 4} = (6^2)^{\log_6 4} = 6^{\log_6 4^2} = 16$.

---

## Solution Framework

1. **Standardize:** Express the base and the argument as powers of the same prime number (e.g., $8 \to 2^3$, $128 \to 2^7$).
2. **Apply Power Rule:** Use $\log_{b^n} (a^m) = \frac{m}{n}$ to pull the exponents out as a fraction.
3. **Simplify:** Evaluate the remaining $\log_b b$ (which is 1) and multiply by the fraction.
4. **Handle Fractions/Decimals:** Convert decimals to fractions (e.g., $0.01 = 10^{-2}$) before applying the rules.

---

## Shortcut Tricks
* **Trick:** If the base is a root (e.g., $\sqrt{2}$), treat it as a fractional exponent ($2^{1/2}$).
* **Why it works:** It converts the root into a standard power, allowing the use of the $\frac{m}{n}$ rule.
* **Example:** $\log_{\sqrt{2}} 32 = \log_{2^{1/2}} 2^5 = \frac{5}{1/2} = 10$.

---

## Common Mistakes
* **Mistake:** Inverting the fraction in the power rule (writing $n/m$ instead of $m/n$).
    * **Fix:** Remember the exponent of the argument ($m$) goes on top, the exponent of the base ($n$) goes on the bottom.
* **Mistake:** Confusing the base and the argument.
    * **Fix:** Always identify the base (the subscript) and the argument (the main number) clearly before starting.
* **Mistake:** Forgetting that $\log_b 1 = 0$ and $\log_b b = 1$.
    * **Fix:** Memorize these two fundamental identities.

---

## Worked Example (Step-by-Step)

**Question:** Evaluate $\log_{343} 7$.

**Solution:**
1. **Standardize:** $343 = 7^3$ and $7 = 7^1$.
2. **Apply Power Rule:** $\log_{7^3} 7^1 = \frac{1}{3} \log_7 7$.
3. **Simplify:** Since $\log_7 7 = 1$, the result is $\frac{1}{3} \times 1 = \frac{1}{3}$.

**Answer:** $\frac{1}{3}$

---

## Similar Patterns
* **Logarithmic Equations:** Distinguished by the presence of a variable ($x$) and an equals sign; requires solving for $x$ rather than evaluating a constant.

---

## Revision Summary
* **Key formula:** $\log_{b^n} (a^m) = \frac{m}{n}$.
* **Spot it by:** Looking for logs with bases and arguments that are powers of the same number.
* **First move:** Convert everything to powers of a common prime base.
* **Fastest method:** Use the $\frac{m}{n}$ rule immediately after converting to powers.
* **Biggest trap:** Flipping the fraction $\frac{m}{n}$ or miscalculating the power of the base.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Exponent Laws:** $a^m \times a^n = a^{m+n}$, $\frac{a^m}{a^n} = a^{m-n}$, and $(a^m)^n = a^{mn}$.
* **Roots as Exponents:** $\sqrt[n]{a} = a^{1/n}$.

### Formulas You Must Know First
$$
\log_b b = 1
$$
**What it means:** The log of a base to itself is always 1.
**Example:** $\log_5 5 = 1$.

$$
\log_b 1 = 0
$$
**What it means:** The log of 1 to any base is 0.
**Example:** $\log_{100} 1 = 0$.

### Terms Used In This Pattern
* **Base:** The subscript number in a logarithm.
* **Argument:** The number inside the logarithm being evaluated.