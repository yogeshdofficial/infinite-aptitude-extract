# Combinations and Committees

## Overview
These questions ask you to select a specific number of people from a larger group to form a committee or team. The central idea is that the **order of selection does not matter**, so you must use the Combination formula ($^nC_r$) rather than Permutations.

---

## Recognition Clues
* **Keywords:** "Committee," "chosen," "selected," "team," "how many ways."
* **Given:** Total number of items/people ($n$) and the size of the group to be formed ($r$).
* **Asked:** The total number of unique combinations possible.
* **Constraint:** Often includes specific subgroup requirements (e.g., "must have 2 men and 3 women").

---

## Key Formulas

### [Combination Formula]
$$
^nC_r = \frac{n!}{r!(n-r)!}
$$

**Variables:**
- $n$ = total number of items available
- $r$ = number of items to be selected

**When to use:** Whenever you need to select a group where the order of members does not change the outcome.

**Worked example:** To choose 3 players from 14 ($^{14}C_3$):
$\frac{14 \times 13 \times 12}{3 \times 2 \times 1} = 364$.

### [Symmetry Property]
$$
^nC_r = ^nC_{n-r}
$$

**Variables:**
- $n, r$ = same as above.

**When to use:** To simplify calculations when $r$ is large (e.g., calculating $^{14}C_{11}$ is hard, so use $^{14}C_3$ instead).

---

## Solution Framework

1. **Identify Subgroups:** Break the total requirement into specific group selections (e.g., men vs. women).
2. **Apply $^nC_r$:** Calculate the number of ways to select the required members for each subgroup independently.
3. **Multiply:** Multiply the results of each subgroup selection (Fundamental Principle of Counting).
4. **Add (if necessary):** If the question offers "OR" scenarios (e.g., Case A OR Case B), calculate each case separately and add the totals.

---

## Shortcut Tricks

* **Trick:** Use the "Cancellation Method" for $^nC_r$.
* **Why it works:** It avoids calculating large factorials by canceling terms in the numerator and denominator immediately.
* **Example:** For $^7C_3$, write $\frac{7 \times 6 \times 5}{3 \times 2 \times 1}$. Cancel $3 \times 2$ with $6$ to get $7 \times 5 = 35$.

---

## Common Mistakes

* **Mistake:** Adding combinations when you should multiply.
    * **Why:** Confusing "AND" (multiply) with "OR" (add).
    * **Fix:** If the committee needs X *and* Y, multiply. If the committee can be formed by Scenario A *or* Scenario B, add.
* **Mistake:** Using Permutations ($^nP_r$).
    * **Why:** Forgetting that in a committee, the order of members doesn't matter.
    * **Fix:** Always use $^nC_r$ for committees.
* **Mistake:** Forgetting "at least" cases.
    * **Why:** Assuming "at least one woman" only means one woman.
    * **Fix:** List all possibilities (1 woman, 2 women, 3 women, etc.) and add them.

---

## Worked Example (Step-by-Step)

**Question:** Out of 5 men and 3 women, a committee of three members is to be formed so that it has 1 woman and 2 men. In how many ways can it be done?

**Solution:**
1. **Identify Subgroups:** We need 1 woman (from 3) AND 2 men (from 5).
2. **Apply $^nC_r$:**
   - Ways to choose 1 woman: $^3C_1 = 3$.
   - Ways to choose 2 men: $^5C_2 = \frac{5 \times 4}{2 \times 1} = 10$.
3. **Multiply:** Since we need both, $3 \times 10 = 30$.

**Answer:** 30 ways.

---

## Similar Patterns

**Permutations:** Distinguish by checking if order matters. If the question asks for "arrangements," "seating," or "positions" (like President/Secretary), use Permutations ($^nP_r$). If it asks for a "committee" or "group," use Combinations ($^nC_r$).

---

## Revision Summary

* **Key formula:** $^nC_r = \frac{n!}{r!(n-r)!}$
* **Spot it by:** "Committee" or "Selection" keywords.
* **First move:** Break the committee into required subgroups.
* **Fastest method:** Use the symmetry property ($^nC_r = ^nC_{n-r}$) to keep $r$ small.
* **Biggest trap:** Adding instead of multiplying for "AND" conditions.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$):** The product of all positive integers up to $n$ (e.g., $4! = 4 \times 3 \times 2 \times 1 = 24$).
* **Fundamental Principle of Counting:** If one task can be done in $m$ ways and another in $n$ ways, both can be done in $m \times n$ ways.

### Formulas You Must Know First
* **$n! = n \times (n-1) \times ... \times 1$**
* **$0! = 1$**

### Terms Used In This Pattern
* **Combination:** A selection of items where order does not matter.
* **Committee:** A group of people selected for a specific purpose.