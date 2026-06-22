# Vowels Constraints

## Overview
These questions ask you to arrange letters of a word while satisfying specific conditions regarding vowel placement (e.g., "at ends," "never together," or "only at odd positions"). The central idea is to treat the arrangement as a multi-step process: group or isolate the vowels first, arrange the remaining letters, and then combine the results using the Fundamental Principle of Counting.

---

## Recognition Clues
* **Keywords:** "vowels at ends," "vowels never together," "vowels occupy odd positions."
* **Given:** A word with a specific number of vowels and consonants.
* **Asked:** The total number of different ways to arrange the letters under the stated constraint.

---

## Key Formulas

### [Permutation of n distinct items]
$$
n! = n \times (n-1) \times \dots \times 1
$$
**Variables:** $n$ = total number of distinct items to be arranged.
**When to use:** When arranging all items in a row without restrictions.
**Worked example:** For the word 'DESIGN' (6 letters), total arrangements = $6! = 720$.

### [Permutation of r items in n positions]
$$
^nP_r = \frac{n!}{(n-r)!}
$$
**Variables:** $n$ = total available positions, $r$ = number of items to place.
**When to use:** When placing a subset of items into specific restricted slots (e.g., vowels in odd positions).
**Worked example:** For 'MACHINE', 3 vowels in 4 odd positions = $^4P_3 = 4 \times 3 \times 2 = 24$.

---

## Solution Framework

1. **Step 1: Categorize** — Identify and count the number of vowels and consonants in the word.
2. **Step 2: Handle Constraints** — If vowels must be together, treat them as one unit. If they must be at ends or specific positions, isolate those slots first.
3. **Step 3: Arrange Restricted Items** — Calculate the number of ways to arrange the vowels in their required positions.
4. **Step 4: Arrange Remaining Items** — Calculate the number of ways to arrange the consonants (and any remaining letters) in the remaining slots.
5. **Step 5: Multiply** — Multiply the results of Step 3 and Step 4 to get the final answer.

---

## Shortcut Tricks
* **Trick:** For "vowels never together," use the **Gap Method** or **Subtraction Method**: Total arrangements minus arrangements where vowels are together.
* **Why it works:** It is mathematically easier to calculate the "together" case and subtract it from the total than to calculate all "never together" permutations directly.
* **When to use it:** Whenever the question asks for "never together" or "not adjacent."
* **Example:** For 'DIGEST', Total ($6! = 720$) - Together ($5! \times 2! = 240$) = $480$.

---

## Common Mistakes
* **Mistake:** Forgetting to arrange the vowels *within* their group (e.g., treating 'IE' as one unit but forgetting it can be 'EI').
* **Why it happens:** Focusing only on the position of the unit and ignoring internal permutations.
* **Fix:** Always multiply by the factorial of the number of items inside the "unit."
* **Mistake:** Adding instead of multiplying the arrangements of vowels and consonants.
* **Why it happens:** Misunderstanding the Fundamental Principle of Counting.
* **Fix:** If the task is "do A AND do B," always multiply.

---

## Worked Example (Step-by-Step)

**Question:** In how many different ways can the letters of the word ‘MACHINE’ be arranged so that the vowels may occupy only the odd positions?

**Solution:**
1. **Categorize:** MACHINE has 7 letters: 3 vowels (A, I, E) and 4 consonants (M, C, H, N).
2. **Identify Slots:** Positions are (1, 2, 3, 4, 5, 6, 7). Odd positions are 1, 3, 5, 7 (4 slots).
3. **Arrange Vowels:** We need to place 3 vowels in 4 odd slots: $^4P_3 = 4 \times 3 \times 2 = 24$.
4. **Arrange Consonants:** We have 4 consonants left for the 4 remaining positions: $4! = 24$.
5. **Multiply:** $24 \times 24 = 576$.

**Answer:** 576

---

## Similar Patterns
* **Arrangements with Alike Letters:** If the word has repeating letters (e.g., 'ENGINEERING'), you must divide by the factorial of the count of each repeating letter. This pattern assumes all letters are distinct.

---

## Revision Summary
* **Key formula:** $n!$ and $^nP_r$.
* **Spot it by:** Looking for "vowels" and "positions" or "together" in the prompt.
* **First move:** Separate vowels from consonants and identify the restricted slots.
* **Fastest method:** Subtraction method for "never together" cases.
* **Biggest trap:** Forgetting to arrange the vowels internally when they are grouped.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$)** — The product of all positive integers up to $n$.
* **Fundamental Principle of Counting** — If one event can occur in $m$ ways and a second in $n$ ways, both can occur in $m \times n$ ways.
* **Permutation** — An arrangement of items where order matters.

### Formulas You Must Know First
$$
n! = n \times (n-1) \times \dots \times 1
$$
**What it means:** The number of ways to arrange $n$ distinct objects in a row.
**Example:** $3! = 3 \times 2 \times 1 = 6$.

### Terms Used In This Pattern
* **Vowel** — The letters A, E, I, O, U.
* **Consonant** — Any letter that is not a vowel.
* **Unit** — A group of letters treated as a single entity for calculation purposes.