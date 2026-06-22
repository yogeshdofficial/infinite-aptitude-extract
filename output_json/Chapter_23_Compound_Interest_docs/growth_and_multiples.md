# Growth and Multiples

## Overview
This pattern involves compound interest problems where a sum grows by a specific multiple over a fixed time period. The central idea is to express the growth factor as a power of the base multiple to determine the time required for a new, larger multiple.

---

## Recognition Clues
* **Keywords:** "doubles itself," "becomes eight times," "becomes 16 times," "at compound interest."
* **Given:** A sum $P$ becomes $kP$ in $T$ years.
* **Asked:** In how many years will it become $mP$ (where $m$ is a power of $k$)?
* **Variation:** Finding the ratio of investments ($x:y:z$) required to yield equal amounts after different time periods.

---

## Key Formulas

### Growth Factor Power Rule
$$
(1 + \frac{R}{100})^{n \times k} = [(1 + \frac{R}{100})^n]^k
$$

**Variables:**
- $R$ = Rate of interest
- $n$ = Initial time period
- $k$ = Multiple of the time period

**When to use:** When you need to find the total time for a sum to become a higher power of the original multiple.

**Worked example:** If a sum doubles in 15 years, to find when it becomes 8 times ($2^3$):
$8 = 2^3 = [(1 + \frac{R}{100})^{15}]^3 = (1 + \frac{R}{100})^{45}$. Time = 45 years.

---

## Solution Framework

1. **Identify the base growth:** Write the equation $P(1 + \frac{R}{100})^T = kP$ to find the growth factor $(1 + \frac{R}{100})^T = k$.
2. **Express the target as a power:** Write the target amount as $m = k^x$.
3. **Apply the exponent:** Raise the base growth equation to the power of $x$.
4. **Equate the time:** Multiply the original time $T$ by the exponent $x$ to get the final time.

---

## Shortcut Tricks

* **Trick:** If a sum becomes $k$ times in $T$ years, it becomes $k^x$ times in $T \times x$ years.
* **Why it works:** Compound interest is geometric; the growth factor is applied multiplicatively over time.
* **When to use:** Any question asking for the time to reach a specific multiple.
* **Example:** Sum doubles ($k=2$) in 15 years ($T=15$). To become 8 times ($2^3$), $x=3$. Time = $15 \times 3 = 45$ years.

---

## Common Mistakes

* **Mistake:** Adding the time instead of multiplying.
    * **Why it happens:** Confusing compound interest with simple interest.
    * **Fix:** Always use the power rule $(k^x)$ for compound interest.
* **Mistake:** Miscalculating the power (e.g., $8 = 2^4$).
    * **Why it happens:** Rushing the exponent calculation.
    * **Fix:** Verify $2 \times 2 \times 2 = 8$ (3 times).
* **Mistake:** Inverting the ratio in equal-amount problems.
    * **Why it happens:** Forgetting that $x \cdot G^a = y \cdot G^b$ implies $x/y = G^{b-a}$.
    * **Fix:** Always set the final amounts equal and solve for the ratio.

---

## Worked Example (Step-by-Step)

**Question:** A sum of money doubles itself at compound interest in 15 years. In how many years will it become eight times?

**Solution:**
1. **Identify base growth:** The sum doubles in 15 years, so $(1 + \frac{R}{100})^{15} = 2$.
2. **Express target:** We want the sum to become 8 times. Since $8 = 2^3$, we set $m = 3$.
3. **Apply exponent:** Raise the base growth to the power of 3: $[(1 + \frac{R}{100})^{15}]^3 = 2^3 = 8$.
4. **Equate time:** The new time is $15 \times 3 = 45$ years.

**Answer:** 45 years.

---

## Similar Patterns
**Simple Interest Growth:** Distinguish by the keyword "Simple Interest"; in SI, the sum increases by a fixed amount (e.g., "doubles in 15 years" means interest = principal, so it triples in 30 years, not 45).

---

## Revision Summary
* **Key formula:** $(1 + \frac{R}{100})^{T \times x} = k^x$.
* **Spot it by:** "Becomes [multiple] times" in compound interest.
* **First move:** Identify the base multiple $k$ and time $T$.
* **Fastest method:** Multiply the time $T$ by the exponent $x$ of the target multiple.
* **Biggest trap:** Adding time instead of multiplying by the exponent.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Exponents:** Understanding that $(a^b)^c = a^{b \times c}$.
* **Compound Interest:** The concept that interest is earned on interest, leading to exponential growth.

### Formulas You Must Know First
$$
A = P(1 + \frac{R}{100})^n
$$
**What it means:** The amount $A$ after $n$ years at rate $R$.

### Terms Used In This Pattern
* **Principal ($P$):** The initial sum of money.
* **Amount ($A$):** The total value after interest is added.
* **Growth Factor:** The multiplier $(1 + \frac{R}{100})$ applied each year.