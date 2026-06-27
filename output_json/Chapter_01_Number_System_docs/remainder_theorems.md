# Remainder Theorems

## Overview
These questions ask for the remainder when a large power or expression is divided by a divisor. The central idea is to manipulate the expression into the form $(x^n \pm a^n)$ to utilize algebraic divisibility properties, or to use modular arithmetic to reduce the base.

---

## Recognition Clues
* **Keywords:** "Find the remainder," "divided by," "large power" (e.g., $7^{126}$).
* **Given:** A base raised to a high power, often with an added or subtracted constant.
* **Asked:** The remainder when divided by a specific integer.
* **Visual cue:** The divisor is usually very close to the base (e.g., $9^6$ divided by 8) or a factor of the base.

---

## Key Formulas

### [Divisibility of $x^n - a^n$]
$$x^n - a^n \text{ is divisible by } (x - a) \text{ for all } n$$
**Variables:** $x$ = base, $a$ = constant, $n$ = exponent.
**When to use:** When the divisor is $(x-a)$.
**Worked example:** $9^6 - 1^6$ divided by $(9-1)=8$. Remainder is 0.

### [Divisibility of $x^n + a^n$]
$$x^n + a^n \text{ is divisible by } (x + a) \text{ for odd } n$$
**Variables:** $x, a, n$ as above.
**When to use:** When the divisor is $(x+a)$ and the exponent is odd.
**Worked example:** $397^{3589} + 1^{3589}$ divided by $(397+1)=398$. Remainder is 0.

### [Modular Reduction]
$$a \equiv b \pmod{n} \implies a^k \equiv b^k \pmod{n}$$
**Variables:** $a$ = base, $b$ = remainder of base/divisor, $n$ = divisor, $k$ = exponent.
**When to use:** When the base is slightly larger or smaller than the divisor.
**Worked example:** $17^{200} \pmod{18}$. Since $17 \equiv -1 \pmod{18}$, then $(-1)^{200} = 1$.

---

## Solution Framework
1. **Identify the divisor:** Determine if the divisor relates to the base via $(x-a)$ or $(x+a)$.
2. **Rewrite the expression:** Adjust the base or exponent to match the algebraic identity.
3. **Apply the identity:** Use the divisibility rules to show the expression is a multiple of the divisor plus a remainder.
4. **Handle constants:** If there is an extra term (e.g., $+5$), add it to the remainder found in step 3.
5. **Final adjustment:** Ensure the final remainder is positive and less than the divisor.

---

## Shortcut Tricks
* **Trick:** If $x \equiv -1 \pmod{n}$, then $x^k \equiv (-1)^k \pmod{n}$.
* **Why it works:** $(-1)^{\text{even}} = 1$ and $(-1)^{\text{odd}} = -1$.
* **When to use:** When the base is exactly 1 less than the divisor.
* **Example:** $17^{200} \div 18 \rightarrow (-1)^{200} = 1$.

---

## Common Mistakes
* **Mistake:** Squaring only the remainder in $N^2 \pmod{d}$. **Fix:** Use $(dq+r)^2$ and expand fully.
* **Mistake:** Forgetting that $x^n + a^n$ is only divisible by $(x+a)$ if $n$ is odd. **Fix:** Check if $n$ is odd before applying.
* **Mistake:** Leaving a negative remainder. **Fix:** Add the divisor to the negative result (e.g., $-1 \equiv 17 \pmod{18}$).

---

## Worked Example (Step-by-Step)

**Question:** Find the remainder when $(397)^{3589} + 5$ is divided by 398.

**Solution:**
1. **Identify:** Divisor is 398. Base is 397. Note $397 = 398 - 1$.
2. **Rewrite:** Use $x^n + a^n$ property. Since $3589$ is odd, $(397)^{3589} + 1^{3589}$ is divisible by $(397+1) = 398$.
3. **Apply:** $(397)^{3589} + 1 = 398k \implies (397)^{3589} = 398k - 1$.
4. **Add constant:** Substitute into expression: $(398k - 1) + 5 = 398k + 4$.
5. **Result:** The remainder is 4.

**Answer:** 4

---

## Similar Patterns
* **Cyclicity/Unit Digit:** Distinguished by the question asking for the "last digit" rather than the "remainder when divided by $n$."

---

## Revision Summary
* **Key formula:** $x^n - a^n$ is divisible by $(x-a)$.
* **Spot it by:** Large powers and a divisor close to the base.
* **First move:** Express the base as $(divisor \pm 1)$.
* **Fastest method:** Use modular arithmetic $x \equiv \pm 1 \pmod{n}$.
* **Biggest trap:** Forgetting the "odd $n$" condition for $(x+a)$ divisibility.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Division Algorithm:** $N = dq + r$, where $0 \le r < d$.
* **Modular Arithmetic:** $a \equiv b \pmod{n}$ means $a$ and $b$ leave the same remainder when divided by $n$.

### Formulas You Must Know First
* $(a+b)^2 = a^2 + 2ab + b^2$
* $(-1)^{\text{even}} = 1$
* $(-1)^{\text{odd}} = -1$

### Terms Used In This Pattern
* **Divisor:** The number by which another number is divided.
* **Remainder:** The amount left over after division.