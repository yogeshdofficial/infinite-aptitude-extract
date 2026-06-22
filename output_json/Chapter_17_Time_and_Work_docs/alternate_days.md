# Alternate Days

## Overview
This pattern involves workers who do not work together simultaneously but take turns on a rotating schedule. The central idea is to calculate the total work completed in one full "cycle" (the time it takes for the rotation to repeat) and then use that to find how many cycles fit into the total work.

---

## Recognition Clues
* **Keywords:** "alternately," "one at a time," "assisted by... on alternate days," "every third day."
* **Given:** Individual time taken by each person to complete the work alone.
* **Asked:** Total time taken to complete the whole work under the specified rotation.

---

## Key Formulas

### [Work in a Cycle]
$$
W_{cycle} = \sum (\text{Rate}_i \times \text{Days}_i)
$$

**Variables:**
- $W_{cycle}$ = Total work done in one full rotation
- $\text{Rate}_i$ = Work done by person $i$ in one day ($\frac{1}{\text{Total Days}}$)
- $\text{Days}_i$ = Number of days person $i$ works within one cycle

**When to use:** To find the "unit" of work that repeats.

**Worked example:** A (12 days) and B (18 days) work alternately.
$W_{cycle} = (\frac{1}{12} \times 1) + (\frac{1}{18} \times 1) = \frac{5}{36}$ in 2 days.

---

## Solution Framework

1. **Step 1: Calculate daily rates:** Convert each person's total days into a daily fraction (e.g., $1/n$).
2. **Step 2: Define the cycle:** Identify how many days make up one full rotation and sum the work done by each person in that cycle.
3. **Step 3: Find full cycles:** Divide the total work (1) by the cycle work ($W_{cycle}$) to find the number of full cycles.
4. **Step 4: Calculate remaining work:** Subtract the work done in full cycles from 1.
5. **Step 5: Finish the remainder:** Calculate how much time the next person(s) in the sequence need to complete the remaining fraction.

---

## Shortcut Tricks

* **Trick:** If the cycle work is a simple fraction $\frac{1}{n}$, the total time is simply $n \times (\text{days in cycle})$.
* **Why it works:** If a cycle of $D$ days completes exactly $1/n$ of the work, it takes $n$ such cycles to complete the whole work.
* **When to use:** When the sum of rates in a cycle results in a unit fraction (numerator is 1).
* **Example:** Q91: Cycle work is $\frac{1}{4}$ in 2 days. Total time = $2 \times 4 = 8$ days.

---

## Common Mistakes

* **Mistake:** Adding all rates together for every day.
    * **Why it happens:** Habit from standard "together" work problems.
    * **Fix:** Only add rates for the specific people working on that specific day of the cycle.
* **Mistake:** Forgetting the cycle length.
    * **Why it happens:** Treating the cycle as 1 day instead of 2 or 3.
    * **Fix:** Always multiply the number of cycles by the number of days in the cycle.
* **Mistake:** Miscalculating the remainder.
    * **Why it happens:** Arithmetic error in $1 - (\text{cycles} \times W_{cycle})$.
    * **Fix:** Use a common denominator for all fractions.

---

## Worked Example (Step-by-Step)

**Question:** A and B can complete a piece of work in 12 and 18 days respectively. A begins to do the work and they work alternatively one at a time for one day each. The whole work will be completed in?

**Solution:**
1. **Rates:** A = $1/12$, B = $1/18$.
2. **Cycle:** 2-day cycle. Work = $1/12 + 1/18 = 5/36$.
3. **Full Cycles:** $1 \div (5/36) = 7.2$. Take 7 full cycles.
4. **Work done:** $7 \times (5/36) = 35/36$.
5. **Remainder:** $1 - 35/36 = 1/36$.
6. **Final Step:** 14 days passed. Day 15 is A's turn. A does $1/12$ per day. Time for $1/36$ is $(1/36) \div (1/12) = 1/3$ day.
7. **Total:** $14 + 1/3 = 14\frac{1}{3}$ days.

**Answer:** $14\frac{1}{3}$ days.

---

## Similar Patterns
* **Standard Work Problems:** If the question says "A and B work together," do not use the cycle method; simply add their rates ($1/A + 1/B$).

---

## Revision Summary
* **Key formula:** $W_{cycle} = \sum (\text{Rate} \times \text{Days})$.
* **Spot it by:** The word "alternately" or "on alternate days."
* **First move:** Calculate the work done in one full rotation cycle.
* **Fastest method:** Find full cycles, then calculate the time for the remaining fraction.
* **Biggest trap:** Forgetting that the cycle length is usually $>1$ day.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Work Rate** — The portion of work completed in one unit of time (day/hour), calculated as $1/n$ where $n$ is the total time.
* **Fractions** — Ability to add and subtract fractions with different denominators.

### Formulas You Must Know First
$$
\text{Work} = \text{Rate} \times \text{Time}
$$
**What it means:** Total work is the product of how fast you work and how long you work.

### Terms Used In This Pattern
* **Cycle** — The sequence of days after which the work pattern repeats.
* **Remainder** — The portion of work left after completing the maximum possible number of full cycles.