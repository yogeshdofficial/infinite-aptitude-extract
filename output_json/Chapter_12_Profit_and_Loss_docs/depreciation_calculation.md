# Depreciation Calculation

## Overview

* This pattern involves calculating the value of an asset that loses a fixed percentage of its worth annually.
* The central idea is treating depreciation as a reverse compound interest problem where the value decreases over time.

---

## Recognition Clues

* **Keywords:** "Depreciates every year," "value at the beginning of that year," "worth X years ago."
* **Given:** Present value ($P$), annual depreciation rate ($r$), and time period ($n$).
* **Asked:** Original value (value $n$ years ago) or future value after $n$ years.

---

## Important Formulas

### [Depreciation Formula]

$$
V_{present} = V_{past} \times \left(1 - \frac{r}{100}\right)^n
$$

*Meaning:* $V_{present}$ is the current value, $V_{past}$ is the initial value, $r$ is the rate, and $n$ is the number of years.

*Use when:* Calculating the value of an asset after $n$ years of depreciation or finding the initial value given the current value.

---

## Solution Framework

1. Identify the present value ($V_{present}$) and the rate ($r$).
2. Convert the rate into a fraction: $1 - \frac{r}{100}$.
3. Set up the equation: $V_{past} = \frac{V_{present}}{(1 - \frac{r}{100})^n}$.
4. Simplify the fraction and raise it to the power of $n$.
5. Multiply $V_{present}$ by the reciprocal of the fraction to find $V_{past}$.

---

## Shortcut Tricks

* **Ratio Method:** Convert the percentage rate to a fraction (e.g., 10% = $\frac{1}{10}$). If the value decreases, the ratio is $\frac{9}{10}$.
* **Why it works:** It avoids complex decimals; simply multiply the present value by the flipped ratio ($\frac{10}{9}$) $n$ times.

---

## Common Mistakes

* **Mistake:** Calculating depreciation on the original value every year (Simple Interest approach).
* **Reason:** Depreciation is calculated on the value at the *beginning* of each year (Compound basis).
* **Fix:** Always use the power $n$ to account for the compounding effect of depreciation.

* **Mistake:** Confusing "worth $n$ years ago" with "worth $n$ years later."
* **Reason:** Misreading the direction of time in the question.
* **Fix:** If looking for the past, divide by the rate; if looking for the future, multiply by the rate.

---

## Similar Patterns

* This is mathematically identical to **Compound Interest** problems, but with a negative rate.
* Distinguish by the keyword "depreciates" (value drops) versus "compounds/increases" (value grows).

---

## Revision Summary

**Key formula:** $V_{past} = V_{present} \div (1 - \frac{r}{100})^n$

**Spot it by:** Looking for "depreciates every year" and a time duration.

**Fastest method:** Use the ratio of the fraction (e.g., $10\% \to \frac{9}{10}$) and multiply/divide accordingly.

**Biggest trap:** Applying the depreciation rate only once instead of compounding it over $n$ years.