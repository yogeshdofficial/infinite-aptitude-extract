# Dishonest Dealer

## Overview
These questions involve a seller who manipulates weights or prices to gain an unfair advantage. The central idea is to calculate the ratio of the **Actual Cost Price** to the **Actual Selling Price** based on the weight discrepancy and the stated profit/loss percentage.

---

## Recognition Clues
* **Keywords:** "Professes to sell at cost price," "false weight," "uses a scale of X instead of Y," "cheats while buying/selling."
* **Given:** Stated profit/loss percentage and the weight/scale discrepancy (e.g., 960g for 1kg).
* **Asked:** Actual gain/loss percentage or the specific weight used to achieve a target profit.

---

## Important Formulas

### [Basic Gain Percentage]
$$
\text{Gain \%} = \left[ \frac{\text{Error}}{\text{True Value} - \text{Error}} \times 100 \right] \%
$$
*Meaning:* Error is the difference between the true weight and the false weight used.
*Use when:* The dealer claims to sell at cost price but uses a false weight.

### [Combined Profit/Loss with Weight Discrepancy]
$$
\text{Gain/Loss \%} = \left[ \frac{y - x}{100 - y} \times 100 \right] \%
$$
*Meaning:* $x$ is the stated profit/loss % (use negative for loss), $y$ is the % of weight reduction.
*Use when:* The dealer sells at a stated profit/loss and uses a false weight.

---

## Solution Framework
1. **Normalize:** Assume the Cost Price (C.P.) of 1 unit (1 kg or 1 m) is ₹1.
2. **Identify True C.P.:** Determine the actual amount of goods the dealer paid for (e.g., if he uses 900g, his C.P. is for 900g).
3. **Identify Actual S.P.:** Calculate the money received based on the stated profit/loss percentage.
4. **Compare:** Calculate the percentage difference between the Actual S.P. and the Actual C.P.

---

## Shortcut Tricks
* **The Ratio Method:** Treat the transaction as a ratio of $\frac{\text{Weight Sold}}{\text{Weight Bought}} \times \frac{\text{Selling Price Factor}}{\text{Cost Price Factor}}$.
* **Why it works:** It bypasses complex algebra by directly comparing the quantity of goods exchanged against the money exchanged.

---

## Common Mistakes
* **Denominator Error:** Using the "True Value" (1000g) as the denominator instead of the "False Value" (e.g., 960g).
    * *Fix:* Always divide by the weight the dealer *actually* gives away.
* **Confusing Buying/Selling Cheats:** Applying the same logic for cheating while buying vs. selling.
    * *Fix:* When buying, you get more than you pay for; when selling, you give less than you charge for.
* **Sign Errors:** Treating a "loss" as a positive value in the combined formula.
    * *Fix:* Always substitute loss as a negative value (e.g., -4% for 4% loss).

---

## Similar Patterns
* **Successive Percentage Change:** Often confused with "cheating while buying AND selling."
* **Distinction:** Use the $(100+x)^2/100 - 100$ formula only for successive percentage changes; use the weight-ratio method for physical weight manipulation.

---

## Revision Summary
**Key formula:** $\text{Gain \%} = \frac{\text{Error}}{\text{False Weight}} \times 100$.
**Spot it by:** Phrases like "false weight," "uses X instead of Y," or "professes to sell at cost."
**Fastest method:** Use the ratio of (Actual S.P. / Actual C.P.) to find the net gain.
**Biggest trap:** Using 1000g as the denominator instead of the actual weight used.