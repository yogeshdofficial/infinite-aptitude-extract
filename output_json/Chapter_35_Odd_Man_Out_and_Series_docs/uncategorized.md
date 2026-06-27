# Number Series and Odd Man Out

## Overview
These questions present a sequence of numbers where you must either identify the "wrong" number that breaks the logic or find the "missing" number that completes the pattern. The central idea is to identify the mathematical relationship (addition, multiplication, powers, or alternating sequences) governing the progression.

---

## Recognition Clues
* **"Find the odd man out" / "Find the wrong number":** You are looking for the one term that does not fit the rule established by the others.
* **"Insert the missing number":** You are looking for the next term in the sequence.
* **Rapid growth:** If numbers increase exponentially, look for multiplication or powers ($n^2, n^3$).
* **Oscillation:** If numbers go up and down, look for alternating sequences or alternating signs.
* **Small gaps:** If differences are small, look for simple addition or subtraction.

---

## Key Formulas

### [Alternating Sequence Rule]
$$ \text{Term}_n = \text{Term}_{n-2} \times \text{Multiplier} $$
**Variables:**
- $\text{Term}_n$ = The current term in a sub-sequence.
- $\text{Term}_{n-2}$ = The previous term in the same sub-sequence.
- $\text{Multiplier}$ = The constant or arithmetic progression factor.

**When to use:** When the sequence doesn't follow a single rule but seems to jump or oscillate.
**Worked example:** In $3, 4, 9, 22.5, 67.5, 202.5, 810$, the sub-sequence $3, 9, 67.5, 810$ uses multipliers $3, 7.5, 12$.

### [Difference Series]
$$ D_n = T_{n+1} - T_n $$
**Variables:**
- $D_n$ = The difference between consecutive terms.
- $T_n$ = The $n^{th}$ term.

**When to use:** When the sequence is increasing or decreasing steadily.
**Worked example:** In $5, 16, 6, 16, 7, 16, 9$, the differences reveal the pattern.

---

## Solution Framework

1. **Check the gaps:** Calculate the difference between consecutive terms to see if it's a simple arithmetic progression.
2. **Check for powers:** Scan for squares ($1, 4, 9, 16...$) or cubes ($1, 8, 27, 64...$) which are often shifted by $\pm 1$.
3. **Test for alternating series:** If the sequence looks erratic, split it into two (1st, 3rd, 5th... and 2nd, 4th, 6th...).
4. **Test for multiplication/division:** If the numbers grow very fast or shrink very fast, check for a common ratio or multiplier.
5. **Verify the "Odd" term:** If finding the wrong number, ensure the rule works for all terms *except* the one you identified.

---

## Shortcut Tricks

* **Trick:** Check the last two digits or the parity (even/odd).
* **Why it works:** Many "odd man out" questions include one number that is even in a sequence of primes, or a non-square in a sequence of squares.
* **When to use:** When you see a list of squares or primes.
* **Example:** In $16, 25, 36, 72, 144, 196, 225$, all are squares except $72$.

---

## Common Mistakes

* **Mistake:** Assuming the series is a single progression.
    * **Why it happens:** Tunnel vision on the first three numbers.
    * **Fix:** Always test if the sequence is actually two interleaved series.
* **Mistake:** Miscalculating the multiplier in a decimal series.
    * **Why it happens:** Rushing the division/multiplication.
    * **Fix:** Use fractions (e.g., $7.5 = \frac{15}{2}$) to simplify mental math.

---

## Worked Example (Step-by-Step)

**Question:** Find the wrong number in: $3, 4, 9, 22.5, 67.5, 202.5, 810$

**Solution:**
1. **Split the sequence:**
   - Series A: $3, 9, 67.5, 810$
   - Series B: $4, 22.5, 202.5$
2. **Analyze Series A:**
   - $3 \times 3 = 9$
   - $9 \times 7.5 = 67.5$
   - $67.5 \times 12 = 810$
   - Multipliers ($3, 7.5, 12$) increase by $4.5$. This is consistent.
3. **Analyze Series B:**
   - $4 \times 5.625 = 22.5$
   - $22.5 \times 9 = 202.5$
   - The first term '4' does not fit the progression established by the others.

**Answer:** 4 is the wrong number.

---

## Similar Patterns
**Arithmetic Progression:** If the difference between every term is constant, it is a simple AP; distinguish this by checking if the difference is the same for all terms.

---

## Revision Summary
* **Key formula:** $\text{Term}_n = \text{Term}_{n-2} \times \text{Multiplier}$
* **Spot it by:** Rapid growth or erratic oscillation.
* **First move:** Calculate differences between consecutive terms.
* **Fastest method:** Check for squares/cubes first, then alternating series.
* **Biggest trap:** Forgetting that the series might be two interleaved sequences.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Numbers** — Numbers divisible only by 1 and themselves ($2, 3, 5, 7, 11...$).
* **Squares/Cubes** — $n^2$ and $n^3$ values up to $20^2$ and $10^3$.
* **Parity** — Understanding even and odd number properties.

### Formulas You Must Know First
* **Arithmetic Progression:** $T_n = a + (n-1)d$ (where $a$ is the first term, $d$ is the common difference).

### Terms Used In This Pattern
* **Odd Man Out** — The term that violates the logical rule of the sequence.
* **Sub-sequence** — A smaller sequence extracted from the main one by taking every $n^{th}$ term.