# Profit And Loss — Chapter Overview

## What This Chapter Is About

This chapter deals with the financial mechanics of buying and selling goods, focusing on the relationship between the price paid to acquire an item and the price received when it is sold. The central quantity that governs every calculation in this chapter is the **Cost Price (CP)**, as all gains, losses, and percentage changes are measured relative to this initial investment. You will encounter various scenarios, ranging from simple profit/loss calculations to complex multi-stage transactions, dishonest trading practices, and adjustments involving discounts and varying quantities.

---

## Core Concepts

**[The Primacy of Cost Price]** — In mathematics, profit and loss are not just absolute values; they are ratios. The most critical rule is that profit or loss is always calculated as a percentage of the Cost Price, not the Selling Price. If you buy an item for ₹100 and sell it for ₹120, your 20% profit is based on the ₹100 you spent, not the ₹120 you received.

**[The Percentage Multiplier]** — Instead of calculating profit or loss in currency and then adding/subtracting, you can treat the Cost Price as 100%. If you gain 20%, your Selling Price is simply 120% of the Cost Price. This mental model allows you to bypass intermediate steps and solve for unknown prices using simple algebraic equations.

**[The Equivalence of Ratios]** — Many problems involve changing conditions (like a price increase or a change in profit margin). By viewing these as ratios—where the ratio of (Cost Price) to (Selling Price) remains constant or shifts by a known percentage—you can solve complex multi-stage problems without needing to find the actual currency value of the item until the very end.

**[The "False Weight" Logic]** — When a dealer uses dishonest weights, they are essentially changing the "true" Cost Price of the goods being sold. The core concept here is that the dealer is selling a smaller quantity than what the customer believes they are buying, which effectively lowers the dealer's actual cost per unit, resulting in a hidden profit.

---

## Key Terms Glossary

**Cost Price (CP)** — The total amount of money spent to acquire an article, including any overheads like transportation or repairs.

**Selling Price (SP)** — The final amount of money received when an article is sold to a customer.

**Profit (Gain)** — The positive difference when the Selling Price is greater than the Cost Price ($SP - CP$).

**Loss** — The negative difference when the Selling Price is less than the Cost Price ($CP - SP$).

**Marked Price (MP)** — The price "tagged" on an item, often used as a reference point for discounts before the final Selling Price is determined.

**Discount** — A reduction offered on the Marked Price, meaning $SP = MP - \text{Discount}$.

---

## Pattern Map

**Basic Profit Loss** (29 questions) — The foundational pattern where you calculate simple gain/loss percentages given the CP and SP.

**Find CP from SP** (8 questions) — You are given the SP and the profit/loss percentage and must work backward to find the original CP.

**Discount and Marked Price** (96 questions) — Involves a three-step relationship: $MP \rightarrow \text{Discount} \rightarrow SP \rightarrow CP$.

**Price Change Scenarios** (86 questions) — Focuses on how a change in the CP or SP affects the final profit percentage.

**Quantity-Price Equivalence** (31 questions) — Deals with scenarios where the number of items bought does not equal the number of items sold.

**Multi-Stage Transactions** (10 questions) — A chain of sales where one person's SP becomes the next person's CP.

**Mixture Profit Loss** (16 questions) — Involves combining two items of different prices and calculating the profit on the resulting mixture.

**Dishonest Dealer** (19 questions) — Unique because it involves calculating profit based on the difference between "true weight" and "false weight."

**Miscellaneous Profit Loss** (12 questions) — Problems that do not fit standard formulas and require logical deduction.

**Uncategorized** (20 questions) — Remaining problems that require applying core concepts to unique, non-standard scenarios.

---

## Core Formulas

### Percentage Profit/Loss
$$
\text{Profit \%} = \left( \frac{SP - CP}{CP} \right) \times 100; \quad \text{Loss \%} = \left( \frac{CP - SP}{CP} \right) \times 100
$$
**Variables:** $SP$ = Selling Price, $CP$ = Cost Price.
**When to use:** When you need to find the rate of return on an investment.
**Key insight:** Always divide by $CP$, never by $SP$.
**Worked example:** $CP=200, SP=250 \rightarrow \frac{50}{200} \times 100 = 25\%$.

### Finding SP from CP
$$
SP = CP \times \left( \frac{100 \pm \text{Profit/Loss \%}}{100} \right)
$$
**Variables:** $SP$ = Selling Price, $CP$ = Cost Price.
**When to use:** When you know the cost and the desired margin.
**Key insight:** A 20% profit means you keep 120% of the cost; a 20% loss means you keep 80%.
**Worked example:** $CP=500, \text{Profit}=10\% \rightarrow SP = 500 \times 1.10 = 550$.

### Finding CP from SP
$$
CP = SP \times \left( \frac{100}{100 \pm \text{Profit/Loss \%}} \right)
$$
**Variables:** $SP$ = Selling Price, $CP$ = Cost Price.
**When to use:** When you know the final sale price and need to find the original investment.
**Key insight:** Do not just subtract the percentage from the SP; you must divide by the percentage factor.
**Worked example:** $SP=660, \text{Profit}=10\% \rightarrow CP = 660 \times \frac{100}{110} = 600$.

---

## Suggested Study Order

1. **Basic Profit Loss** — Start here to master the fundamental relationship between CP, SP, and percentages.
2. **Find CP from SP** — Essential for reversing the logic; required for almost all subsequent patterns.
3. **Discount and Marked Price** — Builds on the CP/SP relationship by adding a third variable (MP).
4. **Price Change Scenarios** — Uses the CP/SP reversal logic to handle shifting market conditions.
5. **Quantity-Price Equivalence** — Introduces the concept of unit-based profit.
6. **Multi-Stage Transactions** — Applies the CP/SP logic across multiple sequential buyers.
7. **Mixture Profit Loss** — Combines multiple CP values into a single weighted average.
8. **Dishonest Dealer** — A specialized application of profit logic using weight ratios.
9. **Miscellaneous/Uncategorized** — Tackle these last to test your flexibility with the core concepts.

---

## Chapter-Wide Traps

**The SP-Denominator Trap:** Using the Selling Price as the base for percentage calculations instead of the Cost Price. → Always identify the "investment" (CP) and use it as the denominator.

**The Percentage-Subtraction Error:** Assuming that a 20% profit followed by a 20% loss returns you to the original price. → Calculate the effect on the CP step-by-step; the base value changes after the first transaction.

**Ignoring Overhead Costs:** Forgetting to add expenses like shipping or repairs to the Cost Price. → Always calculate the "Total CP" before determining profit or loss.