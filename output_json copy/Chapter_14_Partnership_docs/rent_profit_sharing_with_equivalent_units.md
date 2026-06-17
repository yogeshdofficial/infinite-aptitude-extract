# Pattern: Rent/Profit Sharing with Equivalent Units

## 1. Pattern Overview
This pattern provides a systematic method to distribute business profits or rent among partners based on the proportional contribution of their capital over specific time durations. It is essential for ensuring fair financial distribution when partners invest different amounts of money for varying lengths of time.

## 2. Key Formulas
The distribution of profit is always proportional to the **Equivalent Capital** (also known as the product of capital and time).

**Ratio of Profit Sharing:**
$$\text{Share Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3) : \dots$$
Where $C$ is the capital invested and $T$ is the time period of investment.

**Individual Share Calculation:**
$$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right) \times \text{Total Profit}$$

## 3. When to Use This Pattern
*   **Keywords:** "Started a business," "joined after X months," "invested for Y months," "annual profit," "share of each."
*   **Recognition Clues:** The problem involves multiple people contributing money, and either the time periods are different or the capital amounts are different.
*   **Given:** Individual capital amounts and the duration each capital was invested.
*   **To Find:** The specific monetary share of the total profit for each partner.

## 4. Core Concept & Theory
The fundamental principle is that profit is a reward for both **money** and **time**. If Partner A invests \$100 for 1 month, they have contributed 100 "unit-months." If Partner B invests \$50 for 2 months, they have also contributed 100 "unit-months." Therefore, they deserve an equal share of the profit. By calculating the product of capital and time, we normalize all investments into a common unit, allowing for a fair ratio-based division.

## 5. Step-by-Step Solution Method
1.  **Identify Variables:** List the capital ($C$) and time ($T$) for each partner. Ensure all time units are consistent (e.g., convert all to months).
2.  **Calculate Equivalent Units:** Multiply each partner's capital by their respective time period ($C \times T$).
3.  **Simplify the Ratio:** Divide the resulting products by their greatest common divisor to get the simplest integer ratio.
4.  **Sum the Ratios:** Add all parts of the ratio together to find the "Total Parts."
5.  **Calculate Individual Shares:** Multiply the total profit by the fraction represented by each partner's ratio part.

## 6. Worked Examples

**Example 1: Simple Partnership (Equal Time)**
*Given:* A, B, and C invest ₹1,20,000, ₹1,35,000, and ₹1,50,000 respectively for 1 year. Total profit = ₹56,700.
*Solution:*
1. Ratio of investments: $120,000 : 135,000 : 150,000 = 8 : 9 : 10$.
2. Sum of ratios: $8 + 9 + 10 = 27$.
3. A's share: $(8/27) \times 56,700 = ₹16,800$.
4. B's share: $(9/27) \times 56,700 = ₹18,900$.
5. C's share: $(10/27) \times 56,700 = ₹21,000$.

**Example 2: Compound Partnership (Different Time)**
*Given:* Alfred (₹45,000 for 12 months), Peter (₹60,000 for 9 months), Ronald (₹90,000 for 3 months). Total profit = ₹16,500.
*Solution:*
1. Equivalent units: $(45,000 \times 12) : (60,000 \times 9) : (90,000 \times 3)$.
2. Simplify: $540,000 : 540,000 : 270,000 = 2 : 2 : 1$.
3. Sum of ratios: $2 + 2 + 1 = 5$.
4. Alfred/Peter share: $(2/5) \times 16,500 = ₹6,600$ each.
5. Ronald's share: $(1/5) \times 16,500 = ₹3,300$.

## 7. Recognition Clues & Keywords
*   **"Simple Partnership":** All partners invest for the same time; only capital matters.
*   **"Compound Partnership":** Partners invest for different durations; both capital and time matter.
*   **Avoid:** Do not confuse this with simple interest problems; here, the profit is shared based on the *ratio* of contribution, not a fixed percentage rate.

## 8. Common Mistakes
1.  **Ignoring Time:** Students often calculate the ratio based only on capital, forgetting to multiply by the time period.
2.  **Inconsistent Time Units:** Mixing years and months (e.g., using 1 year for one person and 6 months for another without converting both to months).
3.  **Calculation Errors in Simplification:** Failing to simplify the ratio fully, leading to unnecessarily large numbers.
4.  **Misinterpreting "After X months":** If someone joins "after 3 months," their time is $(12 - 3) = 9$ months, not 3.

## 9. Practice Tips
*   **Standardize:** Always convert all time periods to the smallest unit mentioned in the problem (usually months).
*   **Simplify Early:** Cancel out common zeros in the capital amounts before multiplying by time to keep numbers manageable.
*   **Related Patterns:** Study "Ratio and Proportion" and "Weighted Averages," as these are the mathematical foundations for partnership problems.