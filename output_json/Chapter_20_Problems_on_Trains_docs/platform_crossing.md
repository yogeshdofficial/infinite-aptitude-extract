# Platform Crossing

## Overview
This pattern involves a train passing a stationary object with a significant length, such as a platform, bridge, or tunnel. The central idea is that the train must cover its own length plus the length of the object to clear it completely.

---

## Recognition Clues
* **Keywords:** "crosses a platform," "passes a bridge," "tunnel," "length of the train," "length of the platform."
* **Given:** Length of train ($L_t$), length of platform ($L_p$), and speed of train ($S$) or time ($T$).
* **Asked:** Time taken to cross, speed of the train, or length of the train.

---

## Key Formulas

### [Total Distance]
$$
D = L_t + L_p
$$
**Variables:** $D$ = total distance, $L_t$ = length of train, $L_p$ = length of platform.
**When to use:** Every time a train crosses a platform/bridge.
**Worked example:** Train 110m, Platform 165m. $D = 110 + 165 = 275$ m.

### [Speed/Time Calculation]
$$
S = \frac{D}{T} \quad \text{or} \quad T = \frac{D}{S}
$$
**Variables:** $S$ = speed, $D$ = total distance, $T$ = time.
**When to use:** To find the missing variable after calculating $D$.
**Worked example:** $D = 275$ m, $S = \frac{110}{3}$ m/s. $T = 275 \div \frac{110}{3} = 7.5$ seconds.

---

## Solution Framework
1. **Convert Units:** Ensure speed is in m/s (multiply km/hr by $\frac{5}{18}$) and lengths are in meters.
2. **Calculate Total Distance:** Add the length of the train to the length of the platform ($L_t + L_p$).
3. **Apply Formula:** Use $T = \frac{D}{S}$ or $S = \frac{D}{T}$ to find the required value.
4. **Re-convert (if needed):** If the answer is required in km/hr, multiply the final m/s speed by $\frac{18}{5}$.

---

## Shortcut Tricks
* **Trick:** For two platforms of lengths $P_1$ and $P_2$ crossed in times $T_1$ and $T_2$, the train length $L_t$ is found by: $\frac{L_t + P_1}{T_1} = \frac{L_t + P_2}{T_2}$.
* **Why it works:** The speed of the train is constant in both scenarios.
* **When to use:** When the question provides two different platforms and two different times.
* **Example:** $P_1=90, T_1=12; P_2=120, T_2=15$. $\frac{x+90}{12} = \frac{x+120}{15} \implies x=30$ m.

---

## Common Mistakes
* **Mistake:** Using only the platform length as distance. **Fix:** Always add the train's length.
* **Mistake:** Forgetting to convert km/hr to m/s. **Fix:** Check units before starting calculations.
* **Mistake:** Incorrectly equating speeds in two-platform problems. **Fix:** Ensure you set $\frac{L_t + P_1}{T_1} = \frac{L_t + P_2}{T_2}$.

---

## Worked Example (Step-by-Step)

**Question:** A 160-m long train crosses a 160-m long platform in 16 seconds. Find the speed of the train.

**Solution:**
1. **Total Distance:** $D = 160\text{ m (train)} + 160\text{ m (platform)} = 320\text{ m}$.
2. **Calculate Speed (m/s):** $S = \frac{D}{T} = \frac{320}{16} = 20\text{ m/s}$.
3. **Convert to km/hr:** $20 \times \frac{18}{5} = 4 \times 18 = 72\text{ km/hr}$.

**Answer:** 72 km/hr.

---

## Similar Patterns
* **Pole/Man Crossing:** Distinguish by the object length; for a pole or man, the object length is $0$, so $D = L_t$ only.

---

## Revision Summary
* **Key formula:** $D = L_t + L_p$ and $S = \frac{D}{T}$.
* **Spot it by:** "Train" and "Platform/Bridge" lengths given.
* **First move:** Convert speed to m/s.
* **Fastest method:** Add lengths first, then divide.
* **Biggest trap:** Forgetting to add the train's length to the platform's length.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Speed-Distance-Time:** The relationship $D = S \times T$.
* **Unit Conversion:** Converting km/hr to m/s by multiplying by $\frac{5}{18}$.

### Formulas You Must Know First
$$
\text{Speed} = \frac{\text{Distance}}{\text{Time}}
$$
**What it means:** The rate at which distance is covered over time.
**Example:** If you travel 100m in 10s, your speed is $10$ m/s.

### Terms Used In This Pattern
* **m/s:** Meters per second (standard unit for short distances).
* **km/hr:** Kilometers per hour (standard unit for long distances).