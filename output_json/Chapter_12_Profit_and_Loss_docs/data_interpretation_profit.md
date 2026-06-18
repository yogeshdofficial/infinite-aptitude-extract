# Data Interpretation Profit

## Overview
These questions involve calculating total revenue and total costs across multiple categories (e.g., train bogies) to determine net profit or profit margins. The central idea is to aggregate individual class data (Quantity $\times$ Capacity $\times$ Rate) to find total values before performing comparative analysis.

---

## Recognition Clues
* **Keywords:** "Full occupancy," "Profit margin," "Running cost," "Revenue generated," "Percentage of total profit."
* **Given:** Tables or data sets providing capacity per bogie, number of bogies, fare per passenger, and running cost per bogie.
* **Asked:** Total profit, highest profit margin class, or percentage contribution of a specific segment to the total.

---

## Important Formulas

### [Total Revenue]
$$
\text{Revenue} = \sum (\text{Number of Bogies} \times \text{Capacity per Bogie} \times \text{Fare per Passenger})
$$
*Meaning:* Sum of income from all individual classes.
*Use when:* Calculating total earnings or comparing revenue across different classes.

### [Profit Margin]
$$
\text{Profit} = \text{Total Revenue} - \text{Total Running Cost}
$$
*Meaning:* Net gain after subtracting operational expenses from gross income.
*Use when:* Determining the profitability of a specific class or the entire system.

### [Percentage Contribution]
$$
\text{Percentage} = \left( \frac{\text{Part Value}}{\text{Total Value}} \right) \times 100
$$
*Meaning:* Ratio of a specific segment's profit to the aggregate profit.
*Use when:* Comparing the weightage of one class's profit against the total system profit.

---

## Solution Framework
1. **Calculate Revenue:** Multiply (Bogies $\times$ Capacity $\times$ Fare) for each class.
2. **Calculate Costs:** Multiply (Bogies $\times$ Cost per Bogie) for each class.
3. **Find Profit:** Subtract total costs from total revenue for the required segment.
4. **Compare/Ratio:** Use the calculated values to answer specific questions (highest/lowest/percentage).

---

## Shortcut Tricks
* **Ignore Common Factors:** If comparing profit margins between classes with the same number of bogies and same running cost, compare only the (Capacity $\times$ Fare) products.
* **Rounding:** In "approximate" questions, round large numbers to the nearest thousand or hundred to simplify mental division.
* **Why it works:** Since you are comparing relative values, the common multipliers cancel out in ratios or don't change the order of magnitude.

---

## Common Mistakes
* **Miscounting Bogies:** Forgetting to multiply by the number of bogies per class.
    * *Reason:* Overlooking the "Number of bogies" column in the data table.
    * *Fix:* Always list the count of bogies for each class before starting calculations.
* **Mixing Cost and Revenue:** Subtracting revenue from cost instead of cost from revenue.
    * *Reason:* Rushing through the arithmetic.
    * *Fix:* Explicitly label columns as "Revenue" and "Cost" on your scratchpad.
* **Partial Totals:** Calculating profit for one bogie instead of the entire class.
    * *Reason:* Misreading the question as "per bogie" vs "per class."
    * *Fix:* Check if the question asks for "a bogie" or "the class."

---

## Similar Patterns
This is distinct from standard Profit & Loss because it requires **Data Aggregation** (summing multiple sources) before applying the Profit formula. Do not confuse it with simple single-item P&L problems.

---

## Revision Summary
**Key formula:** $\text{Profit} = \text{Revenue} - \text{Cost}$.
**Spot it by:** Tables showing capacity, fare, and running costs per unit.
**Fastest method:** Calculate class-wise totals first; ignore common factors when comparing.
**Biggest trap:** Forgetting to multiply by the total number of bogies in each class.