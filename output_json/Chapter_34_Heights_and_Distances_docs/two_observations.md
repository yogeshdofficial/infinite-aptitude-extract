# Two Observations

## Overview
This pattern involves finding the height of an object or the distance between two points when an observer moves towards or away from an object, changing the angle of elevation or depression. The central idea is to express the common side (usually the height) in terms of the two different angles and equate them to solve for the unknown.

---

## Recognition Clues
* **Keywords:** "Walking towards/away," "retires from," "angle changes from X to Y," "boat coming towards."
* **Given:** Two angles of elevation/depression and the distance between the two observation points.
* **Asked:** Height of the object or the distance from the object to one of the points.
* **Visual:** Two right-angled triangles sharing a common vertical side.

---

## Key Formulas

### Tangent Ratio
$$
\tan \theta = \frac{\text{Height}}{\text{Base}}
$$

**Variables:**
- $\theta$ = angle of elevation or depression
- $\text{Height}$ = vertical side of the triangle
- $\text{Base}$ = horizontal distance from the observer to the object

**When to use:** Every time you need to relate the height of an object to the distance of the observer.

**Worked example:** If height $h = 20$ and base $x = 20\sqrt{3}$, then $\tan \theta = \frac{20}{20\sqrt{3}} = \frac{1}{\sqrt{3}}$, so $\theta = 30^{\circ}$.

---

## Solution Framework

1. **Draw the diagram:** Sketch two right-angled triangles sharing the same vertical height ($h$).
2. **Define variables:** Assign $h$ to the height and $x$ to the unknown horizontal distance.
3. **Write two equations:** Express $h$ in terms of $x$ using $\tan \theta$ for both angles.
4. **Equate or Substitute:** Set the two expressions for $h$ equal to each other or substitute one into the other.
5. **Solve for the unknown:** Isolate the variable to find the required height or distance.

---

## Shortcut Tricks

**Trick:** For angles $30^{\circ}$ and $60^{\circ}$, the distance between points $d$ is related to height $h$ by $h = \frac{d \times \sqrt{3}}{2}$.

**Why it works:** Derived from $h\sqrt{3} - \frac{h}{\sqrt{3}} = d \Rightarrow h(\frac{3-1}{\sqrt{3}}) = d$.

**When to use:** When the angles are specifically $30^{\circ}$ and $60^{\circ}$.

**Example:** In Q3, $d = 24$. $h = \frac{24 \times \sqrt{3}}{2} = 12\sqrt{3} \approx 20.76$ m.

---

## Common Mistakes
* **Mixing up angles:** Using $\tan 30^{\circ} = \sqrt{3}$ instead of $\frac{1}{\sqrt{3}}$.
* **Base error:** Forgetting that the base for the $30^{\circ}$ angle is the *total* distance (e.g., $x + \text{distance moved}$).
* **Calculation error:** Failing to rationalize the denominator when solving for $h$.

---

## Worked Example (Step-by-Step)

**Question:** A man standing on the bank of a river observes that the angle subtended by a tree on the opposite bank is $60^{\circ}$. When he retires 36 m from the bank, he finds the angle to be $30^{\circ}$. Find the breadth of the river.

**Solution:**
1. **Diagram:** Tree height $h$, river breadth $x$. Triangle 1 (at bank): base $x$, angle $60^{\circ}$. Triangle 2 (36m back): base $x+36$, angle $30^{\circ}$.
2. **Equations:** 
   - From $60^{\circ}$: $\tan 60^{\circ} = \frac{h}{x} \Rightarrow h = x\sqrt{3}$.
   - From $30^{\circ}$: $\tan 30^{\circ} = \frac{h}{x+36} \Rightarrow h = \frac{x+36}{\sqrt{3}}$.
3. **Equate:** $x\sqrt{3} = \frac{x+36}{\sqrt{3}}$.
4. **Solve:** $3x = x + 36 \Rightarrow 2x = 36 \Rightarrow x = 18$.

**Answer:** The breadth of the river is 18 m.

---

## Similar Patterns
**Single Observation:** Only one triangle is formed; use simple $\tan \theta$ once.
**Two Objects:** Two triangles are formed on opposite sides of the object; add the bases instead of subtracting.

---

## Revision Summary
* **Key formula:** $\tan \theta = \frac{\text{Height}}{\text{Base}}$.
* **Spot it by:** Two angles and a distance between observation points.
* **First move:** Set up two equations for the common height $h$.
* **Fastest method:** Use the $30^{\circ}-60^{\circ}$ shortcut ($h = \frac{d\sqrt{3}}{2}$).
* **Biggest trap:** Forgetting to add the distance moved to the base of the larger triangle.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Right-Angled Triangle:** A triangle with one $90^{\circ}$ angle.
* **Tangent Ratio:** The ratio of the opposite side to the adjacent side in a right triangle.

### Formulas You Must Know First
* **$\tan 30^{\circ} = \frac{1}{\sqrt{3}}$**
* **$\tan 60^{\circ} = \sqrt{3}$**

### Terms Used In This Pattern
* **Angle of Elevation:** Angle looking up from the horizontal.
* **Angle of Depression:** Angle looking down from the horizontal.