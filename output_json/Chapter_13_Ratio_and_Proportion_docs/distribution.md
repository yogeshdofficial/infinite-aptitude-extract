# Distribution

## Overview
This pattern involves dividing a total quantity into parts based on specific ratio relationships between parties. The central idea is to convert all given relationships into a single unified ratio ($A:B:C...$) and then distribute the total based on the sum of these ratio parts.

---

## Recognition Clues
* **Keywords:** "Divide [amount] among...", "in the ratio...", "A receives [fraction] as much as B and C".
* **Given:** A total sum and either a direct ratio, equality of shares (e.g., $3A = 4B$), or relative shares (e.g., $A$ gets $2/5$ of $B+C$).
* **Asked:** The individual share of each party.

---

## Key Formulas

### [Individual Share]
$$
\text{Share}_i = \frac{\text{Ratio}_i}{\sum \text{Ratio}} \times \text{Total}
$$

**Variables:**
- $\text{Share}_i$ = The amount allocated to person $i$
- $\text{Ratio}_i$ = The specific ratio term for person $i$
- $\sum \text{Ratio}$ = The sum of all terms in the unified ratio
- $\text{Total}$ = The total amount to be divided

**When to use:** Once you have a unified ratio (e.g., $A:B:C = 28:21:12$).

**Worked example:** Total = ₹ 427, Ratio = $28:21:12$. Sum = 61. A's share = $\frac{28}{61} \times 427 = 196$.

---

## Solution Framework

1. **Unify the Ratio:** Convert all given conditions into a single ratio $A:B:C...$ by finding common denominators or equating common terms.
2. **Sum the Terms:** Add all the terms of the unified ratio to find the "total number of parts."
3. **Find Unit Value:** Divide the total amount by the sum of the ratio terms to find the value of "one part."
4. **Calculate Shares:** Multiply each individual's ratio term by the value of one part to get their specific share.

---

## Shortcut Tricks

* **Trick:** For $xA = yB = zC$, the ratio $A:B:C$ is $\frac{1}{x} : \frac{1}{y} : \frac{1}{z}$.
* **Why it works:** To keep the products equal, the shares must be inversely proportional to their coefficients.
* **When to use:** When the question states "x times A's share = y times B's share...".
* **Example:** $3A = 4B = 7C \Rightarrow A:B:C = \frac{1}{3} : \frac{1}{4} : \frac{1}{7} = 28:21:12$.

---

## Common Mistakes

* **Mistake:** Assuming the ratio is $3:4:7$ in $3A=4B=7C$.
    * **Fix:** Always take the reciprocals ($\frac{1}{3}:\frac{1}{4}:\frac{1}{7}$) to find the ratio.
* **Mistake:** Forgetting to normalize common terms in multi-step ratios (e.g., $A:B$ and $B:C$).
    * **Fix:** Ensure the value of the common variable (e.g., $B$) is identical in both ratios before combining.
* **Mistake:** Misinterpreting "A receives $2/5$ as much as B and C together."
    * **Fix:** Write it as $A = \frac{2}{5}(B+C)$, then use $A+B+C = \text{Total}$ to solve for $A$.

---

## Worked Example (Step-by-Step)

**Question:** Divide ₹ 427 among A, B, and C such that 3 times A’s share, 4 times B’s share, and 7 times C’s share are all equal.

**Solution:**
1. **Unify:** $3A = 4B = 7C$. Ratio $A:B:C = \frac{1}{3} : \frac{1}{4} : \frac{1}{7}$. Multiply by LCM (84) to get $28:21:12$.
2. **Sum:** $28 + 21 + 12 = 61$.
3. **Unit Value:** $\frac{427}{61} = 7$.
4. **Shares:** $A = 28 \times 7 = 196$; $B = 21 \times 7 = 147$; $C = 12 \times 7 = 84$.

**Answer:** A = ₹ 196, B = ₹ 147, C = ₹ 84.

---

## Similar Patterns

**Partnership:** Distinguished by the inclusion of "time" as a factor; here, distribution is based solely on static ratios.

---

## Revision Summary

* **Key formula:** $\text{Share} = (\text{Ratio Term} / \text{Sum}) \times \text{Total}$.
* **Spot it by:** "Divide [amount] in ratio..." or equality of shares.
* **First move:** Convert all conditions into a single unified ratio.
* **Fastest method:** Use reciprocals for equality conditions ($xA=yB$).
* **Biggest trap:** Using the coefficients directly as the ratio instead of their reciprocals.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio:** A comparison of two quantities by division, written as $a:b$.
* **LCM (Least Common Multiple):** The smallest number divisible by all given denominators, used to clear fractions in ratios.

### Formulas You Must Know First
* **Equivalent Ratios:** $\frac{a}{b} = \frac{a \times k}{b \times k}$.
    * **What it means:** Multiplying or dividing both terms of a ratio by the same number does not change the ratio.

### Terms Used In This Pattern
* **Antecedent:** The first term in a ratio.
* **Consequent:** The second term in a ratio.
* **Unified Ratio:** A single ratio string (e.g., $A:B:C$) representing the relative values of all parties.