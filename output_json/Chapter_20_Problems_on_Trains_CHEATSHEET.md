# Problems On Trains — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Objects:** Determine if the train is crossing a point object (pole, man) or a length object (platform, bridge, another train).
2. **Check Direction:** If two objects are moving, identify if they are in the same or opposite direction.
3. **Standardize Units:** Immediately convert all speeds to m/sec ($\text{km/hr} \times \frac{5}{18}$) and lengths to meters.
4. **Define Distance:** Total distance = (Length of Train 1) + (Length of Object/Train 2).
5. **Apply Relative Speed:** Opposite = $S_1 + S_2$; Same = $|S_1 - S_2|$.
6. **Calculate:** Use $T = \frac{D}{S}$ or $S = \frac{D}{T}$.
7. **Sanity Check:** Ensure time is positive and speed magnitude is realistic (e.g., 10–40 m/sec).

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Basic Motion | "pole", "man", "pillars" | Speed, Time | Length/Distance |
| Meeting Point | "start from A/B", "meet" | Speeds, Distances | Time/Meeting Point |
| Platform Crossing | "platform", "bridge", "tunnel" | Lengths, Speed | Time/Speed |
| Relative: Opposite | "towards each other" | Two speeds, lengths | Time to cross |
| Relative: Same | "same direction", "overtake" | Two speeds, lengths | Time to cross |
| Speed Ratio | "after they meet", "reach" | Times after meeting | Ratio of speeds |
| Two-Event | "noticed", "passes X and Y" | Two times, one length | Speed/Length |
| Unit Conversion | "kmph to m/sec" | Speed | Speed in new unit |

---

## Formula Bank

**[Basic Train Motion]**
$$\text{Speed} = \frac{\text{Distance}}{\text{Time}}$$
→ *gives: speed in m/sec*
→ *use when: simple motion given*

$$\text{Number of pillars} = \frac{\text{Total Distance}}{\text{Interval}} + 1$$
→ *gives: count of objects*
→ *use when: counting poles/pillars*

**[Meeting Point Problems]**
$$\text{Relative Speed} = S_1 + S_2$$
→ *gives: combined closing speed*
→ *use when: moving towards each other*

**[Platform Crossing]**
$$\text{Total Distance} = L_{\text{train}} + L_{\text{platform}}$$
→ *gives: effective distance*
→ *use when: crossing non-point objects*

**[Relative Speed: Opposite]**
$$\text{Time} = \frac{L_1 + L_2}{S_1 + S_2}$$
→ *gives: time to cross*
→ *use when: trains moving towards each other*

**[Relative Speed: Same Direction]**
$$\text{Time} = \frac{L_1 + L_2}{S_1 - S_2}$$
→ *gives: time to overtake*
→ *use when: trains moving same direction*

**[Speed Ratio After Meeting]**
$$\frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}$$
→ *gives: ratio of speeds*
→ *use when: time after meeting given*

---

## Step Sequences
* **Basic Motion:** Convert units → Divide distance by speed → Answer.
* **Meeting Point:** Calculate relative speed → Divide distance by relative speed → Answer.
* **Platform Crossing:** Sum lengths → Divide by speed → Answer.
* **Relative (Opposite):** Sum speeds → Sum lengths → Divide distance by speed → Answer.
* **Relative (Same):** Subtract speeds → Sum lengths → Divide distance by speed → Answer.
* **Speed Ratio:** Invert times → Take square root → Answer.
* **Two-Event:** Find speed from difference → Calculate length → Answer.

---

## Fastest Tricks
* **Unit Conversion:** Divide km/hr by 18, then multiply by 5 to get m/sec.
* **Platform Crossing:** Train length = (Relative speed) $\times$ (Time difference between crossing two objects).
* **Speed Ratio:** Always use $\sqrt{t_2} : \sqrt{t_1}$ (the inverse order of arrival).
* **Pillar Counting:** Always add 1 to the result of (Total Distance / Gap).

---

## Trap Watch
* **Basic Motion:** Man has no length → Ignore man's length.
* **Platform Crossing:** Forgetting to add train length → Add train length.
* **Relative Speed:** Subtracting speeds in opposite direction → Add speeds.
* **Unit Conversion:** Using km/hr with meters → Convert to m/sec.
* **Meeting Point:** Using total distance instead of remaining → Subtract distance covered.

---

## Last-Minute Reminders
* Always convert km/hr to m/sec before performing any calculation involving meters.
* When a train crosses a platform, the total distance is always the sum of the train length and the platform length.
* In relative speed problems, always add the lengths of both trains regardless of direction.
* When counting pillars or trees, the number of intervals is always one less than the number of objects.
* If a train passes a man, the distance covered is simply the length of the train.