# Missing Capital

## Overview
These questions involve finding an unknown investment amount when profit ratios, time periods, and other partners' investments are provided. The central idea is that the ratio of profit shares is always equal to the ratio of the product of capital and time for each partner.

---

## Recognition Clues
* **Keywords:** "How much money did [Name] contribute?", "What was the amount invested by [Name]?", "Find the initial investment".
* **Given:** Profit ratios (or total profit and individual shares), time periods, and at least one known investment amount.
* **Variations:** Partners joining at different times, withdrawing capital, or adding capital mid-year.
* **Scan for:** "Invested for X months", "After Y months, [Name] joined", "Profit shared in ratio A:B:C".

---

## Important Formulas

### [Profit-Investment-Time Relationship]
$$
\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}
$$
*Meaning:* $P$ = Profit share, $C$ = Capital invested, $T$ = Time period.
*Use when:* Comparing two partners to find an unknown capital ($C$) or time ($T$).

### [Total Investment Summation]
$$
\text{Total Profit} = \sum (\text{Individual Capital} \times \text{Time}) \times \text{Constant}
$$
*Meaning:* Used when total profit is given as a fixed amount rather than a ratio.
*Use when:* You need to find a specific capital amount using the total business profit.

---

## Solution Framework
1. Define the unknown capital as $x$ (or $kx$ if a ratio is given).
2. Calculate the "effective capital" for each partner: $(\text{Capital} \times \text{Time})$.
3. If capital changes mid-year, sum the products: $(C_1 \times T_1) + (C_2 \times T_2)$.
4. Equate the ratio of these products to the given profit ratio.
5. Solve the resulting linear equation for $x$.

---

## Shortcut Tricks
* **Ratio Scaling:** If profit shares are given as fractions (e.g., $\frac{1}{8}, \frac{1}{3}$), convert them to a simple integer ratio immediately by multiplying by the LCM of denominators.
* **Time Normalization:** If all partners invest for the same time, ignore time and equate profit ratio directly to capital ratio.
* **Proportionality:** If $A:B = 3:2$ and $A$'s profit is known, use the multiplier method (e.g., if $3 \text{ units} = 3000$, then $1 \text{ unit} = 1000$) to find $B$ without formal equations.

---

## Common Mistakes
* **Ignoring Time:** Treating profit ratio as equal to capital ratio when time periods differ. *Fix:* Always multiply capital by time before forming the ratio.
* **Partial Year Confusion:** Forgetting to account for the time a partner was *absent* or *inactive*. *Fix:* Clearly write down the months of activity for each partner before calculating.
* **Adding Capital Errors:** Failing to multiply the *new* capital by the *remaining* time in the year. *Fix:* Use the bracketed sum method: $(C_{initial} \times T_{total}) + (C_{added} \times T_{remaining})$.

---

## Similar Patterns
This is distinct from "Missing Time" problems, though the formula is identical. The difference is purely algebraic: here you solve for $C$, there you solve for $T$.

---

## Revision Summary
**Key formula:** $\text{Profit Ratio} = (C_1 \times T_1) : (C_2 \times T_2)$.
**Spot it by:** Looking for "How much did X invest?" alongside profit and time data.
**Fastest method:** Convert profit fractions to integer ratios and use the multiplier method.
**Biggest trap:** Forgetting to multiply the *added* capital by the *remaining* months only.