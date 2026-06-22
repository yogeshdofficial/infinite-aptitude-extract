# Mixture Profit Loss

## Overview
This pattern involves mixing two or more items of different costs to create a final mixture, which is then sold at a specific profit or loss percentage. The central idea is to calculate the **Total Cost Price** of the entire mixture first, then apply the profit/loss percentage to find the required **Selling Price**.

---

## Recognition Clues
* **Keywords:** "mixed with," "adulterating," "varieties," "rate per kg," "gain/profit of X%."
* **Given:** Quantities and individual cost rates of two or more items; target profit/loss percentage.
* **Asked:** Selling price per kg of the mixture OR the ratio in which items were mixed.

---

## Key Formulas

### [Total Cost Price]
$$
\text{Total C.P.} = \sum (\text{Quantity}_i \times \text{Rate}_i)
$$
**Variables:** $Q_i$ = quantity of item $i$, $R_i$ = cost rate of item $i$.
**When to use:** When you need the base cost of the entire batch before calculating profit.
**Example:** 80 kg at ₹13.50 + 120 kg at ₹16 $\rightarrow (80 \times 13.5) + (120 \times 16) = 1080 + 1920 = 3000$.

### [Selling Price from Profit]
$$
\text{S.P.} = \text{Total C.P.} \times \left(1 + \frac{\text{Profit}\%}{100}\right)
$$
**Variables:** $\text{S.P.}$ = total selling price, $\text{Profit}\%$ = target gain percentage.
**When to use:** To find the total revenue required to achieve a specific profit.
**Example:** Total C.P. = 3000, Profit = 16% $\rightarrow 3000 \times 1.16 = 3480$.

### [Alligation Rule (for Ratios)]
$$
\text{Ratio} = (\text{Mean Price} - \text{Cheaper Price}) : (\text{Dearer Price} - \text{Mean Price})
$$
**When to use:** When you know the selling price and profit, and need the ratio of ingredients.
**Example:** Ghee (100), Oil (50), Mean (80) $\rightarrow (80-50) : (100-80) = 30:20 = 3:2$.

---

## Solution Framework
1. **Calculate Total C.P.:** Multiply each quantity by its rate and sum them up.
2. **Adjust for Overheads (if any):** Add any extra expenses to the Total C.P.
3. **Find Mean C.P. (if needed):** If given S.P. and profit%, use $\text{C.P.} = \frac{\text{S.P.}}{1 + \text{Profit}\%}$ to find the cost per unit.
4. **Apply Profit/Loss:** Multiply the Total C.P. by $(1 \pm \text{percentage})$ to get the total S.P.
5. **Calculate Final Rate:** Divide the total S.P. by the total quantity to get the rate per kg.

---

## Shortcut Tricks
* **Trick:** Use the Alligation Rule for ratio problems instead of algebraic equations.
* **Why it works:** It directly maps the difference between individual costs and the mean cost to the required quantities.
* **When to use:** When the question asks "In what ratio should he mix..."
* **Example:** Q17: Mean price 80, Ghee 100, Oil 50. $(80-50)=30$ (for Ghee), $(100-80)=20$ (for Oil). Ratio $30:20 = 3:2$.

---

## Common Mistakes
* **Mistake:** Averaging the rates directly (e.g., $\frac{13.5+16}{2}$).
    * **Why:** It ignores the different quantities (weights) of the items.
    * **Fix:** Always use the weighted average: $\frac{\sum (Q \times R)}{\sum Q}$.
* **Mistake:** Applying profit% to the S.P. instead of the C.P.
    * **Why:** Profit is always calculated on the Cost Price.
    * **Fix:** Use $\text{S.P.} = \text{C.P.} \times (1 + \text{Profit}\%)$.

---

## Worked Example (Step-by-Step)

**Question (Q16):** A grocer purchased 80 kg of sugar at ₹13.50/kg and 120 kg at ₹16/kg. At what rate should he sell the mixture to gain 16%?

**Solution:**
1. **Total C.P.:** $(80 \times 13.50) + (120 \times 16) = 1080 + 1920 = 3000$.
2. **Total Quantity:** $80 + 120 = 200$ kg.
3. **Total S.P. for 16% gain:** $3000 \times 1.16 = 3480$.
4. **Rate per kg:** $\frac{3480}{200} = 17.40$.

**Answer:** ₹17.40 per kg.

---

## Similar Patterns
**Weighted Average Problems:** These are identical in calculation; the only difference is the context (e.g., mixing liquids vs. mixing prices).

---

## Revision Summary
* **Key formula:** $\text{Total C.P.} = \sum (\text{Quantity} \times \text{Rate})$.
* **Spot it by:** Multiple items with different rates being combined.
* **First move:** Calculate the total cost of the entire mixture.
* **Fastest method:** Use Alligation for ratio questions; weighted sum for rate questions.
* **Biggest trap:** Calculating a simple average of rates instead of a weighted average.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Weighted Average** — The average of values where each value has a different "weight" (quantity).
* **Alligation** — A shortcut method to find the ratio of two ingredients when the mean price is known.

### Formulas You Must Know First
$$
\text{Profit} = \text{S.P.} - \text{C.P.}
$$
**What it means:** The difference between selling and buying price.

### Terms Used In This Pattern
* **C.P. (Cost Price):** The price at which goods are bought.
* **S.P. (Selling Price):** The price at which goods are sold.
* **Overhead Expenses:** Extra costs (transport, labor) added to the initial C.P.