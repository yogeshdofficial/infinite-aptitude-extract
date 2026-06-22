# Logical Events

## Overview
These questions involve calculating the probability of one event OR another occurring. The central idea is the **Addition Theorem of Probability**, which accounts for overlapping outcomes to prevent double-counting.

---

## Recognition Clues
* **Keywords:** "or", "either... or", "at random".
* **Given:** Probabilities or counts of two distinct categories (e.g., "red card" and "king").
* **Asked:** The probability that a single selection satisfies at least one of the two conditions.
* **Visual:** Look for overlapping sets (e.g., a card that is both a "spade" and a "ten").

---

## Key Formulas

### Addition Theorem of Probability
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Variables:**
- $P(A \cup B)$ = Probability of event A OR event B occurring.
- $P(A)$ = Probability of event A.
- $P(B)$ = Probability of event B.
- $P(A \cap B)$ = Probability of both events occurring simultaneously (the overlap).

**When to use:** Whenever you see "or" between two events that might share common outcomes.

**Worked example:** Drawing a red card ($A$) or a king ($B$). $P(A) = \frac{26}{52}$, $P(B) = \frac{4}{52}$, $P(A \cap B) = \frac{2}{52}$ (the two red kings).
$P(A \cup B) = \frac{26+4-2}{52} = \frac{28}{52} = \frac{7}{13}$.

---

## Solution Framework

1. **Identify $n(S)$:** Determine the total number of possible outcomes (e.g., 52 for a deck of cards).
2. **Define Events:** Clearly identify the two sets $A$ and $B$.
3. **Identify Overlap ($A \cap B$):** Check if any items belong to both sets; if so, count them.
4. **Calculate Favorable Outcomes:** Use $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.
5. **Compute Probability:** Divide the result by $n(S)$ and simplify the fraction.

---

## Shortcut Tricks

* **Trick:** If events are **mutually exclusive** (cannot happen together), $P(A \cap B) = 0$. Just add $n(A) + n(B)$.
* **Why it works:** The formula $P(A) + P(B) - 0$ simplifies to just the sum.
* **When to use:** When the two categories have zero overlap (e.g., "Queen of clubs" and "King of hearts").
* **Example:** $n(E) = 1 + 1 = 2$. $P(E) = \frac{2}{52} = \frac{1}{26}$.

---

## Common Mistakes

* **Double Counting:** Adding $n(A) + n(B)$ without subtracting the overlap. *Fix: Always ask, "Is there any item that fits both descriptions?"*
* **Ignoring Overlap:** Forgetting to count the overlap at all. *Fix: List the specific items that satisfy both conditions.*
* **Simplification Errors:** Failing to reduce the final fraction. *Fix: Divide both numerator and denominator by their Greatest Common Divisor (GCD).*

---

## Worked Example (Step-by-Step)

**Question:** One card is drawn from a pack of 52 cards. What is the probability that the card drawn is either a red card or a king?

**Solution:**
1. **Identify $n(S)$:** Total cards = 52.
2. **Define Events:** $A$ = Red cards (26), $B$ = Kings (4).
3. **Identify Overlap:** The King of Hearts and King of Diamonds are both red and kings. So, $n(A \cap B) = 2$.
4. **Calculate Favorable Outcomes:** $n(A \cup B) = 26 + 4 - 2 = 28$.
5. **Compute Probability:** $P(E) = \frac{28}{52}$. Divide by 4: $\frac{7}{13}$.

**Answer:** $\frac{7}{13}$

---

## Similar Patterns

**Permutation/Combination Probability:** Distinguish by the number of items drawn. If the question asks for "one card," use the Addition Theorem. If it asks for "two cards drawn," you must use combinations ($^nC_r$).

---

## Revision Summary

* **Key formula:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Spot it by:** The word "or" connecting two categories.
* **First move:** Identify the total sample space ($n(S)$).
* **Fastest method:** Subtract the overlap immediately to avoid double counting.
* **Biggest trap:** Adding the two groups without checking for shared items.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Sample Space ($S$)** — The set of all possible outcomes of an experiment.
* **Event ($E$)** — A specific subset of the sample space.
* **Mutually Exclusive** — Two events that cannot happen at the same time.

### Formulas You Must Know First
$$
P(E) = \frac{n(E)}{n(S)}
$$
**What it means:** Probability is the ratio of favorable outcomes to total possible outcomes.

### Terms Used In This Pattern
* **Suit** — One of the four categories in a deck (Hearts, Diamonds, Clubs, Spades).
* **Face Card** — Cards with faces (Jack, Queen, King).
* **Intersection ($\cap$)** — The set of elements common to both sets.