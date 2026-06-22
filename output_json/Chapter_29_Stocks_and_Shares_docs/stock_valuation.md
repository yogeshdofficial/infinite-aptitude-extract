# Stock Valuation

## Overview
This pattern involves calculating the total cash required to buy or the cash realized from selling a specific amount of stock. The central idea is to determine the **net price per ₹100 face value** by adjusting the market price for premiums, discounts, and brokerage, then applying that rate to the total face value.

---

## Recognition Clues
* **Keywords:** "Find the cost of", "cash required to purchase", "cash realised by selling", "at [number] premium/discount", "brokerage".
* **Given:** Face value of total stock, market price (or premium/discount), and brokerage percentage.
* **Asked:** Total cost (to buy) or total proceeds (to sell).

---

## Key Formulas

### [Total Cost/Proceeds]
$$
\text{Total} = \text{Face Value} \times \frac{\text{Market Price} \pm \text{Brokerage}}{100}
$$

**Variables:**
- **Face Value:** The total nominal value of the stock.
- **Market Price:** The price per ₹100 face value (100 + premium or 100 - discount).
- **Brokerage:** Added when buying; subtracted when selling.

**When to use:** To find the final cash amount for a given face value.

**Worked example:** For ₹3200 stock at 107 with 0.5% brokerage:
$\text{Total} = 3200 \times \frac{107 + 0.5}{100} = 32 \times 107.5 = 3440$.

---

## Solution Framework

**Step 1: Determine Market Price per ₹100.** Start with 100, add premium or subtract discount to get the base market price.
**Step 2: Adjust for Brokerage.** Add brokerage to the market price if buying; subtract it if selling.
**Step 3: Calculate Total.** Multiply the adjusted price by the ratio of (Total Face Value / 100).

---

## Shortcut Tricks
* **Trick:** Calculate the "Net Rate" per ₹100 first.
* **Why it works:** It simplifies the arithmetic by handling the percentage adjustments before multiplying by the large face value.
* **When to use:** Always, to avoid errors in order of operations.
* **Example:** For Q2, instead of calculating brokerage on 3200, calculate $107 + 0.5 = 107.5$. Then $107.5 \times 32 = 3440$.

---

## Common Mistakes
* **Mistake:** Applying brokerage to the market price instead of the face value.
    * **Fix:** Brokerage is always a percentage of the **Face Value**.
* **Mistake:** Subtracting brokerage when buying.
    * **Fix:** Buying costs more (add brokerage); selling yields less (subtract brokerage).
* **Mistake:** Confusing Face Value with Market Value.
    * **Fix:** Face Value is the "printed" amount; Market Value is the "trading" price.

---

## Worked Example (Step-by-Step)

**Question:** Find the cash required to purchase ₹3200, $7\frac{1}{2}\%$ stock at 107 (brokerage $\frac{1}{2}\%$).

**Solution:**
1. **Market Price:** The stock is at 107 per ₹100.
2. **Adjust for Brokerage:** Buying means adding brokerage. $107 + 0.5 = 107.5$ per ₹100.
3. **Calculate Total:** $\frac{107.5}{100} \times 3200 = 107.5 \times 32 = 3440$.

**Answer:** ₹3,440.

---

## Similar Patterns
* **Dividend/Income Problems:** These ask for the *return* on investment rather than the *cost* of the stock. Distinguish by checking if the question asks for "cash required" (this pattern) or "annual income" (dividend pattern).

---

## Revision Summary
* **Key formula:** $\text{Total} = \text{Face Value} \times \frac{\text{Market Price} \pm \text{Brokerage}}{100}$
* **Spot it by:** "Cash required" or "Cash realised" with brokerage/premium/discount.
* **First move:** Find the net price per ₹100 face value.
* **Fastest method:** Calculate net rate per ₹100, then multiply by (Face Value / 100).
* **Biggest trap:** Adding brokerage when selling or subtracting when buying.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage:** Understanding that $x\%$ of $y$ is $\frac{x}{100} \times y$.
* **Face Value vs. Market Value:** Face value is the nominal amount; market value is the actual trading price.

### Formulas You Must Know First
* **Percentage of a number:** $\text{Value} = \frac{\text{Rate}}{100} \times \text{Base}$.

### Terms Used In This Pattern
* **Premium:** Market price > Face value.
* **Discount:** Market price < Face value.
* **Brokerage:** Fee paid to the broker for the transaction.