# Single Observation (Heights and Distances)

## Overview
This pattern involves calculating the height of an object or the distance to it using a single right-angled triangle formed by an observer, the object, and the ground. The central idea is to map the given values (angle and one side) to the correct trigonometric ratio ($\tan, \sin, \text{ or } \cos$) to solve for the unknown side.

---

## Recognition Clues
* **Keywords:** "Angle of elevation," "leaning against a wall," "shadow," "distance from the foot."
* **Given:** One angle (usually $30^\circ, 45^\circ, \text{ or } 60^\circ$) and one side length (height, shadow, or ladder length).
* **Asked:** The missing side of the right-angled triangle.
* **Visual:** A single triangle where the object is the vertical side, the ground is the horizontal side, and the line of sight/ladder is the hypotenuse.

---

## Key Formulas

### Tangent Ratio
$$
\tan \theta = \frac{\text{Opposite}}{\text{Adjacent}}
$$
**Variables:** $\theta$ = angle of elevation; Opposite = height of object; Adjacent = distance on ground.
**When to use:** When you have the height and need the distance (or vice versa).
**Worked example:** If height = $100$ m and $\theta = 30^\circ$, then $\tan 30^\circ = \frac{100}{\text{Distance}} \Rightarrow \frac{1}{\sqrt{3}} = \frac{100}{\text{Distance}} \Rightarrow \text{Distance} = 100\sqrt{3} \approx 173$ m.

### Cosine Ratio
$$
\cos \theta = \frac{\text{Adjacent}}{\text{Hypotenuse}}
$$
**Variables:** $\theta$ = angle with ground; Adjacent = distance from wall; Hypotenuse = length of ladder.
**When to use:** When dealing with a ladder leaning against a wall.
**Worked example:** If ladder = $19$ m and $\theta = 60^\circ$, then $\cos 60^\circ = \frac{\text{Distance}}{19} \Rightarrow \frac{1}{2} = \frac{\text{Distance}}{19} \Rightarrow \text{Distance} = 9.5$ m.

---

## Solution Framework
1. **Draw a sketch:** Label the triangle with the given angle and side to visualize which side is opposite, adjacent, or hypotenuse.
2. **Identify the ratio:** Choose $\tan, \sin, \text{ or } \cos$ based on the sides you have and the side you need.
3. **Set up the equation:** Substitute the known values into the chosen trigonometric ratio.
4. **Account for observer height:** If the observer has height, add it to the calculated vertical side at the very end.
5. **Solve for $x$:** Isolate the unknown variable and calculate the final value.

---

## Shortcut Tricks
* **Trick:** Use the "Ratio Rule" for $30^\circ-60^\circ-90^\circ$ triangles: sides are in ratio $1 : \sqrt{3} : 2$.
* **Why it works:** These are standard triangle properties derived from $\tan 30^\circ = \frac{1}{\sqrt{3}}$ and $\tan 60^\circ = \sqrt{3}$.
* **When to use:** When the angle is $30^\circ$ or $60^\circ$ to avoid writing out full trig equations.
* **Example:** For a $30^\circ$ angle, if the base is $20\sqrt{3}$, the height is simply $20\sqrt{3} \times \frac{1}{\sqrt{3}} = 20$.

---

## Common Mistakes
* **Mistake:** Confusing Opposite and Adjacent sides. **Fix:** Always draw the triangle; the side "touching" the angle is the Adjacent side.
* **Mistake:** Forgetting to add observer height. **Fix:** If the problem mentions "observer height," calculate the triangle height first, then add the observer's height to get the total.
* **Mistake:** Using $\sin$ instead of $\cos$ for ladder problems. **Fix:** Remember the ladder is the Hypotenuse; the ground distance is the Adjacent side.

---

## Worked Example (Step-by-Step)

**Question:** An observer 1.6 m tall is $20\sqrt{3}$ m away from a tower. The angle of elevation from his eye to the top of the tower is $30^{\circ}$. The height of the tower is?

**Solution:**
1. **Sketch:** The triangle has a base of $20\sqrt{3}$ m and an angle of $30^\circ$.
2. **Ratio:** We need the height of the tower above the eye level (Opposite side). Use $\tan 30^\circ = \frac{\text{Opposite}}{\text{Adjacent}}$.
3. **Equation:** $\frac{1}{\sqrt{3}} = \frac{\text{Height}}{20\sqrt{3}}$.
4. **Solve:** $\text{Height} = 20\sqrt{3} \times \frac{1}{\sqrt{3}} = 20$ m.
5. **Final Step:** Add observer height: $20 + 1.6 = 21.6$ m.

**Answer:** 21.6 m.

---

## Similar Patterns
**Two-Observation Pattern:** Distinguished by having two different angles of elevation (e.g., $30^\circ$ and $60^\circ$) from two different points; requires solving two triangles simultaneously.

---

## Revision Summary
* **Key formula:** $\tan \theta = \frac{\text{Opposite}}{\text{Adjacent}}$.
* **Spot it by:** Looking for "angle of elevation" and a single triangle setup.
* **First move:** Draw the triangle and label the given side and angle.
* **Fastest method:** Use the $1 : \sqrt{3} : 2$ ratio for $30^\circ/60^\circ$ angles.
* **Biggest trap:** Forgetting to add the observer's height to the final result.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Right-Angled Triangle** — A triangle with one $90^\circ$ angle.
* **Trigonometric Ratios** — The relationship between angles and side lengths in a right triangle.

### Formulas You Must Know First
* $\tan 30^\circ = \frac{1}{\sqrt{3}}$
* $\tan 60^\circ = \sqrt{3}$
* $\cos 60^\circ = \frac{1}{2}$

### Terms Used In This Pattern
* **Angle of Elevation** — The angle between the horizontal line and the line of sight looking up.
* **Hypotenuse** — The longest side of a right triangle, opposite the $90^\circ$ angle.