# Basic Probability

## Overview
This pattern involves calculating the likelihood of a single, random event occurring. The central idea is to determine the ratio of the number of successful outcomes to the total number of possible outcomes.

---

## Recognition Clues
* **Keywords:** "probability," "at random," "drawn at random," "tossed," "thrown."
* **Given:** A set of items (cards, balls, tickets) or a random experiment (die, coin).
* **Asked:** The probability of a specific outcome or condition (e.g., "multiple of 3," "greater than 4," "a prize").

---

## Key Formulas

### [Probability of an Event]

$$
P(E) = \frac{n(E)}{n(S)}
$$

**Variables:**
- $P(E)$ = Probability of event $E$
- $n(E)$ = Number of favorable outcomes
- $n(S)$ = Total number of possible outcomes (Sample Space)

**When to use:** For any single-event probability question.

**Worked example:** In a die throw, $n(S)=6$. For "multiple of 3" ($E=\{3, 6\}$), $n(E)=2$. Thus, $P(E) = \frac{2}{6} = \frac{1}{3}$.

---

## Solution Framework

**Step 1: Identify $n(S)$** — Count every possible outcome that could occur in the experiment.
**Step 2: Identify $n(E)$** — List or count only the outcomes that satisfy the specific condition in the question.
**Step 3: Apply Formula** — Divide the number of favorable outcomes by the total outcomes.
**Step 4: Simplify** — Reduce the resulting fraction to its simplest form.

---

## Shortcut Tricks
No shortcut faster than the standard framework — apply the steps above directly.

---

## Common Mistakes
* **Mistake:** Miscounting $n(S)$ (e.g., forgetting to add prizes and blanks).
    * **Fix:** Always verify the total count by summing all categories provided.
* **Mistake:** Including boundary numbers incorrectly (e.g., including 4 when asked for "greater than 4").
    * **Fix:** Carefully list the set $E$ before counting.
* **Mistake:** Failing to simplify the final fraction.
    * **Fix:** Always check if the numerator and denominator share a common factor.

---

## Worked Example (Step-by-Step)

**Question:** In a lottery, there are 10 prizes and 25 blanks. A lottery is drawn at random. What is the probability of getting a prize?

**Solution:**
1. **Identify $n(S)$:** Total outcomes = $10 \text{ (prizes)} + 25 \text{ (blanks)} = 35$.
2. **Identify $n(E)$:** Favorable outcomes (prizes) = $10$.
3. **Apply Formula:** $P(E) = \frac{10}{35}$.
4. **Simplify:** Divide both by 5: $\frac{10 \div 5}{35 \div 5} = \frac{2}{7}$.

**Answer:** $\frac{2}{7}$

---

## Similar Patterns
* **Permutation/Combination Probability:** Distinguished by the phrase "two items are drawn" or "two dice are thrown," requiring $nCr$ calculations instead of simple counting.

---

## Revision Summary
* **Key formula:** $P(E) = \frac{n(E)}{n(S)}$.
* **Spot it by:** Looking for "probability" and "at random" in the question.
* **First move:** Calculate the total possible outcomes ($n(S)$).
* **Fastest method:** List the favorable outcomes ($n(E)$) and divide.
* **Biggest trap:** Forgetting to simplify the final fraction.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Sample Space ($S$)** — The set of all possible outcomes of an experiment.
* **Event ($E$)** — A subset of the sample space representing the desired outcome.
* **Simplifying Fractions** — Dividing the numerator and denominator by their Greatest Common Divisor (GCD).

### Formulas You Must Know First
No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Unbiased Die** — A standard 6-sided cube with faces numbered 1-6.
* **Face Card** — In this context, cards including Ace, King, Queen, and Jack (4 per suit, 16 total).
* **Random Experiment** — An action where the outcome cannot be predicted with certainty.