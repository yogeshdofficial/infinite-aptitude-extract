# Equivalent Offers

## Overview
This pattern involves comparing two or more payment options (e.g., cash vs. credit) to determine which is more profitable or to find an equivalent value. The central idea is to bring all future payments to their **Present Worth (P.W.)** using the given interest rate so they can be compared on an equal footing.

---

## Recognition Clues
* **Keywords:** "due in," "due hence," "cash vs. credit," "settle the account," "better offer," "equivalent."
* **Given:** A future amount, a time period, and an interest rate.
* **Asked:** Which offer is better, the total present value, or the amount of a bill under a new payment arrangement.
* **Timeframe:** Always look for time expressed in months or years; convert months to years ($T = \frac{\text{months}}{12}$).

---

## Key Formulas

### Present Worth (P.W.)
$$
\text{P.W.} = \frac{\text{Amount} \times 100}{100 + (R \times T)}
$$

**Variables:**
- $\text{Amount}$ = The future value of the money
- $R$ = Rate of interest per annum
- $T$ = Time in years

**When to use:** To find the current value of a payment due in the future.

**Worked example:** Find P.W. of ₹ 12,880 due in 8 months at 18% p.a.
$T = \frac{8}{12} = \frac{2}{3}$ years.
$\text{P.W.} = \frac{12880 \times 100}{100 + (18 \times \frac{2}{3})} = \frac{1288000}{112} = ₹ 11,500$.

---

## Solution Framework

1. **Standardize Time:** Convert all time periods into years (e.g., 6 months = $0.5$ years).
2. **Calculate P.W. for each option:** Use the P.W. formula for every future payment mentioned in the problem.
3. **Sum the Values:** If an option involves multiple payments, add their individual P.W. values together.
4. **Compare:** Compare the total P.W. of the credit/deferred options against the cash offer to identify the "better" deal or solve for the unknown variable.

---

## Shortcut Tricks
* **Trick:** When comparing two offers, if the cash offer is $C$ and the credit offer is $A$ due in $T$ years, the credit offer is better only if $\frac{A \times 100}{100 + RT} > C$.
* **Why it works:** It directly compares the "today-value" of the credit offer to the cash in hand.
* **When to use:** When asked to choose between a cash payment and a single future payment.

---

## Common Mistakes
* **Mistake:** Comparing the future amount directly to the cash offer.
    * **Fix:** Always discount the future amount to its P.W. first.
* **Mistake:** Forgetting to convert months to years.
    * **Fix:** Always divide months by 12.
* **Mistake:** Using Simple Interest ($SI = \frac{PRT}{100}$) instead of the P.W. formula.
    * **Fix:** Remember $P.W. = \frac{100A}{100+RT}$, not the interest formula.

---

## Worked Example (Step-by-Step)

**Question:** A man wants to sell his scooter. There are two offers: ₹ 12,000 cash or ₹ 12,880 to be paid after 8 months (18% p.a.). Which is better?

**Solution:**
1. **Standardize Time:** 8 months = $\frac{8}{12} = \frac{2}{3}$ years.
2. **Calculate P.W. of credit offer:** $\text{P.W.} = \frac{12880 \times 100}{100 + (18 \times \frac{2}{3})} = \frac{1288000}{112} = 11500$.
3. **Compare:** The cash offer is ₹ 12,000. The credit offer is worth ₹ 11,500 today.
4. **Conclusion:** Since $12000 > 11500$, the cash offer is better.

**Answer:** The cash offer of ₹ 12,000 is better.

---

## Similar Patterns
* **True Discount Problems:** These are identical in mechanics; the only difference is the terminology. If the question asks for "True Discount," calculate $T.D. = \text{Amount} - \text{P.W.}$

---

## Revision Summary
* **Key formula:** $\text{P.W.} = \frac{100A}{100 + RT}$.
* **Spot it by:** Comparing cash vs. future payments.
* **First move:** Convert all time periods to years.
* **Fastest method:** Calculate P.W. for all future amounts and compare.
* **Biggest trap:** Comparing future amounts directly to cash without discounting.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest:** Interest calculated only on the principal amount ($SI = \frac{PRT}{100}$).
* **Present Worth:** The amount of money today that is equivalent to a larger sum of money in the future, given an interest rate.

### Formulas You Must Know First
* **Amount = Principal + Interest:** $A = P + \frac{PRT}{100} = P(1 + \frac{RT}{100})$.

### Terms Used In This Pattern
* **Due:** The date or time when a payment is required.
* **Hence:** A term meaning "from now" (e.g., 1 year hence = 1 year from now).
* **Creditor:** The person to whom money is owed.