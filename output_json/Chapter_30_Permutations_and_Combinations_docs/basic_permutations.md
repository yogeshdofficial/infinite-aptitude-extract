# Basic Permutations

## Overview
This pattern involves finding the total number of ways to arrange all letters of a given word. The central idea is that if a word has $n$ distinct letters, the total number of unique arrangements is the factorial of $n$ ($n!$).

---

## Recognition Clues
* **Keywords:** "In how many different ways can the letters of the word... be arranged?"
* **Given:** A single word (e.g., "FIGHT", "DISPLAY").
* **Asked:** The total number of possible permutations of all letters.
* **Condition:** All letters in the word must be distinct (no repeating letters).

---

## Key Formulas

### Factorial Arrangement
$$
n! = n \times (n-1) \times (n-2) \times \dots \times 1
$$

**Variables:**
- $n$ = total number of distinct letters in the word.
- $n!$ = the total number of unique arrangements.

**When to use:** When you need to arrange *all* letters of a word where every letter is unique.

**Worked example:** For the word "FIGHT", $n=5$.
Calculation: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.

---

## Solution Framework

**Step 1: Count the letters** — Determine the total number of letters ($n$) in the given word.
**Step 2: Verify uniqueness** — Ensure no letters repeat (if they do, this specific pattern does not apply).
**Step 3: Apply factorial** — Calculate $n!$ by multiplying all integers from $n$ down to 1.
**Step 4: Finalize** — The resulting product is the total number of arrangements.

---

## Shortcut Tricks

* **Trick:** Memorize factorials up to $7!$.
* **Why it works:** Most exam questions use words with 5 to 7 letters; knowing $5!=120$, $6!=720$, and $7!=5040$ saves 30+ seconds of manual multiplication.
* **When to use it:** When the word length is between 5 and 7 letters.
* **Example:** For "GAMBLE" ($n=6$), immediately write 720 instead of calculating $6 \times 5 \times 4 \times 3 \times 2 \times 1$.

---

## Common Mistakes

* **Mistake:** Miscounting the number of letters.
    * **Why it happens:** Skipping a letter while counting.
    * **Fix:** Write the letters out individually and number them.
* **Mistake:** Assuming letters repeat when they don't.
    * **Why it happens:** Rushing through the word.
    * **Fix:** Quickly scan the word for duplicates before starting the calculation.
* **Mistake:** Arithmetic errors in large factorials.
    * **Why it happens:** Trying to do $9!$ in one go.
    * **Fix:** Break the multiplication into smaller chunks (e.g., $9 \times 8 = 72$, then multiply by $7$, etc.).

---

## Worked Example (Step-by-Step)

**Question:** In how many different ways can the letters of the word ‘BAKERY’ be arranged?

**Solution:**
1. **Count the letters:** B, A, K, E, R, Y. Total $n = 6$.
2. **Verify uniqueness:** All letters are distinct.
3. **Apply factorial:** We need $6!$.
4. **Calculate:** $6 \times 5 \times 4 \times 3 \times 2 \times 1$.
   - $6 \times 5 = 30$
   - $30 \times 4 = 120$
   - $120 \times 3 = 360$
   - $360 \times 2 = 720$

**Answer:** 720

---

## Similar Patterns

**Permutations with Repeating Letters:** If the word contains repeating letters (e.g., "ENGINEERING"), you must divide $n!$ by the factorial of the count of each repeating letter.

---

## Revision Summary

* **Key formula:** $n! = n \times (n-1) \times \dots \times 1$.
* **Spot it by:** "In how many ways can the letters of [WORD] be arranged?"
* **First move:** Count the letters and check for duplicates.
* **Fastest method:** Memorize $5!=120, 6!=720, 7!=5040$.
* **Biggest trap:** Miscounting the total number of letters.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial** — The product of an integer and all the integers below it down to 1, denoted by $n!$.
* **Permutation** — An arrangement of objects in a specific order.

### Formulas You Must Know First
No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Distinct** — Unique; no two items are the same.
* **Arrangement** — A specific sequence or order of items.