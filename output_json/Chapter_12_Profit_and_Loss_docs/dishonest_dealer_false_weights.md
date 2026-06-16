# Pattern: Dishonest Dealer (False Weights)

## 1. Pattern Overview
The Dishonest Dealer pattern provides a systematic way to calculate the actual profit or loss percentage when a trader manipulates the weight of goods or misrepresents the selling price. This pattern is essential for solving complex commercial arithmetic problems where the "true" cost and "true" weight differ from what is presented to the customer.

## 2. Key Formulas

**Case 1: Selling at Cost Price using False Weights**
$$\text{Gain \%} = \left( \frac{\text{Error}}{\text{True Value} - \text{Error}} \right) \times 100$$

**Case 2: Selling at a Profit ($x\%$) using False Weights ($y\%$ less than actual)**
$$\text{Gain \%} = \left( \frac{100 + x}{100 - y} \times 100 \right) - 100$$

**Case 3: Selling at a Loss ($x\%$) using False Weights ($y\%$ less than actual)**
$$\text{Gain or Loss \%} = \left( \frac{100 - x}{100 - y} \times 100 \right) - 100$$
*(Note: If the result is positive, it is a Gain; if negative, it is a Loss.)*

## 3. When to Use This Pattern
*   **Keywords:** "Professes to sell at cost price," "uses false weights," "gives less weight," "dishonest dealer."
*   **Recognition:** The problem involves a discrepancy between the weight the customer pays for and the weight the customer actually receives.
*   **Given:** The intended profit/loss percentage and the percentage of weight reduction.
*   **To Find:** The effective (actual) profit or loss percentage.

## 4. Core Concept & Theory
The fundamental principle is that **Profit is earned on the Cost Price**. When a dealer uses a false weight, they are effectively reducing their cost (because they give away less product) while maintaining the revenue. By comparing the actual cost incurred to the revenue generated, we can determine the true percentage of gain or loss, which is often higher than the dealer's stated profit margin.

## 5. Step-by-Step Solution Method
1.  **Identify the Scenario:** Determine if the dealer is claiming to sell at Cost Price, at a Profit, or at a Loss.
2.  **Extract Variables:** Identify $x$ (stated profit/loss %) and $y$ (the percentage of weight reduction).
3.  **Select Formula:** Choose the appropriate formula from Section 2 based on the scenario identified in Step 1.
4.  **Substitute and Solve:** Plug the values into the formula.
5.  **Interpret Result:** For Case 3, ensure the sign (+ or -) is correctly identified to label the result as Gain or Loss.

## 6. Worked Examples

**Example 1: Selling at Cost Price**
*A merchant professes to sell his goods at cost price but uses a weight of 900g instead of 1kg. Find his gain percent.*
*   **Given:** True value = 1000g, Error = 100g (1000g - 900g).
*   **Solution:** 
    $$\text{Gain \%} = \left( \frac{100}{1000 - 100} \right) \times 100 = \left( \frac{100}{900} \right) \times 100 = 11.11\%$$

**Example 2: Selling at a Profit**
*A trader professes to sell his goods at a profit of 10% but uses a weight which is 20% less than the actual weight. Find his actual gain percent.*
*   **Given:** $x = 10$, $y = 20$.
*   **Solution:**
    $$\text{Gain \%} = \left( \frac{100 + 10}{100 - 20} \times 100 \right) - 100 = \left( \frac{110}{80} \times 100 \right) - 100 = 137.5 - 100 = 37.5\%$$

## 7. Recognition Clues & Keywords
*   **"Professes to sell":** This is the biggest clue that the stated price is a facade.
*   **"False weight":** Signals that the denominator in your calculation must be adjusted.
*   **Distinction:** Do not confuse "weight is $y\%$ less" with "weight is $y\%$ of the original." If the weight is 20% less, you use 80 (100-20) in your denominator.

## 8. Common Mistakes
1.  **Using the wrong denominator:** Students often use 100 instead of $(100-y)$. Always remember the dealer's cost is based on the *actual* weight given, not the *claimed* weight.
2.  **Ignoring the sign in Case 3:** Forgetting that a negative result indicates a loss. Always check if the final value is less than 100.
3.  **Misinterpreting "x% less":** If a problem says "uses 800g for 1kg," $y$ is 20%, not 80. Ensure $y$ represents the *reduction* percentage.

## 9. Practice Tips
*   **Visualize the Transaction:** Imagine you are the customer. You pay for 1kg, but you only get 900g. The dealer "saved" the cost of 100g.
*   **Mastery:** Practice problems where the dealer claims a loss but still makes a profit due to heavy weight manipulation.
*   **Related Patterns:** Study "Successive Percentage Changes" as it helps in understanding how multiple manipulations (price + weight) compound.