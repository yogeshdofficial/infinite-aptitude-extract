# Missing Total Profit

## Overview
This pattern involves a business where partners join or withdraw at different times, and one partner's specific profit share is provided. The goal is to calculate the total profit of the entire business by using the ratio of equivalent capitals.

---

## Recognition Clues
* **Keywords:** "joins after X months," "withdraws after Y months," "share in the profit was ₹..."
* **Given:** Individual investment ratios (often relative to one another) and specific time durations for each partner.
* **Asked:** The total profit of the business at the end of the year.

---

## Important Formulas

### [Equivalent Capital Ratio]
$$
\text{Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)
$$
*Meaning:* $C$ is the capital invested and $T$ is the time period in months.
*Use when:* Partners invest different amounts for different durations to find the profit-sharing ratio.

### [Total Profit Calculation]
$$
\text{Total Profit} = \text{Individual Share} \times \frac{\text{Sum of Ratio Terms}}{\text{Individual's Ratio Term}}
$$
*Meaning:* Uses the unitary method to scale a known share to the total sum.
*Use when:* You have one partner's profit and need the total business profit.

---

## Solution Framework
1. Assign a variable (e.g., $x$) to the base investment amount.
2. Express all other investments in terms of $x$.
3. Calculate the "Equivalent Capital" for each partner by multiplying their investment by their active months.
4. Simplify the ratio of these equivalent capitals to the smallest integer form.
5. Sum the ratio terms.
6. Set the known partner's fraction of the total equal to their given profit and solve for the total.

---

## Shortcut Tricks
* **Ratio Scaling:** If investments are multiples of each other, ignore the variable $x$ immediately to simplify the ratio calculation.
* **Time Normalization:** Always convert all time periods to months (e.g., 1 year = 12 months) before multiplying to avoid unit errors.

---

## Common Mistakes
* **Time Mismatch:** Using the time a partner was *absent* instead of the time they were *present*.
    * *Fix:* Always verify the "active" months for each partner before multiplying.
* **Ratio Inversion:** Dividing the total profit by the partner's share instead of multiplying by the ratio inverse.
    * *Fix:* Remember: $\text{Total} = \text{Part} \times (\frac{\text{Total Ratio Sum}}{\text{Part Ratio}})$.
* **Ignoring Withdrawals:** Assuming a partner stays for the full year when the problem states they withdrew.
    * *Fix:* Read the "withdraws" clause carefully; it defines the end of that partner's $T$ value.

---

## Similar Patterns
This is a specific case of "Compound Partnership." It is distinct from "Simple Partnership" because time is a variable, not a constant.

---

## Revision Summary
**Key formula:** $\text{Total Profit} = \text{Share} \times \frac{\sum \text{Ratio}}{\text{Partner Ratio}}$.
**Spot it by:** Different investment durations and one known profit share.
**Fastest method:** Simplify the $(C \times T)$ ratio first, then use the unitary method.
**Biggest trap:** Using 12 months for a partner who joined late or withdrew early.