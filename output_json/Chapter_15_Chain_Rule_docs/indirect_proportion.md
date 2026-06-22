# Indirect Proportion

## Overview
This pattern involves scenarios where two quantities are inversely related: as one increases, the other decreases proportionally (e.g., more workers finish a job in less time). The central idea is that the product of the two quantities remains constant across different scenarios.

---

## Recognition Clues
* **Keywords:** "more/less men," "more/less days," "more/less hours," "same work," "same piece of work."
* **Given:** Two sets of values (e.g., Men1 and Days1) and one value of the second set (e.g., Men2).
* **Asked:** The missing value (e.g., Days2) required to complete the same task.
* **Logic Check:** If the number of workers increases, the time taken *must* decrease. If it doesn't, it is not an indirect proportion.

---

## Key Formulas

### [Inverse Proportion Product Rule]

$$
M_1 \times T_1 = M_2 \times T_2
$$

**Variables:**
- $M_1, M_2$ = Number of people/workers in scenario 1 and 2.
- $T_1, T_2$ = Time taken (days/hours) in scenario 1 and 2.

**When to use:** When the total work remains constant and you need to find one of the four variables.

**Worked example:** 36 men ($M_1$) take 25 hours ($T_1$). How long ($T_2$) for 15 men ($M_2$)?
$36 \times 25 = 15 \times T_2 \implies 900 = 15 \times T_2 \implies T_2 = 60$ hours.

---

## Solution Framework

1. **Identify the variables:** Assign values to $M_1, T_1$ and $M_2, T_2$ based on the problem statement.
2. **Verify the relationship:** Confirm that the total work is constant and the relationship is inverse.
3. **Set up the equation:** Write the product of the first pair equal to the product of the second pair ($M_1 \times T_1 = M_2 \times T_2$).
4. **Solve for the unknown:** Isolate the variable by dividing the known product by the coefficient of the unknown.

---

## Shortcut Tricks

* **Trick:** Use the ratio method: $T_2 = T_1 \times (\frac{M_1}{M_2})$.
* **Why it works:** It directly calculates the scaling factor of the change in workers and applies it to the time.
* **When to use it:** When you need to perform the calculation in one line without writing out the full equation.
* **Example:** 56 men take 24 days. How long for 42 men? $24 \times (\frac{56}{42}) = 24 \times (\frac{4}{3}) = 32$ days.

---

## Common Mistakes

* **Mistake:** Setting up as a direct proportion ($\frac{M_1}{M_2} = \frac{T_1}{T_2}$).
    * **Why it happens:** Confusing inverse relationships with direct ones.
    * **Fix:** Always ask, "If I add more people, should the time go up or down?" If down, use multiplication, not division.
* **Mistake:** Forgetting to adjust the worker count (e.g., $x - 9$).
    * **Why it happens:** Misreading "9 people were absent" as the total number of workers.
    * **Fix:** Always define the variable as the *original* number and subtract the absentees.

---

## Worked Example (Step-by-Step)

**Question:** A certain number of people were supposed to complete a work in 24 days. The work, however, took 32 days since 9 people were absent throughout. How many people were supposed to be working originally?

**Solution:**
1. **Identify:** Let original people = $x$. Then $M_1 = x, T_1 = 24$. After 9 left, $M_2 = (x-9), T_2 = 32$.
2. **Verify:** Fewer people take more days; this is an inverse proportion.
3. **Equation:** $x \times 24 = (x - 9) \times 32$.
4. **Solve:** $24x = 32x - 288 \implies 8x = 288 \implies x = 36$.

**Answer:** 36 people.

---

## Similar Patterns

**Direct Proportion:** Distinguish by checking if the variables move in the *same* direction (e.g., more items = more cost). If they move in opposite directions, it is Indirect Proportion.

---

## Revision Summary

* **Key formula:** $M_1 \times T_1 = M_2 \times T_2$.
* **Spot it by:** Looking for "same work" and changing worker/time counts.
* **First move:** Set the product of the first scenario equal to the second.
* **Fastest method:** $T_2 = T_1 \times (\frac{M_1}{M_2})$.
* **Biggest trap:** Setting up a direct ratio instead of an inverse product.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Inverse Proportion** — A relationship where the product of two variables is constant ($xy = k$).
* **Algebraic Isolation** — Moving terms across the equals sign to solve for $x$.

### Formulas You Must Know First
* No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Constant Work** — The assumption that the total task size does not change regardless of the number of workers.