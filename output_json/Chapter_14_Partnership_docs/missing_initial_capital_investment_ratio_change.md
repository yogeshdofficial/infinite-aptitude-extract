# Missing Initial Capital: Investment Ratio Change

## Overview
This pattern involves partners whose initial investments are in a known ratio, but who later add or withdraw capital, resulting in a new, known investment ratio. The central idea is to represent initial investments as variables (e.g., $3x, 5x, 7x$) and equate the ratio of the modified investments to the given final ratio.

---

## Recognition Clues
* **Keywords:** "invests another", "withdraws", "ratio... changes to".
* **Given:** Initial investment ratio, specific amounts added/withdrawn by partners, and the final investment ratio.
* **Asked:** The initial investment amount of a specific partner.
* **Visual Scan:** Look for a ratio followed by a "change" event and a second ratio.

---

## Important Formulas

### [Investment Ratio Equation]
$$
\frac{I_A \pm \Delta A}{I_B \pm \Delta B} = \frac{R_{final, A}}{R_{final, B}}
$$

*Meaning:* $I$ is the initial investment (as $kx$), $\Delta$ is the change amount, and $R$ is the final ratio value.
*Use when:* You need to solve for the common multiplier $x$ to find the actual initial investment.

---

## Solution Framework
1. Assign variables to initial investments using the given ratio (e.g., $3x, 5x, 7x$).
2. Apply the additions or subtractions to the relevant partners' variables.
3. Set up a ratio equation using any two partners from the modified set.
4. Cross-multiply to solve for the variable $x$.
5. Multiply $x$ by the initial ratio coefficient of the requested partner.

---

## Shortcut Tricks
* **Pair Selection:** Choose the two partners whose modified values result in the simplest algebraic equation (e.g., avoid the partner with the largest constant if possible).
* **Validity:** This is valid because any two parts of a ratio are sufficient to determine the value of the common multiplier $x$.

---

## Common Mistakes
* **Variable Confusion:** Forgetting to multiply the initial ratio by $x$ and treating the ratio numbers as absolute values.
    * *Reason:* Treating a ratio as a fixed quantity rather than a proportional representation.
    * *Fix:* Always write initial investments as $ax, bx, cx$.
* **Sign Error:** Adding when the problem says "withdraws" or subtracting when it says "invests".
    * *Reason:* Rushing through the reading of the transaction.
    * *Fix:* Explicitly write $+ \text{amount}$ for investment and $- \text{amount}$ for withdrawal.
* **Ratio Mismatch:** Pairing the wrong numerator with the wrong denominator in the final ratio.
    * *Reason:* Losing track of the order of partners (A, B, C).
    * *Fix:* Write the names above the ratio numbers to maintain alignment.

---

## Similar Patterns
This is distinct from "Compound Partnership" problems because the time period is constant (1 year) for all partners; the change is purely in the capital amount, not the duration of investment.

---

## Revision Summary
**Key formula:** $\frac{\text{Initial}_A \pm \text{Change}_A}{\text{Initial}_B \pm \text{Change}_B} = \frac{\text{Final Ratio}_A}{\text{Final Ratio}_B}$

**Spot it by:** Initial ratio given, followed by specific additions/withdrawals and a final ratio.

**Fastest method:** Use only two partners from the ratio to solve for $x$ via cross-multiplication.

**Biggest trap:** Forgetting to attach the variable $x$ to the initial ratio parts.