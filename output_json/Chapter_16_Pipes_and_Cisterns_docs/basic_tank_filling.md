# Basic Tank Filling

## Overview
This pattern involves multiple pipes (inlets and outlets) working simultaneously to fill or empty a tank. The central idea is to calculate the **net rate** of work by adding the rates of inlet pipes and subtracting the rates of outlet pipes.

---

## Recognition Clues
* **Keywords:** "inlet pipe," "exhaust pipe," "waste pipe," "cistern," "fill," "empty."
* **Given:** Individual times taken by pipes to fill or empty a tank.
* **Asked:** Total time taken to fill/empty the tank when multiple pipes are open, or the rate of a specific pipe.
* **Visual:** Look for a mix of "filling" and "emptying" actions in the same problem.

---

## Key Formulas

### Net Rate of Work
$$
\text{Net Rate} = \sum (\text{Inlet Rates}) - \sum (\text{Outlet Rates})
$$
**Variables:**
- $\text{Inlet Rate} = \frac{1}{\text{Time to fill}}$
- $\text{Outlet Rate} = \frac{1}{\text{Time to empty}}$

**When to use:** When multiple pipes are operating simultaneously.

**Worked example:** Pipe A fills in 4 hrs, Pipe C empties in 8 hrs. Net rate = $\frac{1}{4} - \frac{1}{8} = \frac{1}{8}$ tank per hour.

### Time to Complete
$$
\text{Time} = \frac{1}{\text{Net Rate}}
$$
**Variables:**
- $\text{Net Rate}$ = The combined work done per unit time.

**When to use:** To find the total duration once the net rate is known.

**Worked example:** If net rate is $\frac{1}{8}$ tank/hr, Time = $\frac{1}{1/8} = 8$ hours.

---

## Solution Framework

1. **Step 1: Standardize Units** — Ensure all times are in the same unit (e.g., convert hours to minutes if necessary).
2. **Step 2: Define Rates** — Express each pipe's work as a fraction of the tank per unit time (e.g., $1/x$).
3. **Step 3: Assign Signs** — Assign a positive sign (+) to inlet pipes and a negative sign (-) to outlet/waste pipes.
4. **Step 4: Calculate Net Rate** — Sum the fractions to find the total work done per unit time.
5. **Step 5: Find Total Time** — Take the reciprocal of the net rate to get the final time.

---

## Shortcut Tricks

* **Trick:** For two pipes filling a tank, use $\frac{xy}{x+y}$.
* **Why it works:** It is the algebraic simplification of $\frac{1}{1/x + 1/y}$.
* **When to use:** Only when there are exactly two inlet pipes and no outlets.
* **Example:** Pipe A (30h), Pipe B (45h). Time = $\frac{30 \times 45}{30 + 45} = \frac{1350}{75} = 18$ hours.

---

## Common Mistakes

* **Mistake:** Adding the rate of an outlet pipe.
    * **Fix:** Always subtract the rate of any pipe that empties the tank.
* **Mistake:** Adding times instead of rates (e.g., $30+45=75$).
    * **Fix:** Always convert time to rate ($1/T$) before adding or subtracting.
* **Mistake:** Unit mismatch (e.g., mixing hours and minutes).
    * **Fix:** Convert everything to the smallest unit mentioned in the question before starting.

---

## Worked Example (Step-by-Step)

**Question:** A cistern can be filled by pipes A and B in 4 hours and 6 hours respectively. When full, the cistern can be emptied by pipe C in 8 hours. If all the pipes were turned on at the same time, in how much time will the cistern be filled?

**Solution:**
1. **Rates:** A = $1/4$, B = $1/6$, C = $-1/8$ (C is an outlet).
2. **Net Rate:** $\frac{1}{4} + \frac{1}{6} - \frac{1}{8}$.
3. **Common Denominator (24):** $\frac{6}{24} + \frac{4}{24} - \frac{3}{24} = \frac{7}{24}$.
4. **Time:** Reciprocal of $\frac{7}{24}$ is $\frac{24}{7}$ hours.

**Answer:** $3\frac{3}{7}$ hours.

---

## Similar Patterns
**Work and Wages:** Distinguishable because "Work and Wages" involves people/machines completing a task, whereas this pattern specifically involves volume/capacity and "inlet/outlet" terminology.

---

## Revision Summary
* **Key formula:** $\text{Net Rate} = \sum \text{Inlets} - \sum \text{Outlets}$.
* **Spot it by:** Presence of "inlet" and "exhaust/waste" pipes.
* **First move:** Convert all times to unit rates ($1/T$).
* **Fastest method:** Use the reciprocal of the net rate.
* **Biggest trap:** Adding the rate of an outlet pipe instead of subtracting it.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractions:** Adding and subtracting fractions using a common denominator.
* **Reciprocals:** Understanding that if a pipe fills a tank in $T$ hours, it fills $1/T$ of the tank in 1 hour.

### Formulas You Must Know First
* **Rate Formula:** $\text{Rate} = \frac{\text{Work}}{\text{Time}}$.

### Terms Used In This Pattern
* **Inlet:** A pipe that adds water to the tank.
* **Outlet/Exhaust/Waste:** A pipe that removes water from the tank.
* **Cistern:** A tank used for storing water.