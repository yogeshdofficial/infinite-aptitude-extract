# Stock Reinvestment

## Overview
This pattern involves selling an existing stock holding and using the total proceeds to purchase a different stock. The goal is to calculate the resulting change in annual income by comparing the dividend yield of the old investment against the new one.

---

## Recognition Clues
* **Keywords:** "sells out," "reinvests," "proceeds," "change in income," "service charge."
* **Given:** Initial investment amount, dividend rates, market prices of both stocks, and sometimes service charges.
* **Asked:** The difference between the new annual income and the original annual income.

---

## Key Formulas

### [Number of Shares]
$$
\text{Number of Shares} = \frac{\text{Total Investment}}{\text{Market Price per Share}}
$$
**Variables:** Total Investment (cash available), Market Price (cost to buy one share).
**When to use:** To find how many units of stock you hold after a purchase or before a sale.
**Example:** Investing ₹ 5508 at a market price of 102: $\frac{5508}{102} = 54$ shares.

### [Annual Income]
$$
\text{Annual Income} = \text{Number of Shares} \times (\text{Dividend Rate} \times \text{Face Value})
$$
**Variables:** Dividend Rate (percentage), Face Value (usually ₹ 100 unless specified).
**When to use:** To calculate the yearly return from a specific stock holding.
**Example:** 54 shares of 4% stock (Face Value ₹ 100): $54 \times (0.04 \times 100) = ₹ 216$.

---

## Solution Framework
1. **Calculate Initial Shares:** Divide the initial investment by the first stock's market price.
2. **Calculate Original Income:** Multiply the number of shares by the dividend per share (Rate% of Face Value).
3. **Calculate Sale Proceeds:** Multiply the number of shares by the selling market price (subtracting any service charge if applicable).
4. **Calculate New Shares:** Divide the total proceeds by the new stock's market price (adding any service charge if applicable).
5. **Calculate New Income:** Multiply the new number of shares by the new dividend per share.
6. **Find Change:** Subtract the original income from the new income.

---

## Shortcut Tricks
* **Trick:** Work with the "Income per ₹ 100 invested" if the total investment amount is not provided.
* **Why it works:** Income is proportional to investment; calculating the yield per ₹ 100 allows you to compare efficiency directly.
* **When to use:** When the question asks "which is a better investment" or asks for a percentage change rather than an absolute value.

---

## Common Mistakes
* **Mistake:** Calculating dividend on Market Price. **Fix:** Always calculate dividend on Face Value (usually ₹ 100).
* **Mistake:** Forgetting to adjust for service charges. **Fix:** Subtract charge from sale price; add charge to purchase price.
* **Mistake:** Assuming Face Value is the same as Market Price. **Fix:** Treat them as distinct; Face Value is fixed, Market Price fluctuates.

---

## Worked Example (Step-by-Step)

**Question:** A person invests ₹ 5508 in 4% stock at 102. He afterwards sells out at 105 and reinvests in 5% stock at 126. What is the change in his income?

**Solution:**
1. **Initial Shares:** $\frac{5508}{102} = 54$ shares.
2. **Original Income:** $54 \times (4\% \text{ of } 100) = 54 \times 4 = ₹ 216$.
3. **Sale Proceeds:** $54 \times 105 = ₹ 5670$.
4. **New Shares:** $\frac{5670}{126} = 45$ shares.
5. **New Income:** $45 \times (5\% \text{ of } 100) = 45 \times 5 = ₹ 225$.
6. **Change:** $225 - 216 = ₹ 9$.

**Answer:** The change in income is ₹ 9.

---

## Similar Patterns
* **Better Investment Problems:** These ask which stock is better rather than the change in income; use the same logic but compare the income per unit of investment.

---

## Revision Summary
* **Key formula:** $\text{Income} = \text{Shares} \times (\text{Rate} \times \text{Face Value})$.
* **Spot it by:** "Sells out" and "reinvests" keywords.
* **First move:** Find the number of shares held initially.
* **Fastest method:** Calculate total proceeds first, then new shares.
* **Biggest trap:** Calculating dividends on the market price instead of face value.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage:** Understanding that $x\%$ of $y$ is $\frac{x}{100} \times y$.
* **Proportionality:** Income increases linearly with the number of shares held.

### Formulas You Must Know First
* **Dividend Amount:** $\text{Dividend} = \text{Face Value} \times \text{Rate}$.
* **Net Price:** $\text{Market Price} \pm \text{Brokerage}$.

### Terms Used In This Pattern
* **Face Value:** The printed value on the share certificate (standard is ₹ 100).
* **Market Value:** The actual price at which the share is traded.
* **Brokerage/Service Charge:** A fee added to the cost or subtracted from the sale price.