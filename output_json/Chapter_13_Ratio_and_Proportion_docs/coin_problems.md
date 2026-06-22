# Coin Problems

## Overview
These questions involve a collection of coins of different denominations (e.g., ₹1, 50-paise, 25-paise) where you are given either the ratio of the number of coins or the ratio of their total values. The central idea is to convert all denominations into a single unit (rupees) to equate them to the total given amount.

---

## Recognition Clues
* **Keywords:** "bag contains," "box contains," "ratio of coins," "ratio of their values," "total amount."
* **Given:** Ratio of coins (or values) and the total monetary value of the bag.
* **Asked:** Number of coins of a specific denomination.
* **Scan for:** Denominations in paise (e.g., 50-paise, 25-paise) — these **must** be converted to rupees.

---

## Key Formulas

### Total Value Formula
$$
\text{Total Value} = \sum (\text{Number of coins} \times \text{Value per coin})
$$

**Variables:**
- $\text{Number of coins}$: The count of a specific denomination (e.g., $5x$).
- $\text{Value per coin}$: The worth of one coin in rupees (e.g., 50-paise = $0.50$).

**When to use:** When the ratio of the *number* of coins is given.

**Worked example:** If you have $6x$ coins of 50-paise, the value is $6x \times 0.50 = 3x$ rupees.

### Number of Coins Formula
$$
\text{Number of coins} = \frac{\text{Total Value of Denomination}}{\text{Value per coin}}
$$

**When to use:** When the ratio of the *values* of the coins is given.

**Worked example:** If the value of 50-paise coins is $3x$ rupees, the number of coins is $\frac{3x}{0.50} = 6x$.

---

## Solution Framework

1. **Step 1: Define variables:** Assign $x$ to the ratio parts (e.g., $5x, 6x, 8x$).
2. **Step 2: Standardize units:** Convert all paise values to rupees (e.g., $25\text{ paise} = 0.25\text{ rupees}$).
3. **Step 3: Express total value:** Multiply the number of coins by their value per coin to get the total value in terms of $x$.
4. **Step 4: Equate and solve:** Set the sum of these values equal to the total amount given in the question and solve for $x$.
5. **Step 5: Calculate target:** Multiply $x$ by the specific ratio part requested.

---

## Shortcut Tricks
* **Trick:** If the ratio is of *values*, convert to *number of coins* by dividing the ratio parts by the coin's value.
* **Why it works:** It bypasses complex algebraic fractions by working directly with the count of items.
* **Example:** Ratio of values $2:3:5$ for (₹1, 50p, 25p) becomes $\frac{2}{1} : \frac{3}{0.5} : \frac{5}{0.25} \Rightarrow 2:6:20$.

---

## Common Mistakes
* **Mistake:** Adding the ratio parts directly to the total amount (e.g., $5x + 6x + 8x = 210$).
    * **Fix:** Always multiply by the coin's value first.
* **Mistake:** Forgetting to convert paise to rupees.
    * **Fix:** Always divide paise by 100 before multiplying by $x$.
* **Mistake:** Assuming the ratio given is always the "number of coins."
    * **Fix:** Read carefully—it might be the "ratio of values."

---

## Worked Example (Step-by-Step)

**Question:** A bag contains one-rupee, 50-paise and 25-paise coins in the ratio 5 : 6 : 8. If the total amount is ₹ 210, find the number of 50-paise coins.

**Solution:**
1. **Define:** Number of coins = $5x$ (₹1), $6x$ (50p), $8x$ (25p).
2. **Standardize:** Values are $1$, $0.50$, and $0.25$ rupees.
3. **Total Value:** $(5x \times 1) + (6x \times 0.50) + (8x \times 0.25) = 5x + 3x + 2x = 10x$.
4. **Equate:** $10x = 210 \Rightarrow x = 21$.
5. **Target:** 50-paise coins = $6x = 6 \times 21 = 126$.

**Answer:** 126 coins.

---

## Similar Patterns
* **Partnership Problems:** These involve ratios of investment and time. Distinguish by checking if the problem mentions "coins/denominations" (Coin Problems) or "capital/time" (Partnership).

---

## Revision Summary
* **Key formula:** $\text{Total Value} = \sum (\text{Count} \times \text{Value})$.
* **Spot it by:** Ratio of coins + Total money in bag.
* **First move:** Convert all denominations to rupees.
* **Fastest method:** Use the "Value to Count" conversion if the ratio is of values.
* **Biggest trap:** Adding ratio parts without multiplying by coin value.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio:** Expressing quantities as $ax : bx$.
* **Decimal Multiplication:** Multiplying by $0.50$ (same as dividing by 2) and $0.25$ (same as dividing by 4).

### Formulas You Must Know First
* **Value Conversion:** $100\text{ paise} = 1\text{ rupee}$.

### Terms Used In This Pattern
* **Denomination:** The face value of a coin (e.g., 50-paise).
* **Ratio:** The relative size of two or more quantities.