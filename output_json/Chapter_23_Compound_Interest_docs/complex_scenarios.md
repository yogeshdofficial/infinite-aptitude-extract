# Complex Scenarios (Compound Interest)

## Overview
These questions involve non-standard compound interest scenarios such as recurring deposits, changing interest rates, or partial repayments. The central idea is to treat each time period or transaction as a distinct event, calculating the balance step-by-step rather than using a single lump-sum formula.

---

## Recognition Clues
* **Keywords:** "at the end of each year," "deposits ₹ X on [date]," "compounded half-yearly for first year and yearly for next," "pays back ₹ X."
* **Given:** Multiple deposits, varying compounding frequencies, or periodic repayments.
* **Asked:** Total amount accumulated, total interest earned, or final balance to clear dues.

---

## Key Formulas

### Future Value of Periodic Deposits
$$
\text{Amount} = \sum P(1+r)^t
$$
**Variables:**
- $P$ = amount deposited in each period
- $r$ = rate of interest per period
- $t$ = time remaining until the end of the term

**When to use:** When multiple equal deposits are made at regular intervals.

**Worked example:** For 3 deposits of ₹ 200 at 5% interest: $200(1.05)^3 + 200(1.05)^2 + 200(1.05)^1$.

### Periodic Balance Calculation
$$
\text{Balance}_{new} = (\text{Balance}_{old} \times (1+r)) - \text{Payment}
$$
**Variables:**
- $\text{Balance}_{old}$ = principal at start of period
- $r$ = interest rate for that period
- $\text{Payment}$ = amount paid back at end of period

**When to use:** When a loan is being repaid in installments over time.

---

## Solution Framework

**Step 1: Identify the timeline.** Break the total duration into individual periods (years, half-years, or quarters) based on the compounding frequency.

**Step 2: Calculate interest per period.** Adjust the annual rate $R$ to the specific period (e.g., $R/2$ for half-yearly).

**Step 3: Apply the "Rolling Balance" method.** For each period, calculate the interest on the current principal, add it, and then subtract any deposits or repayments made at that specific time.

**Step 4: Carry forward.** The resulting balance becomes the principal for the next period.

---

## Shortcut Tricks
* **Trick:** Use the "Multiplier" method for constant rates.
* **Why it works:** Instead of calculating interest and adding it, multiply the principal by $(1 + \frac{r}{100})$.
* **When to use:** When the interest rate is constant over several periods.
* **Example:** For 10% interest, multiply by 1.1; for 20% half-yearly (10%), multiply by 1.1.

---

## Common Mistakes
* **Mistake:** Assuming all deposits earn interest for the same duration.
    * **Fix:** Calculate the time remaining for *each* deposit individually.
* **Mistake:** Subtracting the repayment *before* adding the interest for that year.
    * **Fix:** Always add interest to the principal first, then subtract the payment.
* **Mistake:** Using the annual rate for half-yearly compounding.
    * **Fix:** Always divide the rate by the number of compounding periods per year.

---

## Worked Example (Step-by-Step)

**Question:** A man borrows ₹ 4000 at 15% compound interest. At the end of each year he pays back ₹ 1500. How much amount should he pay at the end of the 3rd year to clear all his dues?

**Solution:**
1. **Year 1:** Principal = 4000. Interest = $4000 \times 0.15 = 600$. Amount = $4600$. After payment: $4600 - 1500 = 3100$.
2. **Year 2:** Principal = 3100. Interest = $3100 \times 0.15 = 465$. Amount = $3565$. After payment: $3565 - 1500 = 2065$.
3. **Year 3:** Principal = 2065. Interest = $2065 \times 0.15 = 309.75$. Amount = $2374.75$.
4. **Final Payment:** To clear the debt, he must pay the full remaining amount of ₹ 2374.75. (Note: If he pays 1500 at the end of year 3, the remaining balance is $2374.75 - 1500 = 874.75$).

**Answer:** ₹ 874.75

---

## Similar Patterns
**Standard Compound Interest:** Distinguished by a single principal amount invested once for a fixed duration; use the standard formula $A = P(1+r/100)^n$ directly.

---

## Revision Summary
* **Key formula:** $\text{Balance}_{new} = (\text{Balance}_{old} \times (1+r)) - \text{Payment}$.
* **Spot it by:** Multiple transactions or changing compounding rules.
* **First move:** Break the timeline into individual compounding periods.
* **Fastest method:** Use the multiplier $(1+r)$ for each period.
* **Biggest trap:** Subtracting payments before adding interest.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Compound Interest** — Interest calculated on the initial principal and also on the accumulated interest of previous periods.
* **Geometric Series** — A sequence of numbers where each term after the first is found by multiplying the previous one by a fixed number.

### Formulas You Must Know First
$$
A = P\left(1 + \frac{R}{100}\right)^n
$$
**What it means:** The standard formula for amount $A$ after $n$ years at rate $R$.

### Terms Used In This Pattern
* **p.c.p.a.** — Per cent per annum (annual interest rate).
* **Compounded half-yearly** — Interest is calculated and added to the principal every 6 months.