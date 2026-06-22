# Installment Payments

## Overview
This pattern involves clearing a debt (or purchasing an item) through equal periodic installments under compound interest. The central idea is that the **total debt** must equal the **sum of the present values (P.V.)** of all individual installments.

---

## Recognition Clues
* **Keywords:** "Annual payment," "equal annual installments," "discharge a debt," "cash down payment."
* **Given:** Total debt amount, interest rate ($R\%$), and number of installments ($n$).
* **Asked:** The value of each equal installment ($x$).
* **Scenario:** You see a "cash price" vs. "installment plan" comparison or a loan repayment schedule.

---

## Key Formulas

### Present Value of Installments
$$
\text{Total Debt} = \frac{x}{(1+r)^1} + \frac{x}{(1+r)^2} + \dots + \frac{x}{(1+r)^n}
$$

**Variables:**
- $x$ = value of each equal installment
- $r$ = rate of interest per period (e.g., $5\% = 0.05$)
- $n$ = number of installments

**When to use:** To find the installment amount when the total debt and interest rate are known.

**Worked example:** Debt of ₹ 2550, $R=4\%$, $n=2$.
$\frac{x}{1.04} + \frac{x}{(1.04)^2} = 2550 \Rightarrow \frac{25x}{26} + \frac{625x}{676} = 2550$. Solving gives $x = 1352$.

---

## Solution Framework

**Step 1: Calculate the net debt.** If a down payment is made, subtract it from the total cost first: $\text{Net Debt} = \text{Total Price} - \text{Down Payment}$.

**Step 2: Set up the P.V. equation.** Write the sum of the present values of $n$ installments equal to the Net Debt.

**Step 3: Simplify the fractions.** Convert $(1+r)$ to a simple fraction (e.g., $1.05 = \frac{21}{20}$) to make calculations easier.

**Step 4: Solve for $x$.** Find a common denominator for the fractions and solve the resulting linear equation for $x$.

---

## Shortcut Tricks

**Trick:** Use the "Ratio Method" for 2 or 3 installments. If $r = \frac{1}{k}$, the installments are proportional to $(k+1)^n, (k+1)^{n-1}k, \dots$

**Why it works:** It eliminates the need to write out the full P.V. summation by clearing denominators immediately.

**When to use:** When $n=2$ or $n=3$ and the interest rate is a simple fraction.

**Example:** For $R=10\% = \frac{1}{10}$, $n=2$. The installments are in ratio $(11)^2 : 11 \times 10$ (i.e., $121:110$). Total units = $121+110 = 231$.

---

## Common Mistakes

* **Mistake:** Calculating installments on the full price instead of the balance after the down payment.
    * **Fix:** Always subtract the down payment before starting the P.V. equation.
* **Mistake:** Treating compound interest installments like simple interest (adding them directly).
    * **Fix:** Remember that money has time value; you must discount each installment by $(1+r)^n$.
* **Mistake:** Arithmetic errors in squaring or cubing the denominator.
    * **Fix:** Use the fraction form (e.g., $\frac{21}{20}$) and clear the denominator by multiplying the entire equation by the highest power.

---

## Worked Example (Step-by-Step)

**Question:** A T.V. set is available for ₹ 19650 cash or ₹ 3100 down payment and three equal annual installments at 10% compound interest. Find the installment.

**Solution:**
1. **Net Debt:** $19650 - 3100 = 16550$.
2. **Equation:** $\frac{x}{1.1} + \frac{x}{(1.1)^2} + \frac{x}{(1.1)^3} = 16550$.
3. **Simplify:** $\frac{10x}{11} + \frac{100x}{121} + \frac{1000x}{1331} = 16550$.
4. **Common Denominator:** Multiply by 1331: $1210x + 1100x + 1000x = 16550 \times 1331$.
5. **Solve:** $3310x = 16550 \times 1331 \Rightarrow x = 5 \times 1331 = 6655$.

**Answer:** ₹ 6655.

---

## Similar Patterns
**Simple Interest Installments:** Distinguished by the phrase "Simple Interest" instead of "Compound Interest." In SI, the formula is $\text{Debt} = nP + \frac{R}{100} \times \frac{P}{100} \times [0+1+2+\dots+(n-1)]$.

---

## Revision Summary
* **Key formula:** $\text{Debt} = \sum \frac{x}{(1+r)^n}$.
* **Spot it by:** "Equal annual installments" + "Compound interest."
* **First move:** Subtract down payment from total price.
* **Fastest method:** Use the ratio of powers of the interest fraction.
* **Biggest trap:** Forgetting to discount each installment back to year zero.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Present Value:** The current worth of a future sum of money.
* **Compound Interest:** Interest calculated on the initial principal and also on the accumulated interest of previous periods.

### Formulas You Must Know First
$$
A = P(1+r)^n
$$
**What it means:** The amount $A$ after $n$ years at rate $r$.

### Terms Used In This Pattern
* **Installment:** A fixed portion of a debt paid at regular intervals.
* **Down Payment:** An initial upfront payment made to reduce the principal debt.