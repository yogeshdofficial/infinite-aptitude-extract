# Missing Variables (True Discount)

## Overview
These questions ask you to find a missing Rate ($R$) or Time ($T$) when given the Sum Due and the True Discount ($TD$). The central idea is that the **True Discount is simply the Simple Interest on the Present Worth ($PW$)**.

---

## Recognition Clues
* **Keywords:** "True discount on [Amount] due [Time] hence is [TD]" or "due after a certain time".
* **Given:** The total amount (Sum Due) and the True Discount ($TD$).
* **Asked:** Either the rate percent ($R$) or the time ($T$).
* **Scan for:** A pair of values (Amount and $TD$) and one missing variable ($R$ or $T$).

---

## Key Formulas

### Present Worth
$$
PW = \text{Sum Due} - TD
$$
**When to use:** Always the first step to find the principal amount.

### Rate Calculation
$$
R = \frac{100 \times TD}{PW \times T}
$$
**Worked example:** $TD=122, PW=2440, T=\frac{1}{3}$ year. $R = \frac{100 \times 122}{2440 \times (1/3)} = 15\%$.

### Time Calculation
$$
T = \frac{100 \times TD}{PW \times R}
$$
**Worked example:** $TD=160, PW=1600, R=12\%$. $T = \frac{100 \times 160}{1600 \times 12} = \frac{5}{6}$ years (10 months).

---

## Solution Framework

1. **Find $PW$:** Subtract $TD$ from the Sum Due ($PW = \text{Sum} - TD$).
2. **Identify $TD$ as Interest:** Treat the $TD$ value as the Simple Interest ($I$) earned on the $PW$.
3. **Convert Units:** Ensure time is in years (e.g., 4 months = $4/12 = 1/3$ year).
4. **Apply SI Formula:** Use $I = \frac{P \times R \times T}{100}$ where $P=PW$ and $I=TD$.
5. **Solve for Missing Variable:** Rearrange to isolate $R$ or $T$.

---

## Shortcut Tricks
**Trick:** Use the ratio $\frac{TD}{PW} = \frac{R \times T}{100}$.
**Why it works:** Since $TD = \frac{PW \times R \times T}{100}$, dividing both sides by $PW$ isolates the rate-time product.
**Example:** $TD=122, PW=2440$. $\frac{122}{2440} = \frac{1}{20}$. So, $\frac{R \times T}{100} = \frac{1}{20} \implies R \times T = 5$. If $T=1/3$, then $R=15$.

---

## Common Mistakes
* **Mistake:** Using the "Sum Due" as the Principal ($P$).
    * **Fix:** Always subtract $TD$ first to get the $PW$.
* **Mistake:** Forgetting to convert months to years.
    * **Fix:** Always divide months by 12 before plugging into the formula.
* **Mistake:** Confusing True Discount with Simple Interest.
    * **Fix:** Remember $TD$ is interest on $PW$, not on the final amount.

---

## Worked Example (Step-by-Step)

**Question:** The true discount on ₹ 1760 due after a certain time at 12% per annum is ₹ 160. The time after which it is due is?

**Solution:**
1. **Find $PW$:** $PW = 1760 - 160 = 1600$.
2. **Identify $TD$ as Interest:** $TD = 160$ (this is the interest on $1600$).
3. **Apply Formula:** $T = \frac{100 \times TD}{PW \times R} = \frac{100 \times 160}{1600 \times 12}$.
4. **Calculate:** $T = \frac{16000}{19200} = \frac{160}{192} = \frac{5}{6}$ years.
5. **Convert:** $\frac{5}{6} \times 12 = 10$ months.

**Answer:** 10 months.

---

## Similar Patterns
**Simple Interest Problems:** Distinguished by the fact that they use "Principal" directly, whereas True Discount problems require calculating $PW$ from the "Sum Due" first.

---

## Revision Summary
* **Key formula:** $TD = \frac{PW \times R \times T}{100}$.
* **Spot it by:** Given Sum Due and $TD$, missing $R$ or $T$.
* **First move:** Calculate $PW = \text{Sum} - TD$.
* **Fastest method:** Use the ratio $\frac{TD}{PW} = \frac{R \times T}{100}$.
* **Biggest trap:** Using the Sum Due as the principal instead of $PW$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the principal amount `I = (P*R*T)/100`.
* **Present Worth** — The amount of money that, if invested today at a given rate, would grow to the Sum Due by the due date.

### Formulas You Must Know First
$$
I = \frac{P \times R \times T}{100}
$$
**What it means:** The standard Simple Interest formula.

### Terms Used In This Pattern
* **Sum Due** — The total amount to be paid at a future date.
* **True Discount ($TD$)** — The difference between the Sum Due and the Present Worth.