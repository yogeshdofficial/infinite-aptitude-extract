# Pattern: Dynamic Capital Adjustments During Partnership

## 1. Pattern Overview
This pattern solves problems where partners contribute varying amounts of capital for different durations, requiring the calculation of "equivalent capital" to distribute profits fairly. It is essential because it allows for the equitable division of business gains when investments are not static or simultaneous.

## 2. Key Formulas
The fundamental principle is that profit is proportional to the product of capital and time.

**Equivalent Capital (EC):**
$$\text{EC} = \text{Capital} \times \text{Time Period}$$

**Ratio of Profit Distribution:**
$$\text{Share Ratio} = (\text{C}_1 \times \text{T}_1) : (\text{C}_2 \times \text{T}_2) : \dots : (\text{C}_n \times \text{T}_n)$$

**Individual Share Calculation:**
$$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right) \times \text{Total Profit}$$

## 3. When to Use This Pattern
- **Keywords:** "Joined after X months," "Withdrew capital," "Invested for different periods," "At the end of the year."
- **Recognition Clues:** The problem mentions multiple people entering or leaving a business at different times.
- **Given:** Individual capital amounts and the specific duration each amount was invested.
- **To Find:** The specific monetary share of the total profit for each partner.

## 4. Core Concept & Theory
In a **Compound Partnership**, capital is not just about the amount invested, but the *duration* it remains in the business. A small amount invested for a long time can be more valuable to the business than a large amount invested for a short time. By multiplying Capital by Time, we normalize all investments into a single unit of time (usually months), allowing for a direct comparison of "effective contribution."

## 5. Step-by-Step Solution Method
1. **Standardize Time:** Convert all investment durations into the same unit (e.g., months).
2. **Calculate Equivalent Capital:** Multiply each partner's investment by the number of months it was active.
3. **Simplify the Ratio:** Divide the resulting products by their greatest common divisor (GCD) to get the simplest integer ratio.
4. **Sum the Ratios:** Add all parts of the ratio together to find the "Total Parts."
5. **Calculate Shares:** Multiply the total profit by the fraction representing each partner's share (Partner's Ratio / Total Parts).

## 6. Worked Examples

**Example 1: The Late Joiner Scenario**
*Alfred invested ₹45,000. After 3 months, Peter joined with ₹60,000. After another 6 months, Ronald joined with ₹90,000. Total profit at year-end is ₹16,500.*

**Solution:**
1. **Time periods:** Alfred = 12 months; Peter = 9 months (12-3); Ronald = 3 months (12-9).
2. **Equivalent Capitals:**
   - Alfred: $45,000 \times 12 = 540,000$
   - Peter: $60,000 \times 9 = 540,000$
   - Ronald: $90,000 \times 3 = 270,000$
3. **Ratio:** $540,000 : 540,000 : 270,000 = 2 : 2 : 1$.
4. **Total Parts:** $2 + 2 + 1 = 5$.
5. **Shares:**
   - Alfred: $(2/5) \times 16,500 = ₹6,600$
   - Peter: $(2/5) \times 16,500 = ₹6,600$
   - Ronald: $(1/5) \times 16,500 = ₹3,300$

## 7. Recognition Clues & Keywords
- **Signals:** "Joined," "Left," "Withdrew," "After X months."
- **Distinction:** Do not confuse this with **Simple Partnership**, where all partners invest for the *same* duration. In simple partnerships, you only compare the capital amounts directly.

## 8. Common Mistakes
1. **Ignoring Time:** Students often calculate profit ratios based only on capital, forgetting to multiply by the time invested.
2. **Incorrect Time Calculation:** Calculating the time a partner was *out* of the business instead of the time they were *in*. Always count the months from the date of entry to the end of the accounting period.
3. **Ratio Simplification Errors:** Failing to reduce the ratio to its simplest form, leading to unnecessarily large numbers and calculation errors.
4. **Misinterpreting "After X months":** If someone joins "after 3 months," their time is $(12 - 3) = 9$ months, not 3.

## 9. Practice Tips
- **Visualize the Timeline:** Draw a 12-month line and mark when each partner enters or exits.
- **Master Fractions:** Since profit sharing is essentially fraction multiplication, ensure you are comfortable reducing fractions quickly.
- **Related Patterns:** Study "Partnership with Capital Additions/Withdrawals" (where one person changes their own investment amount mid-year).