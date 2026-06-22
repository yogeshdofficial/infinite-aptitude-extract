# Chain Ratio Races

## Overview
This pattern involves three runners (A, B, C) where you are given the relative performance of A vs B and B vs C. The central idea is to use the **Chain Rule of Ratios** to link them and find the relative performance of A vs C.

---

## Recognition Clues
* **Keywords:** "A beats B by X m", "A gives B a start of X m", "A scores X points", "game of X points".
* **Given:** Two separate ratios (A:B and B:C) or two separate "start" distances.
* **Asked:** The distance or points by which the first person (A) beats the third (C), or the "start" the second person (B) can give the third (C).
* **Context:** Always involves three entities and a common reference point (the race distance or total game points).

---

## Key Formulas

### Chain Ratio Formula
$$
\frac{A}{C} = \frac{A}{B} \times \frac{B}{C}
$$

**Variables:**
- $A, B, C$ = Distance covered or points scored by each runner.

**When to use:** To find the relationship between the first and last runner when the middle runner is the common link.

**Worked example:** If $A:B = 100:75$ and $B:C = 100:96$, then $\frac{A}{C} = \frac{100}{75} \times \frac{100}{96} = \frac{100}{72}$. A beats C by $100 - 72 = 28$ m.

---

## Solution Framework

**Step 1: Convert "beats by" or "start" to a ratio.** Express the distance covered by each runner as $D_{winner} : D_{loser}$ (e.g., "A beats B by 25m in 100m" becomes $100:75$).
**Step 2: Identify the common runner.** Determine which runner appears in both given ratios (e.g., B).
**Step 3: Multiply the ratios.** Use the Chain Ratio Formula to find the ratio of the first runner to the third runner.
**Step 4: Scale to the target.** If the question asks for a specific race length (e.g., 60 points), scale the final ratio so the winner's side matches the target total.
**Step 5: Find the difference.** Subtract the loser's value from the winner's value to find the "start" or "beat" distance.

---

## Shortcut Tricks
* **Trick:** Use the ratio product directly: $\text{Result} = \text{Total} \times (1 - \text{Ratio}_1 \times \text{Ratio}_2)$.
* **Why it works:** It bypasses intermediate steps by calculating the fraction of the race the final runner covers relative to the first.
* **When to use:** When you need the final "beat" distance in a standard race.
* **Example:** In Q4, $100 \times (1 - \frac{75}{100} \times \frac{96}{100}) = 100 \times (1 - 0.72) = 28$ m.

---

## Common Mistakes
* **Mistake:** Adding the distances (e.g., $25+4=29$). **Why:** Ratios are multiplicative, not additive. **Fix:** Always multiply the fractions.
* **Mistake:** Incorrectly setting the ratio (e.g., $75:100$ instead of $100:75$). **Why:** Confusing the "start" with the "distance covered". **Fix:** Always write $100 : (100 - \text{start})$.
* **Mistake:** Forgetting to scale the ratio. **Why:** Assuming the ratio is already in the units of the target race. **Fix:** Always check if the winner's side equals the total race distance.

---

## Worked Example (Step-by-Step)

**Question:** In a 100 m race, A beats B by 25 m and B beats C by 4 m. Find the distance by which A beats C.

**Solution:**
1. **Convert to ratios:** A:B = 100:75; B:C = 100:96.
2. **Identify common runner:** B is the link.
3. **Multiply ratios:** $\frac{A}{C} = \frac{100}{75} \times \frac{100}{96} = \frac{4}{3} \times \frac{100}{96} = \frac{400}{288} = \frac{100}{72}$.
4. **Scale:** The ratio is already based on 100m.
5. **Find difference:** $100 - 72 = 28$ m.

**Answer:** A beats C by 28 m.

---

## Similar Patterns
* **Time-Distance Races:** If the question gives "time" instead of "distance," use the formula $\text{Speed} = \frac{\text{Distance}}{\text{Time}}$ first, then proceed to ratios.

---

## Revision Summary
* **Key formula:** $\frac{A}{C} = \frac{A}{B} \times \frac{B}{C}$.
* **Spot it by:** Three runners and two relative performance statements.
* **First move:** Convert "beats by" into $100 : (100 - \text{beat})$ ratios.
* **Fastest method:** Multiply the ratios and subtract the result from the total.
* **Biggest trap:** Adding the "beat" distances instead of multiplying ratios.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratios** — A comparison of two quantities by division.
* **Proportion** — Equality of two ratios, used to scale values to a specific race length.

### Formulas You Must Know First
$$
\text{Distance} = \text{Speed} \times \text{Time}
$$
**What it means:** The distance covered is proportional to speed when time is constant.

### Terms Used In This Pattern
* **Start** — The distance advantage given to a slower runner.
* **Beat** — The distance by which the winner is ahead of the loser at the finish line.
* **Game of X points** — A race where the first to reach X points wins.