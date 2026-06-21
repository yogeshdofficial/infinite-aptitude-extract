# Rent Sharing: Phased Usage

## Overview

* This pattern involves splitting a fixed total cost (rent) among multiple people who occupy a space for different, overlapping durations.
* The central idea is to calculate the **monthly rent** and distribute it proportionally based on the number of people present during each specific time phase.

---

## Recognition Clues

* **Keywords:** "Took a house on rent," "remained together for X months," "left the house," "after Y more months."
* **Given:** Total rent for a fixed period (usually 1 year), and a timeline of who leaves/joins at specific intervals.
* **Asked:** The total rent share for each individual.

---

## Important Formulas

### [Monthly Rent Calculation]

$$
\text{Monthly Rent} = \frac{\text{Total Rent}}{\text{Total Months}}
$$

*Meaning:* The base cost per unit of time.
*Use when:* The total rent is given for a fixed duration (e.g., 1 year).

### [Phase Share Calculation]

$$
\text{Share per person in phase} = \frac{\text{Monthly Rent} \times \text{Months in Phase}}{\text{Number of occupants in phase}}
$$

*Meaning:* The cost assigned to each person for a specific time block.
*Use when:* Calculating the rent burden for a specific period where the number of occupants is constant.

---

## Solution Framework

1. Calculate the monthly rent by dividing the total rent by the total duration.
2. Break the total duration into distinct "phases" based on when someone leaves or joins.
3. For each phase, multiply the monthly rent by the number of months in that phase.
4. Divide the phase-total by the number of people present during that specific phase.
5. Sum the individual shares from all phases to get the total rent for each person.

---

## Shortcut Tricks

* **No specific shortcut:** This pattern requires systematic phase-by-phase accounting; attempting to use shortcuts often leads to errors in tracking who was present in which phase.

---

## Common Mistakes

* **Mistake:** Dividing the total rent by the number of people first.
    * *Reason:* Rent is time-dependent, not just person-dependent.
    * *Fix:* Always calculate the monthly rent first, then distribute by time-phases.
* **Mistake:** Miscounting the "remaining" months after someone leaves.
    * *Reason:* Confusing "after X months" with "for X months."
    * *Fix:* Draw a simple timeline on your scratchpad to mark the start and end of each phase.
* **Mistake:** Forgetting to add up shares from different phases for the same person.
    * *Reason:* Stopping after calculating the share for only the first phase.
    * *Fix:* Create a table with columns for each person and rows for each phase to ensure no phase is missed.

---

## Similar Patterns

* This is distinct from **Compound Partnership**; in partnership problems, you multiply capital by time to find profit ratios, whereas here you divide a fixed cost by time-phases to find rent shares.

---

## Revision Summary

**Key formula:** $\text{Monthly Rent} \times \text{Phase Duration} \div \text{Occupants}$.

**Spot it by:** A timeline of people leaving or joining a shared rental space.

**Fastest method:** Calculate rent phase-by-phase and sum the results for each person.

**Biggest trap:** Treating the rent as a simple division problem without accounting for the changing number of occupants over time.