# Pattern: Partnership with Salary/Management Commission

## 1. Pattern Overview
This pattern solves problems where business partners receive a fixed salary or commission for managing the business before the remaining profit is distributed according to their investment ratios. It is essential for accurately calculating individual earnings when labor and capital contributions are both rewarded.

## 2. Key Formulas
- **Equivalent Capital:** 
  $$\text{Equivalent Capital} = \text{Investment} \times \text{Time Period}$$
- **Profit Distribution Ratio:** 
  $$\text{Ratio} = (\text{Inv}_A \times T_A) : (\text{Inv}_B \times T_B) : (\text{Inv}_C \times T_C)$$
- **Net Profit for Distribution:** 
  $$\text{Distributable Profit} = \text{Total Profit} - (\text{Total Salary/Commission})$$
- **Individual Share:** 
  $$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio}}{\text{Sum of Ratios}} \right) \times \text{Distributable Profit}$$

## 3. When to Use This Pattern
- **Keywords:** "Managing partner," "salary," "commission," "remuneration," "remaining profit."
- **Recognition Clues:** The problem mentions a total profit but specifies that one or more partners receive a fixed amount for their work before the rest is split.
- **Given:** Individual investments, time periods, total profit, and the specific salary/commission amounts.
- **To Find:** The final total earnings of each partner (Salary + Profit Share).

## 4. Core Concept & Theory
In a business, profit is the reward for both capital and labor. When a partner manages the business, they are entitled to a "wage" (salary/commission) for their time. This must be deducted from the total profit first. The remaining amount is then treated as "pure profit" to be divided based on the ratio of capital invested over time.

## 5. Step-by-Step Solution Method
1. **Calculate Total Salary/Commission:** Sum all fixed payments promised to partners.
2. **Determine Distributable Profit:** Subtract the total salary from the total annual profit.
3. **Calculate Investment Ratios:** Multiply each partner's capital by the time it was invested to find the ratio of equivalent capitals.
4. **Distribute Remaining Profit:** Divide the result from Step 2 using the ratio found in Step 3.
5. **Calculate Final Total:** Add the salary/commission back to the profit share for the managing partner(s).

## 6. Worked Examples

**Example 1: Partnership with Salary**
Given: A and B invest ₹50,000 and ₹70,000. A is the manager and receives a salary of ₹5,000. Total annual profit is ₹25,000.
Solution:
1. **Distributable Profit:** $25,000 - 5,000 = 20,000$.
2. **Ratio:** $50,000 : 70,000 = 5 : 7$.
3. **Profit Share:** 
   - A's share: $\frac{5}{12} \times 20,000 = 8,333.33$
   - B's share: $\frac{7}{12} \times 20,000 = 11,666.67$
4. **Total Earnings:** A gets $8,333.33 + 5,000 = 13,333.33$. B gets $11,666.67$.

**Example 2: Commission-based Profit**
Given: X and Y invest ₹100,000 each. X gets 10% of total profit as commission. Total profit is ₹40,000.
Solution:
1. **Commission:** $10\% \text{ of } 40,000 = 4,000$.
2. **Distributable Profit:** $40,000 - 4,000 = 36,000$.
3. **Ratio:** $1:1$ (equal investment).
4. **Profit Share:** Each gets $36,000 / 2 = 18,000$.
5. **Total Earnings:** X gets $18,000 + 4,000 = 22,000$. Y gets $18,000$.

## 7. Recognition Clues & Keywords
- **Signals:** "Out of the profit, X receives a salary..."
- **Distinction:** Do not confuse "Salary" (fixed amount) with "Profit Share" (variable amount based on ratio).
- **Application:** Always apply the salary deduction *before* calculating the ratio-based distribution.

## 8. Common Mistakes
- **Forgetting to add the salary back:** Students often calculate the profit share but forget to add the salary to the managing partner's total.
- **Deducting salary from the ratio:** Never subtract salary from the capital; it is only subtracted from the profit.
- **Incorrect Time Units:** Failing to convert all time periods to the same unit (e.g., months) before calculating the ratio.
- **Ignoring the "Remaining" clause:** Applying the ratio to the *total* profit instead of the *remaining* profit after salary.

## 9. Practice Tips
- **Visualize the Cash Flow:** Draw a flow chart: Total Profit $\rightarrow$ Minus Salary $\rightarrow$ Remaining Profit $\rightarrow$ Ratio Split.
- **Related Patterns:** Study "Simple Partnership" (fixed time) and "Compound Partnership" (varying time) to ensure you can handle the ratio calculation portion of this problem efficiently.