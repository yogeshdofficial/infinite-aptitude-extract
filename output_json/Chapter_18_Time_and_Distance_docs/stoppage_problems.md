# Stoppage Problems

## Overview
These questions involve a vehicle that travels at a certain speed but makes periodic halts, reducing its overall average speed. The central idea is to isolate the "lost time" (the time spent standing still) from the "driving time" (the time spent in motion).

---

## Recognition Clues
* **Keywords:** "Excluding stoppages," "including stoppages," "halts at," "stops for X minutes after every Y km."
* **Given:** Speed without stops, speed with stops, or total distance and total time including stops.
* **Asked:** Stoppage time per hour, or total time taken for a journey with multiple stops.

---

## Key Formulas

### Stoppage Time per Hour
$$
\text{Stoppage time (min)} = \frac{V_1 - V_2}{V_1} \times 60
$$

**Variables:**
- $V_1$ = Speed excluding stoppages (km/hr)
- $V_2$ = Speed including stoppages (km/hr)

**When to use:** When you are given two different average speeds and need to find how many minutes the vehicle stops per hour.

**Worked example:** Bus speed without stops = 64 km/hr, with stops = 48 km/hr.
Stoppage = $\frac{64 - 48}{64} \times 60 = \frac{16}{64} \times 60 = 15$ minutes.

### Number of Stops
$$
\text{Number of stops} = \left( \frac{\text{Total Distance}}{\text{Distance per stop interval}} \right) - 1
$$

**When to use:** When a vehicle stops at fixed distance intervals and you need to calculate the total time lost.

**Worked example:** 600 km journey, stops every 75 km.
Stops = $(\frac{600}{75}) - 1 = 8 - 1 = 7$ stops.

---

## Solution Framework

1. **Calculate Driving Time:** Divide total distance by the speed *without* stops to find the actual time the vehicle is in motion.
2. **Identify Stoppage Count:** If stops are distance-based, divide total distance by interval distance and subtract 1 (because there is no stop at the final destination).
3. **Calculate Total Stoppage Time:** Multiply the number of stops by the duration of each stop.
4. **Find Total Journey Time:** Add the "Driving Time" (from Step 1) to the "Total Stoppage Time" (from Step 3).

---

## Shortcut Tricks

* **Trick:** To find stoppage time per hour, simply use the ratio of the "speed difference" to the "original speed."
* **Why it works:** The distance "lost" per hour is exactly the distance the vehicle would have covered during the time it spent standing still.
* **Example:** If speed drops from 60 to 40 km/hr, the bus loses 20 km of progress per hour. It takes $\frac{20}{60}$ hours (20 mins) to cover that distance at normal speed.

---

## Common Mistakes

* **Mistake:** Including the final destination as a stop.
    * **Fix:** Always subtract 1 from the total number of intervals.
* **Mistake:** Dividing by the speed *including* stops when calculating lost time.
    * **Fix:** Always divide by the *original* (higher) speed.
* **Mistake:** Forgetting to convert hours to minutes.
    * **Fix:** Multiply by 60 at the final step if the answer is required in minutes.

---

## Worked Example (Step-by-Step)

**Question:** An express train travelled at an average speed of 100 km/hr, stopping for 3 minutes after every 75 km. How long did it take to reach its destination 600 km from the starting point?

**Solution:**
1. **Driving Time:** $\frac{600 \text{ km}}{100 \text{ km/hr}} = 6$ hours.
2. **Number of Stops:** $(\frac{600}{75}) - 1 = 8 - 1 = 7$ stops.
3. **Total Stoppage Time:** $7 \text{ stops} \times 3 \text{ minutes/stop} = 21$ minutes.
4. **Total Journey Time:** $6 \text{ hours} + 21 \text{ minutes} = 6 \text{ hours } 21 \text{ minutes}$.

**Answer:** 6 hours 21 minutes.

---

## Similar Patterns
* **Average Speed Problems:** These involve two different speeds over the *same* distance without stops; distinguish by checking if the question mentions "halts" or "stoppages."

---

## Revision Summary
* **Key formula:** $\text{Stoppage time} = \frac{V_1 - V_2}{V_1} \times 60$.
* **Spot it by:** Looking for "speed including/excluding stops" or "stops every X km."
* **First move:** Calculate the pure driving time (Distance / Speed).
* **Fastest method:** Use the speed difference ratio for per-hour problems.
* **Biggest trap:** Counting the final destination as a stop.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Average Speed** — The total distance divided by the total time taken, including all halts.
* **Time-Distance Relationship** — $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$.

### Formulas You Must Know First
$$
\text{Time} = \frac{\text{Distance}}{\text{Speed}}
$$
**What it means:** The time taken to travel is the distance divided by the rate of travel.

### Terms Used In This Pattern
* **Stoppage:** A scheduled or unscheduled halt where the vehicle's speed becomes 0.
* **Interval:** The distance or time gap between two consecutive stops.