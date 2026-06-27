# Basic Discount Relations

## Overview
These questions involve financial bills where a payment is due at a future date. The core idea is that the **Banker's Discount (B.D.)** is interest on the total face value, while the **True Discount (T.D.)** is interest on the actual present value (Present Worth).

---

## Recognition Clues
* **Keywords:** "Bill," "due date," "discounted," "banker's discount," "true discount," "banker's gain," "present worth."
* **Given:** Usually two of (B.D., T.D., B.G., P.W., Face Value, Rate, Time).
* **Asked:** Find the missing value among the set above.
* **Time Clue:** Look for "due X months hence" or specific dates (requires calculating unexpired time).

---

## Key Formulas

### [Fundamental Identities]
$$
\text{B.D.} = \text{T.D.} + \text{B.G.}
$$
$$
\text{B.G.} = \text{S.I. on T.D.}
$$

**Variables:**
- B.D. = Banker's Discount
- T.D. = True Discount
- B.G. = Banker's Gain

**When to use:** When you have two of these three values and need the third.

**Worked example:** If T.D. = 120 and B.G. = 9, then B.D. = 120 + 9 = 129.

### [Relationship with Present Worth]
$$
\text{T.D.} = \sqrt{\text{P.W.} \times \text{B.G.}}
$$

**Variables:**
- P.W. = Present Worth

**When to use:** When P.W. and T.D. are given, and you need B.G. or B.D.

**Worked example:** P.W. = 1100, T.D. = 110. $\text{B.G.} = \frac{110^2}{1100} = 11$.

---

## Solution Framework

1. **Identify the Time:** Calculate the unexpired time in years (Days/365 or Months/12). Add 3 days of grace if a specific date is provided.
2. **Calculate B.D.:** Use $\text{B.D.} = \text{Face Value} \times \text{Rate} \times \text{Time}$.
3. **Calculate T.D.:** Use $\text{T.D.} = \frac{\text{Face Value} \times \text{Rate} \times \text{Time}}{100 + (\text{Rate} \times \text{Time})}$.
4. **Find B.G.:** Subtract T.D. from B.D. ($\text{B.G.} = \text{B.D.} - \text{T.D.}$).
5. **Find P.W. (if needed):** $\text{P.W.} = \text{Face Value} - \text{T.D.}$

---

## Shortcut Tricks

* **Trick:** $\frac{\text{T.D.}}{\text{B.G.}} = \frac{\text{Sum}}{\text{B.D.}}$
* **Why it works:** Derived from the ratio of interest on P.W. vs interest on Face Value.
* **When to use:** When you are given the Sum (Face Value) and B.D. and need T.D. or B.G.
* **Example:** Sum = 1650, B.D. = 165. Ratio = $1650/165 = 10$. So T.D. = $10 \times \text{B.G.}$

---

## Common Mistakes

* **Mistake:** Forgetting 3 days of grace. **Fix:** Always add 3 days to the nominal due date.
* **Mistake:** Calculating T.D. as S.I. on Face Value. **Fix:** T.D. is S.I. on Present Worth, not Face Value.
* **Mistake:** Confusing B.G. with B.D. **Fix:** B.G. is the *difference* between the two discounts.

---

## Worked Example (Step-by-Step)

**Question:** The present worth of a bill is ₹ 1100 and the true discount is ₹ 110. Find the banker’s discount and banker’s gain.

**Solution:**
1. **Find B.G.:** Use $\text{T.D.} = \sqrt{\text{P.W.} \times \text{B.G.}}$
   $110 = \sqrt{1100 \times \text{B.G.}}$
   $12100 = 1100 \times \text{B.G.}$
   $\text{B.G.} = 11$.
2. **Find B.D.:** Use $\text{B.D.} = \text{T.D.} + \text{B.G.}$
   $\text{B.D.} = 110 + 11 = 121$.

**Answer:** Banker's Discount = ₹ 121, Banker's Gain = ₹ 11.

---

## Similar Patterns
**Simple Interest:** Distinguish by the presence of "Bill," "Grace Days," and "Discounting." If it's just "Sum, Rate, Time," it is standard S.I.

---

## Revision Summary
* **Key formula:** $\text{B.D.} = \text{T.D.} + \text{B.G.}$
* **Spot it by:** Keywords "Bill," "Discounted," "Grace days."
* **First move:** Calculate unexpired time (add 3 days grace).
* **Fastest method:** Use the ratio $\frac{\text{T.D.}}{\text{B.G.}} = \frac{\text{Sum}}{\text{B.D.}}$
* **Biggest trap:** Calculating T.D. on the Face Value instead of P.W.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest (S.I.):** Interest calculated only on the principal amount `S.I. = (P * R * T) / 100`.
* **Grace Days:** 3 extra days added to the nominal due date of a bill to determine the legal due date.

### Formulas You Must Know First
* **S.I. Formula:** `S.I. = (P * R * T) / 100`.

### Terms Used In This Pattern
* **Face Value:** The total amount written on the bill.
* **Present Worth (P.W.):** The value of the bill today (Face Value - T.D.).
* **Unexpired Time:** The time remaining between the date of discounting and the legal due date.