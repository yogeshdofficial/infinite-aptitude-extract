# Cube Roots

## Overview
These questions require finding the cube root of a number or identifying the missing factor to make a number a perfect cube. The central idea is that a perfect cube must have prime factors grouped in triplets ($a^3 \times b^3 \dots$).

---

## Recognition Clues
* **Keywords:** "cube root", "perfect cube", "least number... multiplied to obtain", "$\sqrt[3]{x}$".
* **Given:** A large number (e.g., 2744, 148877) or an equation involving cube roots.
* **Asked:** The value of the cube root or the smallest multiplier required to complete a triplet of prime factors.

---

## Key Formulas

### [Perfect Cube Condition]
$$
\text{Exponent of every prime factor must be a multiple of 3}
$$
**Variables:**
- $n = p_1^{a} \times p_2^{b} \dots$ where $p$ are prime factors and $a, b$ are exponents.
**When to use:** When asked for the "least number to multiply" to make a number a perfect cube.
**Worked example:** For $4320 = 2^5 \times 3^3 \times 5^1$, we need $2^1$ and $5^2$ to make exponents 6 and 3. Multiplier = $2^1 \times 5^2 = 50$.

### [Cube Root of Fractions]
$$
\sqrt[3]{\frac{a}{b}} = \frac{\sqrt[3]{a}}{\sqrt[3]{b}}
$$
**Variables:**
- $a, b$ = integers.
**When to use:** When dealing with decimals (e.g., $0.000216$).
**Worked example:** $\sqrt[3]{0.000216} = \sqrt[3]{\frac{216}{10^6}} = \frac{6}{100} = 0.06$.

---

## Solution Framework

**Step 1: Prime Factorization** — Break the number into its prime components to see the structure of the exponents.
**Step 2: Grouping** — Organize factors into triplets ($x^3$). If a factor is missing, identify what is needed to complete the triplet.
**Step 3: Estimation (for large numbers)** — Use the unit digit and range (e.g., $40^3$ to $60^3$) to narrow down the root.
**Step 4: Verification** — Multiply the estimated root by itself three times to confirm it matches the original number.

---

## Shortcut Tricks

* **Trick:** Use the Unit Digit Rule.
* **Why it works:** The cube of a number ending in $d$ has a unique unit digit (e.g., $2 \to 8, 3 \to 7, 7 \to 3, 8 \to 2$).
* **When to use:** When you have multiple-choice options or need to verify a large cube root quickly.
* **Example:** For $\sqrt[3]{148877}$, the unit digit is 7, so the root must end in 3. Since $50^3 = 125,000$ and $60^3 = 216,000$, the answer is 53.

---

## Common Mistakes

* **Mistake:** Confusing square root methods with cube root methods.
* **Why it happens:** Habitual reliance on square root pairing.
* **Fix:** Always check for triplets ($x^3$), not pairs ($x^2$).
* **Mistake:** Miscounting decimal places in cube roots.
* **Why it happens:** Forgetting that $0.01^3 = 0.000001$ (6 decimal places).
* **Fix:** Convert decimals to fractions with powers of 10 in the denominator.

---

## Worked Example (Step-by-Step)

**Question:** By what least number must 4320 be multiplied to obtain a perfect cube?

**Solution:**
1. **Prime Factorization:** $4320 = 2 \times 2160 = 2^2 \times 1080 = 2^3 \times 540 = 2^4 \times 270 = 2^5 \times 135 = 2^5 \times 3^3 \times 5^1$.
2. **Identify Gaps:** Exponents are $2^5, 3^3, 5^1$. We need multiples of 3.
3. **Calculate Multiplier:** To make $2^5 \to 2^6$, we need $2^1$. To make $5^1 \to 5^3$, we need $5^2$.
4. **Final Value:** $2^1 \times 5^2 = 2 \times 25 = 50$.

**Answer:** 50

---

## Similar Patterns

**Square Roots:** Distinguish by the index; square roots involve pairs ($x^2$), while cube roots involve triplets ($x^3$).

---

## Revision Summary

* **Key formula:** $\sqrt[3]{a^3 \times b^3} = a \times b$.
* **Spot it by:** Looking for "cube root" or "perfect cube" in the question.
* **First move:** Perform prime factorization immediately.
* **Fastest method:** Use the unit digit rule combined with range estimation.
* **Biggest trap:** Forgetting to complete the triplet for every prime factor.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Factorization** — Breaking a number into a product of prime numbers (e.g., $12 = 2^2 \times 3$).
* **Exponents** — Understanding that $a^n \times a^m = a^{n+m}$.

### Formulas You Must Know First
$$
(a \times b)^n = a^n \times b^n
$$
**What it means:** Powers distribute over multiplication.
**Example:** $(2 \times 3)^3 = 2^3 \times 3^3 = 8 \times 27 = 216$.

### Terms Used In This Pattern
* **Perfect Cube** — A number that is the result of multiplying an integer by itself three times.
* **Prime Factor** — A factor of a number that is also a prime number.