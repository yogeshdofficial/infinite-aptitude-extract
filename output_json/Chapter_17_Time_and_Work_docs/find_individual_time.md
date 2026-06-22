# Find Individual Time

## Overview
This pattern involves determining the time taken by an individual to complete a task when given the combined time of a group and the individual times of others. The central idea is to treat work as a rate (1/time) and subtract the known rates from the total combined rate.

---

## Recognition Clues
* **Keywords:** "A and B together," "alone," "with the help of," "finish in X days."
* **Given:** Combined time of two or more people; individual time of one or more of them.
* **Asked:** Time taken by the remaining person(s) working alone.
* **Context:** Often involves calculating shares of a total payment based on work done.

---

## Key Formulas

### [Individual Rate Formula]
$$
\text{Rate}_{\text{Individual}} = \text{Rate}_{\text{Total}} - \text{Rate}_{\text{Others}}
$$

**Variables:**
- $\text{Rate}_{\text{Individual}}$ = Work done by the person in 1 day
- $\text{Rate}_{\text{Total}}$ = Combined work done by the group in 1 day
- $\text{Rate}_{\text{Others}}$ = Sum of work done by known individuals in 1 day

**When to use:** When you need to isolate the work rate of one person from a group.

**Worked example:** If A+B take 15 days ($\frac{1}{15}$) and B takes 20 days ($\frac{1}{20}$), A's rate = $\frac{1}{15} - \frac{1}{20} = \frac{1}{60}$.

---

## Solution Framework

1. **Convert time to rate:** Express each given time as a fraction ($\frac{1}{\text{days}}$) to represent 1-day work.
2. **Set up the equation:** Subtract the known individual rates from the combined group rate.
3. **Solve for the unknown rate:** Perform the fraction subtraction to find the 1-day work of the missing person.
4. **Convert back to time:** Take the reciprocal of the resulting fraction to get the total days required.
5. **Distribute shares (if applicable):** If money is involved, divide the total payment in the ratio of the individual 1-day work rates.

---

## Shortcut Tricks

* **Trick:** For two people (A+B) and (B), A's time = $\frac{\text{Time}_A \times \text{Time}_B}{\text{Time}_B - \text{Time}_A}$.
* **Why it works:** This is the algebraic simplification of $\frac{1}{x} = \frac{1}{A} - \frac{1}{B}$.
* **When to use it:** Only when exactly two people are involved and you have the combined time and one individual time.
* **Example:** Q2: A+B=15, B=20. A = $\frac{15 \times 20}{20 - 15} = \frac{300}{5} = 60$ days.

---

## Common Mistakes

* **Mistake:** Adding rates instead of subtracting. **Fix:** Always subtract the known part from the whole.
* **Mistake:** Distributing money based on time taken. **Fix:** Always distribute money based on the ratio of work done (1-day rates).
* **Mistake:** Forgetting to divide by 2 in "A+B, B+C, C+A" problems. **Fix:** Remember that adding these pairs counts each person twice, so divide the sum by 2.

---

## Worked Example (Step-by-Step)

**Question:** A and B together can complete a piece of work in 15 days and B alone in 20 days. In how many days can A alone complete the work?

**Solution:**
1. **Convert to rates:** (A+B)'s rate = $\frac{1}{15}$; B's rate = $\frac{1}{20}$.
2. **Subtract:** A's rate = $\frac{1}{15} - \frac{1}{20}$.
3. **Solve:** Common denominator is 60. $\frac{4}{60} - \frac{3}{60} = \frac{1}{60}$.
4. **Convert to time:** Reciprocal of $\frac{1}{60}$ is 60.

**Answer:** 60 days.

---

## Similar Patterns

**Work-Efficiency Patterns:** If the question mentions "A is twice as efficient as B," use the ratio of efficiencies rather than just subtracting rates.

---

## Revision Summary

* **Key formula:** $\text{Rate}_{\text{Individual}} = \text{Rate}_{\text{Total}} - \text{Rate}_{\text{Others}}$.
* **Spot it by:** Combined time given, one individual time missing.
* **First move:** Convert all days to fractions ($\frac{1}{n}$).
* **Fastest method:** Use the product/difference shortcut for two-person problems.
* **Biggest trap:** Distributing payment by time instead of work rate.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Work Rate** — The amount of work completed in one unit of time (e.g., 1 day).
* **Reciprocals** — If a person does $\frac{1}{n}$ work in 1 day, they take $n$ days to finish.

### Formulas You Must Know First
$$
\text{Work} = \text{Rate} \times \text{Time}
$$
**What it means:** Total work is the product of the speed of work and the time spent.

### Terms Used In This Pattern
* **1-day work** — The standard unit of measurement for work rate.
* **Share** — The portion of total payment proportional to the work done.