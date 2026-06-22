# Complex Journeys

## Overview
These questions involve journeys split into segments with different speeds, or scenarios where multiple events (leaks, pumps, return trips) occur simultaneously. The central idea is to equate the **total time** spent by all components or to set up a **time-balance equation** based on the distance covered.

---

## Recognition Clues
* **Keywords:** "rest of the distance," "springs a leak," "turns back," "meeting at," "going by cycle and coming back by scooter."
* **Given:** Multiple speeds, partial distances, or rates of accumulation/depletion (leaks/pumps).
* **Asked:** Total distance, required speed, or time taken for a specific mode of transport.
* **Scan for:** "Same time" (implies $T_A = T_B$) or "Total time" (implies $T_1 + T_2 = T_{total}$).

---

## Key Formulas

### Time-Distance Balance
$$
\frac{D_1}{S_1} + \frac{D_2}{S_2} = T_{total}
$$
**Variables:** $D_n$ = distance of segment $n$, $S_n$ = speed of segment $n$, $T_{total}$ = total time.
**When to use:** When a journey is broken into parts with different speeds.
**Example:** $D_1 = \frac{2}{3}x, S_1 = 4, D_2 = \frac{1}{3}x, S_2 = 5, T = \frac{7}{5} \text{ hr} \rightarrow \frac{2x/3}{4} + \frac{x/3}{5} = \frac{7}{5}$.

### Net Rate of Accumulation
$$
R_{net} = R_{in} - R_{out}
$$
**Variables:** $R_{in}$ = rate of water entering, $R_{out}$ = rate of water pumped out.
**When to use:** When a vessel is leaking while being emptied.
**Example:** $R_{in} = \frac{9}{22} \text{ tonnes/min}, R_{out} = \frac{1}{5} \text{ tonnes/min} \rightarrow R_{net} = \frac{9}{22} - \frac{1}{5} = \frac{23}{110} \text{ tonnes/min}$.

---

## Solution Framework
1. **Standardize Units:** Convert all times to hours (or minutes) and all rates to consistent units (e.g., tonnes/min).
2. **Define Variables:** Assign $x$ to the unknown (distance or speed).
3. **Set up Time Equation:** Express time for each segment as $\frac{\text{Distance}}{\text{Speed}}$.
4. **Equate/Sum:** If the journey is sequential, sum the times; if two people meet, equate their times.
5. **Solve for $x$:** Use algebraic simplification to find the unknown.

---

## Shortcut Tricks
* **Trick:** When two people start at the same time and meet, the ratio of their distances equals the ratio of their speeds.
* **Why it works:** Since $T = \frac{D}{S}$ and $T$ is constant, $\frac{D_1}{S_1} = \frac{D_2}{S_2} \Rightarrow \frac{D_1}{D_2} = \frac{S_1}{S_2}$.
* **Example:** In Q20, B travels 72 km while A travels 48 km. Ratio $D_B:D_A = 72:48 = 3:2$. Thus, $S_B:S_A = 3:2$. If $S_B = S_A + 4$, then $3x = 2(x+4) \Rightarrow x=8$.

---

## Common Mistakes
* **Mistake:** Forgetting the return trip distance in "meeting" problems.
    * **Fix:** Always draw a line diagram; if B turns back, $D_B = \text{Total} + \text{Return distance}$.
* **Mistake:** Mixing units (e.g., tonnes/hour vs tonnes/minute).
    * **Fix:** Convert everything to the smallest unit (usually minutes) before calculating $R_{net}$.
* **Mistake:** Calculating $2C$ (two-way cycle) as $C$ (one-way cycle).
    * **Fix:** Clearly label variables as "one-way" or "round-trip" time.

---

## Worked Example (Step-by-Step)

**Question:** Two boys A and B start at the same time to ride from Delhi to Meerut, 60 km away. A travels 4 km/hr slower than B. B reaches Meerut and at once turns back meeting A 12 km from Meerut. Find A’s speed.

**Solution:**
1. **Identify Distances:** B travels to Meerut (60 km) + back (12 km) = 72 km. A travels 60 - 12 = 48 km.
2. **Define Speeds:** Let A's speed = $x$. Then B's speed = $x + 4$.
3. **Set up Equation:** Since they start and meet at the same time, $T_A = T_B$.
4. **Calculate:** $\frac{48}{x} = \frac{72}{x+4}$.
5. **Solve:** $48(x+4) = 72x \Rightarrow 48x + 192 = 72x \Rightarrow 24x = 192 \Rightarrow x = 8$.

**Answer:** A's speed is 8 km/hr.

---

## Similar Patterns
**Relative Speed Problems:** Distinguished by objects moving toward/away from each other without complex "leak" or "multi-segment" constraints; use $S_{rel} = S_1 \pm S_2$ directly.

---

## Revision Summary
* **Key formula:** $\frac{D_1}{S_1} + \frac{D_2}{S_2} = T_{total}$ or $T_A = T_B$.
* **Spot it by:** Multiple segments, leaks, or return-trip meetings.
* **First move:** Standardize all units to hours or minutes.
* **Fastest method:** Use distance ratios for "meeting" problems.
* **Biggest trap:** Forgetting the return distance in meeting problems.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Algebraic Equations** — Solving for $x$ in linear equations.
* **Relative Speed** — $S_1 + S_2$ (opposite) or $S_1 - S_2$ (same direction).
* **Unit Conversion** — $1 \text{ hr} = 60 \text{ min}$; $1 \text{ km/hr} = \frac{5}{18} \text{ m/s}$.

### Formulas You Must Know First
$$
\text{Time} = \frac{\text{Distance}}{\text{Speed}}
$$
**What it means:** The fundamental relationship between motion variables.
**Example:** To cover 100 km at 50 km/hr, time = $\frac{100}{50} = 2 \text{ hours}$.

### Terms Used In This Pattern
* **Leak Rate** — The speed at which a container loses or gains volume.
* **Meeting Point** — The location where two moving objects occupy the same space at the same time.