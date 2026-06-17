# Pattern: Finding Ratio from Linear Constraints

## 1. Pattern Overview
This pattern provides a systematic method to determine the ratio between two or more variables when they are linked by linear equations or algebraic constraints. It is essential for simplifying complex relationships into a standard $a:b$ format, which serves as the foundation for all proportional reasoning in mathematics.

## 2. Key Formulas
The following algebraic manipulations are the building blocks for solving linear constraints:

*   **Standard Linear Equality:**
    $$ax = by \implies \frac{x}{y} = \frac{b}{a} \implies x:y = b:a$$
*   **Sum/Difference Constraint:**
    $$a(x + y) = b(x - y) \implies \frac{x}{y} = \frac{b+a}{b-a}$$
*   **Componendo and Dividendo (for ratios):**
    $$\frac{a}{b} = \frac{c}{d} \implies \frac{a+b}{a-b} = \frac{c+d}{c-d}$$
*   **Cross-Multiplication Principle:**
    $$a:b :: c:d \iff ad = bc$$

## 3. When to Use This Pattern
*   **Keywords:** "Find the ratio," "If $x$ times $A$ equals $y$ times $B$," "The sum of $A$ and $B$ is proportional to their difference."
*   **Recognition Clues:** You are given an equation involving two or more variables and are asked to express the relationship as a ratio.
*   **Given:** A linear equation or a set of constraints involving variables.
*   **To Find:** The ratio of the variables (e.g., $x:y$ or $A:B:C$).

## 4. Core Concept & Theory
The fundamental idea is **Variable Isolation**. By rearranging a linear equation to place all terms of one variable on one side and all terms of the other on the opposite side, we create a fraction. Since a ratio $a:b$ is mathematically equivalent to the fraction $\frac{a}{b}$, isolating the variables allows us to read the ratio directly from the coefficients.

## 5. Step-by-Step Solution Method
1.  **Group Variables:** Move all terms containing the first variable to one side of the equation and all terms containing the second variable to the other side.
2.  **Simplify Coefficients:** Combine like terms so the equation takes the form $Ax = By$.
3.  **Form the Fraction:** Divide both sides by the product of the variables and the coefficients to isolate the ratio $\frac{x}{y}$.
    *   *Example:* $Ax = By \implies \frac{x}{y} = \frac{B}{A}$.
4.  **Verify Units:** Ensure all quantities are in the same units before finalizing the ratio.
5.  **Reduce:** Simplify the resulting fraction to its lowest terms (e.g., $4:6$ becomes $2:3$).

## 6. Worked Examples

**Example 1: Simple Linear Constraint**
Given: $5x = 8y$, find $x:y$.
Solution:
1. Divide both sides by $y$: $5(\frac{x}{y}) = 8$.
2. Divide both sides by $5$: $\frac{x}{y} = \frac{8}{5}$.
3. Result: $x:y = 8:5$.

**Example 2: Sum and Difference Constraint**
Given: $3(A + B) = 5(A - B)$, find $A:B$.
Solution:
1. Expand: $3A + 3B = 5A - 5B$.
2. Group variables: $3B + 5B = 5A - 3A$.
3. Simplify: $8B = 2A$.
4. Rearrange: $\frac{A}{B} = \frac{8}{2} = \frac{4}{1}$.
5. Result: $A:B = 4:1$.

## 7. Recognition Clues & Keywords
*   **Look for:** Equations where variables are added, subtracted, or multiplied by constants.
*   **Avoid confusion with:** "Variation" problems (where $x \propto y$ implies $x=ky$). While related, variation problems usually involve an unknown constant $k$, whereas linear constraints involve fixed coefficients.

## 8. Common Mistakes
1.  **Inverting the Ratio:** Students often write $x:y = A:B$ instead of $B:A$. *Correction:* Always check by substituting values back into the original equation.
2.  **Ignoring Signs:** When moving terms across the equals sign, students often forget to change the sign (e.g., $+5B$ becoming $-5B$).
3.  **Failure to Simplify:** Leaving a ratio as $10:15$ instead of reducing it to $2:3$. Always divide by the Greatest Common Divisor (GCD).
4.  **Unit Mismatch:** Attempting to find a ratio between quantities with different units (e.g., meters and centimeters). Always convert to the same unit first.

## 9. Practice Tips
*   **Master the Algebra:** Practice isolating variables in equations like $2x + 3y = 5x - y$.
*   **Related Patterns:** Study **Variation (VI)** and **Proportion (II)** to understand how these linear constraints behave when more than two variables are involved.
*   **Check your work:** Always plug your final ratio back into the original equation to see if the equality holds.