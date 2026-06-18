# Varying Time Partnership

## Overview
This pattern involves partners joining or leaving a business at different intervals, meaning capital is invested for unequal durations. The central idea is that profit is distributed based on the **Equivalent Capital Ratio**, calculated as the product of investment amount and time period for each partner.

---

## Recognition Clues
* **Keywords:** "After X months", "joined him", "left the business", "at the end of the year/2 years/3 years".
* **Given:** Individual investment amounts and the specific time duration each person stayed in the business.
* **Asked:** The share of profit for one or more partners, or the ratio of profit distribution.
* **Scan:** Look for "started" (usually 12/24/36 months) vs. "joined after X months" (Total time - X).

---

## Important Formulas

### Profit Ratio Formula
$$
\text{Profit}_A : \text{Profit}_B : \text{Profit}_C = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)
$$
*Meaning:* $C$ is the capital invested, $T$ is the time period in months.
*Use when:* You need to find the ratio in which the total profit is divided.

### Individual Share Formula
$$
\text{Partner's Share} = \text{Total Profit} \times \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* The partner's specific ratio divided by the total parts of the ratio.
*Use when:* Calculating the actual monetary value of a partner's profit.

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (usually months).
2. **Calculate Duration:** For each partner, determine the exact number of months their money was invested.
3. **Compute Product:** Multiply each partner's investment by their respective time duration.
4. **Simplify Ratio:** Divide the products by their HCF to get the simplest integer ratio.
5. **Distribute Profit:** Multiply the total profit by the partner's fractional share from the ratio.

---

## Shortcut Tricks
* **Cancel Zeros Early:** Remove common zeros from all investment amounts before multiplying by time to keep numbers small.
* **Ratio Scaling:** If investments are given as multiples (e.g., $x, 2x, 3x$), ignore the $x$ entirely and use the coefficients to find the ratio.
* **Time Symmetry:** If all partners stay for the same time, ignore time and use only the capital ratio (Simple Partnership).

---

## Common Mistakes
* **Wrong Time Calculation:** Using the "joined after" time instead of the "time invested" (e.g., if joined after 3 months in a 12-month year, use 9 months, not 3).
* **Ignoring Total Duration:** Forgetting to adjust the time for the first partner if the business duration is not exactly 12 months.
* **Ratio Inversion:** Accidentally flipping the ratio when calculating the share (e.g., using $3:2$ instead of $2:3$).

---

## Similar Patterns
* **Simple Partnership:** All partners invest for the same time. **Distinction:** If no "joined after" or "left" dates are mentioned, time is constant; ignore time and use capital ratio only.

---

## Revision Summary
**Key formula:** $\text{Profit Ratio} = \text{Capital} \times \text{Time}$.
**Spot it by:** Different partners joining or leaving at different months.
**Fastest method:** Simplify capital amounts first, then multiply by months and reduce the ratio.
**Biggest trap:** Using the "joined after" time instead of the "active" time.