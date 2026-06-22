# Missing Variable (Compound Interest)

## Overview
This pattern involves finding an unknown component (Time, Rate, or Principal) when the other variables and the final Amount are provided. The central idea is to isolate the growth factor $(1 + \frac{R}{100})^n$ and solve for the missing variable using exponent rules or root extraction.

---

## Recognition Clues
* **Keywords:** "In how many years," "At what rate percent," "Find the sum of money."
* **Given:** Principal ($P$), Amount ($A$), and Time ($n$) or Rate ($R$).
* **Asked:** The one variable that is missing from the standard $A = P(1 + \frac{R}{100})^n$ equation.
* **Compounding frequency:** Watch for "half-yearly" or "quarterly," which changes the rate and time units.

---

## Key Formulas

### [Compound Interest Amount Formula]
$$
A = P\left(1 + \frac{R}{100}\right)^n
$$

**Variables:**
- $A$ = Final Amount
- $P$ = Principal (Initial sum)
- $R$ = Rate of interest per annum
- $n$ = Number of compounding periods

**When to use:** To find any missing variable when $P, A, R,$ and $n$ are related by compound interest.

**Worked example:** If $P=100000, A=133100, R=10\%$, then $133100 = 100000(1.1)^n \Rightarrow 1.331 = (1.1)^n \Rightarrow n=3$.

---

## Solution Framework

1. **Step 1: Identify the compounding frequency.** Determine if interest is annual, half-yearly (divide $R$ by 2, multiply $n$ by 2), or quarterly (divide $R$ by 4, multiply $n$ by 4).
2. **Step 2: Set up the equation.** Substitute all known values into $A = P(1 + \frac{R}{100})^n$.
3. **Step 3: Isolate the growth factor.** Divide $A$ by $P$ to get the ratio $\frac{A}{P} = (1 + \frac{R}{100})^n$.
4. **Step 4: Solve for the variable.** Use square/cube roots if $n$ is small, or equate exponents if the bases match.
5. **Step 5: Final adjustment.** If finding $R$, solve the resulting linear equation; if finding $P$, perform the final division.

---

## Shortcut Tricks

* **Trick:** Use the "Ratio of Amounts" for consecutive years.
* **Why it works:** In compound interest, the amount at the end of year $n$ acts as the principal for year $n+1$.
* **When to use:** When given amounts for two consecutive years (e.g., Year 2 and Year 3).
* **Example:** If $A_2 = 7350$ and $A_3 = 8575$, Interest for 1 year = $8575 - 7350 = 1225$. Rate = $\frac{1225}{7350} \times 100 = 16\frac{2}{3}\%$.

---

## Common Mistakes

* **Mistake:** Using the Simple Interest formula for Compound Interest problems.
    * **Fix:** Always check if the question specifies "compounded."
* **Mistake:** Forgetting to adjust $R$ and $n$ for quarterly/half-yearly compounding.
    * **Fix:** Divide $R$ by the number of periods per year and multiply $n$ by the same number.
* **Mistake:** Calculating interest on the original principal for the second year in multi-year problems.
    * **Fix:** Remember that compound interest is calculated on the *amount* at the end of the previous period.

---

## Worked Example (Step-by-Step)

**Question:** Find the sum of money which will amount to ₹ 26010 in 6 months at the rate of 8% per annum when the interest is compounded quarterly.

**Solution:**
1. **Identify frequency:** Quarterly compounding means $R_{q} = \frac{8}{4} = 2\%$ and $n = 6 \text{ months} = 2 \text{ quarters}$.
2. **Set up equation:** $26010 = P(1 + \frac{2}{100})^2$.
3. **Isolate factor:** $26010 = P(1.02)^2 \Rightarrow 26010 = P(\frac{51}{50})^2$.
4. **Solve:** $P = 26010 \times \frac{2500}{2601} = 10 \times 2500 = 25000$.

**Answer:** ₹ 25000.

---

## Similar Patterns
* **Simple Interest (SI) Missing Variable:** Distinguish by the keyword "Simple Interest" vs "Compound Interest." SI uses $I = \frac{PRT}{100}$, which is linear, whereas CI is exponential.

---

## Revision Summary
* **Key formula:** $A = P(1 + \frac{R}{100})^n$.
* **Spot it by:** Missing $P, R,$ or $n$ in a compound interest context.
* **First move:** Divide $A$ by $P$ to isolate the growth factor.
* **Fastest method:** Use ratio of amounts for consecutive years to find $R$ instantly.
* **Biggest trap:** Forgetting to adjust $R$ and $n$ for non-annual compounding.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Exponents:** Understanding that $(x)^n = y$ requires finding the root or log to solve for $n$.
* **Fractions to Percentages:** Converting $8\% \text{ p.a.}$ to $2\%$ per quarter.

### Formulas You Must Know First
* **Simple Interest:** $SI = \frac{P \times R \times T}{100}$.
* **Amount:** $A = P + CI$.

### Terms Used In This Pattern
* **Compounded Quarterly:** Interest is calculated and added to the principal every 3 months.
* **Per Annum (p.a.):** The rate provided is for a full year.