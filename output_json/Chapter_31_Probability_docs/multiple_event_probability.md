# Multiple Event Probability

## Overview
This pattern involves calculating the probability of outcomes when multiple independent events occur simultaneously, such as tossing several coins or rolling multiple dice. The central idea is to determine the total number of possible outcomes (sample space) and count the specific outcomes that satisfy the given condition.

---

## Recognition Clues
* **Keywords:** "Simultaneous throw," "tossed together," "two/three coins," "pair of dice," "drawn at random."
* **Given:** Number of items (coins/dice) and the specific condition (e.g., "sum is 8," "at least one head").
* **Asked:** The probability of a specific event occurring.
* **Visual:** Look for phrases like "two dice are thrown together" or "three coins are tossed."

---

## Key Formulas

### [Probability of an Event]
$$
P(E) = \frac{n(E)}{n(S)}
$$

**Variables:**
- $P(E)$ = Probability of event $E$
- $n(E)$ = Number of favorable outcomes
- $n(S)$ = Total number of outcomes in the sample space

**When to use:** For any basic probability question where all outcomes are equally likely.

**Worked example:** For two coins, $n(S) = 4$. If we want "at least one head," $E = \{HH, HT, TH\}$, so $n(E) = 3$. $P(E) = \frac{3}{4}$.

---

## Solution Framework

1. **Step 1: Calculate $n(S)$:** Determine total outcomes by multiplying individual possibilities (e.g., $6 \times 6 = 36$ for two dice; $2^n$ for $n$ coins).
2. **Step 2: List Favorable Outcomes:** Systematically list or count the pairs/sets that satisfy the condition (e.g., sums of dice, number of heads).
3. **Step 3: Calculate $n(E)$:** Count the number of items in your list from Step 2.
4. **Step 4: Apply Formula:** Divide $n(E)$ by $n(S)$ and simplify the fraction.

---

## Shortcut Tricks

* **Trick:** Use the complement rule for "at least one" questions.
* **Why it works:** $P(\text{at least one}) = 1 - P(\text{none})$. It is often faster to count the single case of "zero" than all cases of "one, two, or three."
* **When to use it:** When the question asks for "at least one" and the "none" case is a single outcome (like $TTT$).
* **Example:** For 3 coins, $P(\text{at least one head}) = 1 - P(\text{no heads}) = 1 - P(TTT) = 1 - \frac{1}{8} = \frac{7}{8}$.

---

## Common Mistakes

* **Mistake:** Miscounting $n(S)$ for dice (e.g., using 12 instead of 36).
    * **Fix:** Always multiply: $6 \times 6 = 36$.
* **Mistake:** Confusing "at most" and "at least."
    * **Fix:** "At most 1" means 0 or 1; "At least 1" means 1, 2, or 3.
* **Mistake:** Double counting or missing pairs in dice sums.
    * **Fix:** List sums in increasing order (e.g., Sum 8: 2+6, 3+5, 4+4, 5+3, 6+2).

---

## Worked Example (Step-by-Step)

**Question:** Two dice are thrown together. What is the probability that the sum of the numbers on the two faces is divisible by 4 or 6?

**Solution:**
1. **Step 1:** Total outcomes $n(S) = 6 \times 6 = 36$.
2. **Step 2:** Identify sums divisible by 4 (4, 8, 12) or 6 (6, 12).
   - Sum 4: (1,3), (2,2), (3,1) [3 outcomes]
   - Sum 6: (1,5), (2,4), (3,3), (4,2), (5,1) [5 outcomes]
   - Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) [5 outcomes]
   - Sum 12: (6,6) [1 outcome]
3. **Step 3:** $n(E) = 3 + 5 + 5 + 1 = 14$.
4. **Step 4:** $P(E) = \frac{14}{36} = \frac{7}{18}$.

**Answer:** $\frac{7}{18}$

---

## Similar Patterns
**Permutation/Combination Probability:** If the question involves drawing balls from a bag or cards from a deck, use $nCr$ (combinations) instead of listing outcomes.

---

## Revision Summary
* **Key formula:** $P(E) = \frac{n(E)}{n(S)}$.
* **Spot it by:** Multiple items (coins/dice) tossed simultaneously.
* **First move:** Calculate total sample space ($6^n$ for dice, $2^n$ for coins).
* **Fastest method:** Use the complement rule ($1 - P(\text{none})$) for "at least one" questions.
* **Biggest trap:** Forgetting to simplify the final fraction.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Sample Space** — The set of all possible outcomes of an experiment.
* **Complementary Events** — The event that $E$ does not occur, denoted as $E^c$, where $P(E) + P(E^c) = 1$.

### Formulas You Must Know First
* **Multiplication Principle:** If one event has $m$ outcomes and another has $n$ outcomes, the total outcomes for both is $m \times n$.

### Terms Used In This Pattern
* **Unbiased:** A fair object where every outcome has an equal chance of occurring.
* **At least:** The minimum number required (includes the number and everything higher).
* **At most:** The maximum number allowed (includes the number and everything lower).