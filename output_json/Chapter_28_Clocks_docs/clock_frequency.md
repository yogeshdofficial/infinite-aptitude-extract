# Clock Frequency

## Overview
This pattern deals with the periodic behavior of clock hands (coinciding, straight lines, right angles) and the cumulative striking of clocks. The central idea is to identify the frequency of an event within a 12-hour cycle and scale it to the required time frame (usually 24 hours).

---

## Recognition Clues
* **Keywords:** "How many times," "coincide," "straight line," "right angle," "opposite direction," "strikes."
* **Given:** A time duration (e.g., "in a day," "from 1 p.m. to 10 p.m.").
* **Asked:** The frequency of a specific geometric alignment or the total count of bell strikes.

---

## Key Formulas

### [Sum of Strikes]
$$
\text{Total} = 2 \times \frac{n(n+1)}{2}
$$
**Variables:**
- $n$ = the last hour of the 12-hour cycle (always 12).
**When to use:** When asked for the total number of strikes in a 24-hour day.
**Worked example:** For a 12-hour cycle, sum = $\frac{12(13)}{2} = 78$. For a day, $78 \times 2 = 156$.

### [Frequency Scaling]
$$
\text{Total Occurrences} = \text{Occurrences in 12h} \times \left( \frac{\text{Total Time}}{12 \text{ hours}} \right)
$$
**Variables:**
- $\text{Occurrences in 12h}$ = The constant frequency (e.g., 11 for coincidences).
**When to use:** To find occurrences over any duration (e.g., 24 hours or 9 hours).

---

## Solution Framework

1. **Identify the 12-hour constant:** Determine the frequency of the event in a standard 12-hour cycle (e.g., 11 for coincidences, 22 for right angles).
2. **Adjust for the specific interval:** If the question asks for a 24-hour period, multiply the 12-hour constant by 2.
3. **Handle partial intervals:** If the interval is less than 12 hours, multiply the number of hours by the frequency per hour (e.g., 2 for right angles).
4. **Verify boundary conditions:** Check if the start or end times of the interval include or exclude specific "lost" positions (like the 12 o'clock overlap).

---

## Shortcut Tricks

* **Trick:** Right angles occur exactly 22 times in 12 hours.
* **Why it works:** The hands lose two positions per 12 hours due to the overlap at 12:00 and 6:00.
* **When to use:** Any question asking for right angles in a day.
* **Example:** For 24 hours, $22 \times 2 = 44$.

* **Trick:** For strikes, use $n(n+1)$ for a full 24-hour day.
* **Why it works:** The formula $\frac{n(n+1)}{2}$ for 12 hours multiplied by 2 simplifies to $n(n+1)$.
* **Example:** $12 \times 13 = 156$.

---

## Common Mistakes

* **Mistake:** Assuming 24 coincidences in a day.
* **Why it happens:** Thinking the hands meet once every hour.
* **Fix:** Remember the hands meet 11 times in 12 hours, not 12.
* **Mistake:** Miscounting hours in a range.
* **Why it happens:** Including both start and end times incorrectly.
* **Fix:** Count the number of gaps (e.g., 1 p.m. to 10 p.m. is 9 hours).

---

## Worked Example (Step-by-Step)

**Question:** How many times are the hour hand and the minute hand of a clock at right angles during their motion from 1.00 p.m. to 10.00 p.m.?

**Solution:**
1. **Identify frequency:** In one hour, the hands are at right angles twice.
2. **Calculate duration:** From 1.00 p.m. to 10.00 p.m. is $10 - 1 = 9$ hours.
3. **Apply formula:** $9 \text{ hours} \times 2 \text{ right angles/hour} = 18$.

**Answer:** 18 times.

---

## Similar Patterns
**Relative Speed Problems:** Distinguished by asking for the *exact time* (e.g., "at what time between 2 and 3") rather than the *number of times* an event occurs.

---

## Revision Summary
* **Key formula:** $\text{Total} = \text{Frequency}_{12h} \times \text{Cycles}$.
* **Spot it by:** "How many times" in a given duration.
* **First move:** Determine the frequency per 12-hour cycle.
* **Fastest method:** Memorize the 12-hour constants (11 for overlap, 22 for right angles).
* **Biggest trap:** Assuming 24 occurrences in a day for coincidences.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Clock Cycle** — A standard clock face represents 12 hours; the minute hand completes 1 rotation per hour, the hour hand per 12 hours.
* **Sum of Natural Numbers** — The sum of integers from 1 to $n$ is $\frac{n(n+1)}{2}$.

### Formulas You Must Know First
$$
\text{Sum} = \frac{n(n+1)}{2}
$$
**What it means:** Used to calculate total strikes when the clock strikes $1, 2, 3...n$ times.
**Example:** For 3 o'clock, $1+2+3 = 6$.

### Terms Used In This Pattern
* **Coincide** — When the hour and minute hands overlap (0°).
* **Straight Line** — When the hands are at 0° or 180°.
* **Right Angle** — When the hands are at 90°.