# 1. Pattern Overview
- This pattern provides a systematic method for distributing business profits or losses among partners based on their respective capital investments and the duration of those investments.
- It is essential because it ensures fair financial distribution in business scenarios where partners contribute unequal amounts of money or participate for different lengths of time.

# 2. Key Formulas
- **Ratio of Division of Gains (Simple Partnership):**
  $$\text{Share Ratio} = \text{Investment}_A : \text{Investment}_B : \text{Investment}_C$$
- **Ratio of Division of Gains (Compound Partnership):**
  $$\text{Share Ratio} = (\text{Capital}_A \times \text{Time}_A) : (\text{Capital}_B \times \text{Time}_B) : (\text{Capital}_C \times \text{Time}_C)$$
- **Individual Share Calculation:**
  $$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio Part}}{\text{Sum of all Ratio Parts}} \right) \times \text{Total Profit}$$

# 3. When to Use This Pattern
- **Keywords:** "Started a business," "invested," "joined after X months," "annual profit," "share of each."
- **Recognition Clues:** The problem involves multiple parties contributing capital and a total profit/loss to be divided.
- **Given:** Individual capital amounts and the time duration for each investment.
- **To Find:** The specific monetary share of the total profit for each partner.

# 4. Core Concept & Theory
- The fundamental principle is that **profit is proportional to the product of capital and time.**
- In a **Simple Partnership**, time is constant for all, so profit depends solely on capital.
- In a **Compound Partnership**, we calculate "equivalent capital" by multiplying the investment by the time it was active. This normalizes the contributions to a single unit of time, allowing for a fair comparison.

# 5. Step-by-Step Solution Method
1. **Identify the Partnership Type:** Determine if all partners invested for the same duration (Simple) or different durations (Compound).
2. **Calculate Equivalent Capital:** For each partner, multiply their investment by the number of months/units of time they were involved.
3. **Simplify the Ratio:** Divide the resulting products by their greatest common divisor to get the simplest integer ratio.
4. **Sum the Ratio Parts:** Add all the parts of the ratio together to find the denominator for the share calculation.
5. **Calculate Individual Shares:** Multiply the total profit by the fraction representing each partner's portion of the ratio.

# 6. Worked Examples

**Example 1: Simple Partnership**
Given: A, B, and C invest 120,000, 135,000, and 150,000 respectively. Total profit = 56,700.
Solution:
1. Ratio of investments: 120,000 : 135,000 : 150,000 = 8 : 9 : 10.
2. Sum of ratio parts: 8 + 9 + 10 = 27.
3. A's share: $(8/27) \times 56,700 = 16,800$.
4. B's share: $(9/27) \times 56,700 = 18,900$.
5. C's share: $(10/27) \times 56,700 = 21,000$.

**Example 2: Compound Partnership**
Given: Alfred (45,000 for 12 months), Peter (60,000 for 9 months), Ronald (90,000 for 3 months). Total profit = 16,500.
Solution:
1. Calculate equivalent capitals:
   - Alfred: $45,000 \times 12 = 540,000$
   - Peter: $60,000 \times 9 = 540,000$
   - Ronald: $90,000 \times 3 = 270,000$
2. Ratio: 540,000 : 540,000 : 270,000 = 2 : 2 : 1.
3. Sum of parts: 2 + 2 + 1 = 5.
4. Alfred's share: $(2/5) \times 16,500 = 6,600$.
5. Peter's share: $(2/5) \times 16,500 = 6,600$.
6. Ronald's share: $(1/5) \times 16,500 = 3,300$.

# 7. Recognition Clues & Keywords
- **Keywords:** "Joined," "withdrew," "at the end of the year," "ratio of investments."
- **Distinction:** Do not confuse this with simple interest problems. Partnership is about *division of gains*, not *accrual of interest*.

# 8. Common Mistakes
- **Ignoring Time:** Students often forget to multiply by time in compound partnerships, treating them as simple partnerships.
- **Incorrect Time Calculation:** Miscounting the months (e.g., "after 3 months" means the partner was active for $12 - 3 = 9$ months). Always calculate the *active* duration.
- **Ratio Errors:** Failing to simplify the ratio before calculating shares, which leads to unnecessarily large numbers and higher risk of arithmetic error.

# 9. Practice Tips
- **Standardize Units:** Always convert time to the same unit (e.g., months) before multiplying.
- **Check the Sum:** After calculating individual shares, always add them up to ensure they equal the total profit.
- **Related Patterns:** Study "Ratio and Proportion" and "Percentage Distribution" to strengthen the foundational math required for these problems.