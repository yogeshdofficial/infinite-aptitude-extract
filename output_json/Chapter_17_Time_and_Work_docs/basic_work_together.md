# Basic Work Together

## Overview
This pattern involves calculating the total time required for multiple people to complete a task when their individual work rates are known. The central idea is to convert "time taken" into "work done per unit of time" (rate), sum these rates, and then take the reciprocal to find the total time.

---

## Recognition Clues
* **Keywords:** "together," "in how many days," "complete the same work," "both of them."
* **Given:** Individual time taken by two or more people (e.g., "A in 4 days, B in 5 days").
* **Asked:** Time taken when they work simultaneously.
* **Variation:** Sometimes asked for "part of the work done in a day" instead of total time.

---

## Key Formulas

### Combined Time Formula (for two people)
$$
\text{Time} = \frac{xy}{x+y}
$$

**Variables:**
- $x$ = time taken by person A
- $y$ = time taken by person B

**When to use:** When exactly two people are working together.

**Worked example:** Roger (8 days) and Antony (5 days).
$\text{Time} = \frac{8 \times 5}{8 + 5} = \frac{40}{13} = 3\frac{1}{13}$ days.

### Combined Rate Formula (for any number of people)
$$
\text{Total Time} = \frac{1}{\frac{1}{t_1} + \frac{1}{t_2} + \dots + \frac{1}{t_n}}
$$

**Variables:**
- $t_1, t_2, \dots, t_n$ = time taken by each individual.

**When to use:** When three or more people are working together.

**Worked example:** A (4 days), B (5 days), C (10 days).
$\text{Rate} = \frac{1}{4} + \frac{1}{5} + \frac{1}{10} = \frac{5+4+2}{20} = \frac{11}{20}$.
$\text{Time} = \frac{20}{11} = 1\frac{9}{11}$ days.

---

## Solution Framework

1. **Step 1: Identify individual rates** — Express each person's work as a fraction of the whole ($\frac{1}{\text{time}}$).
2. **Step 2: Sum the rates** — Add the fractions to find the total work completed in one unit of time.
3. **Step 3: Take the reciprocal** — Flip the resulting fraction to find the total time required for the whole task.

---

## Shortcut Tricks

* **Trick:** Use the "LCM Method" for the sum of rates.
* **Why it works:** It avoids complex fraction addition by converting all rates to a common denominator (the LCM of the times).
* **When to use:** When dealing with 3+ people or large numbers.
* **Example:** A(4), B(5), C(10). LCM of 4, 5, 10 is 20.
  A does 5 units/day, B does 4 units/day, C does 2 units/day.
  Total = 11 units/day. Time = $\frac{20}{11}$ days.

---

## Common Mistakes

* **Mistake:** Adding the number of days (e.g., $8+5=13$).
  * **Why it happens:** Intuitive but mathematically incorrect; rates are additive, not times.
  * **Fix:** Always convert to rates ($\frac{1}{t}$) before adding.
* **Mistake:** Forgetting to take the reciprocal at the end.
  * **Why it happens:** Stopping after finding the "1-day work" fraction.
  * **Fix:** Remember that the sum is the *rate*, not the *time*.

---

## Worked Example (Step-by-Step)

**Question:** A can do a work in 4 days, B in 5 days and C in 10 days. Find the time taken by A, B and C to do the work together.

**Solution:**
1. **Identify rates:** A = $\frac{1}{4}$, B = $\frac{1}{5}$, C = $\frac{1}{10}$.
2. **Sum rates:** $\frac{1}{4} + \frac{1}{5} + \frac{1}{10} = \frac{5+4+2}{20} = \frac{11}{20}$.
3. **Reciprocal:** Time = $\frac{20}{11} = 1\frac{9}{11}$ days.

**Answer:** $1\frac{9}{11}$ days.

---

## Similar Patterns

**Work with Efficiency/Ratio:** Distinguished by phrases like "A is twice as fast as B." Use the ratio of work to find individual times first, then apply the standard framework.

---

## Revision Summary

* **Key formula:** $\text{Time} = \frac{1}{\sum \text{Rates}}$.
* **Spot it by:** "Together" and individual times given.
* **First move:** Convert days to fractions ($\frac{1}{d}$).
* **Fastest method:** LCM of days to find total units of work.
* **Biggest trap:** Adding the days directly instead of the rates.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractions** — Basic addition of fractions using a common denominator.
* **Reciprocals** — The inverse of a number $n$ is $\frac{1}{n}$.
* **LCM (Least Common Multiple)** — The smallest number divisible by all given time values.

### Formulas You Must Know First
$$
\text{Work} = \text{Rate} \times \text{Time}
$$
**What it means:** The total work is the product of the speed of work and the time spent.

### Terms Used In This Pattern
* **Unit of time:** The standard duration (day, hour, minute) used to measure work rate.
* **Rate:** The portion of work completed in one unit of time.