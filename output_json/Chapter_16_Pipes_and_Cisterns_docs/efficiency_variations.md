# Efficiency Variations

## Overview
These questions involve pipes with varying diameters or relative efficiency levels (e.g., "A is twice as efficient as B"). The central idea is that **Time is inversely proportional to Efficiency**, and for pipes, **Efficiency is proportional to the square of the diameter ($d^2$)**.

---

## Recognition Clues
* **Keywords:** "diameter twice as much," "twice as efficient," "inlet/outlet," "plugged."
* **Given:** Relative diameters or relative efficiency ratios between pipes.
* **Asked:** Time taken to fill/empty the tank when pipes are used in different combinations.

---

## Key Formulas

### Efficiency and Diameter
$$
\text{Rate}_1 : \text{Rate}_2 = d_1^2 : d_2^2
$$
**Variables:** $d$ = diameter of the pipe.
**When to use:** When comparing two pipes based on their physical size.
**Example:** If $d_2 = 2d_1$, then $\text{Rate}_2 = (2)^2 \times \text{Rate}_1 = 4 \times \text{Rate}_1$.

### Time and Efficiency
$$
\text{Time} = \frac{\text{Total Capacity}}{\text{Net Efficiency}}
$$
**Variables:** $\text{Capacity}$ = total units, $\text{Net Efficiency}$ = sum of rates (inlet = $+$, outlet = $-$).
**When to use:** To find the final time after determining individual rates.
**Example:** If Capacity = 80 units and Net Efficiency = 3 units/hr, Time = $\frac{80}{3} = 26\frac{2}{3}$ hours.

---

## Solution Framework
1. **Assign Units:** Assign an efficiency value (e.g., 1 unit/hr) to the least efficient pipe.
2. **Calculate Rates:** Determine the efficiency of all other pipes based on the given ratios or diameter squares.
3. **Find Capacity:** Multiply the efficiency of a pipe by the time it takes to complete the task (if given).
4. **Calculate Net Rate:** Add the efficiencies of inlet pipes and subtract the efficiencies of outlet pipes.
5. **Solve for Time:** Divide the Total Capacity by the Net Rate.

---

## Shortcut Tricks
* **Trick:** If Pipe B is $n$ times as efficient as Pipe A, then Time B = $\frac{1}{n} \times$ Time A.
* **Why it works:** Efficiency and Time are inversely proportional.
* **When to use:** When you need to quickly find the time of one pipe given the time of another.
* **Example:** If Pipe A takes 40 mins and Pipe B has double the diameter ($d^2=4$), Pipe B takes $\frac{40}{4} = 10$ mins.

---

## Common Mistakes
* **Mistake:** Assuming Rate $\propto$ Diameter. **Fix:** Rate $\propto$ Diameter$^2$.
* **Mistake:** Adding diameters instead of rates. **Fix:** Always convert to rates (units/hr) before adding/subtracting.
* **Mistake:** Forgetting to subtract outlet pipe efficiency. **Fix:** Always mark outlet pipes with a negative sign.

---

## Worked Example (Step-by-Step)

**Question:** A pipe can empty a tank in 40 minutes. A second pipe with diameter twice as much as that of the first is also attached to empty it. How much time will the two pipes together take to empty the tank?

**Solution:**
1. **Assign Rates:** Let Pipe 1 rate = $1$ unit/min. Since Pipe 2 has $2\times$ diameter, its rate = $2^2 = 4$ units/min.
2. **Find Capacity:** Pipe 1 empties in 40 mins at 1 unit/min, so Total Capacity = $40 \times 1 = 40$ units.
3. **Calculate Net Rate:** Both are emptying, so Net Rate = $1 + 4 = 5$ units/min.
4. **Solve for Time:** Time = $\frac{\text{Capacity}}{\text{Net Rate}} = \frac{40}{5} = 8$ minutes.

**Answer:** 8 minutes.

---

## Similar Patterns
**Work-Time Efficiency:** Distinguish by looking for "diameter" or "cross-section" keywords; if absent, it is a standard work-time problem.

---

## Revision Summary
* **Key formula:** $\text{Rate} \propto d^2$ and $\text{Time} = \frac{\text{Capacity}}{\text{Rate}}$.
* **Spot it by:** Mentions of "diameter" or "efficiency ratios."
* **First move:** Convert all pipes to a common unit rate (e.g., units/hr).
* **Fastest method:** Use the inverse relationship between efficiency and time.
* **Biggest trap:** Treating diameter as a linear multiplier for rate.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Inverse Proportion** — As one value increases, the other decreases at the same rate.
* **Efficiency** — The amount of work done per unit of time.

### Formulas You Must Know First
$$
\text{Work} = \text{Efficiency} \times \text{Time}
$$
**What it means:** Total work is the product of the rate of work and the time spent.

### Terms Used In This Pattern
* **Inlet** — A pipe that adds volume to the tank (positive rate).
* **Outlet** — A pipe that removes volume from the tank (negative rate).