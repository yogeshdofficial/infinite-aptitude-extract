# Pattern: Finding SP or CP from Percentage Change

## 1. Pattern Overview
This pattern provides a systematic method to calculate the **Selling Price (SP)** when the **Cost Price (CP)** and percentage profit/loss are known, or to calculate the **Cost Price (CP)** when the **Selling Price (SP)** and percentage profit/loss are known. It is essential because it allows for rapid conversion between cost and revenue without calculating the raw profit/loss amount first.

## 2. Key Formulas
The following formulas are derived from the fundamental principle that profit or loss is always calculated as a percentage of the Cost Price.

**To find SP when CP is known:**
*   **Profit Scenario:** $$SP = CP \times \left( \frac{100 + \text{Gain}\%}{100} \right)$$
*   **Loss Scenario:** $$SP = CP \times \left( \frac{100 - \text{Loss}\%}{100} \right)$$

**To find CP when SP is known:**
*   **Profit Scenario:** $$CP = SP \times \left( \frac{100}{100 + \text{Gain}\%}\right)$$
*   **Loss Scenario:** $$CP = SP \times \left( \frac{100}{100 - \text{Loss}\%}\right)$$

**Percentage Shortcut:**
*   **Gain of $x\%$:** $$SP = (100 + x)\% \text{ of } CP$$
*   **Loss of $x\%$:** $$SP = (100 - x)\% \text{ of } CP$$

## 3. When to Use This Pattern
*   **Keywords:** "Sold at a gain of...", "Sold at a loss of...", "Find the cost price if...", "Find the selling price if...".
*   **Recognition:** The problem provides one monetary value (either CP or SP) and one percentage rate.
*   **Given:** Either CP or SP, and the Profit/Loss percentage.
*   **To Find:** The missing monetary value (SP or CP).

## 4. Core Concept & Theory
The core concept is that **Cost Price is always the base (100%)**. When you gain $x\%$, your selling price becomes $100\% + x\%$ of the cost. When you lose $x\%$, your selling price becomes $100\% - x\%$ of the cost. By treating the CP as the reference point, we can use simple algebraic ratios to isolate the unknown variable.

## 5. Step-by-Step Solution Method
1.  **Identify the Given:** Determine if you have the CP or the SP.
2.  **Identify the Change:** Determine if the transaction resulted in a Gain or a Loss and note the percentage.
3.  **Select the Formula:** 
    *   If finding SP: Multiply CP by the percentage factor.
    *   If finding CP: Multiply SP by the reciprocal of the percentage factor.
4.  **Calculate:** Perform the arithmetic. Ensure the percentage is converted to a decimal or fraction correctly (e.g., $135\% = 1.35$).

## 6. Worked Examples

**Example 1: Finding SP from CP**
*Description: A trader buys an item for ₹500 and sells it at a 20% profit.*
*   **Given:** $CP = 500$, $\text{Gain}\% = 20\%$.
*   **Solution:** 
    $$SP = CP \times \left( \frac{100 + 20}{100} \right)$$
    $$SP = 500 \times \left( \frac{120}{100} \right) = 500 \times 1.2 = 600$$
    The Selling Price is ₹600.

**Example 2: Finding CP from SP**
*Description: An item is sold for ₹800 at a loss of 20%. Find the CP.*
*   **Given:** $SP = 800$, $\text{Loss}\% = 20\%$.
*   **Solution:**
    $$CP = SP \times \left( \frac{100}{100 - 20} \right)$$
    $$CP = 800 \times \left( \frac{100}{80} \right) = 800 \times 1.25 = 1000$$
    The Cost Price is ₹1000.

## 7. Recognition Clues & Keywords
*   **"Reckoned on CP":** Always remember that profit/loss percentages are applied to the Cost Price, never the Selling Price unless explicitly stated.
*   **"Sold at":** Usually precedes the SP.
*   **"Purchased for":** Usually precedes the CP.
*   **Avoid Confusion:** Do not confuse "Profit %" with "Profit amount." If the problem asks for the *amount*, calculate the percentage of CP first.

## 8. Common Mistakes
1.  **Applying % to SP:** Students often calculate profit as a percentage of the Selling Price. **Correction:** Always use CP as the base.
2.  **Inverting the Fraction:** Using the wrong formula for finding CP (e.g., multiplying by $1.2$ instead of dividing by $1.2$). **Correction:** Remember that CP is usually smaller than SP in a profit scenario; if your calculated CP is higher than SP during a profit, you have inverted the fraction.
3.  **Arithmetic Errors:** Forgetting to add/subtract the percentage from 100 before dividing.

## 9. Practice Tips
*   **Mental Check:** If you have a profit, your SP must be greater than your CP. If you have a loss, your SP must be less than your CP. Use this to verify your answers.
*   **Related Patterns:** Study "False Weights" (Pattern XIII-XV) next, as they build upon the concept of adjusting the CP/SP relationship.
*   **Drill:** Practice converting percentages to decimals (e.g., $15\% \text{ gain} = 1.15$ multiplier) to speed up calculations.