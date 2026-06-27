# Basic Square Roots

## Overview
This pattern involves finding the square root of perfect square integers, large numbers, or fractions. The central idea is to decompose the number into prime factors or use the long division algorithm to systematically extract the root.

---

## Recognition Clues
* **Keywords:** "Evaluate", "Find the square root", "Perfect square", "Exactly divisible".
* **Given:** A large integer, a mixed fraction, or a set of numbers requiring an LCM.
* **Asked:** The square root value, or the smallest number to add/multiply to make a number a perfect square.

---

## Key Formulas

### [Prime Factorization Property]
$$
\sqrt{a^2 \times b^2 \times c^2} = a \times b \times c
$$
**Variables:** $a, b, c$ are prime factors.
**When to use:** For smaller numbers or when prime factors are easily identifiable.
**Worked example:** For $\sqrt{6084}$, factors are $2^2 \times 3^2 \times 13^2$. Root = $2 \times 3 \times 13 = 78$.

### [Fractional Square Root]
$$
\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}
$$
**Variables:** $a$ = numerator, $b$ = denominator.
**When to use:** When the input is a fraction or mixed number.
**Worked example:** For $\sqrt{1\frac{9}{16}}$, convert to $\sqrt{\frac{25}{16}} = \frac{\sqrt{25}}{\sqrt{16}} = \frac{5}{4}$.

---

## Solution Framework

1. **Simplify/Convert:** Convert mixed fractions to improper fractions or find the LCM if the question asks for a number divisible by a set.
2. **Factorize or Group:** Use prime factorization for smaller numbers or group digits into pairs (from right to left) for large numbers.
3. **Extract Root:** Apply the factorization property or the long division algorithm.
4. **Adjust (if needed):** If asked for the "smallest number to add," find the next perfect square and subtract the original number.

---

## Shortcut Tricks
* **Trick:** For "smallest number to add," find the square root by long division, take the next integer, square it, and subtract the original number.
* **Why it works:** It identifies the gap between the current non-square number and the very next perfect square.
* **When to use:** When asked "what must be added to $X$ to make it a perfect square."
* **Example:** For 1780, $\sqrt{1780} \approx 42.1$. Next integer is 43. $43^2 = 1849$. Add $1849 - 1780 = 69$.

---

## Common Mistakes
* **Grouping Error:** Starting digit grouping from the left instead of the unit's digit (right).
* **Trial Divisor Error:** Forgetting to double the *entire* current quotient when calculating the next trial divisor in long division.
* **Fraction Error:** Taking the square root of the whole number and fraction separately instead of converting to an improper fraction first.

---

## Worked Example (Step-by-Step)

**Question:** Find the greatest number of five digits which is a perfect square.

**Solution:**
1. **Identify:** The greatest 5-digit number is 99999.
2. **Group:** Group digits as $(9)(99)(99)$.
3. **Long Division:** 
   - $3^2 = 9$. Remainder 0.
   - Bring down 99. Trial divisor $3 \times 2 = 6$. $61 \times 1 = 61$. Remainder 38.
   - Bring down 99. Current quotient 31. Trial divisor $31 \times 2 = 62$. $626 \times 6 = 3756$. Remainder 143.
4. **Adjust:** Subtract the remainder from the original number: $99999 - 143 = 99856$.

**Answer:** 99856

---

## Similar Patterns
**Cube Roots:** Distinguished by the index $3$ (e.g., $\sqrt[3]{x}$); requires prime factorization in triplets instead of pairs.

---

## Revision Summary
* **Key formula:** $\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}$.
* **Spot it by:** Looking for "perfect square" or "square root" in the prompt.
* **First move:** Group digits in pairs from the right or factorize into primes.
* **Fastest method:** Long division for large numbers; prime factorization for small ones.
* **Biggest trap:** Forgetting to double the quotient during long division steps.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Factorization** — Breaking a number into a product of prime numbers.
* **Perfect Square** — A number that is the product of an integer multiplied by itself.

### Formulas You Must Know First
$$
a^2 \times b^2 = (a \times b)^2
$$
**What it means:** The product of two squares is the square of their product.
**Example:** $2^2 \times 3^2 = 4 \times 9 = 36 = 6^2$.

### Terms Used In This Pattern
* **Period** — A pair of digits in a number, marked off from right to left for square root extraction.
* **Trial Divisor** — The number used to test the next digit of the square root during long division.