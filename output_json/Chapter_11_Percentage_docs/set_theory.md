# Set Theory

## Overview
This pattern deals with problems involving two overlapping groups (e.g., students failing in two subjects or people reading two newspapers). The central idea is the **Inclusion-Exclusion Principle**, which prevents double-counting the individuals who belong to both groups.

---

## Recognition Clues
* **Keywords:** "Failed in both," "Passed in both," "Read both," "At least one," "Neither."
* **Given:** Percentages or counts for two individual groups and their intersection (both).
* **Asked:** The percentage/count of those who passed/failed in both, or those who did neither.
* **Visual:** If you see two categories and an overlap, it is a Set Theory problem.

---

## Key Formulas

### Inclusion-Exclusion Principle
$$
n(A \cup B) = n(A) + n(B) - n(A \cap B)
$$

**Variables:**
- $n(A \cup B)$ = Total percentage/number in at least one group (A or B or both).
- $n(A)$ = Total in group A.
- $n(B)$ = Total in group B.
- $n(A \cap B)$ = Those in both groups (the overlap).

**When to use:** To find the total coverage of two groups or to find the overlap when the total is known.

**Worked example:** If 35% fail Hindi ($A$) and 45% fail English ($B$) with 20% in both ($A \cap B$):
$n(A \cup B) = 35 + 45 - 20 = 60\%$.

---

## Solution Framework

1. **Identify the sets:** Define $A$ and $B$ based on the categories (e.g., Hindi/English).
2. **Standardize the units:** Ensure all values are either percentages or absolute numbers.
3. **Apply the formula:** Calculate $n(A \cup B)$ using $n(A) + n(B) - n(A \cap B)$.
4. **Find the complement:** If the question asks for "neither" or "passed both," subtract your result from 100% (or the total population).
5. **Solve for $x$:** If the total population is unknown, equate the calculated percentage to the given absolute number to find $x$.

---

## Shortcut Tricks

* **Trick:** To find "Neither," use: $100 - (A + B - \text{Both})$.
* **Why it works:** It calculates the union first (those who did at least one) and subtracts it from the total.
* **When to use:** When the question asks for the percentage of people who did not participate in either activity.
* **Example:** Q354: $100 - (40 + 50 - 10) = 100 - 80 = 20\%$.

---

## Common Mistakes

* **Mistake:** Adding $n(A) + n(B)$ without subtracting the intersection.
    * **Why it happens:** Forgetting that people in "both" are counted twice.
    * **Fix:** Always subtract the intersection.
* **Mistake:** Confusing "failed" sets with "passed" sets.
    * **Why it happens:** Not checking if the question asks for the complement.
    * **Fix:** Clearly label your sets as "Failed" or "Passed" at the start.

---

## Worked Example (Step-by-Step)

**Question:** In an examination, 80% of the students passed in English, 85% in Mathematics and 75% in both. If 40 students failed in both, find the total number of students.

**Solution:**
1. **Identify sets:** $A$ = Passed English (80%), $B$ = Passed Math (85%), $A \cap B$ = Passed both (75%).
2. **Calculate Union:** $n(A \cup B) = 80 + 85 - 75 = 90\%$. (These are students who passed at least one).
3. **Find Complement:** Students who failed both = $100\% - 90\% = 10\%$.
4. **Solve for $x$:** We know $10\%$ of $x = 40$.
5. **Final Calculation:** $\frac{10}{100} \times x = 40 \implies x = 400$.

**Answer:** 400 students.

---

## Similar Patterns
**Venn Diagram Problems:** This is the same as Set Theory; use the formula above to avoid drawing complex diagrams under time pressure.

---

## Revision Summary
* **Key formula:** $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.
* **Spot it by:** Overlapping groups and "both" keywords.
* **First move:** Define your sets (e.g., all "failed" or all "passed").
* **Fastest method:** Use the formula directly; don't draw diagrams.
* **Biggest trap:** Forgetting to subtract the overlap.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage:** A fraction of 100.
* **Complement:** The remaining part of a whole (e.g., if 60% failed, 40% passed).

### Formulas You Must Know First
* **Percentage of a number:** $\frac{P}{100} \times \text{Total}$.

### Terms Used In This Pattern
* **Intersection ($A \cap B$):** The group belonging to both categories.
* **Union ($A \cup B$):** The group belonging to at least one category.