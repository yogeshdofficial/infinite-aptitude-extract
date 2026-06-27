# Number Properties

## Overview
These questions test your ability to classify numbers (prime, composite) or manipulate their internal structure (factors, digits, zeros). The central idea is to decompose complex expressions into their prime building blocks or use divisibility rules to isolate specific properties.

---

## Recognition Clues
* **"Which of the following are prime numbers?"**: Direct classification task.
* **"Exactly divisible by $x$"**: Algebraic expression involving divisibility.
* **"Total number of prime factors"**: Expression with exponents and composite bases.
* **"Number of zeros at the end"**: Product of a sequence or factorial.

---

## Key Formulas

### [Trial Division for Primes]
$$k^2 > n$$
**Variables:**
- $n$ = the number being tested
- $k$ = the smallest integer whose square exceeds $n$

**When to use:** To check if a number is prime. Test divisibility of $n$ by all prime numbers less than $k$.

**Worked example:** For $n=241$, $\sqrt{241} \approx 15.5$, so $k=16$. Test primes $\{2, 3, 5, 7, 11, 13\}$. None divide 241, so it is prime.

### [Legendre’s Formula]
$$E_p(n!) = \sum_{k=1}^{\infty} \lfloor \frac{n}{p^k} \rfloor$$
**Variables:**
- $E_p(n!)$ = highest power of prime $p$ in $n!$
- $\lfloor \dots \rfloor$ = floor function (integer part of the division)

**When to use:** To find the number of trailing zeros in $n!$ (use $p=5$).

**Worked example:** For $100!$, zeros = $\lfloor \frac{100}{5} \rfloor + \lfloor \frac{100}{25} \rfloor = 20 + 4 = 24$.

---

## Solution Framework
1. **Decompose:** If the base is composite (e.g., 4, 10, 125), rewrite it as a power of prime factors (e.g., $4 = 2^2$).
2. **Apply Exponent Rules:** Use $(a^m)^n = a^{m \times n}$ to simplify the expression into a product of prime bases.
3. **Identify Constraints:** For divisibility questions, express the fraction as a sum of terms to isolate the divisor.
4. **Count Factors:** For prime factor counts, sum the exponents of the prime bases.
5. **Apply Legendre’s:** For trailing zeros, count the occurrences of the prime factor 5 (or 2 if 5 is more abundant).

---

## Shortcut Tricks
* **Trick:** For trailing zeros in $n!$, ignore the prime 2; it is always more abundant than 5.
* **Why it works:** A zero is formed by $2 \times 5$. Since there are always more 2s than 5s in a factorial, the number of 5s limits the number of zeros.
* **When to use:** Any question asking for "zeros at the end" of a factorial or product of consecutive integers.

---

## Common Mistakes
* **Mistake:** Checking all integers up to $\sqrt{n}$ for primality.
    * **Fix:** Only check prime numbers up to $\sqrt{n}$.
* **Mistake:** Forgetting higher powers in Legendre's (e.g., dividing by 5 but not 25).
    * **Fix:** Always divide by $p, p^2, p^3 \dots$ until $p^k > n$.
* **Mistake:** Counting composite bases as prime factors.
    * **Fix:** Always convert bases to prime numbers first (e.g., $4^{11} \to 2^{22}$).

---

## Worked Example (Step-by-Step)

**Question:** Find the total number of prime factors in $(4)^{11} \times (7)^5 \times (11)^2$.

**Solution:**
1. **Decompose:** The base 4 is not prime. Rewrite $4$ as $2^2$.
2. **Apply Exponent Rules:** $(2^2)^{11} \times 7^5 \times 11^2 = 2^{2 \times 11} \times 7^5 \times 11^2 = 2^{22} \times 7^5 \times 11^2$.
3. **Count Factors:** The prime bases are 2, 7, and 11. The total number of prime factors is the sum of the exponents: $22 + 5 + 2 = 29$.

**Answer:** 29

---

## Similar Patterns
* **Divisibility Rules:** Confused with Number Properties when checking if a number is divisible by 3, 9, or 11; distinguish by checking if the question asks for *properties* of the number or *remainder* after division.

---

## Revision Summary
* **Key formula:** Legendre's Formula $\sum \lfloor \frac{n}{p^k} \rfloor$.
* **Spot it by:** Keywords like "prime factors," "zeros at the end," or "divisible by."
* **First move:** Convert all bases to prime numbers.
* **Fastest method:** Use Legendre's for zeros; use trial division by primes for primality.
* **Biggest trap:** Forgetting to divide by higher powers of the prime (e.g., $5^2, 5^3$).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Number** — A number with exactly two factors: 1 and itself.
* **Composite Number** — A number with more than two factors.
* **Factorial ($n!$)** — The product of all positive integers up to $n$ ($n \times (n-1) \times \dots \times 1$).

### Formulas You Must Know First
* **Exponent Laws:** $a^m \times a^n = a^{m+n}$ and $(a^m)^n = a^{m \times n}$.
* **Sum of AP:** $\frac{n}{2}(a+l)$ where $a$ is the first term and $l$ is the last term.

### Terms Used In This Pattern
* **Divisor** — A number that divides another without leaving a remainder.
* **Trailing Zeros** — The number of zeros at the end of a number, determined by factors of 10 ($2 \times 5$).