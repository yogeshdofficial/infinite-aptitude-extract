# Relative Speed Start

## Overview
This pattern involves races where one runner is given a head start (distance) or a time advantage. The central idea is that the ratio of distances covered by two runners in the same time is equal to the ratio of their speeds.

---

## Recognition Clues
* **Keywords:** "gives a start of X m", "beats him by Y seconds", "reach the finish line at the same time".
* **Given:** Speed ratio or individual speeds, and the "start" distance or time difference.
* **Asked:** Total race distance, or the speed of the slower runner.

---

## Key Formulas

### Distance Ratio (Constant Time)
$$
\frac{D_A}{D_B} = \frac{S_A}{S_B}
$$

**Variables:**
- $D_A, D_B$ = Distances covered by A and B
- $S_A, S_B$ = Speeds of A and B

**When to use:** When both runners reach the finish line at the same time.

**Worked example:** If $S_A:S_B = 7:4$ and the race is $7$ m, A covers $7$ m while B covers $4$ m.

---

## Solution Framework

1. **Define the Speed Ratio:** Express the runners' speeds as a ratio $S_A : S_B$.
2. **Adjust Distances:** If a "start" of $X$ m is given, the slower runner covers $(Total - X)$ m while the faster runner covers the full $Total$ m.
3. **Set up Proportion:** Use the ratio $\frac{D_A}{D_B} = \frac{S_A}{S_B}$ to solve for the unknown variable (Total distance or speed).
4. **Account for Time:** If a time difference is given, calculate the time taken by the faster runner and add/subtract the difference to find the slower runner's time.

---

## Shortcut Tricks

* **Trick:** In a race of distance $L$, if A gives B a start of $S$ and they finish together, the ratio of speeds is $L : (L-S)$.
* **Why it works:** Since time is constant, the ratio of distances covered is the ratio of speeds.
* **When to use:** When the question asks for the winning post distance or speed ratio given a start.
* **Example:** In Q2, $S_A/S_B = 7/4$. A gives $84$ m start. $7/4 = L/(L-84) \implies 7L - 588 = 4L \implies 3L = 588 \implies L = 196$ m.

---

## Common Mistakes

* **Mistake:** Using the full race distance for the runner who received a start.
    * **Fix:** Always subtract the "start" distance from the total race length for that runner.
* **Mistake:** Adding the time difference to the faster runner.
    * **Fix:** The slower runner takes *more* time; always add the "beat by" time to the faster runner's time to get the slower runner's time.
* **Mistake:** Inverting the speed ratio.
    * **Fix:** Ensure the faster runner corresponds to the larger part of the ratio.

---

## Worked Example (Step-by-Step)

**Question:** In a 100 m race, A runs at 8 km/hr. If A gives B a start of 5 m and still beats him by 15 seconds, what is B’s speed?

**Solution:**
1. **Convert A's speed:** $8 \text{ km/hr} = 8 \times \frac{5}{18} = \frac{20}{9}$ m/s.
2. **Find A's time:** $T_A = \frac{100}{20/9} = 45$ seconds.
3. **Find B's time:** Since A beats B by 15s, $T_B = 45 + 15 = 60$ seconds.
4. **Adjust B's distance:** B runs $100 - 5 = 95$ m.
5. **Calculate B's speed:** $S_B = \frac{95}{60}$ m/s.
6. **Convert to km/hr:** $\frac{95}{60} \times \frac{18}{5} = 5.7$ km/hr.

**Answer:** 5.7 km/hr.

---

## Similar Patterns
**Time-Distance-Speed:** This is a subset of general motion problems; distinguish by the presence of a "start" (head start) or "beating" someone by a specific margin.

---

## Revision Summary
* **Key formula:** $D_A/D_B = S_A/S_B$ (for same time).
* **Spot it by:** "Start of X meters" or "Beats by Y seconds".
* **First move:** Convert all units to m/s and seconds.
* **Fastest method:** Use the ratio of distances to find the missing race length.
* **Biggest trap:** Forgetting to subtract the start distance from the slower runner's total.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio and Proportion** — Expressing relationships between two quantities as $a:b$.
* **Unit Conversion** — Converting km/hr to m/s by multiplying by $\frac{5}{18}$.

### Formulas You Must Know First
$$
\text{Speed} = \frac{\text{Distance}}{\text{Time}}
$$
**What it means:** The rate at which distance is covered over time.

### Terms Used In This Pattern
* **Start:** A distance advantage given to a slower runner.
* **Winning Post:** The finish line of the race.