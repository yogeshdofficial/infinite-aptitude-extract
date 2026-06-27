# Odd Man Out And Series — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Scan for Parity/Type:** Check if all numbers are prime, even, odd, or squares. If one deviates, that is the "Odd Man."
2. **Check Differences:** Calculate the difference between consecutive terms. If constant, it is Arithmetic; if increasing/decreasing, check for squares/cubes.
3. **Check Ratios:** If differences grow rapidly, calculate the ratio between terms ($T_n / T_{n-1}$). If constant, it is Geometric.
4. **Test Complex Patterns:** If simple arithmetic/geometric fails, test digit manipulation (sum, product, or middle-digit relations).
5. **Verify Consistency:** Apply the identified rule to all terms. If one term breaks the rule, it is the answer.
6. **Sanity Check:** Ensure the final answer fits the sequence logic and matches the provided options.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| **Odd One Out** | "Which is wrong", "Find odd" | Set of numbers | The outlier |
| **Series Completion** | "Next term", "Missing number" | Sequence of numbers | The next term |
| **Alternating Series** | "Alternating", "Fluctuating" | Sequence | Missing/Wrong term |

---

## Formula Bank

**[Odd One Out]**
$$ \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} $$
→ *produces: sum of first n squares*
→ *use when: identifying perfect square sequences*

$$ \text{Middle Digit} = \text{First Digit} \pm \text{Third Digit} $$
→ *produces: digit relationship check*
→ *use when: 3-digit numbers are present*

$$ \text{First Digit} \times \text{Third Digit} = \text{Middle Digit} $$
→ *produces: digit product check*
→ *use when: middle digit is product*

$$ x^2 \pm k $$
→ *produces: deviation from square*
→ *use when: numbers are near squares*

$$ T_{n+1} = T_n + n $$
→ *produces: triangular number sequence*
→ *use when: differences increase linearly*

**[Series Completion]**
$$ T_n \times T_{n+1} = T_{n+2} $$
→ *produces: next term via product*
→ *use when: terms grow exponentially*

$$ \text{Term}_n = n \times (2n+1) $$
→ *produces: specific term value*
→ *use when: series follows quadratic growth*

$$ \text{Term}_n = (P_n)^3 $$
→ *produces: cube of prime*
→ *use when: terms are large cubes*

$$ a_n = a_{n-1} \times r $$
→ *produces: geometric progression term*
→ *use when: ratio is constant*

$$ x_{n+1} = 2x_n \pm 1 $$
→ *produces: recursive sequence term*
→ *use when: doubling with offset*

---

## Step Sequences

**Odd One Out:** Check parity → Check primality → Check squares → Identify outlier.
**Series Completion:** Calculate differences → Calculate ratios → Identify rule → Apply to last.
**Alternating Series:** Split into sub-series → Apply rule to each → Find missing term.

---

## Fastest Tricks

* **Odd One Out:** Check for primes first; 12, 21, 27 are common non-prime traps.
* **Series Completion:** If terms grow very fast, check for multiplication or powers immediately.
* **Series Completion:** If terms fluctuate (up/down), check for alternating operations or sub-series.
* **Odd One Out:** If numbers are 3-digits, sum the digits or check middle-digit arithmetic.

---

## Trap Watch

* **Odd One Out:** 12 is not prime → check factors.
* **Odd One Out:** 21 is not even → check divisibility.
* **Series Completion:** Miscalculating large products → use estimation.
* **Series Completion:** Assuming arithmetic progression → always check ratios first.
* **Uncategorized:** Ignoring sub-sequence structure → split into two series.

---

## Last-Minute Reminders

* Always verify if 1 is treated as a prime or square in the specific context.
* Remember that 2 is the only even prime number.
* When differences are inconsistent, check for squares ($n^2$) or cubes ($n^3$) of the position index.
* If a series involves negative numbers, check for alternating signs or geometric ratios with negative $r$.
* Always re-check the final term calculation to ensure it doesn't violate the established pattern.