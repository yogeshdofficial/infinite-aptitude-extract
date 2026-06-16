# Pattern: Profit Distribution with Varying Investment Durations

## 1. Pattern Overview
This pattern provides a systematic method for calculating the distribution of business profits among partners when their capital investments are held for different lengths of time. It is essential for accurately determining the "effective capital" of each partner to ensure a fair division of gains.

## 2. Key Formulas
The fundamental principle is that profit is distributed in proportion to the product of capital and time.

**Ratio of Profit Distribution:**
$$\text{Profit}_A : \text{Profit}_B : \text{Profit}_C = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$

**Individual Share Calculation:**
$$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right) \times \text{Total Profit}$$

*Where $C$ represents the Capital invested and $T$ represents the Time duration of the investment.*

## 3. When to Use This Pattern
- **Keywords:** "Joined after X months," "Withdrew capital," "At the end of the year," "Business started by..."
- **Recognition Clues:** The problem mentions multiple partners investing different amounts of money for different durations.
- **Given:** Individual capital amounts, the time each capital was invested, and the total profit.
- **To Find:** The specific monetary share of profit for each partner.

## 4. Core Concept & Theory
In a **Compound Partnership**, money earns profit based on both *how much* is invested and *how long* it stays in the business. We calculate the "equivalent capital" by multiplying the investment by the time units. This converts all investments into a common baseline, allowing us to compare them fairly regardless of when the partners entered or exited the business.

## 5. Step-by-Step Solution Method
1. **Identify Time Units:** Determine the total duration of the business (e.g., 12 months) and calculate how many months each partner's capital was active.
2. **Calculate Equivalent Capital:** Multiply each partner's investment by their respective time duration ($C \times T$).
3. **Simplify the Ratio:** Divide the resulting products by their greatest common divisor to get the simplest integer ratio.
4. **Calculate Total Parts:** Add the terms of the ratio together to find the denominator for the fractional share.
5. **Distribute Profit:** Multiply the total profit by each partner's fractional share (Ratio Part / Total Parts).

## 6. Worked Examples

**Example 1: Partners joining at different times**
Alfred invested ₹45,000. After 3 months, Peter joined with ₹60,000. After another 6 months, Ronald joined with ₹90,000. Total profit at the end of the year is ₹16,500.

*   **Step 1 (Time):** Alfred = 12 months; Peter = 9 months (12-3); Ronald = 3 months (12-3-6).
*   **Step 2 (Equivalent Capital):** 
    *   Alfred: $45,000 \times 12 = 540,000$
    *   Peter: $60,000 \times 9 = 540,000$
    *   Ronald: $90,000 \times 3 = 270,000$
*   **Step 3 (Ratio):** $540,000 : 540,000 : 270,000 = 2 : 2 : 1$.
*   **Step 4 (Total Parts):** $2 + 2 + 1 = 5$.
*   **Step 5 (Share):** 
    *   Alfred: $(2/5) \times 16,500 = 6,600$
    *   Peter: $(2/5) \times 16,500 = 6,600$
    *   Ronald: $(1/5) \times 16,500 = 3,300$

## 7. Recognition Clues & Keywords
- **"At the end of the year":** Signals that the time frame is 12 months.
- **"Joined after X months":** Signals that the time duration for that partner is (Total Time - X).
- **"Withdrew":** Signals a change in capital, requiring a split calculation for that partner's investment periods.

## 8. Common Mistakes
1. **Ignoring Time:** Treating it as a simple partnership where only capital matters. This leads to incorrect ratios.
2. **Incorrect Time Calculation:** Forgetting to subtract the "joined after" time from the total duration. Always verify the time active in the business.
3. **Calculation Errors in Simplification:** Failing to simplify the ratio fully, which makes the final multiplication unnecessarily difficult.
4. **Mixing Units:** Ensure all time is in months or all in years. Do not mix them.

## 9. Practice Tips
- **Visualize the Timeline:** Draw a 12-month line and mark when each partner enters or exits.
- **Simplify Early:** Always simplify the ratio of $(C \times T)$ before multiplying by the profit to keep numbers manageable.
- **Related Patterns:** Study "Simple Partnership" (where time is constant) to understand the baseline before moving to "Compound Partnership."