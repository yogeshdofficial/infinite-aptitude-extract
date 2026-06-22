# Group Work

## Overview
This pattern involves calculating the time taken by mixed groups (e.g., men, women, children) to complete a task. The central idea is to convert the work capacity of each individual into a common unit (a "daily work rate") and then sum these rates based on the group composition.

---

## Recognition Clues
* **Keywords:** "piece of work," "together," "in how many days," "men, women, and children."
* **Given:** Different groups (e.g., 2 men and 3 boys) completing a task in a specific number of days.
* **Asked:** The time taken by a different combination of the same workers.
* **Variation:** Sometimes earnings are given instead of work units; the logic remains identical (calculate daily earning per person).

---

## Key Formulas

### [Daily Work Rate]
$$
\text{Rate} = \frac{1}{\text{Total Days}}
$$
**Variables:**
- $\text{Rate}$ = fraction of work completed in 1 day.
- $\text{Total Days}$ = time taken to complete the entire task.

**When to use:** To convert "days to complete" into a usable "work per day" value.

**Worked example:** If 9 children take 360 days, 1 child's rate = $\frac{1}{9 \times 360} = \frac{1}{3240}$.

---

## Solution Framework
1. **Find individual daily rates:** Calculate the work done by 1 unit of each type (e.g., 1 man, 1 woman) in 1 day.
2. **Set up equations:** If the problem gives two different group scenarios, create a system of linear equations ($ax + by = \text{rate}$).
3. **Solve for variables:** Use substitution or elimination to find the individual rate ($x$ and $y$).
4. **Calculate target group rate:** Multiply the individual rates by the number of people in the target group and sum them.
5. **Invert for time:** Take the reciprocal of the target group's total daily rate to find the total days.

---

## Shortcut Tricks
* **Trick:** If given total earnings for groups, divide total money by days first to get "Daily Group Earning," then solve the system of equations.
* **Why it works:** It reduces the problem to a standard "Work Rate" problem by treating money as the "work" unit.
* **When to use:** When the question provides total earnings over a period (e.g., Q22).
* **Example:** 3 men + 4 women earn ₹3780 in 7 days $\rightarrow$ $3m + 4w = \frac{3780}{7} = 540$.

---

## Common Mistakes
* **Mistake:** Using the number of days directly in equations instead of the reciprocal (work rate).
* **Why it happens:** Forgetting that work is inversely proportional to time.
* **Fix:** Always convert "days" to "1/days" before adding or equating.
* **Mistake:** Forgetting to multiply the individual rate by the number of people in the target group.
* **Fix:** Always write out the full expression: $(\text{Number} \times \text{Rate}) + (\text{Number} \times \text{Rate})$.

---

## Worked Example (Step-by-Step)

**Question:** 2 men and 3 boys can do a piece of work in 10 days while 3 men and 2 boys can do the same work in 8 days. In how many days can 2 men and 1 boy do the work?

**Solution:**
1. **Find rates:** Let 1 man's rate = $x$, 1 boy's rate = $y$.
2. **Equations:** $2x + 3y = \frac{1}{10}$ and $3x + 2y = \frac{1}{8}$.
3. **Solve:** Multiply eq1 by 2 and eq2 by 3: $4x + 6y = \frac{1}{5}$ and $9x + 6y = \frac{3}{8}$. Subtracting gives $5x = \frac{7}{40} \rightarrow x = \frac{7}{200}$. Substituting $x$ gives $y = \frac{1}{100}$.
4. **Target group:** $2x + 1y = 2(\frac{7}{200}) + 1(\frac{1}{100}) = \frac{14+2}{200} = \frac{16}{200} = \frac{2}{25}$.
5. **Invert:** Total days = $\frac{25}{2} = 12.5$ days.

**Answer:** $12\frac{1}{2}$ days.

---

## Similar Patterns
* **Time and Work (Individual):** If the question only involves one type of worker, you don't need a system of equations; just add the rates directly.

---

## Revision Summary
* **Key formula:** $\text{Rate} = \frac{1}{\text{Days}}$.
* **Spot it by:** Multiple groups of different workers given in days.
* **First move:** Convert all "days" into "1/days" (daily rates).
* **Fastest method:** Use elimination to solve the system of equations for individual rates.
* **Biggest trap:** Adding the number of days instead of the work rates.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Reciprocals** — If a task takes $n$ days, the work done in 1 day is $\frac{1}{n}$.
* **System of Equations** — Solving two equations with two variables ($x$ and $y$) using elimination.

### Formulas You Must Know First
$$
\text{Work} = \text{Rate} \times \text{Time}
$$
**What it means:** The total work done is the product of the rate of work and the time spent.
**Example:** If a man works at a rate of $\frac{1}{10}$ per day, in 5 days he does $\frac{1}{10} \times 5 = \frac{1}{2}$ of the work.

### Terms Used In This Pattern
* **Unit of work** — The total task, usually represented as 1.
* **Efficiency** — The rate at which a person completes work.