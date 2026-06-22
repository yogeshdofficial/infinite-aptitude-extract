# Permutations with Repetition

## Overview
This pattern involves finding the number of ways to arrange the letters of a word when some letters appear more than once. The central idea is to calculate the total permutations as if all letters were unique, then divide by the factorials of the counts of each repeating letter to remove duplicate arrangements.

---

## Recognition Clues
* **Keywords:** "In how many different ways can the letters of the word... be arranged?"
* **Given:** A specific word (e.g., "ENGINEERING", "PRESENT").
* **Asked:** Total number of distinct arrangements.
* **Visual Cue:** Scan the word for letters that appear more than once (e.g., 'E' in 'PRESENT', 'N' and 'E' in 'ENGINEERING').

---

## Key Formulas

### [Permutations of a Multiset]

$$
\text{Arrangements} = \frac{n!}{p_1! \times p_2! \times \dots \times p_k!}
$$

**Variables:**
- $n$ = total number of letters in the word.
- $p_1, p_2, \dots, p_k$ = the frequency (count) of each repeating letter.

**When to use:** Whenever a word contains duplicate letters and you need the total number of unique arrangements.

**Worked example:** For the word 'TOTAL' ($n=5$), 'T' repeats 2 times ($p_1=2$).
Arrangements = $\frac{5!}{2!} = \frac{120}{2} = 60$.

---

## Solution Framework

**Step 1: Count total letters ($n$)** — Determine the length of the word to find the numerator ($n!$).
**Step 2: Identify frequencies** — List every letter and count how many times each appears.
**Step 3: Set up the fraction** — Place $n!$ in the numerator and the product of the factorials of all repeating counts in the denominator.
**Step 4: Simplify and calculate** — Cancel out common factorial terms to solve the division quickly.

---

## Shortcut Tricks

* **Trick:** Cancel the largest factorial in the denominator with the numerator immediately.
* **Why it works:** It reduces the number of multiplications required, preventing large, error-prone numbers.
* **When to use:** Whenever the denominator contains a large factorial (e.g., $7! / 3!$).
* **Example:** For 'RIDDLED' ($7! / 3!$), write $7 \times 6 \times 5 \times 4 \times \frac{3!}{3!} = 7 \times 6 \times 5 \times 4 = 840$.

---

## Common Mistakes

* **Mistake:** Dividing by the number of repetitions instead of the factorial of the repetitions.
    * **Why it happens:** Confusing simple division with permutation logic.
    * **Fix:** Always write the factorial symbol ($!$) next to the count.
* **Mistake:** Miscounting the total number of letters ($n$).
    * **Why it happens:** Skipping letters during a quick scan.
    * **Fix:** Write the word out and number each position.
* **Mistake:** Forgetting to include letters that appear only once.
    * **Why it happens:** Thinking only repeating letters matter.
    * **Fix:** While $1! = 1$ and doesn't change the result, include it in your setup to ensure you haven't missed any letters.

---

## Worked Example (Step-by-Step)

**Question:** How many arrangements can be made out of the letters of the word ‘ENGINEERING’?

**Solution:**
1. **Count total letters:** E-N-G-I-N-E-E-R-I-N-G has 11 letters. $n = 11$.
2. **Identify frequencies:** E(3), N(3), G(2), I(2), R(1).
3. **Set up formula:** $\frac{11!}{3! \times 3! \times 2! \times 2! \times 1!}$.
4. **Calculate:** $\frac{39,916,800}{6 \times 6 \times 2 \times 2 \times 1} = \frac{39,916,800}{144} = 277,200$.

**Answer:** 277,200

---

## Similar Patterns

**Permutations with Constraints:** If the question adds conditions (e.g., "vowels must be together" or "vowels at ends"), this is a *constrained permutation* problem. Use the grouping method (treat the group as one unit) before applying the repetition formula.

---

## Revision Summary

* **Key formula:** $\frac{n!}{p_1! p_2! \dots}$
* **Spot it by:** Looking for words with repeating letters.
* **First move:** Count total letters ($n$) and identify frequencies of repeats.
* **Fastest method:** Cancel the largest denominator factorial against the numerator.
* **Biggest trap:** Dividing by the count instead of the factorial of the count.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$):** The product of all positive integers up to $n$ (e.g., $4! = 4 \times 3 \times 2 \times 1 = 24$).
* **Permutation:** An arrangement of objects where order matters.

### Formulas You Must Know First
* **$n! = n \times (n-1) \times \dots \times 1$**
    * **What it means:** The total ways to arrange $n$ distinct items.
    * **Example:** $3! = 3 \times 2 \times 1 = 6$.

### Terms Used In This Pattern
* **Multiset:** A collection of items where some items are identical.
* **Frequency:** The number of times a specific letter appears in a word.