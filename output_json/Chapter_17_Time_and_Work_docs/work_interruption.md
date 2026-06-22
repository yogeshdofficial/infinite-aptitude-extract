# Work Interruption

## Overview
This pattern involves tasks where workers start together, but one or more individuals leave or join at specific points in time. The central idea is to isolate the work done by each person during their active period and solve for the remaining work or time.

---

## Recognition Clues
* **Keywords:** "leaves after X days," "X days before completion," "finished the remaining work in Y days."
* **Given:** Individual capacities (days to complete work) and specific interruption points (days worked or days before finish).
* **Asked:** Total time taken to complete the work or the specific day a worker left.

---

## Key Formulas

### Individual Work Rate
$$
\text{Rate} = \frac{1}{\text{Time taken to complete total work}}
$$
**Variables:** Rate = fraction of work done in 1 day.
**When to use:** To convert "days to complete" into a usable daily work unit.
**Example:** If A takes 80 days, Rate = $\frac{1}{80}$.

### Combined Work Rate
$$
\text{Combined Rate} = \text{Rate}_A + \text{Rate}_B + \dots
$$
**Variables:** Rate = individual daily work rates.
**When to use:** When multiple people work simultaneously.
**Example:** (A+B) rate = $\frac{1}{80} + \frac{1}{48} = \frac{8}{240} = \frac{1}{30}$.

---

## Solution Framework

1. **Calculate individual rates:** Convert all "days to complete" into daily work fractions.
2. **Identify fixed work segments:** Calculate the work done by individuals working alone (e.g., the last few days before completion).
3. **Subtract from total:** Subtract the work done in fixed segments from the total work (1) to find the "remaining work."
4. **Equate to combined rate:** Divide the remaining work by the combined rate of the people working during that interval to find the duration of that interval.
5. **Sum the time:** Add the durations of all segments to get the total time.

---

## Shortcut Tricks

* **Trick:** If someone leaves $n$ days before completion, *add* the work they *would have done* in those $n$ days to the total work, then divide by the combined rate of all workers.
* **Why it works:** It treats the work as if no one left, effectively "filling in" the gap.
* **When to use:** When a worker leaves a fixed number of days *before the end*.
* **Example:** Q12 (A leaves 2 days before end). Total work = $1 + (\text{A's rate} \times 2)$. Divide by (A+B)'s rate.

---

## Common Mistakes

* **Mistake:** Adding the number of days (e.g., 80+48) instead of adding work rates.
    * **Fix:** Always add rates ($\frac{1}{A} + \frac{1}{B}$), never add the days directly.
* **Mistake:** Forgetting that "X days before completion" means the other person worked alone for those X days.
    * **Fix:** Always subtract the "alone" work from the total (1) first.
* **Mistake:** Miscalculating the duration of the "middle" phase.
    * **Fix:** Use a variable $x$ for total time if multiple people leave at different times (as in Q13).

---

## Worked Example (Step-by-Step)

**Question:** A can do a piece of work in 10 days and B in 20 days. They work together but 2 days before the completion of the work, A leaves. In how many days was the work completed?

**Solution:**
1. **Rates:** A = $\frac{1}{10}$, B = $\frac{1}{20}$.
2. **Fixed Segment:** A leaves 2 days before the end, so B works alone for 2 days. B's work = $2 \times \frac{1}{20} = \frac{1}{10}$.
3. **Remaining Work:** $1 - \frac{1}{10} = \frac{9}{10}$.
4. **Combined Rate:** A + B = $\frac{1}{10} + \frac{1}{20} = \frac{3}{20}$.
5. **Time for segment:** $\frac{9}{10} \div \frac{3}{20} = \frac{9}{10} \times \frac{20}{3} = 6$ days.
6. **Total Time:** $6 \text{ (together)} + 2 \text{ (B alone)} = 8$ days.

**Answer:** 8 days.

---

## Similar Patterns
* **Work-Efficiency Patterns:** Distinguished by "A is twice as fast as B" rather than "A leaves after X days."

---

## Revision Summary
* **Key formula:** $\text{Rate} = \frac{1}{\text{Time}}$.
* **Spot it by:** "Leaves," "joins," or "before completion" phrases.
* **First move:** Convert all times to daily work rates ($\frac{1}{n}$).
* **Fastest method:** Subtract "alone" work from 1, then divide by combined rate.
* **Biggest trap:** Adding days instead of rates.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractions:** Basic arithmetic with fractions (addition/subtraction).
* **Work-Rate Relationship:** Work = Rate $\times$ Time.

### Formulas You Must Know First
$$
\text{Total Work} = 1
$$
**What it means:** The entire task is represented as 1 unit.

### Terms Used In This Pattern
* **Rate:** The portion of work completed in one unit of time (day/hour).
* **Remaining Work:** The portion of the task left after specific segments are completed.