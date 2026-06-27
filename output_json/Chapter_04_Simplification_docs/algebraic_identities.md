# Algebraic Identities

## Overview
These questions involve expressions with squares, cubes, or ratios that match standard algebraic identities. The central idea is to transform the given information into a form that fits a known identity, allowing you to solve for the unknown without tedious expansion.

---

## Recognition Clues
* **Keywords:** "If $x+y = \dots$ and $xy = \dots$", "find the value of $\frac{a^2-b^2}{a^2+b^2}$", or expressions involving cubes like $a^3+b^3+c^3 = 3abc$.
* **Given:** Sums, products, or ratios of variables.
* **Asked:** A specific algebraic expression (e.g., $x^2+y^2$, or a fraction of squares).
* **Visual Cue:** Presence of squared terms ($x^2, y^2$) or cubed terms ($x^3, y^3$) in the target expression.

---

## Key Formulas

### [Square of a Binomial]
$$ (x \pm y)^2 = x^2 + y^2 \pm 2xy $$
**Variables:** $x, y$ are the variables provided in the question.
**When to use:** When you are given the sum/difference and product of two variables and need the sum of their squares.
**Worked example:** Given $x+y=23, xy=126$. Then $(23)^2 = x^2+y^2 + 2(126) \Rightarrow 529 = x^2+y^2 + 252 \Rightarrow x^2+y^2 = 277$.

### [Sum of Cubes Property]
$$ \text{If } a^3 + b^3 + c^3 = 3abc, \text{ then } a + b + c = 0 $$
**Variables:** $a, b, c$ are expressions (e.g., $x-4, x-9, x-8$).
**When to use:** When an equation is presented in the form $a^3+b^3+c^3 = 3abc$.
**Worked example:** $(x-4)^3 + (x-9)^3 + (x-8)^3 = 3(x-4)(x-9)(x-8)$. Set $(x-4)+(x-9)+(x-8) = 0 \Rightarrow 3x-21=0 \Rightarrow x=7$.

---

## Solution Framework

1. **Identify the Identity:** Match the given expression to a standard identity (e.g., $(a+b)^2$ or $a^3+b^3+c^3$).
2. **Substitute Knowns:** Plug the given numerical values into the identity.
3. **Simplify/Isolate:** Perform arithmetic to isolate the target variable or expression.
4. **Ratio Manipulation:** If given ratios (e.g., $a/b$), divide the target expression by the variable power (e.g., divide by $a^2$) to express it in terms of the known ratio.

---

## Shortcut Tricks

* **Trick:** For expressions like $\frac{a^2-b^2}{a^2+b^2}$ given $a/b$, divide numerator and denominator by $b^2$ to get $\frac{(a/b)^2 - 1}{(a/b)^2 + 1}$.
* **Why it works:** It converts a two-variable problem into a single-variable problem using the known ratio.
* **When to use:** When the expression is homogeneous (all terms have the same degree).
* **Example:** If $a/b = 4/5$, then $\frac{a^2-b^2}{a^2+b^2} = \frac{(4/5)^2 - 1}{(4/5)^2 + 1} = \frac{16/25 - 1}{16/25 + 1} = \frac{-9/25}{41/25} = -9/41$.

---

## Common Mistakes

* **Mistake:** Forgetting the $2$ in $2xy$ when expanding $(x+y)^2$.
* **Why it happens:** Rushing the expansion.
* **Fix:** Always write out the full identity $(x+y)^2 = x^2+y^2+2xy$ before substituting.
* **Mistake:** Inverting ratios (e.g., using $a/c$ when you need $c/a$).
* **Fix:** Double-check the target expression's numerator and denominator.

---

## Worked Example (Step-by-Step)

**Question:** If $a^2 + b^2 = 117$ and $ab = 54$, find $\frac{a + b}{a - b}$.

**Solution:**
1. **Find $(a+b)$:** Use $(a+b)^2 = a^2+b^2+2ab = 117 + 2(54) = 117 + 108 = 225$. So, $a+b = \sqrt{225} = 15$.
2. **Find $(a-b)$:** Use $(a-b)^2 = a^2+b^2-2ab = 117 - 2(54) = 117 - 108 = 9$. So, $a-b = \sqrt{9} = 3$.
3. **Calculate:** Divide the results: $\frac{a+b}{a-b} = \frac{15}{3} = 5$.

**Answer:** 5

---

## Similar Patterns
* **Simplification:** Distinguish by the absence of squared/cubed variables; if it's just basic arithmetic, use BODMAS.

---

## Revision Summary
* **Key formula:** $(x+y)^2 = x^2+y^2+2xy$ and $a^3+b^3+c^3=3abc \Rightarrow a+b+c=0$.
* **Spot it by:** Squared/cubed terms or given sums/products of variables.
* **First move:** Write down the relevant identity.
* **Fastest method:** Substitute known values directly into the identity.
* **Biggest trap:** Forgetting the $2$ in $2ab$ or $2xy$.

---

## Appendix: Prerequisites
* **Concepts:** Basic algebraic expansion, properties of ratios, and square roots.
* **Formulas:** $(a+b)^2 = a^2+b^2+2ab$, $(a-b)^2 = a^2+b^2-2ab$, $a^2-b^2 = (a-b)(a+b)$.
* **Terms:** *Homogeneous expression* (all terms have the same degree), *Binomial* (expression with two terms).