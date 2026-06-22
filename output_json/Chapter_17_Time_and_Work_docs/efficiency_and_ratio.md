# Efficiency and Ratio

## Overview
This pattern involves problems where workers have different speeds or "efficiencies" relative to one another. The central idea is to convert these efficiency ratios into a common unit (like "units of work per day") to calculate the total work and individual time taken.

---

## Recognition Clues
* **Keywords:** "twice as good," "thrice as much time," "X% more efficient," "speeds in the ratio."
* **Given:** A relationship between the speeds/efficiencies of two or more people, and the time taken by one or all of them.
* **Asked:** The time taken by one person to complete the work alone.

---

## Key Formulas

### [Efficiency-Time Inverse Relationship]
$$
\text{Time}_A : \text{Time}_B = \text{Efficiency}_B : \text{Efficiency}_A
$$
**Variables:**
- $\text{Time}_A, \text{Time}_B$ = Time taken by A and B respectively.
- $\text{Efficiency}_A, \text{Efficiency}_B$ = Work rate of A and B respectively.

**When to use:** When given a comparison of efficiency and asked for time.

**Worked example:** If A is twice as efficient as B (Ratio 2:1), the time ratio is 1:2. If A takes 12 days, B takes $12 \times 2 = 24$ days.

---

## Solution Framework

1. **Define Rates:** Assign a variable or unit value to the efficiency of each person based on the given ratio.
2. **Calculate Combined Rate:** Sum the individual rates to find the "total units per day" when working together.
3. **Find Total Work:** Multiply the combined rate by the total time given for the group to finish the job.
4. **Calculate Individual Time:** Divide the Total Work by the specific person's individual rate.

---

## Shortcut Tricks

* **Trick:** If $A$ is $n$ times as efficient as $B$, and they finish in $T$ days, $B$ alone takes $T(n+1)$ days.
* **Why it works:** $B$'s rate is $1$ unit, $A$'s is $n$ units, combined is $(n+1)$. Total work is $(n+1)T$. Time for $B = \frac{(n+1)T}{1}$.
* **Example:** A is twice as good as B ($n=2$), together they take 18 days ($T=18$). B takes $18(2+1) = 54$ days.

---

## Common Mistakes

* **Mistake:** Assuming time ratio is the same as efficiency ratio.
    * **Why it happens:** Forgetting that speed and time are inversely proportional.
    * **Fix:** Always invert the efficiency ratio to get the time ratio.
* **Mistake:** Adding the times taken by individuals to find the total time.
    * **Why it happens:** Confusing time with work rates.
    * **Fix:** Always add work rates (reciprocals of time), never add the times themselves.

---

## Worked Example (Step-by-Step)

**Question:** A is twice as good a workman as B and together they finish a piece of work in 18 days. In how many days will A alone finish the work?

**Solution:**
1. **Define Rates:** B's rate = 1 unit/day. A's rate = 2 units/day.
2. **Calculate Combined Rate:** $1 + 2 = 3$ units/day.
3. **Find Total Work:** $3 \text{ units/day} \times 18 \text{ days} = 54$ units.
4. **Calculate Individual Time:** A's time = $\frac{\text{Total Work}}{\text{A's Rate}} = \frac{54}{2} = 27$ days.

**Answer:** 27 days.

---

## Similar Patterns
* **Work-Time-Person:** If the question gives specific days for each person without comparing their "efficiency" (e.g., "A does in 10, B in 15"), use the LCM method for total work instead of ratios.

---

## Revision Summary
* **Key formula:** $\text{Time} \propto \frac{1}{\text{Efficiency}}$.
* **Spot it by:** Phrases like "twice as good" or "efficiency ratio."
* **First move:** Assign a unit rate to the slowest person.
* **Fastest method:** Use the shortcut $T(n+1)$ for two-person efficiency problems.
* **Biggest trap:** Adding times instead of adding rates.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Inverse Proportion** — When one value increases, the other decreases at the same rate.
* **Work Rate** — The amount of work completed in one unit of time (e.g., 1 day).

### Formulas You Must Know First
$$
\text{Total Work} = \text{Rate} \times \text{Time}
$$
**What it means:** The total job is the product of how fast you work and how long you work.
**Example:** If you work at 5 units/day for 4 days, total work is 20 units.

### Terms Used In This Pattern
* **Efficiency** — The rate at which work is performed.
* **Workman** — A person performing the task.