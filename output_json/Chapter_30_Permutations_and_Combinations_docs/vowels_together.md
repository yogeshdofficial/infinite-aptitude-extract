# Vowels Together

## Overview
This pattern involves arranging letters of a word such that all vowels are kept together as a single block. The central idea is to treat the vowel group as one "super-letter" and then multiply the arrangements of the resulting units by the internal arrangements of the vowels within that block.

---

## Recognition Clues
* **Keywords:** "vowels always come together," "vowels together," "vowels adjacent."
* **Given:** A word with a specific number of letters (some may repeat).
* **Asked:** Total number of possible arrangements (permutations).

---

## Key Formulas

### [Total Arrangements]
$$
\text{Total} = (\text{Arrangements of units}) \times (\text{Internal arrangements of vowels})
$$

**Variables:**
- $\text{Arrangements of units}$: Permutations of the consonants plus the one vowel block.
- $\text{Internal arrangements}$: Permutations of the vowels within the block.

**When to use:** Every question where vowels must be grouped together.

**Worked example:** For 'JUDGE' (5 letters, vowels U, E):
- Units: J, D, G, (UE) = 4 units. $4! = 24$.
- Internal: (U, E) = 2 vowels. $2! = 2$.
- Total: $24 \times 2 = 48$.

---

## Solution Framework

**Step 1: Identify and separate** — List all vowels and consonants in the word.
**Step 2: Create the block** — Treat all vowels as a single unit (the "vowel block").
**Step 3: Count total units** — Count the consonants plus the 1 vowel block.
**Step 4: Arrange units** — Calculate permutations of these units (use $\frac{n!}{p!}$ if there are repeated letters).
**Step 5: Arrange vowels** — Calculate permutations of the vowels inside the block.
**Step 6: Multiply** — Multiply the results of Step 4 and Step 5 to get the final answer.

---

## Shortcut Tricks
* **Trick:** If the word has no repeated letters, the answer is $(n-k+1)! \times k!$ where $n$ is total letters and $k$ is the number of vowels.
* **Why it works:** It combines the steps into a single algebraic expression for distinct letters.
* **When to use it:** Only when all letters in the word are distinct (e.g., DAUGHTER, SOFTWARE).
* **Example:** For 'DAUGHTER' ($n=8, k=3$): $(8-3+1)! \times 3! = 6! \times 3! = 720 \times 6 = 4320$.

---

## Common Mistakes
* **Mistake:** Forgetting to multiply by internal vowel arrangements.
    * **Why it happens:** Treating the vowel block as a single fixed entity rather than a group that can be rearranged.
    * **Fix:** Always multiply by $k!$ (where $k$ is the number of vowels).
* **Mistake:** Ignoring repeated consonants when arranging the units.
    * **Why it happens:** Assuming all units are distinct.
    * **Fix:** Use $\frac{n!}{p!}$ if any consonants repeat.

---

## Worked Example (Step-by-Step)

**Question:** In how many different ways can the letters of the word ‘DIRECTOR’ be arranged so that the vowels are always together?

**Solution:**
1. **Identify:** Vowels are {I, E, O}. Consonants are {D, R, C, T, R}.
2. **Block:** Treat (IEO) as 1 unit.
3. **Units:** {D, R, C, T, R} + (IEO) = 6 units.
4. **Arrange Units:** The 6 units contain two R's. Arrangements = $\frac{6!}{2!} = \frac{720}{2} = 360$.
5. **Arrange Vowels:** The 3 vowels (I, E, O) are distinct. Arrangements = $3! = 6$.
6. **Multiply:** $360 \times 6 = 2160$.

**Answer:** 2160

---

## Similar Patterns
* **Vowels Never Together:** Use the "Gap Method" (arrange consonants first, then place vowels in the gaps between them).

---

## Revision Summary
* **Key formula:** $(\text{Units})! \times (\text{Vowels})!$ (adjust for repeats).
* **Spot it by:** "Vowels always come together" in the question.
* **First move:** Group all vowels into one single block.
* **Fastest method:** Calculate unit permutations $\times$ internal vowel permutations.
* **Biggest trap:** Forgetting to divide by repeats or forgetting internal vowel arrangements.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factorial ($n!$)** — The product of all positive integers up to $n$ ($n! = n \times (n-1) \times \dots \times 1$).
* **Permutations with Repetition** — If an object repeats $p$ times, divide the total permutations by $p!$.

### Formulas You Must Know First
$$
n! = n \times (n-1) \times \dots \times 1
$$
**What it means:** The number of ways to arrange $n$ distinct items.
**Example:** $3! = 3 \times 2 \times 1 = 6$.

### Terms Used In This Pattern
* **Vowel** — The letters A, E, I, O, U.
* **Consonant** — Any letter that is not a vowel.
* **Unit** — A single item or a group treated as one item for arrangement purposes.