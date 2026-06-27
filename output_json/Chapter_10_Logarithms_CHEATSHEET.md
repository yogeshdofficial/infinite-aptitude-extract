# Logarithms — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify the Goal:** Is it evaluating a value, finding an unknown $x$, or simplifying an expression?
2. **Standardize:** Convert all terms to the same base using $\log_b a = \frac{\log_k a}{\log_k b}$ or $\log_{b^n} a^m = \frac{m}{n} \log_b a$.
3. **Condense:** Use $\log A + \log B = \log(AB)$ and $\log A - \log B = \log(\frac{A}{B})$ to collapse the expression into a single log.
4. **Exponentiate:** If solving for $x$, convert $\log_b A = C$ to $A = b^C$.
5. **Sanity Check:** Ensure arguments of logs are positive; check if the result matches the magnitude of the input.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Characteristic/Mantissa | "number of digits", "logarithm is" | $\log$ value | Digits or parts |
| Finding Unknowns | "satisfies the relation", "find x" | Log equation | Value of $x$ |
| Logarithm Evaluation | "evaluate", "value of" | Log expression | Numerical result |
| Logarithmic Simplification | "simplify", "evaluate" | Complex log sum | Simplified value |
| Logarithmic Values | "if $\log 2 = ...$", "find $\log 50$" | Known log values | Unknown log value |
| Miscellaneous Properties | "not correct", "AP", "$a^x=b^y$" | Relation | Correct statement/x |
| Uncategorized | "sum", "product" | Series of logs | Total value |

---

## Formula Bank

**[Characteristic and Mantissa]**
$$\text{Digits} = \lfloor \log_{10} x \rfloor + 1$$
→ *produces: total digits in $x$*
→ *use when: finding magnitude of $x^n$*

$$\log x = \text{char} + \text{mantissa}$$
→ *produces: integer and decimal parts*
→ *use when: decomposing negative logs*

**[Finding Unknowns]**
$$\log_b a = y \iff b^y = a$$
→ *produces: value of $a$ or $b$*
→ *use when: removing the log operator*

$$\log_b A + \log_b B = \log_b (AB)$$
→ *produces: single log argument*
→ *use when: combining multiple log terms*

**[Logarithm Evaluation]**
$$\log_b b^n = n$$
→ *produces: exponent value*
→ *use when: base matches argument*

$$\log_{b^n} a^m = \frac{m}{n} \log_b a$$
→ *produces: simplified coefficient*
→ *use when: base and argument are powers*

**[Logarithmic Simplification]**
$$\frac{1}{\log_a b} = \log_b a$$
→ *produces: reciprocal log*
→ *use when: log is in denominator*

$$\log_a b \times \log_b c = \log_a c$$
→ *produces: chain rule result*
→ *use when: multiplying different logs*

**[Logarithmic Values]**
$$\log_b \left(\frac{x}{y}\right) = \log_b x - \log_b y$$
→ *produces: difference of logs*
→ *use when: argument is a fraction*

$$\log_b (x^n) = n \log_b x$$
→ *produces: scaled log*
→ *use when: argument has exponent*

**[Miscellaneous Properties]**
$$2 \log B = \log A + \log C$$
→ *produces: AP condition*
→ *use when: logs are in AP*

**[Uncategorized]**
$$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$
→ *produces: sum of integers*
→ *use when: logs are in a series*

---

## Step Sequences

*   **Characteristic/Mantissa:** Calc $\log x$ → Find integer → Add 1 → Answer
*   **Finding Unknowns:** Condense logs → Exponentiate → Solve quadratic/linear → Answer
*   **Logarithm Evaluation:** Prime factorize → Apply power rule → Simplify → Answer
*   **Logarithmic Simplification:** Change base → Combine terms → Cancel factors → Answer
*   **Logarithmic Values:** Prime factorize argument → Substitute knowns → Simplify → Answer
*   **Miscellaneous Properties:** Apply log rules → Form equation → Solve for variable → Answer
*   **Uncategorized:** Sum exponents → Apply log rule → Simplify → Answer

---

## Fastest Tricks

*   **Characteristic:** $\lfloor n \log_{10} a \rfloor + 1$ gives digits for $a^n$ instantly.
*   **Negative Log:** For $-3.153$, char is $-4$, mantissa is $1 - 0.153 = 0.847$.
*   **Chain Rule:** $\log_a b \cdot \log_b c \cdot \log_c a = 1$ always.
*   **Base Change:** $\log_{b^n} a^m$ is always $\frac{m}{n} \log_b a$.
*   **Log 5:** Always use $\log 5 = 1 - \log 2$.

---

## Trap Watch

*   **Characteristic:** Forgetting to add 1 → Add 1 to integer part.
*   **Negative Mantissa:** Leaving mantissa negative → Subtract decimal from 1.
*   **Log Sum:** Assuming $\log(a+b) = \log a + \log b$ → Never distribute logs.
*   **Base/Exponent:** Confusing $b^y=x$ with $x^y=b$ → Keep base as base.
*   **Quadratic:** Forgetting to reject negative $x$ → Check argument $> 0$.

---

## Last-Minute Reminders

The logarithm of 1 to any base is always 0.
The logarithm of the base itself is always 1.
Arguments of logarithms must always be strictly greater than zero.
$\log(a+b)$ cannot be simplified using standard log rules.
Always convert mixed fractions to improper fractions before taking logs.