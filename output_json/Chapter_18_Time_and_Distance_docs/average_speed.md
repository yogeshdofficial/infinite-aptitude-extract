# Average Speed

## Overview
Average speed questions involve a journey split into multiple segments with different speeds or a round trip. The central idea is that average speed is **never** the simple arithmetic mean of the speeds; it is always the **Total Distance** divided by the **Total Time**.

---

## Recognition Clues
* **Keywords:** "Average speed for the entire journey," "whole journey," "travelled back at," "four sides of a square."
* **Given:** Multiple segments with specific distances and speeds, or a round trip with two different speeds.
* **Asked:** The average speed for the entire trip or the distance of a journey given the total time.

---

## Key Formulas

### [General Average Speed]
$$
\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}
$$
**Variables:**
- Total Distance = Sum of all individual segment distances.
- Total Time = Sum of all individual segment times ($\frac{\text{distance}}{\text{speed}}$).

**When to use:** When the journey is broken into distinct segments with different distances and speeds.

**Worked example:** Q7: Total distance = $4315$ km. Total time = $37\frac{1}{3}$ hr. Average speed = $4315 \div \frac{112}{3} = 115\frac{65}{112}$ km/hr.

### [Round Trip Average Speed]
$$
\text{Average Speed} = \frac{2xy}{x+y}
$$
**Variables:**
- $x$ = speed of the first leg.
- $y$ = speed of the return leg.

**When to use:** Only when the distance for the outgoing and return journey is **identical**.

**Worked example:** Q10: $x=25, y=4$. Average speed = $\frac{2 \times 25 \times 4}{25+4} = \frac{200}{29}$ km/hr.

---

## Solution Framework
1. **Step 1: Identify segments.** List the distance and speed for every part of the journey.
2. **Step 2: Calculate time for each segment.** Use $T = \frac{D}{S}$ for each part.
3. **Step 3: Sum the totals.** Add all distances to get Total Distance and all times to get Total Time.
4. **Step 4: Divide.** Calculate $\frac{\text{Total Distance}}{\text{Total Time}}$ to find the average speed.
5. **Step 5: Adjust (if needed).** If the question asks for one-way distance, divide the total distance by 2.

---

## Shortcut Tricks
* **Trick:** For equal distances at different speeds, use the Harmonic Mean formula $\frac{2xy}{x+y}$.
* **Why it works:** It mathematically simplifies the $\frac{\text{Total Distance}}{\text{Total Time}}$ calculation when distances cancel out.
* **When to use it:** Only when the distance covered at speed $x$ is exactly equal to the distance covered at speed $y$.
* **Example:** Q10 (Round trip) uses this to avoid calculating the distance $d$ explicitly until the final step.

---

## Common Mistakes
* **Mistake:** Taking the arithmetic mean (e.g., $\frac{25+4}{2} = 14.5$).
    * **Why it happens:** Intuitive but mathematically incorrect for speed.
    * **Fix:** Always use $\frac{\text{Total Distance}}{\text{Total Time}}$.
* **Mistake:** Forgetting to convert minutes to hours.
    * **Why it happens:** Speed is in km/hr, but time is often given in minutes.
    * **Fix:** Divide minutes by $60$ before adding to the total time.
* **Mistake:** Using the round-trip formula for unequal distances.
    * **Why it happens:** Over-reliance on shortcuts.
    * **Fix:** Only use $\frac{2xy}{x+y}$ if the distance is the same for both legs.

---

## Worked Example (Step-by-Step)

**Question:** A man travelled from the village to the post-office at $25$ kmph and walked back at $4$ kmph. The whole journey took $5$ hours $48$ minutes. Find the distance of the post-office from the village.

**Solution:**
1. **Identify:** Round trip, same distance $d$. Speeds $x=25, y=4$.
2. **Average Speed:** $\frac{2 \times 25 \times 4}{25+4} = \frac{200}{29}$ km/hr.
3. **Total Time:** $5$ hours $48$ minutes = $5 + \frac{48}{60} = 5\frac{4}{5} = \frac{29}{5}$ hours.
4. **Total Distance:** $\text{Avg Speed} \times \text{Total Time} = \frac{200}{29} \times \frac{29}{5} = 40$ km.
5. **One-way Distance:** Since $40$ km is the round trip, one-way distance = $\frac{40}{2} = 20$ km.

**Answer:** $20$ km.

---

## Similar Patterns
**Relative Speed:** Confused when two objects move simultaneously. Distinguish by checking if the question asks for the "average" of a single journey (this pattern) or the "meeting time/distance" of two objects (Relative Speed).

---

## Revision Summary
* **Key formula:** $\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}$.
* **Spot it by:** Looking for "average speed" over multiple segments or a round trip.
* **First move:** Calculate the time taken for each individual segment.
* **Fastest method:** Use $\frac{2xy}{x+y}$ only for equal-distance round trips.
* **Biggest trap:** Averaging the speeds directly (arithmetic mean).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractions:** Adding fractions with different denominators using LCM.
* **Time Conversion:** Converting minutes to hours by dividing by $60$.
* **Algebraic Substitution:** Representing unknown distance as $x$ to solve for it.

### Formulas You Must Know First
$$
\text{Time} = \frac{\text{Distance}}{\text{Speed}}
$$
**What it means:** The time taken is the distance divided by the rate of travel.
**Example:** $100$ km at $50$ km/hr takes $\frac{100}{50} = 2$ hours.

### Terms Used In This Pattern
* **kmph:** Kilometers per hour, the standard unit of speed.
* **Round trip:** A journey from point A to B and back to A.