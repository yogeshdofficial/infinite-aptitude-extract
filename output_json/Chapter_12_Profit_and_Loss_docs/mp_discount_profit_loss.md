# MP, Discount, Profit/Loss

## Overview
These questions involve a chain of price adjustments starting from a Marked Price (MP) to a final Selling Price (SP), often involving multiple discounts or a target profit percentage. The central idea is to link MP, SP, and CP using the chain: $MP \xrightarrow{\text{Discount}} SP \xrightarrow{\text{Profit/Loss}} CP$.

---

## Recognition Clues
* **Keywords:** "Marked price," "List price," "Successive discounts," "Commission," "Labelled price," "Offered at."
* **Given:** MP, CP, or SP; discount percentages; profit/loss percentages.
* **Asked:** Find the missing price (MP or SP), the first/second discount percentage, or the final profit percentage.
* **Visual cue:** Look for a sequence of percentage changes applied to a base value.

---

## Important Formulas

### [Successive Price Chain]
$$
SP = MP \times \left(1 - \frac{d_1}{100}\right) \times \left(1 - \frac{d_2}{100}\right)
$$
*Meaning:* $d_1, d_2$ are successive discount percentages.
*Use when:* You need to find the final price after multiple discounts or find a missing discount.

### [Profit/Loss Link]
$$
SP = CP \times \left(1 + \frac{P\%}{100}\right) \quad \text{or} \quad SP = CP \times \left(1 - \frac{L\%}{100}\right)
$$
*Meaning:* $P\%$ is profit percent, $L\%$ is loss percent.
*Use when:* You need to relate the final selling price back to the original cost price.

---

## Solution Framework
1. **Assume a base:** If no values are given, assume $CP = 100$ or $MP = 100$.
2. **Apply discounts:** Calculate the SP by applying discount percentages to the MP.
3. **Apply profit/loss:** Use the SP to find the CP (or vice versa) using the profit/loss percentage.
4. **Solve for variable:** Set up the equation based on the unknown value and solve.
5. **Verify:** Ensure the final SP matches the conditions provided in the question.

---

## Shortcut Tricks
* **Free Item Discount:** If you get $n$ items free on a purchase of $m$ items, the discount is $\frac{n}{m+n} \times 100\%$.
    * *Why:* You are receiving $n$ items for free out of a total of $m+n$ items.
* **Successive Discount:** Two discounts of $a\%$ and $b\%$ are equivalent to a single discount of $(a + b - \frac{ab}{100})\%$.
    * *Why:* This accounts for the second discount being applied to the already reduced price.

---

## Common Mistakes
* **Applying discounts to CP:** Students often subtract discounts from the Cost Price.
    * *Reason:* Discounts are always calculated on the Marked Price.
    * *Fix:* Always map the flow: $MP \to \text{Discount} \to SP \to \text{Profit/Loss} \to CP$.
* **Adding percentages directly:** Adding $20\%$ and $10\%$ to get $30\%$ discount.
    * *Reason:* Successive discounts are multiplicative, not additive.
    * *Fix:* Use the formula $(1 - d_1)(1 - d_2)$ or the successive discount trick.
* **Confusing "Profit on SP" vs "Profit on CP":** Assuming profit is always on SP.
    * *Reason:* Standard profit/loss is always on CP unless specified otherwise.
    * *Fix:* Read carefully; if the question says "profit on sales," it refers to SP.

---

## Similar Patterns
* **False Weight Problems:** These are distinct because they involve a ratio of "True Weight" vs "False Weight" rather than price discounts.
* **Successive Percentage Change:** Similar to population growth or compound interest; treat discounts as negative percentage changes.

---

## Revision Summary
**Key formula:** $SP = MP \times (1 - \frac{d}{100})$ and $SP = CP \times (1 + \frac{P}{100})$.

**Spot it by:** Keywords like "Marked Price," "Discount," or "Commission."

**Fastest method:** Use the multiplier method (e.g., $0.80 \times 0.90$ for $20\%$ and $10\%$ discounts).

**Biggest trap:** Applying discounts to the Cost Price instead of the Marked Price.