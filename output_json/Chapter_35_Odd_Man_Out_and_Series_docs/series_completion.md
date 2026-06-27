# Series Completion

## Overview
Series completion questions present a sequence of numbers with a missing term or an "odd one out." The central idea is to identify the mathematical rule (arithmetic, geometric, or functional) governing the progression of terms.

---

## Recognition Clues
* **Visual:** A string of numbers separated by commas, often ending in `(...)` or a question mark.
* **Instruction:** Look for phrases like "Find the missing number," "Find the wrong number," or "Find the odd man out."
* **Structure:** If the numbers grow rapidly, suspect multiplication or powers; if they grow slowly, suspect addition or subtraction.

---

## Key Formulas

### [General Term Rule]
$$
a_n = f(a_{n-1})
$$
**Variables:**
- $a_n$ = the $n$-th term
- $f$ = the function or operation applied to the previous term

**When to use:** When each term is derived from the one immediately preceding it.

**Worked example:** In Q41 (4, -8, 16, -32, 64), the rule is $a_n = a_{n-1} \times (-2)$. Thus, $64 \times (-2) = -128$.

### [Power Series]
$$
a_n = n^k
$$
**Variables:**
- $n$ = the position of the term (1, 2, 3...)
- $k$ = the constant exponent (e.g., 2 for squares, 3 for cubes)

**When to use:** When terms are perfect squares ($1, 4, 9...$) or cubes ($1, 8, 27...$).

**Worked example:** In Q44 (1, 8, 27, 64, 125, 216), $a_7 = 7^3 = 343$.

---

## Solution Framework

**Step 1: Calculate Differences** — Subtract consecutive terms to check for a constant or pattern-based difference.
**Step 2: Check Ratios/Products** — If differences aren't constant, divide consecutive terms to check for a multiplier.
**Step 3: Test Powers/Primes** — Check if terms are squares, cubes, or prime numbers.
**Step 4: Identify Alternating Patterns** — If the sequence fluctuates (e.g., $+3, \times 2$), check for two interleaved rules.
**Step 5: Verify the Rule** — Apply the identified rule to the entire sequence to ensure it holds for every term.

---

## Shortcut Tricks

* **Trick:** Check the "Difference of Differences" (Second-order difference).
* **Why it works:** Many complex series become simple arithmetic progressions when you subtract the differences between terms.
* **When to use:** When Step 1 (simple differences) shows no obvious pattern.
* **Example:** In a series like 2, 5, 10, 17... differences are 3, 5, 7... (the second-order difference is a constant 2).

---

## Common Mistakes

* **Mistake:** Assuming the pattern is simple addition when it is actually multiplication.
* **Why it happens:** Rushing to calculate differences without checking for rapid growth.
* **Fix:** If the numbers increase significantly, test multiplication or powers first.
* **Mistake:** Stopping the check after the first three terms.
* **Why it happens:** Overconfidence in a perceived pattern.
* **Fix:** Always verify the rule against the *last* two terms in the sequence.

---

## Worked Example (Step-by-Step)

**Question:** 5, 10, 13, 26, 29, 58, 61, (...)

**Solution:**
1. **Step 1 (Differences):** $10-5=5$, $13-10=3$, $26-13=13$. No constant difference.
2. **Step 2 (Ratios):** $10/5=2$, $26/13=2$, $58/29=2$.
3. **Step 4 (Alternating):** Notice the pattern: $5 \times 2 = 10$, $10 + 3 = 13$, $13 \times 2 = 26$, $26 + 3 = 29$, $29 \times 2 = 58$, $58 + 3 = 61$.
4. **Step 5 (Apply):** The last operation was $+3$, so the next is $\times 2$. $61 \times 2 = 122$.

**Answer:** 122

---

## Similar Patterns
**Analogy/Coding-Decoding:** These involve relationships between words or letters rather than numerical growth; if the sequence contains letters, it is not a Series Completion problem.

---

## Revision Summary
* **Key formula:** $a_n = f(a_{n-1})$ or $a_n = n^k$.
* **Spot it by:** Missing terms or "odd one out" instructions.
* **First move:** Calculate differences between consecutive terms.
* **Fastest method:** Check for squares/cubes first, then alternating operations.
* **Biggest trap:** Assuming a pattern holds without checking the final terms.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Numbers** — Numbers divisible only by 1 and themselves ($2, 3, 5, 7, 11...$).
* **Squares/Cubes** — The result of a number multiplied by itself ($n^2$) or three times ($n^3$).

### Formulas You Must Know First
* **Arithmetic Progression:** $a_n = a + (n-1)d$ (where $d$ is the common difference).
* **Geometric Progression:** $a_n = a \cdot r^{(n-1)}$ (where $r$ is the common ratio).

### Terms Used In This Pattern
* **Term:** A single number in a sequence.
* **Odd Man Out:** The term that does not follow the established rule of the series.