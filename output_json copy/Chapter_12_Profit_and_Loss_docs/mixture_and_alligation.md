# Pattern: Mixture and Alligation

## 1. Pattern Overview
- **Definition:** Mixture and Alligation is a mathematical technique used to find the ratio in which two or more ingredients at different prices must be mixed to produce a mixture of a desired mean price.
- **Why it matters:** It simplifies complex problems involving weighted averages, allowing you to solve for ratios or unknown prices without setting up cumbersome algebraic equations.

## 2. Key Formulas
The **Alligation Rule** states that if two ingredients are mixed, the ratio of their quantities is inversely proportional to the difference between their prices and the mean price.

Let $C_1$ be the cost price of the cheaper ingredient and $C_2$ be the cost price of the dearer (expensive) ingredient. Let $M$ be the mean price of the mixture.

**The Alligation Rule:**
$$\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{C_2 - M}{M - C_1}$$

**Visual Representation:**
*   Cheaper Price ($C_1$) $\quad \quad \quad$ Dearer Price ($C_2$)
*   $\quad \quad \quad \quad \quad \searrow \quad \swarrow$
*   $\quad \quad \quad \quad \quad \quad \text{Mean Price } (M)$
*   $\quad \quad \swarrow \quad \searrow$
*   $(C_2 - M) \quad \quad \quad \quad (M - C_1)$

## 3. When to Use This Pattern
- **Keywords:** "In what ratio," "mixed," "blended," "mean price," "average price."
- **Recognition Clues:** You are given the individual rates of two items and the final rate of the resulting mixture.
- **Given:** $C_1$, $C_2$, and $M$.
- **To Find:** The ratio of the quantities of the two ingredients.

## 4. Core Concept & Theory
The method works because it calculates the "deviation" of each ingredient's price from the target mean price. By balancing these deviations, we ensure that the total cost of the mixture remains consistent with the desired mean price. It is essentially a shortcut for the weighted average formula:
$$M = \frac{Q_1C_1 + Q_2C_2}{Q_1 + Q_2}$$

## 5. Step-by-Step Solution Method
1.  **Identify the Prices:** Clearly label the cheaper price ($C_1$) and the dearer price ($C_2$).
2.  **Identify the Mean:** Identify the target mean price ($M$). Ensure all units are identical (e.g., all per kg).
3.  **Calculate Differences:** Subtract the mean from the dearer price ($C_2 - M$) and the cheaper price from the mean ($M - C_1$).
4.  **Form the Ratio:** Place the results in the ratio $\frac{C_2 - M}{M - C_1}$.
5.  **Simplify:** Reduce the ratio to its simplest form.

## 6. Worked Examples

**Example 1: Mixing two types of sugar**
*Given:* Sugar at \$15/kg is mixed with sugar at \$20/kg to produce a mixture worth \$16.50/kg. Find the ratio.
*Solution:*
1. $C_1 = 15$, $C_2 = 20$, $M = 16.50$.
2. Difference 1 (Dearer - Mean): $20 - 16.50 = 3.50$.
3. Difference 2 (Mean - Cheaper): $16.50 - 15 = 1.50$.
4. Ratio = $3.50 : 1.50 = 35 : 15 = 7 : 3$.
*Result:* The sugar must be mixed in a ratio of 7:3.

**Example 2: Finding the Mean Price**
*Given:* 20kg of rice at \$10/kg is mixed with 30kg of rice at \$15/kg. Find the mean price.
*Solution:*
1. Total Cost = $(20 \times 10) + (30 \times 15) = 200 + 450 = 650$.
2. Total Quantity = $20 + 30 = 50$ kg.
3. Mean Price ($M$) = $\frac{650}{50} = \$13/kg$.

## 7. Recognition Clues & Keywords
- **Look for:** "In what proportion," "How much of X must be added to Y."
- **Distinction:** Do not confuse this with simple Profit and Loss percentage problems. Alligation is specifically for **mixing quantities**, whereas Profit/Loss is for **single-item transactions**.

## 8. Common Mistakes
1.  **Unit Mismatch:** Using different units (e.g., one price per kg, one per gram). Always convert to the same unit first.
2.  **Inverting the Ratio:** Placing the cheaper difference on the wrong side. Remember: The difference from the *dearer* price gives the quantity of the *cheaper* item.
3.  **Ignoring the Mean:** Using the selling price instead of the cost price when calculating the mean. Alligation must be performed on Cost Prices.

## 9. Practice Tips
- **Mastery:** Practice problems where the mean price is not given, but a profit percentage is provided (you must calculate the Cost Price of the mixture first using Profit/Loss formulas).
- **Related Patterns:** Study "Weighted Averages" and "Ratio and Proportion" to build a stronger foundation for Alligation.