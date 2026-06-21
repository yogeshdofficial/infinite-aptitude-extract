# Rent Sharing

## Overview
These problems involve distributing a total cost (rent) among multiple parties based on their usage of a resource. The core principle is that the share of rent is directly proportional to the product of the quantity used (e.g., cows) and the time duration.

---

## Recognition Clues
* **Keywords:** "Rented a pasture," "rented a set of DVDs," "grazed X cows for Y months."
* **Given:** Multiple parties, different quantities (cows/items), and different time durations.
* **Asked:** The share of one specific party or the total rent.
* **Structure:** A fixed total amount is to be divided based on weighted contributions.

---

## Important Formulas

### [Weighted Ratio of Shares]
$$
\text{Share Ratio} = (Q_1 \times T_1) : (Q_2 \times T_2) : (Q_3 \times T_3) \dots
$$
*Meaning:* $Q$ is the quantity (cows/items) and $T$ is the time duration.
*Use when:* You need to determine the proportion of the total rent each person must pay.

### [Individual Share Calculation]
$$
\text{Individual Share} = \text{Total Rent} \times \left( \frac{\text{Individual Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* Distributes the total rent based on the calculated weighted ratio.
*Use when:* You have the total rent and need to find a specific person's contribution.

---

## Solution Framework
1. Calculate the weighted contribution for each person: $Q \times T$.
2. Simplify the resulting ratio to the smallest possible integer form.
3. Sum the parts of the ratio to find the "Total Parts."
4. If a specific share is given, equate it to its ratio part to find the value of one "part."
5. Multiply the value of one "part" by the required person's ratio or the sum of all ratios.

---

## Shortcut Tricks
* **Ratio Simplification:** Divide all $Q \times T$ products by their HCF immediately before summing. This keeps numbers small and prevents calculation errors.
* **Direct Proportion:** If you need to find a total rent from one person's share, use: $\text{Total} = \text{Known Share} \times \frac{\text{Sum of all ratios}}{\text{Known person's ratio}}$.

---

## Common Mistakes
* **Ignoring Time:** Multiplying only by the number of cows/items and forgetting to multiply by the time duration.
* **Ratio Mismatch:** Using the raw $Q \times T$ values instead of the simplified ratio, leading to massive, unmanageable numbers.
* **Total vs. Individual:** Confusing the "Total Rent" with an "Individual Share" when setting up the final equation. Always verify if the given value is a part or the whole.

---

## Similar Patterns
This is a specific application of **Compound Partnership**. The only difference is that instead of dividing *profit*, you are dividing *cost (rent)*, but the mathematical ratio logic remains identical.

---

## Revision Summary
**Key formula:** $\text{Ratio} = Q \times T$.
**Spot it by:** Multiple entities using a resource for different quantities and times.
**Fastest method:** Simplify the $Q \times T$ ratio before calculating the total.
**Biggest trap:** Forgetting to multiply by time or failing to simplify the ratio early.