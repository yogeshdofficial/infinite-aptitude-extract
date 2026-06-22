# Permutations And Combinations — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Order:** Does the order of selection matter? If **Yes** (arrangements, seating, words), use **Permutations**. If **No** (committees, groups, teams), use **Combinations**.
2. **Check Constraints:** Are there restrictions? (e.g., "vowels together," "at least one," "odd positions").
3. **Handle Repetition:** Are there identical items? If **Yes**, divide by the factorial of the count of each repeating item.
4. **Apply Grouping:** If items must be together, treat the group as one single unit, then multiply by the internal arrangements of that unit.
5. **Calculate:** Use the appropriate formula ($n!$, $^nP_r$, or $^nC_r$).
6. **Sanity Check:** Ensure the result is a positive integer and fits the logical constraints of the problem.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Basic Permutations | "Arranged", "Different ways" | Distinct items | Total arrangements |
| Combinations/Committees | "Chosen", "Selected", "Committee" | Total items, group size | Number of ways |
| Logical Arrangements | "Choices", "Fail to", "Set" | Options, constraints | Total possibilities |
| Mathematical Eval | "Evaluate", "Calculate" | Factorials, P, C | Numerical value |
| Permutations w/ Repetition | "Letters of the word" | Word with repeats | Unique arrangements |
| Vowels Constraints | "Ends", "Odd positions" | Word, position rule | Valid arrangements |
| Vowels Together | "Always together" | Word, vowel group | Valid arrangements |

---

## Formula Bank

**[Basic Permutations]**
$$n! = n \times (n-1) \times \dots \times 1$$
→ *produces: total distinct arrangements*
→ *use when: all items are distinct*

**[Combinations and Committees]**
$$^nC_r = \frac{n!}{r!(n-r)!}$$
→ *produces: number of unique groups*
→ *use when: order does not matter*

$$^nC_r = ^nC_{n-r}$$
→ *produces: simplified combination value*
→ *use when: $r > \frac{n}{2}$*

**[Logical Arrangements]**
$$\text{Total} = n^k$$
→ *produces: total possible outcomes*
→ *use when: $n$ choices for $k$ slots*

**[Mathematical Evaluations]**
$$^nP_r = \frac{n!}{(n-r)!}$$
→ *produces: ordered arrangements*
→ *use when: selecting $r$ from $n$*

$$^nP_2 - ^nC_2 = ^nC_2$$
→ *produces: difference value*
→ *use when: comparing P and C*

**[Permutations with Repetition]**
$$\text{Arrangements} = \frac{n!}{p!q!r!\dots}$$
→ *produces: unique arrangements*
→ *use when: items repeat $p, q, r$ times*

**[Vowels Constraints]**
$$^nP_r = \frac{n!}{(n-r)!}$$
→ *produces: restricted arrangements*
→ *use when: specific positions required*

**[Vowels Together]**
$$\text{Total} = (n-k+1)! \times k!$$
→ *produces: arrangements with block*
→ *use when: $k$ items must stay together*

---

## Step Sequences
- **Basic Permutations:** Count letters → Apply $n!$ → Calculate.
- **Combinations:** Identify $n$ and $r$ → Apply $^nC_r$ → Simplify.
- **Logical Arrangements:** Identify choices ($n$) → Identify slots ($k$) → Calculate $n^k$.
- **Mathematical Eval:** Expand factorials → Cancel common terms → Multiply.
- **Permutations w/ Repetition:** Count total ($n$) → Count repeats ($p, q$) → Divide $n!$ by $p!q!$.
- **Vowels Constraints:** Fix restricted positions → Arrange remaining items → Multiply.
- **Vowels Together:** Group vowels as 1 unit → Count total units → Multiply by internal vowel permutations.

---

## Fastest Tricks
- **Combinations:** Use $^nC_r = ^nC_{n-r}$ to always pick the smaller $r$.
- **Factorials:** $\frac{50!}{48!} = 50 \times 49$; never calculate the full factorial.
- **Vowels Together:** Treat the block as one item, then multiply by internal arrangements.
- **Permutations:** $^nP_2 = n(n-1)$ and $^nC_2 = \frac{n(n-1)}{2}$.

---

## Trap Watch
- **Combinations:** Using permutations instead of combinations → Use $^nC_r$ for groups.
- **Repetition:** Forgetting to divide by repeated letter factorials → Divide by $p!$.
- **Vowels Together:** Forgetting to arrange the vowel block internally → Multiply by $k!$.
- **Factorials:** Assuming $0! = 0$ → Remember $0! = 1$.

---

## Last-Minute Reminders
- Always verify if the question implies order (Permutation) or selection (Combination).
- When items must be together, the group counts as one single unit plus the remaining items.
- If a question asks for "at least one," calculate the total and subtract the "none" case.
- Always simplify fractions by canceling out the largest factorial in the denominator.
- Double-check the count of letters in a word before applying any formula.