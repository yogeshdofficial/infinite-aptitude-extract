# Pattern: Rent Sharing with Changing Occupancy

## 1. Pattern Overview
This pattern provides a systematic method to distribute shared costs (like rent or business profits) among multiple parties when their duration of participation or contribution levels vary over time. It is essential for ensuring fair financial distribution based on the "weighted contribution" of each participant.

## 2. Key Formulas
The fundamental principle is that the share of profit or cost is proportional to the product of capital and time.

**Equivalent Capital (Weighted Contribution):**
$$\text{Equivalent Capital} = \text{Investment} \times \text{Time Period}$$

**Ratio of Distribution:**
$$\text{Share Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$

**Individual Share Calculation:**
$$\text{Individual Share} = \left( \frac{\text{Individual Ratio}}{\text{Sum of all Ratios}} \right) \times \text{Total Amount}$$

## 3. When to Use This Pattern
- **Keywords:** "Joined after X months," "Left after Y months," "Annual profit," "Shared rent," "Proportional to time and investment."
- **Recognition Clues:** The problem involves multiple people contributing different amounts of money for different durations.
- **Given:** Individual investment amounts and the specific time duration each person was involved.
- **To Find:** The specific monetary share of profit or cost for each individual.

## 4. Core Concept & Theory
The core concept is **Compound Partnership**. Unlike simple partnerships where everyone stays for the same duration, compound partnerships recognize that money invested for a longer period contributes more to the business than the same amount invested for a shorter period. By multiplying the capital by the time, we normalize all contributions to a single unit of time, allowing for a fair ratio-based division.

## 5. Step-by-Step Solution Method
1. **Identify Time Periods:** Determine exactly how many months/units each person was involved. (e.g., if the total is 12 months and someone joins after 3, their time is $12 - 3 = 9$ months).
2. **Calculate Equivalent Capital:** Multiply each person's investment by their respective time duration.
3. **Simplify the Ratio:** Divide the resulting products by their greatest common divisor to get the simplest integer ratio.
4. **Calculate Total Ratio Units:** Sum the parts of the ratio.
5. **Distribute the Total:** Use the Individual Share formula to multiply the total amount by the fraction of the total ratio.

## 6. Worked Examples

**Example 1: Business Profit with Delayed Entry**
*Given:* Alfred invests ₹45,000. Peter joins after 3 months with ₹60,000. Ronald joins 6 months after Peter with ₹90,000. Total profit after 1 year is ₹16,500.

*Solution:*
1. **Time:** Alfred = 12 months; Peter = 9 months; Ronald = 3 months.
2. **Equivalent Capital:** 
   - Alfred: $45,000 \times 12 = 540,000$
   - Peter: $60,000 \times 9 = 540,000$
   - Ronald: $90,000 \times 3 = 270,000$
3. **Ratio:** $540,000 : 540,000 : 270,000 = 2 : 2 : 1$.
4. **Total Units:** $2 + 2 + 1 = 5$.
5. **Shares:** 
   - Alfred: $(2/5) \times 16,500 = 6,600$
   - Peter: $(2/5) \times 16,500 = 6,600$
   - Ronald: $(1/5) \times 16,500 = 3,300$

**Example 2: Simple Partnership (Equal Time)**
*Given:* A, B, and C invest ₹120k, ₹135k, and ₹150k for the same duration. Profit is ₹56,700.

*Solution:*
1. **Ratio:** $120,000 : 135,000 : 150,000 = 8 : 9 : 10$.
2. **Total Units:** $8 + 9 + 10 = 27$.
3. **Shares:**
   - A: $(8/27) \times 56,700 = 16,800$
   - B: $(9/27) \times 56,700 = 18,900$
   - C: $(10/27) \times 56,700 = 21,000$

## 7. Recognition Clues & Keywords
- **"After X months":** Signals a change in the time variable.
- **"At the end of the year":** Defines the total time frame (usually 12 months).
- **"Jointly":** Signals a partnership problem.
- **Do not confuse with:** Simple interest problems where time is used for interest calculation rather than profit-sharing ratios.

## 8. Common Mistakes
1. **Ignoring Time:** Treating all investments as equal regardless of duration. Always multiply by time.
2. **Miscalculating Time:** Using the "joined after" number instead of the "time active" number (e.g., using 3 months instead of 9 months).
3. **Ratio Errors:** Failing to simplify the ratio before calculating shares, leading to unnecessarily large numbers.
4. **Total Units Error:** Forgetting to add all parts of the ratio together when calculating the denominator.

## 9. Practice Tips
- **Visualize the Timeline:** Draw a 12-month line and mark when each person enters or exits.
- **Simplify Early:** Always reduce your investment-time products to the smallest possible ratio before doing the final division.
- **Related Patterns:** Study "Mixture and Alligation" and "Work and Time" as they share similar proportional logic.