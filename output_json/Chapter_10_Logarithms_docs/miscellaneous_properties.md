# Miscellaneous Properties (Logarithms)

## Overview
This pattern involves solving equations or verifying statements using logarithmic properties. You will recognize these by the presence of `log` terms, often involving variables in exponents or sequences (like AP). The central idea is to convert logarithmic expressions into algebraic ones using standard log rules.

---

## Recognition Clues
* **Keywords:** "log", "arithmetic progression", "not correct", "if... then...".
* **Given:** Logarithmic equations, sequences of log terms, or multiple-choice statements about log properties.
* **Asked:** The value of a variable ($x$), or identifying an incorrect property.

---

## Key Formulas

### [Logarithm of a Product]
$$
\log(ab) = \log a + \log b
$$
**Variables:** $a, b$ = positive real numbers.
**When to use:** To expand a product inside a log or combine two logs into one.
**Worked example:** $\log(2 \times 3) = \log 2 + \log 3 = \log 6$.

### [Power Rule]
$$
\log(a^n) = n \log a
$$
**Variables:** $a$ = base, $n$ = exponent.
**When to use:** To bring an exponent down to the base level to solve for a variable.
**Worked example:** $\log(3^x) = x \log 3$.

### [Arithmetic Progression Property]
$$
2b = a + c
$$
**Variables:** $a, b, c$ = three consecutive terms in AP.
**When to use:** When the question states three log terms are in AP.
**Worked example:** If $\log 3, \log(3^x-2), \log(3^x+4)$ are in AP, then $2 \log(3^x-2) = \log 3 + \log(3^x+4)$.

---

## Solution Framework

**Step 1: Translate the condition** — If in AP, use $2b = a + c$; if an equation, use log rules to simplify both sides.
**Step 2: Remove the logs** — Use the property $\log A = \log B \Rightarrow A = B$ to convert the equation into an algebraic one.
**Step 3: Substitute/Simplify** — Use a substitution (e.g., $y = 3^x$) if the equation is quadratic.
**Step 4: Solve for the variable** — Solve the resulting algebraic equation for the unknown.
**Step 5: Verify constraints** — Ensure the argument of any log is positive (e.g., $3^x - 2 > 0$).

---

## Shortcut Tricks

* **Trick:** For $\log(a+b)$, there is no simplified form; do not split it.
* **Why it works:** Logarithms are defined for products and quotients, not sums.
* **When to use:** When evaluating "which statement is incorrect" questions.
* **Example:** $\log(2+3) = \log 5$, which is NOT $\log 2 + \log 3$.

---

## Common Mistakes

* **Mistake:** Assuming $\log(a+b) = \log a + \log b$.
    * **Why it happens:** Confusing the product rule with addition.
    * **Fix:** Remember $\log(ab) = \log a + \log b$ only.
* **Mistake:** Ignoring the domain of the log.
    * **Why it happens:** Solving the algebra without checking if the argument becomes negative.
    * **Fix:** Always check if the resulting value makes the original log argument $> 0$.

---

## Worked Example (Step-by-Step)

**Question:** If $\log 3$, $\log (3^x - 2)$ and $\log (3^x + 4)$ are in arithmetic progression, then $x$ is equal to?

**Solution:**
1. **Translate:** Since they are in AP, $2 \times (\text{middle term}) = \text{first} + \text{third}$.
   $2 \log(3^x - 2) = \log 3 + \log(3^x + 4)$.
2. **Simplify:** Use power rule: $\log(3^x - 2)^2 = \log[3(3^x + 4)]$.
3. **Remove logs:** $(3^x - 2)^2 = 3(3^x + 4)$.
4. **Substitute:** Let $y = 3^x$. Then $(y-2)^2 = 3(y+4) \Rightarrow y^2 - 4y + 4 = 3y + 12$.
5. **Solve:** $y^2 - 7y - 8 = 0 \Rightarrow (y-8)(y+1) = 0$. Since $y=3^x$ must be positive, $y=8$.
6. **Final:** $3^x = 8 \Rightarrow x = \log_3 8$.

**Answer:** $x = \log_3 8$

---

## Similar Patterns
**Algebraic Sequences:** Distinguish by checking if the terms are inside a `log` function; if they are, use log properties first, then the sequence property.

---

## Revision Summary
* **Key formula:** $2b = a + c$ for AP; $\log(ab) = \log a + \log b$.
* **Spot it by:** Log terms in a sequence or equality.
* **First move:** Convert the log condition into an algebraic equation.
* **Fastest method:** Use $A=B$ after removing logs from both sides.
* **Biggest trap:** Treating $\log(a+b)$ as $\log a + \log b$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Arithmetic Progression (AP)** — A sequence where the difference between consecutive terms is constant.
* **Quadratic Equations** — Equations of the form $ay^2 + by + c = 0$, solved by factoring or the quadratic formula.

### Formulas You Must Know First
$$
\log_a 1 = 0
$$
**What it means:** The log of 1 to any base is always 0.
**Example:** $\log_{10} 1 = 0$.

$$
\log_a a = 1
$$
**What it means:** The log of the base to itself is 1.
**Example:** $\log_{10} 10 = 1$.

### Terms Used In This Pattern
* **Argument** — The value inside the log function (e.g., in $\log x$, $x$ is the argument).
* **Base** — The subscript in a log (e.g., in $\log_a x$, $a$ is the base).