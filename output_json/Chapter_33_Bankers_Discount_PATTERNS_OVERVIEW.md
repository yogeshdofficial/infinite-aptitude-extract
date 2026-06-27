# Bankers Discount — Chapter Overview

## What This Chapter Is About

This chapter deals with the financial mathematics of "Bills of Exchange," which are essentially written promises to pay a specific sum of money at a future date. The central relationship revolves around the difference between the "Face Value" of a bill and its "Present Worth," calculated through two different types of interest: Banker's Discount and True Discount. You will learn to calculate these values, determine the "Banker's Gain," and solve for unknown variables like time, rate, or principal when a bill is cashed before its maturity date.

---

## Core Concepts

**[Face Value]** — This is the total amount written on the bill, which the debtor is legally obligated to pay on the maturity date. Think of it as the "final price" of the transaction. *Example: If you buy goods worth ₹10,000 on credit, the bill will have a face value of ₹10,000.*

**[Legally Due Date]** — A bill is not just due on the date written; the law grants a "grace period" of three extra days. The legally due date is the nominal date plus these three days, and this is the date used for all interest calculations. *Example: If a 5-month bill is drawn on July 14, the nominal date is December 14, making the legally due date December 17.*

**[Banker’s Discount (B.D.)]** — This is the interest charged by a bank for paying the bill holder before the due date. Crucially, the bank calculates this interest on the *Face Value* of the bill, not the actual present value. *Example: If you cash a ₹6,000 bill early, the bank calculates interest on the full ₹6,000 for the remaining days.*

**[True Discount (T.D.)]** — This is the interest on the *Present Worth* (the actual value of the money today) rather than the Face Value. It represents the "fair" interest that would accrue if you were investing the present value at the given rate. *Example: If you need ₹100 today to have ₹110 in a year, the ₹10 difference is the True Discount.*

**[Banker’s Gain (B.G.)]** — Because the bank calculates interest on the Face Value (which is higher than the Present Worth), they earn slightly more than the "fair" interest. This difference is the Banker's Gain. *Example: If the Banker's Discount is ₹120 and the True Discount is ₹110, the Banker's Gain is ₹10.*

---

## Key Terms Glossary

**Bill of Exchange** — A written order used primarily in international trade that binds one party to pay a fixed sum of money to another party at a predetermined future date.

**Unexpired Time** — The period between the date the bill is actually discounted (cashed at the bank) and the legally due date.

**Present Worth (P.W.)** — The amount of money that, if invested today at the given rate, would grow to equal the Face Value of the bill by the legally due date.

---

## Pattern Map

**Basic Discount Relations** (11 questions) — Focuses on calculating B.D., T.D., and B.G. using the fundamental definitions and the relationship between them.

**Sum and Rate Calculation** (7 questions) — Requires solving for the Face Value (Sum) or the interest rate when the discount amounts are provided.

**Time Equivalence** (2 questions) — Involves finding the specific duration (time) when the relationship between B.D. and T.D. is defined by a specific ratio or equality.

---

## Core Formulas

### Banker's Discount
$$
\text{B.D.} = \text{S.I. on Face Value for the unexpired time}
$$
**Variables:** S.I. = Simple Interest.
**When to use:** Whenever you need to find the amount the bank deducts.
**Key insight:** Always use the Face Value as the principal, not the Present Worth.
**Worked example:** For ₹6,000 at 10% for 1 year, B.D. = $6000 \times 0.10 \times 1 = 600$.

### Banker's Gain
$$
\text{B.G.} = \text{B.D.} - \text{T.D.} = \text{S.I. on T.D.}
$$
**Variables:** B.D. = Banker's Discount; T.D. = True Discount.
**When to use:** When you are given one discount and need the other, or need to find the gain.
**Key insight:** The Banker's Gain is effectively the interest earned on the True Discount itself.
**Worked example:** If B.D. is ₹120 and T.D. is ₹110, B.G. = $120 - 110 = 10$.

### True Discount (from Amount)
$$
\text{T.D.} = \frac{\text{Amount} \times \text{Rate} \times \text{Time}}{100 + (\text{Rate} \times \text{Time})}
$$
**Variables:** Amount = Face Value; Rate = % per annum; Time = years.
**When to use:** When you have the Face Value and need the True Discount.
**Key insight:** The denominator includes the interest factor because T.D. is based on the Present Worth, not the Face Value.
**Worked example:** For ₹1100 at 10% for 1 year, T.D. = $\frac{1100 \times 10 \times 1}{100 + 10} = 100$.

---

## Suggested Study Order

1. **Basic Discount Relations** — Start here to master the definitions and the fundamental link between B.D., T.D., and B.G.
2. **Sum and Rate Calculation** — Study next because these problems use the basic relations as a foundation to solve for missing variables.
3. **Time Equivalence** — Study last as these are often the most abstract, requiring you to manipulate the time variable within the discount formulas.

---

## Chapter-Wide Traps

**Ignoring Grace Days:** Forgetting to add the 3 days of grace to the nominal due date will result in an incorrect "unexpired time" calculation → Always add 3 days to the nominal date unless the problem specifies otherwise.

**Confusing Principal:** Using the Present Worth as the principal for Banker's Discount instead of the Face Value → Remember: B.D. is always calculated on the Face Value.

**Time Units:** Using months or days in the formula without converting them to years → Always ensure the time variable is expressed in years (e.g., 6 months = 0.5 years).