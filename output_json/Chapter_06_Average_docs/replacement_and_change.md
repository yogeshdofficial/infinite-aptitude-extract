# Replacement and Change

## Overview
This pattern involves a group where the average changes because a member is added, removed, or replaced. The central idea is to equate the **Total Sum** before and after the change to find the value of the specific item involved.

---

## Recognition Clues
* **Keywords:** "Average increases/decreases by...", "replaced by", "included", "left the class".
* **Given:** Original count, original average, and the amount of change (or the value of the new/replaced member).
* **Asked:** The value of the person/item added, removed, or the new average.

---

## Key Formulas

### [Total Sum Formula]
$$
\text{Total} = \text{Average} \times \text{Count}
$$

**Variables:**
- $\text{Total}$ = Sum of all values in the group
- $\text{Average}$ = The mean value
- $\text{Count}$ = Number of observations

**When to use:** To find the aggregate value before and after a change occurs.

**Worked example:** 50 students with an average of 45 kg. $\text{Total} = 50 \times 45 = 2250$ kg.

---

## Solution Framework

**Step 1: Calculate the initial total** — Multiply the original average by the original count.
**Step 2: Determine the new count** — Add or subtract 1 (or more) based on whether a person joined or left.
**Step 3: Determine the new average** — Add or subtract the given change from the original average.
**Step 4: Calculate the new total** — Multiply the new average by the new count.
**Step 5: Find the difference** — Subtract the two totals to find the value of the added/removed/replaced item.

---

## Shortcut Tricks

* **Trick:** $\text{Value of new member} = \text{Old Average} \pm (\text{Change in Average} \times \text{New Count})$.
* **Why it works:** The new member must compensate for the change in the average of every member in the new group.
* **When to use:** When one person is added or replaced.
* **Example (Q18):** Teacher included (39+1=40 people). Average increases by 0.25 years. Teacher's age = $15 + (0.25 \times 40) = 15 + 10 = 25$ years.

---

## Common Mistakes

* **Mistake:** Using the old count for the new total.
    * **Why it happens:** Habit of using the initial number of people.
    * **Fix:** Always update the count (e.g., $N+1$ or $N-1$) before multiplying.
* **Mistake:** Forgetting to convert units (months to years, grams to kg).
    * **Why it happens:** Ignoring the units in the question statement.
    * **Fix:** Standardize all units to the same scale before calculation.

---

## Worked Example (Step-by-Step)

**Question:** In a class there are 50 students. Their average weight is 45 kg. When a student leaves the class, the average is reduced by 100 g. Find the weight of the student who left the class.

**Solution:**
1. **Initial Total:** $50 \times 45 = 2250$ kg.
2. **New Count:** $50 - 1 = 49$ students.
3. **New Average:** $100\text{ g} = 0.1\text{ kg}$. New average $= 45 - 0.1 = 44.9$ kg.
4. **New Total:** $49 \times 44.9 = 2200.1$ kg.
5. **Difference:** $2250 - 2200.1 = 49.9$ kg.

**Answer:** 49.9 kg.

---

## Similar Patterns
* **Weighted Average:** Distinguish by checking if you are combining two distinct groups with different averages (use weighted average) vs. changing a single group (use this pattern).

---

## Revision Summary
* **Key formula:** $\text{Total} = \text{Average} \times \text{Count}$.
* **Spot it by:** Look for "average increases/decreases" and "person left/joined".
* **First move:** Calculate the initial total sum.
* **Fastest method:** Use the shortcut: $\text{Old Avg} \pm (\text{Change} \times \text{New Count})$.
* **Biggest trap:** Forgetting to update the count after a person leaves or joins.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Mean (Average):** The sum of all values divided by the number of values.
* **Unit Conversion:** Knowing that $1\text{ kg} = 1000\text{ g}$ and $1\text{ year} = 12\text{ months}$.

### Formulas You Must Know First
$$
\text{Average} = \frac{\text{Sum}}{\text{Count}}
$$
**What it means:** The central value of a data set.
**Example:** Average of 10 and 20 is $(10+20)/2 = 15$.

### Terms Used In This Pattern
* **Observation:** A single data point or person in the group.
* **Replacement:** Removing one item and adding another in its place.