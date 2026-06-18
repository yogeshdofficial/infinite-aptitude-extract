# Phased Usage (Rent/Expense Distribution)

## Overview
This pattern involves splitting a total cost (like rent) among partners who enter or leave the arrangement at different time intervals. The central idea is to calculate the cost per unit of time and distribute it only among those present during that specific phase.

---

## Recognition Clues
* **Keywords:** "Remained together for X months," "After Y more months," "Left the house/business."
* **Given:** Total cost for a fixed period (e.g., one year) and a sequence of departures.
* **Asked:** Total share of cost to be paid by each individual.
* **Structure:** A timeline is provided where the number of active participants changes at specific intervals.

---

## Important Formulas

### [Monthly Cost Calculation]
$$
\text{Monthly Cost} = \frac{\text{Total Cost}}{\text{Total Duration}}
$$
*Meaning:* The cost incurred per unit of time (e.g., per month).
*Use when:* The total cost is given for a fixed period, and you need to break it down into manageable phases.

### [Phase Share Calculation]
$$
\text{Share per person in phase} = \frac{\text{Monthly Cost} \times \text{Phase Duration}}{\text{Number of active partners}}
$$
*Meaning:* The amount each person present during a specific phase must contribute.
*Use when:* Calculating the individual burden for a specific time block.

---

## Solution Framework
1. Calculate the cost per unit of time (e.g., monthly rent).
2. Divide the total timeline into distinct phases based on when partners leave or join.
3. For each phase, multiply the monthly cost by the number of months in that phase.
4. Divide that phase's total cost equally among the partners active during that specific time.
5. Sum the individual shares from all phases to find the total amount each person owes.

---

## Shortcut Tricks
* **Phase-Summation:** Instead of calculating individual shares per phase, calculate the total "person-months" for each individual.
* **Validity:** Since the cost per month is constant, the total cost for a person is simply $(\text{Monthly Cost}) \times (\text{Total months they stayed})$.

---

## Common Mistakes
* **Ignoring the "After X more months" phrasing:** Students often add the months incorrectly; always draw a timeline to track the cumulative time.
* **Dividing by total partners:** Dividing the phase cost by the total number of partners instead of only those present during that specific phase.
* **Miscounting the final phase:** Forgetting to account for the remaining months after the last person leaves or the period ends.

---

## Similar Patterns
* **Compound Partnership:** Unlike this pattern, which divides a *fixed cost*, Compound Partnership divides a *variable profit* based on the ratio of (Investment $\times$ Time).

---

## Revision Summary
**Key formula:** $\text{Monthly Cost} = \frac{\text{Total Cost}}{\text{Total Duration}}$.
**Spot it by:** Multiple people leaving or joining at different time intervals.
**Fastest method:** Calculate the cost per phase and divide by the number of active partners.
**Biggest trap:** Miscalculating the duration of each phase or including partners who have already left.