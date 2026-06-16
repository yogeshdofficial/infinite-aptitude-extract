# Pattern Name: Multi-Step Profit/Loss Adjustment

## 1. Pattern Overview
This pattern addresses complex transactions where an item undergoes multiple price changes, intermediate expenses, or sequential percentage adjustments before reaching the final selling price. It is essential for solving real-world business scenarios where the initial cost price is modified by overheads or successive markups/markdowns.

## 2. Key Formulas
The following formulas are foundational for calculating adjustments:

*   **Gain/Loss Amount:**
    $$\text{Gain} = S.P. - C.P.$$
    $$\text{Loss} = C.P. - S.P.$$
*   **Percentage Calculation:**
    $$\text{Gain \%} = \left( \frac{\text{Gain}}{C.P.} \times 100 \right)$$
    $$\text{Loss \%} = \left( \frac{\text{Loss}}{C.P.} \times 100 \right)$$
*   **Finding S.P. from C.P. with Percentage:**
    $$\text{S.P.} = C.P. \times \left( \frac{100 + \text{Gain \%}}{100} \right)$$
    $$\text{S.P.} = C.P. \times \left( \frac{100 - \text{Loss \%}}{100} \right)$$
*   **Finding C.P. from S.P. with Percentage:**
    $$\text{C.P.} = \frac{S.P. \times 100}{100 + \text{Gain \%}}$$
    $$\text{C.P.} = \frac{S.P. \times 100}{100 - \text{Loss \%}}$$

## 3. When to Use This Pattern
*   **Keywords:** "Sold at a profit of...", "After spending on repairs...", "Successive transactions", "If it had been sold for X more".
*   **Recognition:** Use this when the problem provides an initial cost and a series of conditions (e.g., "A bought a car, spent money on repairs, then sold it at a profit").
*   **Given vs. Found:** Typically, you are given the initial cost and percentage rates; you must find the final selling price or the effective cost price after adjustments.

## 4. Core Concept & Theory
The core concept is that **Profit and Loss are always reckoned on the Cost Price (C.P.)**. In multi-step problems, the "Effective C.P." must be calculated first by adding all overheads (repairs, transport, etc.) to the original purchase price. Once the total investment is established, the percentage formulas are applied to this base value.

## 5. Step-by-Step Solution Method
1.  **Identify the Total C.P.:** Sum the purchase price and any additional overheads (repairs, shipping).
2.  **Determine the Target:** Identify if you need to find the final S.P. or the final Profit/Loss percentage.
3.  **Apply the Adjustment:** Use the percentage formulas (VI or VII) to calculate the S.P. based on the total C.P.
4.  **Verify:** Ensure the final S.P. reflects the total investment, not just the initial purchase price.

## 6. Worked Examples

**Example 1: Repair and Resale**
*Given:* A man buys a machine for ₹5,000, spends ₹500 on repairs, and sells it for ₹6,600.
*Solution:*
1. Total C.P. = Purchase Price + Repairs = ₹5,000 + ₹500 = ₹5,500.
2. S.P. = ₹6,600.
3. Gain = S.P. - C.P. = 6,600 - 5,500 = ₹1,100.
4. Gain % = (1,100 / 5,500) * 100 = 20%.

**Example 2: Sequential Adjustment**
*Given:* An item is sold at 10% profit. If it had been sold for ₹50 more, the profit would have been 15%. Find the C.P.
*Solution:*
1. Let C.P. = $x$.
2. Initial S.P. = $1.10x$.
3. New S.P. = $1.15x$.
4. Difference: $1.15x - 1.10x = 50 \Rightarrow 0.05x = 50$.
5. $x = 50 / 0.05 = 1,000$. The C.P. is ₹1,000.

## 7. Recognition Clues & Keywords
*   **"Overhead expenses":** Always add to C.P.
*   **"Had it been sold for...":** Signals a comparison between two potential scenarios.
*   **"Successive":** Signals that the second percentage applies to the result of the first.
*   **Avoid:** Do not calculate profit percentage on the Selling Price unless explicitly stated.

## 8. Common Mistakes
1.  **Ignoring Overheads:** Students often calculate profit based only on the purchase price, forgetting repair or transport costs.
2.  **Reckoning on S.P.:** Mistakenly calculating profit percentage using S.P. as the denominator. Always use C.P.
3.  **Additive Percentages:** Assuming a 10% gain followed by a 10% gain equals a 20% gain. (It is actually 21% due to compounding).
4.  **Formula Confusion:** Using the Gain formula when the problem specifies a Loss. Always check the sign.

## 9. Practice Tips
*   **Draw a Timeline:** For multi-step problems, draw a flow chart showing: Purchase $\rightarrow$ Overheads $\rightarrow$ Total C.P. $\rightarrow$ Profit/Loss $\rightarrow$ Final S.P.
*   **Related Patterns:** Study "False Weight" problems (Pattern XIII-XV) as they are a specialized form of multi-step adjustment.
*   **Mental Check:** If the S.P. is higher than the C.P., your result must be a profit. If lower, a loss. Use this to sanity-check your answers.