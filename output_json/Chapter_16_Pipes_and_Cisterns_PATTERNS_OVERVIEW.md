# Pipes And Cisterns — Chapter Overview

## What This Chapter Is About

This chapter deals with the mathematical relationship between the rates at which different pipes fill or empty a container. The central quantity in every problem is the "work rate"—the fraction of the tank's total capacity that a pipe can process in a single unit of time (like one hour or one minute). By calculating these individual rates and combining them, you can determine how long it takes for various combinations of pipes to fill or empty a tank under different conditions.

---

## Core Concepts

**[Work Rate as a Fraction]** — Since the total capacity of a tank is often unknown, we treat the entire tank as "1 unit." If a pipe fills a tank in $x$ hours, its work rate is $\frac{1}{x}$ of the tank per hour. For example, if a pipe fills a tank in 5 hours, it completes $\frac{1}{5}$ of the job every hour.

**[Inlet vs. Outlet]** — Pipes are categorized by their function: an "inlet" adds water (positive work), while an "outlet" or "leak" removes water (negative work). When calculating the net effect of multiple pipes, you must add the rates of inlets and subtract the rates of outlets.

**[Net Efficiency]** — This is the combined rate of all active pipes. If you have an inlet working at $\frac{1}{A}$ and an outlet working at $\frac{1}{B}$, the net rate is $\frac{1}{A} - \frac{1}{B}$. If the result is positive, the tank is filling; if negative, it is emptying.

**[Time-Efficiency Inverse Relationship]** — The time taken to complete a task is inversely proportional to the rate of work. If you double the efficiency of a pipe (e.g., by doubling its diameter), you halve the time required to fill the tank.

---

## Key Terms Glossary

**Inlet** — A pipe that pours water into a tank, contributing to the total volume.

**Outlet (or Waste Pipe)** — A pipe that drains water out of a tank, reducing the total volume.

**Cistern** — A technical term for a tank or reservoir used for storing water.

**Capacity** — The total volume of the tank, usually represented as "1" in fractional calculations or a common multiple of the time values in efficiency-based calculations.

---

## Pattern Map

**Basic Tank Filling** (9 questions) — The standard scenario where you calculate the combined time for multiple pipes to fill or empty a tank from scratch.

**Partial Operation** (5 questions) — The scenario where pipes are turned on or off at different times, or the tank starts with a specific amount of water already inside.

**Efficiency Variations** (2 questions) — The scenario where the physical properties of the pipes (like diameter) change, or the work rate is affected by external factors like leaks.

---

## Core Formulas

### Net Work Rate
$$
\text{Net Rate} = \sum (\text{Inlet Rates}) - \sum (\text{Outlet Rates})
$$
**Variables:**
- $\text{Inlet Rates}$ = $\frac{1}{\text{time taken by each inlet}}$
- $\text{Outlet Rates}$ = $\frac{1}{\text{time taken by each outlet}}$

**When to use:** Whenever multiple pipes are operating simultaneously.

**Key insight:** Always assign a negative sign to the outlet rate; forgetting this is the most common error.

**Worked example:** If Pipe A fills in 4 hours and Pipe B empties in 6 hours, Net Rate = $\frac{1}{4} - \frac{1}{6} = \frac{1}{12}$ tank per hour.

---

## Suggested Study Order

1. **Basic Tank Filling** — Start here to master the fundamental concept of adding and subtracting work rates.
2. **Partial Operation** — Study next because it requires you to track the "state" of the tank (how much is filled) at different time intervals.
3. **Efficiency Variations** — Study last as it introduces external variables (like pipe diameter) that modify the base work rates learned in the first two sections.

---

## Chapter-Wide Traps

**Ignoring the "Emptying" Sign:** Treating an outlet pipe as an inlet pipe in your equation → Always subtract the outlet rate from the total.

**Confusing Time with Rate:** Assuming that if two pipes take 10 and 20 hours, they take 15 hours together (the average) → Always add the rates ($\frac{1}{10} + \frac{1}{20}$), not the times.

**Units Mismatch:** Mixing hours and minutes in the same calculation → Always convert all time values to the same unit (e.g., all into hours or all into minutes) before starting the calculation.