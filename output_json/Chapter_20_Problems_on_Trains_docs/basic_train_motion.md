# Basic Train Motion

## Overview
This pattern covers scenarios where a train passes a stationary point object (pole, man, or tree). The central idea is that the distance covered by the train to fully cross the object is exactly equal to the train's own length.

---

## Recognition Clues
* **Keywords:** "passes a man," "crosses a pole," "standing near the line," "telegraph pole."
* **Given:** Train length (meters), Speed (km/hr), Time (seconds).
* **Asked:** Time taken to cross, or the length of the train, or the speed of the train.
* **Key indicator:** The object being passed has negligible length (a pole or a man).

---

## Key Formulas

### [Time to Cross]
$$
\text{Time} = \frac{\text{Length of Train}}{\text{Speed of Train}}
$$

**Variables:**
- $\text{Length of Train}$ = distance in meters ($m$)
- $\text{Speed of Train}$ = speed in meters per second ($m/s$)

**When to use:** When you need to find how long it takes for the train to clear a stationary point object.

**Worked example:** Train length = $100\text{ m}$, Speed = $30\text{ km/hr}$. 
Convert speed: $30 \times \frac{5}{18} = \frac{25}{3}\text{ m/s}$. 
Time = $100 \div \frac{25}{3} = 12\text{ seconds}$.

---

## Solution Framework

**Step 1: Standardize Units** — Convert speed from $\text{km/hr}$ to $\text{m/s}$ by multiplying by $\frac{5}{18}$ (since length is in meters and time in seconds).
**Step 2: Identify Distance** — Set the distance equal to the train's length (because the object has no length).
**Step 3: Apply Formula** — Use $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$ or $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$ as required.
**Step 4: Final Conversion (if needed)** — If the answer is required in $\text{km/hr}$, multiply the resulting $\text{m/s}$ speed by $\frac{18}{5}$.

---

## Shortcut Tricks

* **Trick:** Use the "18/5" or "5/18" conversion factor immediately.
* **Why it works:** It eliminates the need for intermediate steps when switching between standard units.
* **When to use:** Every time you see a mix of $\text{km/hr}$ and meters/seconds.
* **Example:** $144\text{ km/hr} \times \frac{5}{18} = 40\text{ m/s}$. Much faster than converting to meters/hour first.

---

## Common Mistakes

* **Mistake:** Adding the width of the pole or man to the train length.
    * **Why it happens:** Confusing point objects with platforms/bridges.
    * **Fix:** Remember that point objects have zero length.
* **Mistake:** Forgetting to convert $\text{km/hr}$ to $\text{m/s}$.
    * **Why it happens:** Rushing the calculation.
    * **Fix:** Always check units before dividing.

---

## Worked Example (Step-by-Step)

**Question:** A train 132 m long passes a telegraph pole in 6 seconds. Find the speed of the train.

**Solution:**
1. **Identify Distance:** The train passes a pole, so Distance = Length of train = $132\text{ m}$.
2. **Calculate Speed in m/s:** $\text{Speed} = \frac{\text{Distance}}{\text{Time}} = \frac{132}{6} = 22\text{ m/s}$.
3. **Convert to km/hr:** Multiply by $\frac{18}{5}$ to get the standard unit: $22 \times \frac{18}{5} = \frac{396}{5} = 79.2\text{ km/hr}$.

**Answer:** $79.2\text{ km/hr}$

---

## Similar Patterns

**Train Passing Platform/Bridge:** Distinguish by checking if the object has a length (e.g., "84 m long platform"). If it does, add the object's length to the train's length for the total distance.

---

## Revision Summary

* **Key formula:** $\text{Time} = \frac{\text{Length}}{\text{Speed}}$.
* **Spot it by:** Looking for "pole," "man," or "tree."
* **First move:** Convert $\text{km/hr}$ to $\text{m/s}$ using $\frac{5}{18}$.
* **Fastest method:** Use the $\frac{5}{18}$ factor immediately.
* **Biggest trap:** Adding the object's length (it is always $0$).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Speed-Distance-Time:** The relationship $\text{Distance} = \text{Speed} \times \text{Time}$.
* **Unit Conversion:** $1\text{ km} = 1000\text{ m}$ and $1\text{ hour} = 3600\text{ seconds}$.

### Formulas You Must Know First
$$
\text{Speed in m/s} = \text{Speed in km/hr} \times \frac{5}{18}
$$
**What it means:** Converts speed to match meter/second units.
**Example:** $36\text{ km/hr} \times \frac{5}{18} = 10\text{ m/s}$.

### Terms Used In This Pattern
* **Stationary Object:** An object that is not moving (pole, tree, man).
* **Relative Speed:** Not applicable here as the object is stationary (speed = $0$).