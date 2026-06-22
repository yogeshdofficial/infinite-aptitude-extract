# Two-Event Comparison

## Overview
This pattern involves a train passing two different objects (e.g., a pole and a platform) at a constant speed. The central idea is that since the speed is constant, you can equate the speed expressions for both events to solve for an unknown variable (length or time).

---

## Recognition Clues
* **Keywords:** "passes a [stationary object/man/pole] in X seconds" AND "passes a [platform/train] in Y seconds."
* **Given:** Two different time durations and at least one length (either the train's or the platform's).
* **Asked:** Usually the length of the train, the length of the platform, or the speed of the train.
* **Constant:** The speed of the train remains the same in both scenarios.

---

## Key Formulas

### [Constant Speed Equivalence]

$$
\frac{L}{T_1} = \frac{L + P}{T_2}
$$

**Variables:**
- $L$ = Length of the train
- $P$ = Length of the platform/stationary object
- $T_1$ = Time taken to pass the first object (e.g., a pole)
- $T_2$ = Time taken to pass the second object (e.g., a platform)

**When to use:** When you have two events and need to find the train's length or the platform's length.

**Worked example:** Train passes a pole in 20s ($T_1$) and a 100m platform ($P$) in 30s ($T_2$).
$\frac{L}{20} = \frac{L+100}{30} \Rightarrow 30L = 20L + 2000 \Rightarrow 10L = 2000 \Rightarrow L = 200$ m.

---

## Solution Framework

1. **Step 1: Convert units** — Ensure speed is in m/sec (multiply km/hr by $\frac{5}{18}$) and all lengths are in metres.
2. **Step 2: Define the distance** — Identify that passing a pole/man covers distance $L$, while passing a platform covers $L + P$.
3. **Step 3: Set up the equation** — Write the speed expression for both events: $S = \frac{L}{T_1}$ and $S = \frac{L+P}{T_2}$.
4. **Step 4: Equate and solve** — Set $\frac{L}{T_1} = \frac{L+P}{T_2}$ to find the unknown variable.
5. **Step 5: Final calculation** — If asked for speed, substitute $L$ back into either expression.

---

## Shortcut Tricks

* **Trick:** Use the ratio of times to find the length: $\frac{L}{L+P} = \frac{T_1}{T_2}$.
* **Why it works:** Since $S$ is constant, $D \propto T$.
* **When to use:** When you need to find $L$ quickly without calculating speed first.
* **Example:** $T_1=20, T_2=30, P=100$. $\frac{L}{L+100} = \frac{20}{30} = \frac{2}{3} \Rightarrow 3L = 2L + 200 \Rightarrow L = 200$.

---

## Common Mistakes

* **Mistake:** Forgetting to add the train's length ($L$) when passing a platform.
    * **Why it happens:** Treating the platform as the only distance.
    * **Fix:** Always use $L + P$ for objects with length.
* **Mistake:** Mixing units (km/hr vs m/sec).
    * **Why it happens:** Rushing the calculation.
    * **Fix:** Convert everything to m/sec at the very start.
* **Mistake:** Using the wrong time for the wrong distance.
    * **Why it happens:** Misreading the question.
    * **Fix:** Map $T_1$ to $L$ and $T_2$ to $L+P$ explicitly before calculating.

---

## Worked Example (Step-by-Step)

**Question:** A train passes a station platform in 36 seconds and a man standing on the platform in 20 seconds. If the speed of the train is 54 km/hr, what is the length of the platform?

**Solution:**
1. **Convert units:** Speed = $54 \times \frac{5}{18} = 15$ m/sec.
2. **Find Train Length ($L$):** The train passes a man in 20s. $L = \text{Speed} \times \text{Time} = 15 \times 20 = 300$ m.
3. **Set up for Platform:** The train passes the platform in 36s. Total distance = $L + P = 300 + P$.
4. **Solve:** $\frac{300 + P}{36} = 15 \Rightarrow 300 + P = 540 \Rightarrow P = 240$ m.

**Answer:** 240 metres.

---

## Similar Patterns

**Relative Speed Pattern:** Use this when two objects are moving (e.g., two trains or a train and a running man). Distinguish by checking if the second object has a speed (km/hr) or is stationary.

---

## Revision Summary

* **Key formula:** $\frac{L}{T_1} = \frac{L+P}{T_2}$.
* **Spot it by:** Two different objects passed in two different times.
* **First move:** Convert speed to m/sec.
* **Fastest method:** Use the ratio $\frac{T_1}{T_2} = \frac{L}{L+P}$.
* **Biggest trap:** Forgetting to add the train's length to the platform's length.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Speed-Distance-Time:** The relationship $S = \frac{D}{T}$.
* **Unit Conversion:** Converting km/hr to m/sec by multiplying by $\frac{5}{18}$.

### Formulas You Must Know First
$$
S = \frac{D}{T}
$$
**What it means:** Speed is distance divided by time.
**Example:** A train covering 100m in 10s has a speed of 10 m/sec.

### Terms Used In This Pattern
* **Stationary:** Not moving (speed = 0).
* **Passes:** The time taken from the front of the train entering the object to the rear of the train leaving it.