# Compound Interest — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify the Goal:** Determine if you need the final Amount, the Interest, the Principal, the Rate, or the Time.
2. **Check Compounding Frequency:** Look for "half-yearly" (divide $R$ by 2, multiply $T$ by 2), "quarterly" (divide $R$ by 4, multiply $T$ by 4), or "annually."
3. **Select Pattern:** Match the question structure to the Quick-Recognition Table below.
4. **Set Up Equation:** Use the standard formula $A = P(1 + \frac{R}{100})^n$ or the installment/difference formulas.
5. **Execute Calculation:** Use effective rates or ratios for speed; watch for fractional years.
6. **Sanity Check:** Ensure the interest is higher than Simple Interest; check if the answer magnitude is logical.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Complex Scenarios | "saves", "lends", "tax", "borrow" | Periodic flows, rates | Final balance |
| CI Calculation | "compound interest", "compounded" | $P, R, T$ | $CI$ or $A$ |
| Growth/Multiples | "doubles", "times", "years" | Growth factor, time | Future multiplier |
| Installments | "annual payment", "discharge debt" | Total debt, $R, T$ | Installment amount |
| Interest Comparison | "difference", "SI and CI" | $SI$ or $CI$ diff | $P, R,$ or $T$ |
| Missing Variable | "in how many years", "at what rate" | $P, A, T$ or $CI$ | $R, T,$ or $P$ |
| Uncategorized | "divide", "equal amounts" | Total sum, $T, R$ | Split shares |

---

## Formula Bank

**[Complex Scenarios]**
$$A = P(1 + \frac{R}{100})^n$$
→ *produces: Future value of principal*
→ *use when: Standard compounding applies*

$$Effective Rate = R \times (1 - Tax Rate)$$
→ *produces: Adjusted interest rate*
→ *use when: Tax is deducted from interest*

**[CI Calculation]**
$$A = P(1 + \frac{R/k}{100})^{nk}$$
→ *produces: Amount with frequency $k$*
→ *use when: Compounding is not annual*

$$A = P(1 + \frac{R}{100})^n(1 + \frac{f \times R}{100})$$
→ *produces: Amount for fractional years*
→ *use when: Time includes months/days*

**[Growth and Multiples]**
$$A = P(1 + \frac{R}{100})^n$$
→ *produces: Future sum*
→ *use when: Calculating growth over time*

**[Installment Payments]**
$$P = \sum \frac{x}{(1+r)^n}$$
→ *produces: Present value of installments*
→ *use when: Paying debt in installments*

**[Interest Comparison]**
$$D = P \times (\frac{R}{100})^2$$
→ *produces: Difference for 2 years*
→ *use when: Comparing SI and CI*

$$D = P \times \frac{R^2(300+R)}{100^3}$$
→ *produces: Difference for 3 years*
→ *use when: Comparing SI and CI*

**[Missing Variable]**
$$R = \frac{SI \times 100}{P \times T}$$
→ *produces: Simple interest rate*
→ *use when: Finding rate from SI*

**[Uncategorized]**
$$A = P(1 + \frac{R}{100})^n$$
→ *produces: Amount at time $n$*
→ *use when: Equating two future values*

---

## Step Sequences

* **Complex Scenarios:** Identify flows → Adjust rates → Sum geometric series → Final balance.
* **CI Calculation:** Adjust $R$ and $T$ → Apply formula → Subtract $P$ → Result.
* **Growth/Multiples:** Identify $k$ times → Use $k^m$ rule → Multiply time → Result.
* **Installments:** Set PV equation → Sum fractions → Solve for $x$ → Result.
* **Interest Comparison:** Identify $T$ → Apply difference formula → Solve for $P$ → Result.
* **Missing Variable:** Set up ratio $\frac{A}{P}$ → Simplify power → Solve for $R/T$ → Result.
* **Uncategorized:** Set $A_1 = A_2$ → Form ratio → Divide total → Result.

---

## Fastest Tricks

* **Growth:** If sum becomes $k$ times in $t$ years, it becomes $k^m$ times in $m \times t$ years.
* **2-Year CI-SI:** Difference is $P \times (\frac{R}{100})^2$.
* **3-Year CI-SI:** Difference is $P \times \frac{R^2(300+R)}{100^3}$.
* **Effective Rate:** For 2 years, $CI\% = 2R + \frac{R^2}{100}$.

---

## Trap Watch

* **CI Calculation:** Treating months as decimals → Use fraction $\frac{months}{12}$.
* **Installments:** Forgetting to discount each payment → Discount back to $T=0$.
* **Growth:** Adding time instead of multiplying → Multiply years by power.
* **Interest Comparison:** Confusing $SI$ and $CI$ formulas → Use specific $D$ formulas.

---

## Last-Minute Reminders

Always convert quarterly rates by dividing the annual rate by 4 and multiplying time by 4.
The difference between CI and SI for 2 years is always $P(R/100)^2$.
When calculating for fractional years, calculate CI for full years first, then SI for the remaining fraction.
Always check if the question asks for the Amount or the Interest earned.
In installment questions, the sum of the present values of all installments must equal the principal.