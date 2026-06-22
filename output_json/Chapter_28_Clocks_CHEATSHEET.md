# Clocks — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Goal:** Determine if the question asks for an angle, a time, a frequency, or an error correction.
2. **Map Pattern:** Use the "Quick-Recognition Table" to match keywords to the specific pattern.
3. **Standardize Units:** Convert all times to minutes or hours; ensure AM/PM is handled via 24-hour format.
4. **Apply Formula:** Select the specific formula from the "Formula Bank" based on the identified pattern.
5. **Sanity Check:** Ensure the result is logical (e.g., angle $< 180^{\circ}$ for minor angle, time between $H$ and $H+1$).

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Clock Angles | "angle", "rotate", "turn" | Time, duration | Angle in degrees |
| Clock Error | "gain", "lose", "slow", "fast" | Error rate, time | Correct time |
| Clock Frequency | "how many times", "coincide" | Duration | Count of occurrences |
| Hands Coincidence | "together", "right angle", "apart" | Time range | Exact time |
| Time Duration | "behind", "reaches", "journey" | Start/End times | Elapsed duration |

---

## Formula Bank

**[Clock Angles]**
$$\theta = |30H - 5.5M|$$
→ *produces: Angle between hands in degrees*
→ *use when: Given specific time H:M*

$$\text{Angle} = \text{Time in minutes} \times 6^{\circ}$$
→ *produces: Angle moved by minute hand*
→ *use when: Only minute hand movement needed*

$$\text{Angle} = \text{Time in hours} \times 30^{\circ}$$
→ *produces: Angle moved by hour hand*
→ *use when: Only hour hand movement needed*

**[Clock Error]**
$$\text{True Time} = \text{Faulty Time} \times \frac{24}{24 \pm \text{Gain/Loss}}$$
→ *produces: Correct time from faulty clock*
→ *use when: Clock gains or loses time*

$$\text{Gain} = \left(\frac{720/11 - T}{T}\right) \times 1440$$
→ *produces: Gain/loss per day*
→ *use when: Hands meet at interval T*

**[Clock Frequency]**
$$\text{Occurrences} = \text{Hours} \times 2$$
→ *produces: Total coincidences/straight lines*
→ *use when: Calculating frequency in 24h*

**[Hands Coincidence]**
$$M = \frac{60}{11} \times (5H \pm \text{Gap})$$
→ *produces: Minutes past H o'clock*
→ *use when: Finding specific hand positions*

**[Time Duration]**
$$\text{Duration} = \text{Time to Midnight} + \text{Time from Midnight}$$
→ *produces: Total elapsed time*
→ *use when: Journey crosses midnight*

---

## Step Sequences

**Clock Angles:** Identify H, M → Apply $|30H - 5.5M|$ → Calculate reflex if needed → Answer.
**Clock Error:** Find ratio true/faulty → Multiply by faulty time → Adjust for start time → Answer.
**Clock Frequency:** Identify event type → Multiply 12h rate by 2 → Adjust for 24h → Answer.
**Hands Coincidence:** Identify H and gap → Apply $\frac{60}{11}(5H \pm \text{Gap})$ → Solve for M → Answer.
**Time Duration:** Convert to 24h → Subtract start from end → Borrow 60m if needed → Answer.

---

## Fastest Tricks

**Clock Angles:** Angle at $H:M$ is $|30H - 5.5M|$.
**Clock Error:** True time = $\text{Faulty Time} \times \frac{\text{Total Time}}{\text{Faulty Time Elapsed}}$.
**Coincidence:** Hands coincide every $65\frac{5}{11}$ minutes.
**Frequency:** Hands coincide 22 times, are opposite 22 times, and at right angles 44 times in 24h.

---

## Trap Watch

**Clock Angles:** Assuming hour hand is static → Use $0.5^{\circ}$ per minute.
**Clock Error:** Confusing gain/loss per hour vs per day → Check units.
**Hands Coincidence:** Forgetting the $\pm$ cases for right angles → Calculate both.
**Time Duration:** Crossing midnight/noon → Use 24-hour clock.

---

## Last-Minute Reminders

The hour hand moves $0.5^{\circ}$ per minute and the minute hand moves $6^{\circ}$ per minute.
The hands coincide 11 times in 12 hours and 22 times in 24 hours.
A "straight line" includes both coinciding ($0^{\circ}$) and opposite ($180^{\circ}$) positions.
Always convert mixed fractions to improper fractions before multiplying by $\frac{60}{11}$.
If the clock is slow, the true time is ahead of the clock time.