# Partial Operation

## Overview
This pattern involves tanks that are not empty at the start or pipes that are turned on/off at different times. The central idea is to equate the **net work done** by all active pipes over their respective durations to the **total capacity** (or the specific fraction of the tank) to be filled or emptied.

---

## Recognition Clues
* **Keywords:** "already two-fifths full," "closed 6 minutes before," "opened at the instant," "tank is half filled."
* **Given:** Individual rates of pipes, specific time offsets (e.g., "closed $x$ minutes before"), or initial volume states.
* **Asked:** Total time taken to fill/empty the tank or the time a specific pipe was active.

---

## Key Formulas

### [Time-Work Equation]
$$
\sum (\text{Rate}_i \times \text{Time}_i) = \text{Work Done}
$$

**Variables:**
- $\text{Rate}_i$: The fraction of the tank filled/emptied by pipe $i$ per minute (positive for inlet, negative for outlet).
- $\text{Time}_i$: The duration pipe $i$ was open.
- $\text{Work Done}$: The total fraction of the tank filled (usually 1) or the specific fraction to be emptied.

**When to use:** When pipes are opened or closed at different times.

**Worked example:** If Pipe A (rate $\frac{1}{12}$) and B (rate $\frac{1}{15}$) work for $x$ mins, and C (rate $-\frac{1}{20}$) works for $(x-6)$ mins to fill a tank: $\frac{x}{12} + \frac{x}{15} - \frac{x-6}{20} = 1$.

---

## Solution Framework

1. **Define the variable:** Let $x$ be the total time taken to fill/empty the tank.
2. **Assign rates:** Convert each pipe's time to a rate (e.g., 12 mins $\rightarrow \frac{1}{12}$ per min). Use negative signs for outlet pipes.
3. **Map durations:** Identify how long each pipe was active in terms of $x$ (e.g., if closed 6 mins early, time is $x-6$).
4. **Set up the equation:** Sum the work done by each pipe ($\text{Rate} \times \text{Time}$) and equate to the target volume (1 for full, or the specific fraction given).
5. **Solve for $x$:** Use basic algebra to isolate the variable.

---

## Shortcut Tricks
**No shortcut faster than the standard framework** — the algebraic setup is the most reliable method for varying start/stop times.

---

## Common Mistakes
* **Mistake:** Using $x+6$ instead of $x-6$ for a pipe closed early.
    * **Why it happens:** Confusing "before" with "after."
    * **Fix:** If a pipe stops early, it works for less time than the total duration ($x - \text{time}$).
* **Mistake:** Forgetting to subtract the outlet pipe's rate.
    * **Why it happens:** Focusing only on the filling pipes.
    * **Fix:** Always assign a negative sign to any pipe that empties the tank.
* **Mistake:** Using the full tank capacity when the tank is already partially filled.
    * **Why it happens:** Ignoring the initial state.
    * **Fix:** Subtract the initial volume from the target (1) before setting up the equation.

---

## Worked Example (Step-by-Step)

**Question:** Two pipes A and B can fill a tank in 12 and 15 minutes. Pipe C can empty it in 20 minutes. All are opened, but C is closed 6 minutes before the tank is full. In what time will the tank be full?

**Solution:**
1. **Define:** Let total time be $x$.
2. **Rates:** A = $\frac{1}{12}$, B = $\frac{1}{15}$, C = $-\frac{1}{20}$.
3. **Durations:** A and B work for $x$ mins. C works for $(x-6)$ mins.
4. **Equation:** $\frac{x}{12} + \frac{x}{15} - \frac{x-6}{20} = 1$.
5. **Solve:** Multiply by 60: $5x + 4x - 3(x-6) = 60 \Rightarrow 9x - 3x + 18 = 60 \Rightarrow 6x = 42 \Rightarrow x = 7$.

**Answer:** 7 minutes.

---

## Similar Patterns
**Standard Work/Time:** If all pipes are open for the same duration, use the simple $\frac{1}{A} + \frac{1}{B} - \frac{1}{C}$ formula. This pattern is distinct because of the **variable durations** (pipes starting/stopping at different times).

---

## Revision Summary
* **Key formula:** $\sum (\text{Rate} \times \text{Time}) = \text{Work}$.
* **Spot it by:** Pipes closing/opening at different times or partial initial fill.
* **First move:** Define total time as $x$ and express each pipe's active time as $x$ or $x \pm \text{offset}$.
* **Fastest method:** Algebraic equation based on work done.
* **Biggest trap:** Forgetting to subtract the outlet pipe's rate or miscalculating the time offset.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Rate of Work:** If a pipe fills a tank in $T$ hours, its rate is $\frac{1}{T}$ per hour.
* **Net Rate:** When multiple pipes work, the net rate is the sum of individual rates (inlets positive, outlets negative).

### Formulas You Must Know First
$$
\text{Time} = \frac{\text{Work}}{\text{Rate}}
$$
**What it means:** The time taken is the total work divided by the rate of work.

### Terms Used In This Pattern
* **Inlet:** A pipe that fills the tank.
* **Outlet:** A pipe that empties the tank.
* **Cistern:** Another word for a tank or reservoir.