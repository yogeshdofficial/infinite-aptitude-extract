# Complementary Probability

## Overview
This pattern applies when a question asks for the probability of "at least one" occurrence of a specific event. Instead of calculating multiple scenarios (e.g., exactly 1, 2, or 3 blue marbles), calculate the probability of the event **not** happening at all and subtract that result from 1.

---

## Recognition Clues
* **Keywords:** "At least one", "at least one is [color]".
* **Given:** A total set of items (marbles/balls) categorized by color, and the number of items to be picked.
* **Asked:** The probability that at least one item of a specific color is selected.

---

## Key Formulas

### [Complementary Probability]
$$
P(\text{at least one}) = 1 - P(\text{none})
$$

**Variables:**
- $P(\text{at least one})$ = Probability of the event occurring 1 or more times.
- $P(\text{none})$ = Probability of the event occurring 0 times.

**When to use:** Whenever the phrase "at least one" appears in a probability question.

### [Combination Formula]
$$
^nC_r = \frac{n!}{r!(n-r)!}
$$

**Variables:**
- $n$ = Total number of items to choose from.
- $r$ = Number of items being selected.

**When to use:** To calculate the number of ways to select items from a group where order does not matter.

**Worked example:** Picking 3 marbles from 12 total: $^{12}C_3 = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$.

---

## Solution Framework

1. **Identify Total Items:** Sum all items to find the total sample space size ($n$).
2. **Identify "Non-Target" Items:** Subtract the number of target items (e.g., blue marbles) from the total to find how many items are "not" the target.
3. **Calculate Total Ways ($n(S)$):** Use $^nC_r$ to find the total ways to pick the required number of items from the total pool.
4. **Calculate "None" Ways ($n(E)$):** Use $^nC_r$ to find the ways to pick the required number of items *only* from the "non-target" pool.
5. **Find Probability of None:** Divide $n(E)$ by $n(S)$.
6. **Subtract from 1:** The final answer is $1 - P(\text{none})$.

---

## Shortcut Tricks
* **Trick:** Use $^nC_r = ^nC_{n-r}$ to simplify calculations.
* **Why it works:** It reduces the number of terms in the numerator and denominator.
* **When to use:** When $r$ is greater than half of $n$ (e.g., picking 5 items out of 9, use $^9C_4$ instead of $^9C_5$).
* **Example:** In Q33, calculating $^9C_5$ is the same as $^9C_4 = \frac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126$.

---

## Common Mistakes
* **Mistake:** Calculating the probability of "exactly one" instead of "at least one."
    * **Fix:** Always use the $1 - P(\text{none})$ rule.
* **Mistake:** Using the target items when calculating $P(\text{none})$.
    * **Fix:** Ensure the numerator for $P(\text{none})$ uses only the "non-target" count.
* **Mistake:** Incorrectly identifying the total number of items.
    * **Fix:** Double-check the sum of all categories before starting.

---

## Worked Example (Step-by-Step)

**Question:** A basket contains 4 red, 5 blue and 3 green marbles. If three marbles are picked up at random what is the probability that at least one is blue?

**Solution:**
1. **Total Items:** $4 + 5 + 3 = 12$.
2. **Non-Target (Non-blue):** $4 + 3 = 7$.
3. **Total Ways ($n(S)$):** $^{12}C_3 = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$.
4. **"None" Ways ($n(E)$):** $^7C_3 = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$.
5. **$P(\text{none})$:** $\frac{35}{220} = \frac{7}{44}$.
6. **Final Probability:** $1 - \frac{7}{44} = \frac{37}{44}$.

**Answer:** $\frac{37}{44}$

---

## Similar Patterns
* **Direct Probability:** If the question asks for "exactly one" or "all are blue," do not use the complement rule; calculate the specific favorable outcomes directly.

---

## Revision Summary
* **Key formula:** $P(\text{at least one}) = 1 - P(\text{none})$.
* **Spot it by:** The phrase "at least one" in the question.
* **First move:** Calculate the total number of items and the number of "non-target" items.
* **Fastest method:** Use the complement rule to avoid calculating multiple scenarios.
* **Biggest trap:** Forgetting to subtract the complement from 1.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Probability** — The ratio of favorable outcomes to total possible outcomes: $P(E) = \frac{n(E)}{n(S)}$.
* **Combinations** — Selecting items where order does not matter, denoted by $^nC_r$.

### Formulas You Must Know First
* **Factorial ($n!$)** — The product of all positive integers up to $n$ (e.g., $4! = 4 \times 3 \times 2 \times 1 = 24$).

### Terms Used In This Pattern
* **Sample Space ($S$)** — The set of all possible outcomes of an experiment.
* **Event ($E$)** — A specific subset of the sample space.
* **Complement** — The event that the target outcome does not occur.