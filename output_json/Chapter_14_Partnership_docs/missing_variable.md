# Missing Variable

## Overview
This pattern involves finding an unknown time period or capital amount in a partnership business. The central idea is that the profit ratio is always equal to the ratio of the product of capital and time for each partner.

---

## Recognition Clues
* **Keywords:** "After how many months did [Name] join?", "C's capital was...", "value of x is".
* **Given:** Total profit, individual investments, and time durations (with one variable $x$).
* **Asked:** The missing time $x$ or the missing capital $x$.
* **Structure:** A mix of fixed values and an algebraic variable $x$ representing a duration or investment.

---

## Key Formulas

### [Profit Ratio Formula]
$$
\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}
$$

**Variables:**
- $P_1, P_2$ = Profit shares of partner 1 and 2
- $C_1, C_2$ = Capital invested by partner 1 and 2
- $T_1, T_2$ = Time period for which capital was invested

**When to use:** When comparing two partners' shares to find a missing time or capital.

**Worked example:** A invests 76000 for 12 months, B invests 57000 for $(12-x)$ months. Profit ratio is $2:1$.
$\frac{76000 \times 12}{57000 \times (12-x)} = \frac{2}{1} \implies \frac{16}{12-x} = 2 \implies 12-x = 8 \implies x=4$.

---

## Solution Framework

1. **Define the variable:** Assign $x$ to the unknown (usually months joined or capital amount).
2. **Determine time units:** Express each partner's time as a function of $x$ (e.g., $12-x$ for someone joining late).
3. **Set up the ratio:** Write the equation: $\text{Ratio} = \frac{C_1 \times T_1}{C_2 \times T_2}$.
4. **Simplify:** Reduce the capital values (divide by common factors) before multiplying.
5. **Solve for $x$:** Use basic algebra to isolate $x$.

---

## Shortcut Tricks

* **Trick:** Simplify the capital ratio first.
* **Why it works:** Large numbers like 76000 and 57000 share common factors (19000); reducing them to 4:3 makes the equation trivial.
* **When to use:** Always, before performing any multiplication.
* **Example:** $76000:57000$ becomes $4:3$. The equation $\frac{4 \times 12}{3 \times (12-x)} = \frac{2}{1}$ is solved in seconds.

---

## Common Mistakes

* **Mistake:** Using $x$ for the time a partner was in the business instead of $(12-x)$.
    * **Why it happens:** Forgetting that $x$ is the time *after* which they joined.
    * **Fix:** Always write "Time = Total Time - $x$".
* **Mistake:** Forgetting to include the new partner's capital in the total capital sum.
    * **Why it happens:** Treating the total capital as fixed when it includes the unknown $x$.
    * **Fix:** Always write the denominator as the sum of all individual investments.

---

## Worked Example (Step-by-Step)

**Question:** A invested ₹ 76000. After few months, B joined with ₹ 57000. At the end of the year, profit was divided 2 : 1. After how many months did B join?

**Solution:**
1. **Define:** Let B join after $x$ months. B's time = $(12-x)$.
2. **Ratio:** $\frac{A_{cap} \times A_{time}}{B_{cap} \times B_{time}} = \frac{2}{1}$.
3. **Substitute:** $\frac{76000 \times 12}{57000 \times (12-x)} = \frac{2}{1}$.
4. **Simplify:** $\frac{4 \times 12}{3 \times (12-x)} = 2 \implies \frac{16}{12-x} = 2$.
5. **Solve:** $16 = 24 - 2x \implies 2x = 8 \implies x = 4$.

**Answer:** B joined after 4 months.

---

## Similar Patterns

**Simple Partnership:** If all partners invest for the same time, the time variable $T$ cancels out. Look for "at the end of the year" for all partners to identify this.

---

## Revision Summary

* **Key formula:** $\text{Profit Ratio} = \frac{C_1 \times T_1}{C_2 \times T_2}$.
* **Spot it by:** Missing $x$ in time or capital with a given profit ratio.
* **First move:** Simplify the capital ratio by dividing by common factors.
* **Fastest method:** Cross-multiply after simplifying the ratio.
* **Biggest trap:** Using $x$ as the investment time instead of $(12-x)$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratios:** Understanding that $a:b = \frac{a}{b}$.
* **Linear Equations:** Solving $ax + b = c$ for $x$.

### Formulas You Must Know First
* **Profit Sharing:** $\text{Profit} \propto \text{Capital} \times \text{Time}$.

### Terms Used In This Pattern
* **Capital:** The amount of money invested in the business.
* **Partnership:** A business arrangement where profits are shared based on investment and time.