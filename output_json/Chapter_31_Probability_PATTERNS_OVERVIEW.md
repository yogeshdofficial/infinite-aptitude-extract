# Probability — Chapter Overview

## What This Chapter Is About

Probability is the mathematical study of uncertainty, quantifying the likelihood that a specific outcome will occur within a random experiment. The central relationship is the ratio of the number of favorable outcomes to the total number of possible outcomes in a given scenario. This chapter covers everything from simple coin tosses and dice rolls to complex selections involving cards or colored objects, providing the tools to calculate the odds of single or combined events.

---

## Core Concepts

**[Random Experiment]** — An action where the exact result cannot be predicted in advance, even though all possible outcomes are known. For example, rolling a standard six-sided die is a random experiment because you know the result will be 1 through 6, but you cannot predict which one will appear.

**[Sample Space]** — The complete set of all possible outcomes that can result from an experiment. If you toss two coins, the sample space is {HH, HT, TH, TT}, representing every possible combination of heads and tails.

**[Event]** — A specific subset of the sample space that we are interested in. If you are looking for the probability of getting "at least one head" when tossing two coins, the event is the set {HH, HT, TH}.

**[Equally Likely Outcomes]** — A condition where each individual outcome in the sample space has the same chance of occurring. In a fair die, each face is equally likely to land face up, which allows us to use simple counting to determine probability.

**[Complementary Events]** — The relationship between an event occurring and it not occurring. Since the sum of all probabilities in a sample space must equal 1, the probability of an event not happening is simply 1 minus the probability of it happening.

---

## Key Terms Glossary

**Unbiased/Fair** — A term indicating that an object (like a die or coin) is not weighted or manipulated, ensuring all outcomes are equally likely.

**Suit** — One of the four categories in a deck of cards: Spades, Clubs, Hearts, or Diamonds. Each suit contains 13 cards.

**Face Cards** — The cards in a deck that feature a person: Kings, Queens, and Jacks. There are 12 face cards in a standard 52-card deck.

**At Most/At Least** — Phrases used to define the boundaries of an event. "At most 1 head" means 0 or 1 head; "at least 1 head" means 1 or more heads.

**Intersection ($\cap$)** — The set of outcomes that are common to two different events; it represents the scenario where both events happen simultaneously.

**Union ($\cup$)** — The set of outcomes that belong to either one event, the other, or both; it represents the scenario where at least one of the events occurs.

---

## Pattern Map

**[Basic Probability]** (9 questions) — The simplest form where you directly count favorable outcomes over the total sample space.

**[Logical Events]** (10 questions) — Involves using set theory (unions and intersections) to find the probability of "A or B" occurring.

**[Combinatorial Selection]** (22 questions) — Uses combinations ($^nC_r$) to calculate the sample space and favorable outcomes when selecting multiple items from a group.

**[Multiple Event Probability]** (12 questions) — Focuses on the sequence of events or the probability of multiple independent or dependent occurrences.

**[Complementary Probability]** (3 questions) — Uses the "1 minus" rule to find the probability of an event by calculating the probability of its opposite.

**[Uncategorized]** (1 questions) — Miscellaneous problems that do not fit into the standard classification of the above patterns.

---

## Core Formulas

### Probability of an Event
$$
P(E) = \frac{n(E)}{n(S)}
$$
**Variables:** $n(E)$ = number of favorable outcomes; $n(S)$ = total number of outcomes in the sample space.
**When to use:** Any basic probability problem where outcomes are equally likely.
**Key insight:** Always ensure your sample space $n(S)$ is exhaustive and all outcomes are truly equally likely.
**Worked example:** Rolling a 4 on a die: $n(E)=1, n(S)=6$, so $P(E) = \frac{1}{6}$.

### Addition Rule for Events
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$
**Variables:** $P(A \cup B)$ = probability of A or B; $P(A \cap B)$ = probability of both A and B.
**When to use:** When you need the probability of at least one of two events occurring.
**Key insight:** You must subtract the intersection to avoid double-counting outcomes that belong to both events.
**Worked example:** Probability of drawing a King or a Heart: $P(\text{King}) + P(\text{Heart}) - P(\text{King of Hearts})$.

### Complementary Event Rule
$$
P(\bar{A}) = 1 - P(A)
$$
**Variables:** $P(\bar{A})$ = probability that event A does not occur.
**When to use:** When it is significantly easier to calculate the probability of an event *not* happening than the event itself.
**Key insight:** This is most useful for "at least one" type questions.
**Worked example:** Probability of not rolling a 6: $1 - \frac{1}{6} = \frac{5}{6}$.

---

## Suggested Study Order

1. **Basic Probability** — Start here to master the fundamental ratio of favorable to total outcomes.
2. **Logical Events** — Learn how to combine events using the addition rule and set logic.
3. **Combinatorial Selection** — Move to this once you are comfortable with basic counting, as it introduces $^nC_r$ for larger sets.
4. **Multiple Event Probability** — Study this to understand how outcomes change when multiple actions are performed in sequence.
5. **Complementary Probability** — Study last as a shortcut method to simplify complex problems by looking at the "opposite" scenario.

---

## Chapter-Wide Traps

**Ignoring the "Replacement" condition:** Failing to notice if items are replaced after being drawn changes the total sample space for subsequent events. → Always check if the problem specifies "with replacement" or "without replacement."

**Double-counting the intersection:** Forgetting to subtract the overlap when calculating the probability of "A or B." → Always ask yourself: "Are there any outcomes that satisfy both conditions?" and subtract them if they exist.

**Miscalculating the Sample Space:** Assuming the sample space is always simple when it actually involves complex combinations. → Use combinations ($^nC_r$) whenever the order of selection does not matter.