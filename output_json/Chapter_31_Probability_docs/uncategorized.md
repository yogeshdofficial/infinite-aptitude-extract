# Probability of Combined Events (OR)

## Overview
This pattern involves finding the probability of an event occurring when the condition is defined by "OR" (e.g., a number is a multiple of 3 OR 5). The central idea is to identify the favorable outcomes for each condition and subtract the overlap to avoid double-counting.

---

## Recognition Clues
* **Keywords:** "multiple of X or Y", "divisible by X or Y".
* **Given:** A range of numbers (e.g., 1 to 20) or a set of outcomes.
* **Asked:** The probability of a single draw satisfying one of two conditions.

---

## Key Formulas

### [Addition Rule for Probability]

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Variables:**
- $P(A \cup B)$ = Probability of event A OR event B occurring.
- $P(A)$ = Probability of event A.
- $P(B)$ = Probability of event B.
- $P(A \cap B)$ = Probability of both events occurring (the overlap).

**When to use:** When you need to find the probability of one event or another occurring, especially when they share common outcomes.

**Worked example:** For multiples of 3 or 5 up to 20:
$P(3) = \frac{6}{20}$, $P(5) = \frac{4}{20}$, $P(3 \cap 5) = P(15) = \frac{1}{20}$.
$P(3 \cup 5) = \frac{6}{20} + \frac{4}{20} - \frac{1}{20} = \frac{9}{20}$.

---

## Solution Framework

1. **Define Sample Space ($S$):** Identify the total number of possible outcomes ($n(S)$).
2. **List Event A:** Write down all numbers satisfying the first condition.
3. **List Event B:** Write down all numbers satisfying the second condition.
4. **Identify Overlap ($A \cap B$):** Find numbers that appear in both lists (multiples of the LCM of the two numbers).
5. **Calculate Favorable Outcomes ($n(E)$):** Use $n(A) + n(B) - n(A \cap B)$.
6. **Final Probability:** Divide $n(E)$ by $n(S)$ and simplify the fraction.

---

## Shortcut Tricks
* **Trick:** Use the "LCM Overlap" method.
* **Why it works:** The overlap between multiples of $x$ and $y$ is always the set of multiples of $\text{LCM}(x, y)$.
* **When to use:** When the range is large and listing is tedious.
* **Example:** For multiples of 3 or 5 up to 20: Multiples of 3 = $\lfloor 20/3 \rfloor = 6$; Multiples of 5 = $\lfloor 20/5 \rfloor = 4$; Multiples of 15 (LCM) = $\lfloor 20/15 \rfloor = 1$. Total = $6 + 4 - 1 = 9$.

---

## Common Mistakes
* **Mistake:** Counting the overlap twice (e.g., counting 15 as both a multiple of 3 and 5).
* **Why it happens:** Forgetting the subtraction step in the addition rule.
* **Fix:** Always check if the LCM of the two numbers falls within the given range.
* **Mistake:** Miscounting the total sample space.
* **Why it happens:** Assuming the range is 1 to $N$ without checking if it's inclusive.
* **Fix:** Verify the range boundaries (e.g., 1 to 20 includes both 1 and 20).

---

## Worked Example (Step-by-Step)

**Question:** Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?

**Solution:**
1. **Sample Space:** Total tickets = 20. $n(S) = 20$.
2. **Event A (Multiples of 3):** $\{3, 6, 9, 12, 15, 18\}$. $n(A) = 6$.
3. **Event B (Multiples of 5):** $\{5, 10, 15, 20\}$. $n(B) = 4$.
4. **Overlap ($A \cap B$):** The number 15 is in both lists. $n(A \cap B) = 1$.
5. **Favorable Outcomes:** $n(E) = 6 + 4 - 1 = 9$.
6. **Probability:** $P(E) = \frac{9}{20}$.

**Answer:** $\frac{9}{20}$

---

## Similar Patterns
* **Independent Events:** If the question asks for "AND" (e.g., drawing two tickets), you multiply probabilities instead of adding them.

---

## Revision Summary
* **Key formula:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Spot it by:** "OR" condition between two sets of multiples.
* **First move:** List multiples for both conditions.
* **Fastest method:** Use $\lfloor \text{Range} / \text{Number} \rfloor$ to count multiples.
* **Biggest trap:** Double-counting the LCM of the two numbers.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Sample Space** — The set of all possible outcomes of an experiment.
* **Event** — A specific subset of the sample space.
* **LCM (Least Common Multiple)** — The smallest number that is a multiple of two or more numbers.

### Formulas You Must Know First
* **Probability Definition:** $P(E) = \frac{n(E)}{n(S)}$.
    * *Meaning:* The ratio of favorable outcomes to total possible outcomes.
    * *Example:* In a set of 10, picking a number < 3 (i.e., 1, 2) is $\frac{2}{10} = \frac{1}{5}$.

### Terms Used In This Pattern
* **Multiple** — A number that can be divided by another number without a remainder.
* **Random** — An outcome chosen without bias or specific pattern.