# Remainder of Powers (Cyclicity)

## Overview
This pattern involves finding the remainder when a large power of a number (e.g., $4^{96}$) is divided by a smaller divisor. The central idea is to identify the **cyclicity** or repeating pattern of remainders by calculating the first few powers modulo the divisor.

---

## Recognition Clues
* **Format:** A base raised to a large exponent (e.g., $a^n$) divided by a number $m$.
* **Keywords:** "What is the remainder when...", "divided by".
* **Given:** A base, a large exponent, and a divisor.
* **Asked:** The remainder of the division.

---

## Key Formulas

### Remainder of Powers
$$
a^n \pmod{m}
$$

**Variables:**
- $a$ = the base number
- $n$ = the exponent
- $m$ = the divisor

**When to use:** Whenever you see a large exponent that cannot be calculated directly.

**Worked example:** For $4^{96} \div 6$:
1. $4^1 = 4 \equiv 4 \pmod{6}$
2. $4^2 = 16 \equiv 4 \pmod{6}$
3. Since the remainder repeats as $4$, any power $4^n$ will leave a remainder of $4$ when divided by $6$.

---

## Solution Framework

1. **Calculate initial powers:** Find the remainder of $a^1, a^2, a^3 \dots$ when divided by $m$.
2. **Identify the cycle:** Look for the point where the remainder starts repeating.
3. **Simplify the exponent:** If the cycle length is $k$, express the exponent $n$ in terms of $k$ (or simply observe the constant remainder).
4. **Determine the result:** Map the exponent to the corresponding remainder in the cycle.

---

## Shortcut Tricks

* **Trick:** Check if the base $a$ is congruent to $1$ or $-1$ modulo $m$.
* **Why it works:** $1^n = 1$ and $(-1)^n$ is either $1$ or $-1$, making the calculation instant.
* **When to use it:** If the base is close to the divisor or a multiple of the divisor.
* **Example:** For $7^{100} \div 6$, since $7 \equiv 1 \pmod{6}$, then $7^{100} \equiv 1^{100} \equiv 1 \pmod{6}$.

---

## Common Mistakes

* **Mistake:** Trying to calculate the actual value of $4^{96}$.
    * **Why it happens:** Lack of familiarity with modular arithmetic.
    * **Fix:** Always work with remainders at every step of the multiplication.
* **Mistake:** Assuming the remainder is always $0$ or $1$.
    * **Why it happens:** Over-generalizing from simple cases.
    * **Fix:** Always calculate the first two powers to verify the pattern.

---

## Worked Example (Step-by-Step)

**Question:** What is the remainder when $4^{96}$ is divided by $6$?

**Solution:**
1. **Step 1:** Calculate $4^1 \pmod{6} = 4 \pmod{6} = 4$.
2. **Step 2:** Calculate $4^2 \pmod{6} = 16 \pmod{6} = 4$ (since $16 = 6 \times 2 + 4$).
3. **Step 3:** Observe the pattern: $4^1 \equiv 4$, $4^2 \equiv 4$, $4^3 \equiv 64 \equiv 4$. The remainder is always $4$.
4. **Step 4:** Since the pattern is constant, $4^{96} \equiv 4 \pmod{6}$.

**Answer:** 4

---

## Similar Patterns

**Unit Digit Problems:** These are similar but ask for the last digit (modulo 10) instead of a remainder modulo $m$. Distinguish them by checking if the divisor is $10$ (unit digit) or another number (remainder).

---

## Revision Summary

* **Key formula:** $a^n \pmod{m}$
* **Spot it by:** Large exponent divided by a small number.
* **First move:** Calculate the first two powers modulo $m$.
* **Fastest method:** Look for a repeating cycle or a base congruent to $\pm 1$.
* **Biggest trap:** Attempting to compute the full value of the exponent.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Modular Arithmetic** — The study of remainders; $a \equiv b \pmod{m}$ means $a$ and $b$ leave the same remainder when divided by $m$.

### Formulas You Must Know First
* **Remainder Theorem** — $(a \times b) \pmod{m} = [(a \pmod{m}) \times (b \pmod{m})] \pmod{m}$.

### Terms Used In This Pattern
* **Remainder** — The amount left over after division.
* **Cyclicity** — The property where remainders repeat in a fixed sequence.