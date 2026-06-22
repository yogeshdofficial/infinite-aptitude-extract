# Work Equivalence

## Overview
This pattern involves tasks performed by different groups (e.g., men, women, boys) or changing conditions (e.g., hours, rations, reinforcement). The central idea is to convert all variables into a single common unit or use the chain rule to equate the work done in two different scenarios.

---

## Recognition Clues
* **"Or" / "And" phrasing:** Questions like "12 men OR 18 women..." or "8 men AND 16 women...".
* **Changing conditions:** Phrases like "After X days, Y men left/joined" or "provisions for X days at Y rate".
* **Multiple variables:** Presence of men, days, hours, and work units in the same problem.
* **Goal:** Finding the number of days, the number of men, or the total earning.

---

## Key Formulas

### [Chain Rule]
$$
\frac{M_1 \times D_1 \times H_1}{W_1} = \frac{M_2 \times D_2 \times H_2}{W_2}
$$

**Variables:**
- $M$ = Men/Workers, $D$ = Days, $H$ = Hours/Day, $W$ = Work done.

**When to use:** When a project is split into two phases with different workforce or time constraints.

**Worked example:** 105 men, 25 days, 8 hours, $2/5$ work.
$\frac{105 \times 25 \times 8}{2/5} = \frac{M_2 \times 25 \times 9}{3/5} \implies M_2 = 140$.

### [Work Equivalence]
$$
\text{Total Work} = \text{Men} \times \text{Days} \times \text{Ration}
$$

**Variables:**
- $M$ = Men, $D$ = Days, $R$ = Ration per head.

**When to use:** Garrison/provision problems where consumption rates change.

**Worked example:** 3300 men, 25 days, 850g.
$3300 \times 25 \times 850 = M_2 \times 17 \times 825 \implies M_2 = 5000$.

---

## Solution Framework

1. **Standardize Units:** If given "X men or Y women", find the ratio (1 man = $Y/X$ women) to convert all workers to one type.
2. **Identify Remaining Work/Time:** Subtract completed work from total (1) and elapsed days from total days.
3. **Set up Chain Rule:** Place all "input" variables (Men, Days, Hours) in the numerator and "output" (Work) in the denominator.
4. **Equate:** Set the first scenario equal to the second scenario.
5. **Solve for Unknown:** Isolate the variable ($x$) and calculate.

---

## Shortcut Tricks

* **Trick:** Use the ratio of rates directly.
* **Why it works:** Since $M_1 \times D_1 = M_2 \times D_2$ (for constant work), you can cross-multiply ratios.
* **When to use:** When only two variables (like Men and Days) are changing.
* **Example:** 12 men = 18 women $\implies$ 1 man = 1.5 women. 8 men + 16 women = $(8 \times 1.5) + 16 = 28$ women.

---

## Common Mistakes

* **Mistake:** Adding men and women directly (e.g., $8+16=24$). **Fix:** Always convert to a common unit using the "or" ratio first.
* **Mistake:** Using total days instead of remaining days. **Fix:** Always subtract elapsed time from the total contract time.
* **Mistake:** Forgetting to subtract original men to find "additional" men. **Fix:** The result of the formula is the *total* required; subtract the starting count.

---

## Worked Example (Step-by-Step)

**Question:** If 12 men or 18 women can do a work in 14 days, in how many days will 8 men and 16 women do the same work?

**Solution:**
1. **Standardize:** 12 men = 18 women $\implies$ 1 man = $1.5$ women.
2. **Convert:** 8 men + 16 women = $(8 \times 1.5) + 16 = 12 + 16 = 28$ women.
3. **Proportion:** 18 women take 14 days. 28 women take $x$ days.
4. **Calculate:** $18 \times 14 = 28 \times x \implies x = \frac{18 \times 14}{28} = 9$.

**Answer:** 9 days.

---

## Similar Patterns
* **Time and Work:** This pattern is a subset of Time and Work. Distinguish by the presence of "or" equivalence ratios or multiple worker types.

---

## Revision Summary
* **Key formula:** $\frac{M_1 D_1 H_1}{W_1} = \frac{M_2 D_2 H_2}{W_2}$.
* **Spot it by:** "Or" statements and changing workforce/conditions.
* **First move:** Convert all workers to a single unit using the "or" ratio.
* **Fastest method:** Cross-multiply ratios for simple two-variable problems.
* **Biggest trap:** Adding different worker types without converting them first.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Direct Proportion:** If $A$ increases, $B$ increases ($A/B = k$).
* **Indirect Proportion:** If $A$ increases, $B$ decreases ($A \times B = k$).

### Formulas You Must Know First
* **Work = Efficiency $\times$ Time.**

### Terms Used In This Pattern
* **Garrison:** A body of troops stationed in a fortress.
* **Reinforcement:** Additional personnel sent to support a group.
* **Provisions:** Supplies of food or other necessities.