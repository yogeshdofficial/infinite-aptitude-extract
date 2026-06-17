# Pattern: Finding Missing Variables (Time or Capital)

## 1. Pattern Overview
This pattern allows you to determine an unknown investment amount or an unknown duration of investment by leveraging the proportional relationship between capital, time, and profit distribution. It is essential for solving complex partnership problems where business contributions are not uniform.

## 2. Key Formulas
The fundamental principle of partnership is that profit is distributed in proportion to the product of capital and time.

**General Profit Ratio Formula:**
$$\text{Profit}_A : \text{Profit}_B : \text{Profit}_C = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$

Where:
*   $C$ = Capital invested
*   $T$ = Time period of investment

**Finding a Missing Variable:**
If the profit ratio ($P_1 : P_2$) and one variable (e.g., $C_1, C_2, T_1$) are known, use:
$$\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}$$

## 3. When to Use This Pattern
*   **Keywords:** "Joined after X months," "Withdrew capital," "Left the business," "Ratio of profits," "Find the investment."
*   **Recognition Clues:** The problem involves multiple partners entering or leaving at different times, or changing their capital amounts mid-term.
*   **Given:** Usually the total profit, the duration of the business, and partial information about capital or time.
*   **To Find:** The missing capital amount or the specific month a partner joined/left.

## 4. Core Concept & Theory
In a **Compound Partnership**, profit is not just about how much money you put in, but how *long* that money works for you. We calculate "Equivalent Capital" by multiplying the investment by the time it remained in the business. This creates a common unit of measurement, allowing us to compare partners who invested different amounts for different durations on an equal footing.

## 5. Step-by-Step Solution Method
1.  **Standardize Time:** Convert all time periods into the same unit (usually months). If the business runs for a year, use 12 months as the base.
2.  **Calculate Equivalent Capital:** For each partner, multiply their capital by the number of months it was invested ($C \times T$).
3.  **Formulate the Ratio:** Simplify the resulting products into the smallest possible integer ratio.
4.  **Apply the Profit Share:** Divide the total profit by the sum of the ratio parts to find the value of "one part."
5.  **Solve for the Variable:** If a variable is missing, set up an algebraic equation using the ratio formula and solve for the unknown ($x$).

## 6. Worked Examples

**Example 1: Finding Missing Capital**
*A and B start a business. A invests ₹5000 for 12 months. B invests ₹X for 8 months. If they share profits equally, find X.*
**Given:** $C_A=5000, T_A=12, C_B=X, T_B=8, P_A=P_B$ (Ratio 1:1).
**Solution:**
1. Ratio of profits = $(5000 \times 12) : (X \times 8)$
2. Since profits are equal: $60000 / 8X = 1/1$
3. $8X = 60000 \implies X = 7500$.
**Result:** B invested ₹7500.

**Example 2: Finding Missing Time**
*A and B invest in a ratio of 3:2. A stays for 12 months. If they share profits in a ratio of 9:4, how long did B invest?*
**Given:** $C_A:C_B = 3:2, T_A=12, P_A:P_B = 9:4$.
**Solution:**
1. $\frac{P_A}{P_B} = \frac{C_A \times T_A}{C_B \times T_B} \implies \frac{9}{4} = \frac{3 \times 12}{2 \times T_B}$
2. $\frac{9}{4} = \frac{36}{2 \times T_B} \implies 18 \times T_B = 144$
3. $T_B = 8$.
**Result:** B invested for 8 months.

## 7. Recognition Clues & Keywords
*   **"Joined after X months":** Subtract X from the total business duration to find the active time.
*   **"Left after X months":** The active time is exactly X.
*   **"At the end of the year":** Total time is 12 months.
*   **Do not confuse with:** Simple interest problems; partnership is strictly about *proportional distribution*, not interest accumulation.

## 8. Common Mistakes
1.  **Ignoring Time:** Treating all investments as if they were for the full year (only valid for Simple Partnerships).
2.  **Incorrect Time Calculation:** Forgetting to subtract "joined after" time from the total duration.
3.  **Ratio Inversion:** Placing the profit ratio upside down in the equation. Always keep the order consistent (e.g., A:B = A:B).
4.  **Calculation Errors:** Failing to simplify the large numbers (e.g., 120000:135000) before multiplying by time.

## 9. Practice Tips
*   **Simplify Early:** Always reduce the capital ratios (e.g., remove common zeros) before multiplying by time to keep numbers manageable.
*   **Draw a Timeline:** For complex problems, draw a line from 0 to 12 months and mark when each partner enters or exits.
*   **Related Patterns:** Study "Mixture and Alligation" and "Ratio and Proportion," as these are the mathematical foundations for solving partnership equations.