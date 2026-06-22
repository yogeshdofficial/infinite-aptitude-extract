# Boats And Streams — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Variables:** Scan for "still water speed" ($u$), "stream speed" ($v$), "downstream" ($D = u+v$), and "upstream" ($U = u-v$).
2. **Check Constraints:** Look for total time, distance, or ratios. If two scenarios are given, it is a **Simultaneous Equation** problem.
3. **Select Pattern:** Use the Quick-Recognition Table to match the question type.
4. **Unit Check:** Ensure all time is in hours (convert minutes by dividing by 60) and distance is in km.
5. **Execute:** Apply the specific formula or set up the algebraic system.
6. **Sanity Check:** Ensure $u > v$ (boat must be faster than current) and that speeds are positive.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Basic Speed | "still water", "stream", "along/against" | Speeds or Dist/Time | $u$ or $v$ |
| River Crossing | "perpendicularly", "width", "cross" | Width, speeds | Time taken |
| Simultaneous | "two scenarios", "total time" | Two dist/time pairs | $u$ and $v$ |
| Time-Distance | "twice as long", "ratio", "round trip" | Time/Distance ratios | Distance or $u/v$ |

---

## Formula Bank

**[Basic Speed Calculation]**
$$u = \frac{1}{2}(\text{Downstream} + \text{Upstream})$$
→ *produces: speed in still water*
→ *use when: both directional speeds are known*

$$v = \frac{1}{2}(\text{Downstream} - \text{Upstream})$$
→ *produces: speed of stream*
→ *use when: both directional speeds are known*

**[River Crossing]**
$$v_{eff} = \sqrt{u^2 - v^2}$$
→ *produces: effective crossing speed*
→ *use when: crossing river perpendicularly*

$$T = \frac{\text{Width}}{v_{eff}}$$
→ *produces: time to cross*
→ *use when: width and effective speed known*

**[Simultaneous Equations]**
$$\frac{D_1}{u-v} + \frac{D_2}{u+v} = T$$
→ *produces: system of equations*
→ *use when: two different trips provided*

**[Time-Distance Relationship]**
$$D = \frac{T(u^2 - v^2)}{2u}$$
→ *produces: total distance*
→ *use when: round trip time is given*

$$\frac{T_{up}}{T_{down}} = \frac{u+v}{u-v}$$
→ *produces: time ratio*
→ *use when: distance is constant*

---

## Step Sequences

* **Basic Speed:** Calculate $D$ and $U$ → Add/Subtract → Divide by 2.
* **River Crossing:** Calculate $v_{eff}$ → Divide width by $v_{eff}$ → Convert units.
* **Simultaneous:** Set $X=\frac{1}{u-v}, Y=\frac{1}{u+v}$ → Solve linear system → Convert back.
* **Time-Distance:** Set up ratio/equation → Solve for unknown variable → Verify units.

---

## Fastest Tricks

* **Basic Speed:** Still water speed is the arithmetic mean of $D$ and $U$.
* **Basic Speed:** Stream speed is half the difference of $D$ and $U$.
* **Time-Distance:** For round trips, average speed is the harmonic mean: $\frac{2 \cdot D \cdot U}{D+U}$.
* **Time-Distance:** If time taken upstream is $n$ times downstream, $u = v(\frac{n+1}{n-1})$.

---

## Trap Watch

* **Basic Speed:** Forgetting to convert minutes to hours → Divide minutes by 60.
* **River Crossing:** Using swimming speed as effective speed → Use Pythagoras.
* **Simultaneous:** Forgetting to divide by 2 for $u$ and $v$ → Divide result by 2.
* **Time-Distance:** Using arithmetic mean for average speed → Use harmonic mean.

---

## Last-Minute Reminders

* Always ensure $u$ (boat) is greater than $v$ (stream) for upstream travel to be possible.
* Downstream speed is always the sum of boat and stream speeds.
* Upstream speed is always the difference between boat and stream speeds.
* When crossing a river perpendicularly, the boat must aim upstream to compensate for drift.
* Time and speed are inversely proportional when distance is constant.