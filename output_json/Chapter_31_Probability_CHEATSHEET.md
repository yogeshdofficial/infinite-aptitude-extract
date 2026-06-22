# Probability — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Sample Space:** Determine the total number of possible outcomes ($n(S)$).
2. **Identify Event:** Determine the specific condition required ($n(E)$).
3. **Check for Selection:** If picking multiple items, use Combinations ($^nC_r$). If order matters, use Permutations (rare).
4. **Check for Logical Operators:** If "OR" appears, use $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. If "AND" appears, multiply probabilities.
5. **Check for "At Least One":** If "at least one" is present, calculate $1 - P(\text{none})$.
6. **Calculate Ratio:** Divide favorable outcomes by total outcomes and simplify the fraction.
7. **Sanity Check:** Ensure $0 \le P(E) \le 1$. If the answer is $>1$ or $<0$, re-check your counting.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Basic | "at random", "probability of" | Total set, condition | $P(E)$ |
| Combinatorial | "drawn together", "balls/cards" | Group size, selection | $P(E)$ |
| Complementary | "at least one" | Total items, subset | $P(\text{at least one})$ |
| Logical Events | "or", "either...or" | Two events | $P(A \cup B)$ |
| Multiple Event | "tossed", "thrown together" | Multiple trials | $P(\text{combined})$ |
| Uncategorized | "multiple of X or Y" | Range, divisors | $P(A \cup B)$ |

---

## Formula Bank

**[Basic Probability]**
$$P(E) = \frac{n(E)}{n(S)}$$
→ *produces: probability of simple event*
→ *use when: single trial, clear outcomes*

**[Combinatorial Selection]**
$$^nC_r = \frac{n!}{r!(n-r)!}$$
→ *produces: number of ways to select*
→ *use when: picking multiple items together*

$$P(E) = \frac{\text{Favorable Combinations}}{\text{Total Combinations}}$$
→ *produces: probability of selection*
→ *use when: drawing multiple items*

**[Complementary Probability]**
$$P(A) = 1 - P(A^c)$$
→ *produces: probability of event*
→ *use when: "at least one" appears*

**[Logical Events]**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
→ *produces: probability of A or B*
→ *use when: events are not exclusive*

**[Multiple Event Probability]**
$$P(E) = 1 - P(\text{not } E)$$
→ *produces: probability of event*
→ *use when: easier to count failure*

**[Uncategorized]**
$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$
→ *produces: count of favorable items*
→ *use when: finding multiples of X or Y*

---

## Step Sequences

**Basic:** Count total → Count favorable → Divide → Simplify.
**Combinatorial:** Calculate total combinations → Calculate favorable combinations → Divide → Simplify.
**Complementary:** Find total ways → Find "none" ways → Subtract from 1.
**Logical Events:** Find $P(A)$ → Find $P(B)$ → Subtract intersection → Sum.
**Multiple Event:** Define sample space → List favorable outcomes → Divide → Simplify.
**Uncategorized:** Count multiples of A → Count multiples of B → Subtract common multiples → Divide.

---

## Fastest Tricks

* **Basic:** For multiples up to $N$, use $\lfloor \frac{N}{\text{divisor}} \rfloor$ to find count.
* **Combinatorial:** For 2 cards, total ways is $\frac{n(n-1)}{2}$.
* **Complementary:** "At least one" is always $1 - P(\text{none})$.
* **Multiple Event:** For dice sums $>7$, count is $5, 4, 3, 2, 1$ for sums $8, 9, 10, 11, 12$.
* **Logical:** If events are mutually exclusive, $P(A \cap B) = 0$.

---

## Trap Watch

* **Basic:** Including boundary numbers → check range carefully.
* **Combinatorial:** Using permutations instead of combinations → use $^nC_r$.
* **Complementary:** Forgetting to subtract from 1 → always do $1 - P$.
* **Logical:** Double counting the intersection → subtract $P(A \cap B)$.
* **Multiple Event:** Miscounting sample space for dice → use $6^n$.

---

## Last-Minute Reminders

* The probability of any event must always be between 0 and 1 inclusive.
* When drawing cards, remember that the deck size decreases if drawing without replacement.
* A "multiple of 3" includes 3, 6, 9, 12, etc.; do not stop at 6.
* "At most one head" in two coin tosses includes zero heads and one head.
* Always simplify your final fraction to its lowest terms to match exam options.