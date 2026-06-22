# Equalizing Amounts at Compound Interest

## Overview
This pattern involves splitting a total sum into two parts such that their future values (amounts) become equal after different time periods at a fixed compound interest rate. The central idea is to equate the two future value expressions and solve for the ratio of the two parts.

---

## Recognition Clues
* **Keywords:** "Divide [Total Amount] between A and B", "amount of A after [T1] years is equal to the amount of B after [T2] years".
* **Given:** Total sum, interest rate ($R$), and two different time periods ($T1, T2$).
* **Asked:** The individual shares of A and B.

---

## Key Formulas

### [Equal Amount Equation]
$$
P_1 \left(1 + \frac{R}{100}\right)^{T_1} = P_2 \left(1 + \frac{R}{100}\right)^{T_2}
$$

**Variables:**
- $P_1, P_2$ = The two parts of the total sum.
- $R$ = Rate of interest per annum.
- $T_1, T_2$ = Time periods for A and B respectively.

**When to use:** Whenever the question states that the amounts (principal + interest) of two parts are equal after different durations.

**Worked example:** Total ₹ 1301, $R=4\%$, $T_1=7, T_2=9$.
Equation: $P_1(1.04)^7 = P_2(1.04)^9$.
Simplified: $P_1 = P_2(1.04)^2 \implies P_1 = P_2(\frac{26}{25})^2 = P_2(\frac{676}{625})$.

---

## Solution Framework

1. **Define Variables:** Let the two parts be $x$ and $(Total - x)$.
2. **Set up Equality:** Write the amount formula for both parts: $x(1+r)^{T_1} = (Total-x)(1+r)^{T_2}$.
3. **Simplify Powers:** Divide both sides by the smaller power of $(1+r)$ to leave a single power on one side.
4. **Solve for Ratio:** Express $x$ in terms of $(Total-x)$ using the simplified growth factor.
5. **Calculate Shares:** Solve the linear equation to find $x$, then find $(Total-x)$.

---

## Shortcut Tricks

* **Trick:** The ratio of the shares $P_1 : P_2$ is $(1+r)^{T_2-T_1} : 1$.
* **Why it works:** Dividing both sides of the equality by the smaller time factor leaves the difference in time on one side.
* **When to use:** When you need to find the ratio of the two parts quickly.
* **Example:** $T_2 - T_1 = 9 - 7 = 2$. Ratio $= (1.04)^2 : 1 = 676 : 625$. Total parts $= 676 + 625 = 1301$. Since total is 1301, shares are exactly 676 and 625.

---

## Common Mistakes

* **Mistake:** Equating the *Interest* instead of the *Amount*.
    * **Why it happens:** Misreading the question; "Amount" includes principal, "Interest" does not.
    * **Fix:** Always use the formula $P(1+r)^n$ for Amount.
* **Mistake:** Incorrectly assigning the larger time period to the smaller share.
    * **Why it happens:** For the amounts to be equal, the part invested for a *shorter* time must be *larger*.
    * **Fix:** Check: $P_1 > P_2$ if $T_1 < T_2$.

---

## Worked Example (Step-by-Step)

**Question:** Divide ₹ 1301 between A and B, so that the amount of A after 7 years is equal to the amount of B after 9 years, the interest being compounded at 4% per annum.

**Solution:**
1. **Define:** Let A's share be $x$, B's share be $1301-x$.
2. **Equation:** $x(1.04)^7 = (1301-x)(1.04)^9$.
3. **Simplify:** Divide by $(1.04)^7$: $x = (1301-x)(1.04)^2$.
4. **Calculate:** $x = (1301-x)(\frac{104}{100})^2 = (1301-x)(\frac{676}{625})$.
5. **Solve:** $625x = 676(1301) - 676x \implies 1301x = 676 \times 1301 \implies x = 676$.
6. **Result:** A = ₹ 676, B = ₹ 625.

**Answer:** A = ₹ 676, B = ₹ 625.

---

## Similar Patterns
**Simple Interest Division:** If the question mentions "Simple Interest" instead of "Compound Interest," use $P_1(1 + \frac{R \cdot T_1}{100}) = P_2(1 + \frac{R \cdot T_2}{100})$.

---

## Revision Summary
* **Key formula:** $P_1(1+r)^{T_1} = P_2(1+r)^{T_2}$.
* **Spot it by:** "Amount of A equals amount of B" after different times.
* **First move:** Set up the ratio $P_1/P_2 = (1+r)^{T_2-T_1}$.
* **Fastest method:** Use the ratio of the growth factors to split the total.
* **Biggest trap:** Confusing the time periods or forgetting to include the principal in the "Amount".

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Compound Interest** — Interest calculated on the initial principal and also on the accumulated interest of previous periods.
* **Ratio Division** — Dividing a total quantity into parts based on a given ratio $a:b$.

### Formulas You Must Know First
$$
A = P\left(1 + \frac{R}{100}\right)^n
$$
**What it means:** The total amount ($A$) after $n$ years at rate $R$ for principal $P$.

### Terms Used In This Pattern
* **Amount** — The sum of the principal and the interest earned.
* **Compounded Annually** — Interest is added to the principal once every year.