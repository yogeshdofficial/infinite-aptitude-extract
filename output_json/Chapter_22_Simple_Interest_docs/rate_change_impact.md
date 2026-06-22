# Rate Change Impact

## Overview
This pattern involves scenarios where a principal amount is invested at a simple interest rate, and that rate is subsequently modified (increased or decreased). The goal is to find the new interest or the new total amount, or to determine the principal based on the change in interest.

---

## Recognition Clues
* **Keywords:** "rate is increased by X%", "rate becomes Y times of itself", "interest rate increases from A% to B%".
* **Given:** Original principal, original time, original amount (or interest), and the change in rate.
* **Asked:** New amount, new interest, or the original principal.
* **Time Pressure Tip:** If the question mentions a "change in rate" and a "change in income/interest," you are dealing with a rate impact problem.

---

## Key Formulas

### Simple Interest (SI)
$$
SI = \frac{P \times R \times T}{100}
$$

**Variables:**
- $P$ = Principal
- $R$ = Rate of interest per annum
- $T$ = Time in years

**When to use:** To calculate the interest earned or to find the original rate $R$ when $P, T,$ and $SI$ are known.

**Worked example:** $P=800, SI=120, T=3$. $120 = \frac{800 \times R \times 3}{100} \implies 120 = 24R \implies R=5\%$.

---

## Solution Framework

**Step 1: Identify the original rate.** If not given, use $SI = \frac{P \times R \times T}{100}$ with the initial values to find $R$.
**Step 2: Calculate the new rate.** Add or multiply the rate change as specified in the question.
**Step 3: Calculate the new interest.** Use the new rate and the same principal/time to find the new $SI$.
**Step 4: Find the final value.** Add the new interest to the principal to get the new amount, or use the difference in interest to solve for $P$.

---

## Shortcut Tricks

* **Trick:** For "rate increased by $x\%$," the increase in interest is simply $\frac{P \times x \times T}{100}$.
* **Why it works:** It isolates the *change* in interest, bypassing the need to calculate the total interest twice.
* **When to use:** When the question asks for the *difference* in interest or the *new amount* directly.
* **Example:** $P=800, T=3, \text{rate increase}=3\%$. Increase in $SI = \frac{800 \times 3 \times 3}{100} = 72$. New Amount = $920 + 72 = 992$.

---

## Common Mistakes

* **Mistake:** Adding the rate increase to the *amount* instead of the *rate*.
    * **Fix:** Always apply the percentage change to the interest rate ($R$) only.
* **Mistake:** Forgetting to multiply the rate increase by the time period ($T$).
    * **Fix:** Remember that interest is earned *every year*; if the rate changes, it affects every year of the duration.
* **Mistake:** Calculating the new interest on the *amount* instead of the *principal*.
    * **Fix:** Simple interest is always calculated on the original principal ($P$).

---

## Worked Example (Step-by-Step)

**Question:** A sum of ₹ 800 amounts to ₹ 920 in 3 years at simple interest. If the interest rate is increased by 3%, it would amount to how much?

**Solution:**
1. **Find original rate:** $SI = 920 - 800 = 120$. $120 = \frac{800 \times R \times 3}{100} \implies R = 5\%$.
2. **Find new rate:** $R_{new} = 5\% + 3\% = 8\%$.
3. **Calculate new interest:** $SI_{new} = \frac{800 \times 8 \times 3}{100} = 192$.
4. **Find new amount:** $800 + 192 = 992$.

**Answer:** ₹ 992.

---

## Similar Patterns

**Variable Principal/Time Patterns:** If the question involves different principals or different time periods for different rates, use the summation method: $SI = \frac{P}{100}(R_1T_1 + R_2T_2 + \dots)$.

---

## Revision Summary

* **Key formula:** $SI = \frac{P \times R \times T}{100}$.
* **Spot it by:** "Rate increased by X%" or "Rate becomes Y times".
* **First move:** Find the original rate $R$ if it is missing.
* **Fastest method:** Use the shortcut $\Delta SI = \frac{P \times \Delta R \times T}{100}$.
* **Biggest trap:** Applying the rate increase to the total amount instead of the rate.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the original principal.
* **Percentage Change** — Adding or multiplying rates ($R_{new} = R + x$ or $R_{new} = R \times k$).

### Formulas You Must Know First
$$
\text{Amount} = P + SI
$$
**What it means:** The total money returned is the sum of the original principal and the interest earned.

### Terms Used In This Pattern
* **Principal ($P$)** — The initial sum of money invested.
* **Rate ($R$)** — The percentage of the principal paid as interest per year.
* **Time ($T$)** — The duration for which the money is invested.