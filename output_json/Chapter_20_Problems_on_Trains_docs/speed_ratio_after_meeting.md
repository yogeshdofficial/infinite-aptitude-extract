# Speed Ratio After Meeting

## Overview
This pattern involves two objects moving towards each other from two different points. The key is that they meet at a point and then take specific, known times to reach their respective destinations.

---

## Recognition Clues
* **Keywords:** "start simultaneously," "after they meet," "reach their destinations after [x] and [y] hours."
* **Given:** Time taken by both objects to reach their destinations *after* the meeting point.
* **Asked:** The ratio of their speeds, or the actual speed of one train (if distance is provided).

---

## Key Formulas

### Speed Ratio Formula
$$
\frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}
$$

**Variables:**
- $S_1, S_2$ = Speeds of the first and second train.
- $t_1$ = Time taken by the first train to reach its destination *after* meeting.
- $t_2$ = Time taken by the second train to reach its destination *after* meeting.

**When to use:** Whenever you are given the time taken by two objects to complete their journey *after* they have crossed each other.

**Worked example:** If $t_1 = 9$ hours and $t_2 = 16$ hours, then $\frac{S_1}{S_2} = \sqrt{\frac{16}{9}} = \frac{4}{3}$. The ratio is $4:3$.

---

## Solution Framework

1. **Identify $t_1$ and $t_2$:** Extract the times taken by each train to reach the destination *after* the meeting point.
2. **Apply the Ratio Formula:** Calculate the ratio of speeds using $\sqrt{t_2} : \sqrt{t_1}$.
3. **Assign Variables:** If the actual speed is needed, represent speeds as $S_1 = ax$ and $S_2 = bx$.
4. **Calculate Meeting Time:** Use $\text{Time} = \frac{\text{Total Distance}}{\text{Relative Speed (sum of speeds)}}$.
5. **Solve for $x$:** Equate the total time taken by one train (Meeting Time + Time after meeting) to $\frac{\text{Total Distance}}{\text{Speed of that train}}$.

---

## Shortcut Tricks
* **Trick:** The ratio of speeds is always the *inverse* square root of the ratio of times.
* **Why it works:** The distance the first train covers after meeting is the same distance the second train covered before meeting.
* **When to use:** Use this for any "meeting and crossing" problem to jump straight to the speed ratio.

---

## Common Mistakes
* **Mistake:** Using $\sqrt{t_1} : \sqrt{t_2}$ instead of $\sqrt{t_2} : \sqrt{t_1}$.
    * **Fix:** Always remember the ratio is inverted (the train that takes longer is the slower one).
* **Mistake:** Using the time taken to *meet* instead of the time taken *after meeting*.
    * **Fix:** Read the question carefully; the formula only applies to the time *after* the meeting.

---

## Worked Example (Step-by-Step)

**Question:** Two trains start simultaneously from two stations 270 km apart, each to the opposite station; they reach their destinations in $6\frac{1}{4}$ hours and 4 hours after they meet. The rate at which the slower train travels is?

**Solution:**
1. **Identify times:** $t_1 = 6.25$ hours ($\frac{25}{4}$), $t_2 = 4$ hours.
2. **Ratio of speeds:** $\frac{S_1}{S_2} = \sqrt{\frac{4}{25/4}} = \sqrt{\frac{16}{25}} = \frac{4}{5}$.
3. **Assign variables:** Slower train speed $= 4x$, Faster train speed $= 5x$.
4. **Meeting time:** $\text{Time} = \frac{270}{4x + 5x} = \frac{270}{9x} = \frac{30}{x}$.
5. **Solve for $x$:** The slower train takes $\frac{270}{4x}$ total time. This equals (Meeting time + Time after meeting):
   $\frac{270}{4x} = \frac{30}{x} + 6.25 \implies 270 = 120 + 25x \implies 150 = 25x \implies x = 6$.
6. **Final Answer:** Slower train speed $= 4 \times 6 = 24$ km/hr.

---

## Similar Patterns
**Relative Speed Problems:** If the question asks for time to cross *without* mentioning the time taken *after* meeting, use standard relative speed formulas ($D = S \times T$).

---

## Revision Summary
* **Key formula:** $\frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}$.
* **Spot it by:** "After they meet, they reach destinations in..."
* **First move:** Square root the times and invert them to get the speed ratio.
* **Fastest method:** Use the ratio to define speeds as $ax$ and $bx$.
* **Biggest trap:** Forgetting to invert the ratio of the square roots.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Relative Speed** — When two objects move in opposite directions, their speeds add up ($S_1 + S_2$).
* **Ratios** — Expressing the relationship between two quantities as $a:b$.

### Formulas You Must Know First
$$
\text{Speed} = \frac{\text{Distance}}{\text{Time}}
$$
**What it means:** The fundamental relationship between motion variables.

### Terms Used In This Pattern
* **Simultaneously** — Starting at the exact same time.
* **Relative Speed** — The speed of one object as observed from the other.