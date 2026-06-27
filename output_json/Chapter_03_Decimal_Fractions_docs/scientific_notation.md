# Scientific Notation

## Overview
Scientific notation is a way to express very large or very small numbers as a product of a decimal between 1 and 10 and a power of 10. The central idea is to shift the decimal point to create a number $a$ (where $1 \le a < 10$) and adjust the exponent $n$ to keep the value equivalent.

---

## Recognition Clues
* **Keywords:** "expressed in scientific notation," "equals," "value of $k$."
* **Given:** A standard decimal number (e.g., $518,000,000$ or $0.000006723$) or an equation involving $10^k$.
* **Asked:** The equivalent form $a \times 10^n$ or the value of the exponent $k$.
* **Visual:** Look for strings of zeros or numbers with many decimal places.

---

## Key Formulas

### Scientific Notation Form
$$
N = a \times 10^n
$$
**Variables:**
- $N$ = the original number
- $a$ = a coefficient such that $1 \le a < 10$
- $n$ = an integer exponent

**When to use:** Converting any standard number into scientific notation.

**Worked example:** For $518,000,000$, move the decimal 8 places left to get $5.18$. Thus, $5.18 \times 10^8$.

### Exponent Rule for Division
$$
\frac{1}{10^n} = 10^{-n}
$$
**Variables:**
- $n$ = the number of places the decimal is moved to the right.

**When to use:** Converting small decimals (e.g., $0.000006723$) to scientific notation.

**Worked example:** $0.000006723 = 6.723 \times 10^{-6}$.

---

## Solution Framework

**Step 1: Identify the target coefficient $a$** — Place the decimal point after the first non-zero digit to ensure $1 \le a < 10$.
**Step 2: Count the shifts** — Count how many places the decimal point moved from its original position to the new position.
**Step 3: Determine the sign of $n$** — Use a positive exponent ($+n$) if the original number was $\ge 10$; use a negative exponent ($-n$) if the original number was $< 1$.
**Step 4: Write the final form** — Combine the coefficient and the power of 10 as $a \times 10^n$.

---

## Shortcut Tricks
* **Trick:** "Left is Positive, Right is Negative."
* **Why it works:** Moving the decimal left divides the number by 10, so you must multiply by $10^n$ to compensate; moving right multiplies by 10, so you must multiply by $10^{-n}$.
* **When to use:** Every conversion problem.
* **Example:** $518,000,000 \rightarrow$ move decimal 8 places **Left** $\rightarrow 10^{+8}$. $0.000006723 \rightarrow$ move decimal 6 places **Right** $\rightarrow 10^{-6}$.

---

## Common Mistakes
* **Mistake:** Choosing $a$ outside the range $[1, 10)$ (e.g., $51.8 \times 10^7$).
    * **Fix:** Always ensure only one non-zero digit is to the left of the decimal.
* **Mistake:** Confusing the sign of the exponent for small decimals.
    * **Fix:** Remember that numbers starting with $0.00...$ always have a negative exponent.
* **Mistake:** Miscounting the number of shifts.
    * **Fix:** Use a pencil to "hop" over each digit while counting.

---

## Worked Example (Step-by-Step)

**Question:** If $1.125 \times 10^k = 0.001125$, then the value of $k$ is:

**Solution:**
1. **Isolate $10^k$:** Divide both sides by $1.125 \rightarrow 10^k = \frac{0.001125}{1.125}$.
2. **Convert to scientific notation:** Express $0.001125$ as $1.125 \times 10^{-3}$ (moving the decimal 3 places to the right).
3. **Simplify:** $\frac{1.125 \times 10^{-3}}{1.125} = 10^{-3}$.
4. **Equate exponents:** Since $10^k = 10^{-3}$, then $k = -3$.

**Answer:** $k = -3$

---

## Similar Patterns
* **Decimal Fractions:** These involve basic arithmetic or conversion to vulgar fractions. Scientific notation is distinct because it specifically requires the $a \times 10^n$ format.

---

## Revision Summary
* **Key formula:** $a \times 10^n$ where $1 \le a < 10$.
* **Spot it by:** Large numbers with many zeros or small decimals like $0.000...$.
* **First move:** Place the decimal after the first non-zero digit.
* **Fastest method:** Count shifts; Left = Positive exponent, Right = Negative exponent.
* **Biggest trap:** Forgetting that $0.00...$ numbers require a negative exponent.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Decimal Place Value** — Understanding that each position to the right of the decimal represents a power of $10^{-1}, 10^{-2}$, etc.
* **Exponent Laws** — Specifically $a^m \times a^n = a^{m+n}$ and $\frac{a^m}{a^n} = a^{m-n}$.

### Formulas You Must Know First
$$
a^m \times a^n = a^{m+n}
$$
**What it means:** When multiplying powers with the same base, add the exponents.
**Example:** $10^2 \times 10^3 = 10^5$.

### Terms Used In This Pattern
* **Coefficient** — The number $a$ in $a \times 10^n$.
* **Exponent** — The power $n$ to which 10 is raised.
* **Vulgar Fraction** — A fraction in the form $\frac{p}{q}$.