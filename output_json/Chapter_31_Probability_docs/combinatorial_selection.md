# Combinatorial Selection

## Overview
This pattern involves calculating the probability of selecting a specific subset of items from a larger group (e.g., drawing balls from a bag or cards from a deck). The central idea is to use the combination formula $^nC_r$ to determine the number of favorable outcomes and the total possible outcomes.

---

## Recognition Clues
* **Keywords:** "drawn at random," "drawn together," "selecting," "subset," "probability."
* **Given:** Total number of items (e.g., 52 cards, 10 balls) and the number of items to be selected (e.g., "two cards are drawn").
* **Asked:** Probability of a specific condition (e.g., "both are same color," "one is a spade and one is a heart").
* **Constraint:** Items are drawn "together" or "at random," implying order does not matter.

---

## Key Formulas

### [Combination Formula]
$$
^nC_r = \frac{n!}{r!(n-r)!}
$$
**Variables:**
- $n$ = total number of items available
- $r$ = number of items to be selected

**When to use:** To find the number of ways to choose $r$ items from $n$ without regard to order.
**Worked example:** Choosing 2 balls from 6: $^6C_2 = \frac{6 \times 5}{2 \times 1} = 15$.

### [Probability Formula]
$$
P(E) = \frac{n(E)}{n(S)}
$$
**Variables:**
- $P(E)$ = probability of event $E$
- $n(E)$ = number of favorable outcomes
- $n(S)$ = total number of possible outcomes (sample space)

**When to use:** To calculate the final probability after finding combinations.
**Worked example:** If $n(E) = 21$ and $n(S) = 45$, $P(E) = \frac{21}{45} = \frac{7}{15}$.

---

## Solution Framework
1. **Step 1: Calculate $n(S)$** — Use $^nC_r$ to find the total ways to pick the required items from the entire set.
2. **Step 2: Identify cases** — Determine if the favorable event has multiple mutually exclusive scenarios (e.g., "both white" OR "both black").
3. **Step 3: Calculate $n(E)$** — Use $^nC_r$ for each case and add them (if OR) or multiply them (if AND).
4. **Step 4: Calculate Probability** — Divide $n(E)$ by $n(S)$ and simplify the fraction.
5. **Step 5: Adjust for Overlap** — If the question asks for "A or B," subtract the intersection $P(A \cap B)$ if the events are not mutually exclusive.

---

## Shortcut Tricks
* **Trick:** For $^nC_2$, use $\frac{n(n-1)}{2}$.
* **Why it works:** It skips the factorial expansion $n!/(n-2)!$ by canceling out terms immediately.
* **When to use:** Whenever you are selecting exactly 2 items.
* **Example:** For $n=10$, $^10C_2 = \frac{10 \times 9}{2} = 45$.

---

## Common Mistakes
* **Mistake:** Using permutations ($^nP_r$) instead of combinations ($^nC_r$).
    * **Fix:** Remember that "drawing together" means order does not matter; always use $^nC_r$.
* **Mistake:** Forgetting to subtract the intersection in "OR" questions (e.g., "black OR queen").
    * **Fix:** Use $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Mistake:** Adding probabilities when you should be multiplying combinations.
    * **Fix:** Multiply combinations for simultaneous events (e.g., 1 spade AND 1 heart).

---

## Worked Example (Step-by-Step)

**Question:** A bag contains 6 white and 4 black balls. Two balls are drawn at random. Find the probability that they are of the same colour.

**Solution:**
1. **$n(S)$:** Total balls = 10. Ways to draw 2: $^{10}C_2 = \frac{10 \times 9}{2} = 45$.
2. **Cases:** Same color means (2 White) OR (2 Black).
3. **$n(E)$:** 
   - 2 White: $^6C_2 = \frac{6 \times 5}{2} = 15$.
   - 2 Black: $^4C_2 = \frac{4 \times 3}{2} = 6$.
   - Total $n(E) = 15 + 6 = 21$.
4. **Probability:** $P(E) = \frac{21}{45} = \frac{7}{15}$.

**Answer:** $\frac{7}{15}$

---

## Similar Patterns
**Permutation Problems:** Distinguish by looking for keywords like "arranged," "seated in a row," or "order matters." If the order of selection changes the outcome, use permutations.

---

## Revision Summary
* **Key formula:** $^nC_r = \frac{n!}{r!(n-r)!}$ and $P(E) = \frac{n(E)}{n(S)}$.
* **Spot it by:** "Drawn at random" or "selecting a subset."
* **First move:** Calculate total ways $n(S)$ using $^nC_r$.
* **Fastest method:** Use $\frac{n(n-1)}{2}$ for $^nC_2$ calculations.
* **Biggest trap:** Forgetting to subtract the intersection in "OR" probability questions.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$):** The product of all positive integers up to $n$ (e.g., $4! = 4 \times 3 \times 2 \times 1 = 24$).
* **Mutually Exclusive Events:** Events that cannot happen at the same time; their probabilities are added.

### Formulas You Must Know First
* **Addition Rule:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

### Terms Used In This Pattern
* **Sample Space ($S$):** The set of all possible outcomes.
* **Event ($E$):** A specific subset of the sample space.
* **Suit:** One of the four categories in a deck of cards (Spades, Hearts, Diamonds, Clubs).