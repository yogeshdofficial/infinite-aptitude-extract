# Rent Sharing

## Overview
These problems involve distributing a total cost (rent) among multiple parties based on their usage of a resource (cows/pasture or time/DVDs). The central idea is that the rent is shared in direct proportion to the "weighted usage" (Quantity $\times$ Time) of each participant.

---

## Recognition Clues
* **Keywords:** "Rented a pasture," "rented a set of DVDs," "grazed [X] cows for [Y] months."
* **Given:** Individual usage quantities (cows/hours), individual time durations, and either the total rent or one person's specific share.
* **Asked:** Total rent or the share of a specific individual.

---

## Important Formulas

### [Share Ratio]
$$
\text{Ratio} = (Q_1 \times T_1) : (Q_2 \times T_2) : (Q_3 \times T_3) \dots
$$
*Meaning:* $Q$ is the quantity (cows/items), $T$ is the time duration.
*Use when:* Calculating the proportional weight of each person's contribution to the total rent.

### [Individual Share]
$$
\text{Individual Share} = \text{Total Rent} \times \left( \frac{\text{Individual Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* The individual's portion of the total rent based on their relative weight.
*Use when:* You have the total rent and need to find a specific person's payment.

---

## Solution Framework
1. Calculate the "weighted usage" for each person by multiplying quantity by time.
2. Simplify the resulting ratio to the smallest possible integer form.
3. Sum the parts of the ratio to find the "Total Parts."
4. If one person's share is given, equate their ratio part to that value to find the "value of one part."
5. Multiply the "value of one part" by the target person's ratio or the sum of all ratios to get the answer.

---

## Shortcut Tricks
* **Simplify Early:** Divide all weighted values by their HCF immediately before summing them. This keeps numbers small and prevents calculation errors.
* **Fractional Equivalence:** If $A$'s share is given as $S_A$ and their ratio part is $R_A$, then Total Rent = $S_A \times \frac{\text{Total Ratio Sum}}{R_A}$. This avoids calculating the "value of one part" as a separate intermediate step.

---

## Common Mistakes
* **Ignoring Time:** Multiplying only by the number of cows/items. Always check if time is provided; if it is, it must be included in the ratio.
* **Ratio Inversion:** Placing the total ratio sum in the numerator instead of the denominator. Remember: (Part / Whole) $\times$ Total.
* **Calculation Errors:** Forgetting to simplify the ratio before summing. Large numbers increase the probability of arithmetic slips.

---

## Similar Patterns
This is a specific application of **Compound Partnership**. Distinguish it by the context: "Rent Sharing" involves paying for a service/resource, whereas "Partnership" involves dividing profit from an investment.

---

## Revision Summary
**Key formula:** $\text{Ratio} = (\text{Quantity} \times \text{Time})$.
**Spot it by:** Multiple parties using a resource for different durations or quantities.
**Fastest method:** Simplify the ratio of weighted usages first, then use the fractional share method.
**Biggest trap:** Forgetting to multiply by time when it is explicitly provided in the problem.