# Pattern: Evaluating Expressions using Ratio Substitutions

## 1. Pattern Overview
This pattern provides a systematic method for evaluating algebraic expressions by substituting ratio variables with a common constant multiplier ($k$). It is essential for simplifying complex fractional expressions where the relationship between variables is defined by a ratio rather than absolute values.

## 2. Key Formulas
Given a ratio $a : b = x : y$, we represent the variables as:
$$a = xk, \quad b = yk$$
Where $k$ is a non-zero constant.

For a general expression involving multiple variables $a, b, c$ where $a:b:c = x:y:z$:
$$a = xk, \quad b = yk, \quad c = zk$$

For homogeneous expressions (where the degree of the numerator equals the degree of the denominator), the constant $k$ cancels out:
$$\frac{f(ak, bk)}{g(ak, bk)} = \frac{k^n \cdot f(a, b)}{k^n \cdot g(a, b)} = \frac{f(a, b)}{g(a, b)}$$

## 3. When to Use This Pattern
*   **Keywords:** "If $a:b = x:y$, find the value of...", "Given the ratio...", "Evaluate the expression..."
*   **Recognition Clues:** The problem provides a ratio between two or more variables and asks for the value of a fraction or algebraic expression involving those same variables.
*   **Given:** A ratio relationship (e.g., $a:b = 3:4$).
*   **To Find:** The numerical value of an expression (e.g., $\frac{3a + 4b}{5a - 2b}$).

## 4. Core Concept & Theory
The fundamental idea is that a ratio $a:b = x:y$ does not define the exact values of $a$ and $b$, but rather their relative proportions. By introducing a constant $k$, we transform the ratio into absolute algebraic terms. Because the expressions in these problems are typically **homogeneous** (every term has the same total degree), the constant $k$ will always cancel out, leaving a single numerical result.

## 5. Step-by-Step Solution Method
1.  **Assign the Constant:** Assign $k$ to the ratio terms. If $a:b = x:y$, set $a = xk$ and $b = yk$.
2.  **Substitute:** Replace every instance of the variables in the target expression with their $k$-equivalent terms.
3.  **Simplify:** Expand the expression. If the expression is homogeneous, the $k$ terms will factor out and cancel.
4.  **Calculate:** Perform the final arithmetic operations to reach the numerical answer.

## 6. Worked Examples

**Example 1: Basic Substitution**
Given: $a : b = 3 : 4$. Find the value of $\frac{5a - 3b}{7a + 2b}$.
Solution:
1. Let $a = 3k$ and $b = 4k$.
2. Substitute into the expression: $\frac{5(3k) - 3(4k)}{7(3k) + 2(4k)}$.
3. Simplify: $\frac{15k - 12k}{21k + 8k} = \frac{3k}{29k}$.
4. Cancel $k$: $\frac{3}{29}$.

**Example 2: Multi-variable Substitution**
Given: $x : y : z = 2 : 3 : 5$. Find the value of $\frac{x + y + z}{2x + y - z}$.
Solution:
1. Let $x = 2k, y = 3k, z = 5k$.
2. Substitute: $\frac{2k + 3k + 5k}{2(2k) + 3k - 5k}$.
3. Simplify: $\frac{10k}{4k + 3k - 5k} = \frac{10k}{2k}$.
4. Result: $5$.

## 7. Recognition Clues & Keywords
*   **Look for:** Ratios given as $a:b$ or fractions $\frac{a}{b} = \frac{x}{y}$.
*   **Distinguish from:** Problems involving "Variation" (where $x \propto y$ implies $x = ky$, but $k$ is a constant to be determined by specific data points, not canceled out).
*   **Warning:** If the expression is **not** homogeneous (e.g., $\frac{a^2 + b}{a + b}$), the $k$ will not cancel, and the answer will remain dependent on $k$. Check if the problem provides an absolute value for one variable to solve for $k$.

## 8. Common Mistakes
1.  **Forgetting the constant $k$:** Students often plug in $3$ and $4$ directly. While this works for homogeneous expressions, it is mathematically incorrect and fails if the expression is not homogeneous.
2.  **Algebraic errors during expansion:** Forgetting to distribute the multiplier (e.g., writing $5(3k)$ as $5+3k$ instead of $15k$).
3.  **Canceling $k$ prematurely:** Ensure all terms in the numerator and denominator are multiplied by $k$ before canceling.
4.  **Confusing Ratio with Proportion:** Do not confuse this with $a:b :: c:d$ (Proportion), where you equate the product of means and extremes.

## 9. Practice Tips
*   **Mastery:** Practice with expressions containing squares and cubes to ensure you handle the powers of $k$ correctly (e.g., $(3k)^2 = 9k^2$).
*   **Related Patterns:** Study **Variation (VI)** to understand when $k$ is a variable to be solved versus a constant to be canceled.
*   **Verification:** Always check if the expression is homogeneous. If it is, your $k$ should always cancel out. If it doesn't, re-read the problem to see if you missed a specific value for one of the variables.