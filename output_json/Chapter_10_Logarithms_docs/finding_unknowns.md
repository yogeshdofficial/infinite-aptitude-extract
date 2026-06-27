# Finding Unknowns in Logarithmic Equations

## Overview
This pattern involves solving for an unknown variable ($x, p, q$) trapped inside a logarithmic expression. The central idea is to systematically "peel away" the logarithms by converting them into their equivalent exponential forms.

---

## Recognition Clues
* **Keywords:** "If $\log_b (\dots) = C$", "find the value of $x$".
* **Given:** A logarithmic equation where the variable is inside the argument or base.
* **Asked:** The numerical value of the variable.
* **Visual:** Nested logs (e.g., $\log[\log(\dots)]$) or logs added/subtracted with constants.

---

## Key Formulas

### [Logarithmic Definition]
$$
\log_b A = C \iff A = b^C
$$
**Variables:** $b$ = base, $A$ = argument, $C$ = result.
**When to use:** To remove a single logarithm from an equation.
**Worked example:** $\log_3 x = -2 \implies x = 3^{-2} = \frac{1}{9}$.

### [Logarithmic Product Rule]
$$
\log_b A + \log_b B = \log_b (A \times B)
$$
**Variables:** $A, B$ = arguments, $b$ = base.
**When to use:** When multiple logs with the same base are added.
**Worked example:** $\log_{10} 3 + \log_{10} 4 = \log_{10} 12$.

---

## Solution Framework
1. **Simplify:** Use log properties (like the Product Rule) to combine terms into a single $\log_b (\text{expression}) = \text{constant}$ form.
2. **Convert:** Apply the definition $\log_b A = C \implies A = b^C$ to eliminate the logarithm.
3. **Isolate:** Solve the resulting algebraic equation (linear or quadratic) for the variable.
4. **Verify:** Ensure the argument of the original log is positive (if required by the exam).

---

## Shortcut Tricks
* **Trick:** Convert constants to logs: $1 = \log_{10} 10$, $2 = \log_{10} 100$.
* **Why it works:** Allows you to combine all terms into a single log expression on both sides, then drop the "log" operator entirely.
* **When to use:** When an equation has a constant term (e.g., $\log x + \log y = 1$).
* **Example:** $\log_{10} 3 + \log_{10} x = 1 \implies \log_{10} (3x) = \log_{10} 10 \implies 3x = 10$.

---

## Common Mistakes
* **Mistake:** Calculating $b^C$ as $b \times C$. (e.g., $3^{-2} = -6$). **Fix:** Remember $b^C$ is repeated multiplication.
* **Mistake:** Solving from the inside out for nested logs. **Fix:** Always work from the outermost log inward.
* **Mistake:** Forgetting to convert the constant term to a log base. **Fix:** Always match the base of the constant to the base of the logs in the equation.

---

## Worked Example (Step-by-Step)

**Question:** If $\log_2 [\log_3 (\log_2 x)] = 1$, find the value of $x$.

**Solution:**
1. **Step 1 (Outermost):** Remove $\log_2$ by converting to exponential: $\log_3 (\log_2 x) = 2^1 = 2$.
2. **Step 2 (Middle):** Remove $\log_3$: $\log_2 x = 3^2 = 9$.
3. **Step 3 (Innermost):** Remove $\log_2$: $x = 2^9$.
4. **Step 4 (Calculate):** $x = 512$.

**Answer:** $512$

---

## Similar Patterns
* **Exponential Equations:** Distinguished by the variable being in the exponent (e.g., $2^x = 8$) rather than inside a log argument.

---

## Revision Summary
* **Key formula:** $\log_b A = C \implies A = b^C$.
* **Spot it by:** Variable trapped inside $\log(\dots)$.
* **First move:** Combine logs or convert the outermost log to exponential form.
* **Fastest method:** Convert constants to logs to equate arguments.
* **Biggest trap:** Confusing $b^C$ with $b \times C$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Exponents** — $a^n = a \times a \times \dots$ ($n$ times).
* **Quadratic Factoring** — Splitting the middle term to solve $ax^2 + bx + c = 0$.
* **Negative Exponents** — $a^{-n} = \frac{1}{a^n}$.

### Formulas You Must Know First
$$
(a^m)^n = a^{m \times n}
$$
**What it means:** Power of a power rule.
**Example:** $(2^3)^2 = 2^6 = 64$.

### Terms Used In This Pattern
* **Base ($b$)** — The subscript number in $\log_b x$.
* **Argument ($x$)** — The value inside the log function.
* **Characteristic** — The integer part of a log (not used in these specific algebraic problems).