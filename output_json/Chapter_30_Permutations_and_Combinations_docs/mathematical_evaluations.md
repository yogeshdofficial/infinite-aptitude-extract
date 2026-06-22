# Mathematical Evaluations

## Overview
This pattern involves simplifying expressions containing factorials ($n!$), permutations ($^nP_r$), and combinations ($^nC_r$). The central idea is to expand the larger factorial to cancel out the smaller one in the denominator, reducing the expression to simple multiplication or division.

---

## Recognition Clues
* **Keywords:** "Evaluate", "!", "P", "C", or expressions like $\frac{50!}{48!}$.
* **Given:** Large factorial values or P/C notation.
* **Asked:** A single numerical value resulting from the simplification.
* **Visual:** Fractions with factorials or differences between P and C terms.

---

## Key Formulas

### Factorial Expansion
$$
n! = n \times (n-1) \times (n-2) \times \dots \times 1
$$
**Variables:** $n$ = positive integer.
**When to use:** To simplify fractions like $\frac{50!}{48!}$.
**Worked example:** $\frac{50!}{48!} = \frac{50 \times 49 \times 48!}{48!} = 50 \times 49 = 2450$.

### Permutation Formula
$$
^nP_r = \frac{n!}{(n-r)!}
$$
**Variables:** $n$ = total items, $r$ = items to arrange.
**When to use:** When asked for arrangements or specific $^nP_r$ values.
**Worked example:** $^{50}P_3 = \frac{50!}{(50-3)!} = 50 \times 49 \times 48 = 117600$.

### Combination Formula
$$
^nC_r = \frac{n!}{r!(n-r)!}
$$
**Variables:** $n$ = total items, $r$ = items to select.
**When to use:** When asked for selections or specific $^nC_r$ values.
**Worked example:** $^{10}C_3 = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.

---

## Solution Framework
1. **Expand:** Write out the larger factorial until it matches the smaller factorial in the denominator.
2. **Cancel:** Strike out the common factorial terms from the numerator and denominator.
3. **Simplify:** Perform the remaining multiplication or division.
4. **Apply Properties:** Use $^nC_r = ^nC_{n-r}$ to reduce large $r$ values and $^nC_n = 1$ or $0! = 1$ to resolve edge cases.

---

## Shortcut Tricks
* **Trick:** Use $^nC_r = ^nC_{n-r}$ for large $r$.
* **Why it works:** Selecting $r$ items is the same as leaving $n-r$ items behind.
* **When to use:** When $r > \frac{n}{2}$ (e.g., $^{100}C_{98}$ becomes $^{100}C_2$).
* **Example:** $^{100}C_{98} = ^{100}C_2 = \frac{100 \times 99}{2 \times 1} = 4950$.

---

## Common Mistakes
* **Mistake:** Calculating the full value of $50!$. **Fix:** Always expand only until you can cancel the denominator.
* **Mistake:** Assuming $0! = 0$. **Fix:** Remember $0! = 1$.
* **Mistake:** Forgetting to divide by $r!$ in combinations. **Fix:** Permutations are ordered; combinations are not—always divide by $r!$ for combinations.

---

## Worked Example (Step-by-Step)

**Question:** Evaluate $(^{75}P_2 - ^{75}C_2)$

**Solution:**
1. **Expand Permutation:** $^{75}P_2 = \frac{75!}{(75-2)!} = \frac{75 \times 74 \times 73!}{73!} = 75 \times 74 = 5550$.
2. **Expand Combination:** $^{75}C_2 = \frac{75!}{2!(75-2)!} = \frac{75 \times 74}{2 \times 1} = 75 \times 37 = 2775$.
3. **Subtract:** $5550 - 2775 = 2775$.

**Answer:** 2775

---

## Similar Patterns
* **Word Arrangement Problems:** These use the same factorial logic but require identifying repeating letters (e.g., "ENGINEERING") and dividing by the factorial of the count of repeats.

---

## Revision Summary
* **Key formula:** $^nP_r = \frac{n!}{(n-r)!}$ and $^nC_r = \frac{n!}{r!(n-r)!}$.
* **Spot it by:** Factorial symbols or P/C notation in the question.
* **First move:** Expand the larger factorial to cancel the smaller one.
* **Fastest method:** Use $^nC_r = ^nC_{n-r}$ to simplify large combinations.
* **Biggest trap:** Calculating full factorials instead of canceling terms.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$)** — The product of all integers from $n$ down to $1$.
* **Permutation** — An arrangement where order matters.
* **Combination** — A selection where order does not matter.

### Formulas You Must Know First
* **$0! = 1$** — By definition, the factorial of zero is one.
* **$^nC_n = 1$** — Selecting all $n$ items from $n$ can be done in only 1 way.

### Terms Used In This Pattern
* **$n!$** — Factorial notation.
* **$^nP_r$** — Permutation of $n$ items taken $r$ at a time.
* **$^nC_r$** — Combination of $n$ items taken $r$ at a time.