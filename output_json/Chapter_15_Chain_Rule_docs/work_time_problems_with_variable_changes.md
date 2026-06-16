# Pattern Name: Work-Time Problems with Variable Changes

## 1. Pattern Overview
This pattern provides a systematic method for solving problems where the completion of a task depends on multiple changing variables, such as the number of workers, time duration, or quantity of resources. It is essential for mastering efficiency calculations and resource allocation in competitive examinations.

## 2. Key Formulas
The fundamental relationship for these problems is governed by the **Chain Rule**, expressed as:

$$\frac{M_1 \times D_1 \times H_1}{W_1} = \frac{M_2 \times D_2 \times H_2}{W_2}$$

Where:
*   $M$ = Number of Men (or workers/agents)
*   $D$ = Number of Days
*   $H$ = Number of Hours per day
*   $W$ = Work done (or quantity produced)

*Note: If a variable is not mentioned in the problem, it is treated as a constant (1) and omitted from the equation.*

## 3. When to Use This Pattern
*   **Keywords:** "If X men can do Y work in Z days," "How many more/less," "Same work," "Required to finish."
*   **Recognition:** Look for a scenario where a specific output is achieved by a specific input, and you are asked to find the new input required for a modified output.
*   **Given:** Initial set of conditions ($M_1, D_1, H_1, W_1$) and a partial set of new conditions.
*   **To Find:** The missing variable ($M_2, D_2, H_2,$ or $W_2$).

## 4. Core Concept & Theory
The approach relies on **Proportionality**:
*   **Direct Proportion:** As one variable increases, the other increases (e.g., More workers = More work done).
*   **Indirect (Inverse) Proportion:** As one variable increases, the other decreases (e.g., More workers = Less time required).
By comparing every variable to the "term to be found," we determine whether to place the larger or smaller number in the numerator of our ratio, ensuring the logic of the work-time relationship is maintained.

## 5. Step-by-Step Solution Method
1.  **Identify Variables:** List all given values ($M_1, D_1, H_1, W_1$) and the target variable ($x$).
2.  **Determine Proportionality:** Compare the variable to be found with each known variable.
    *   Ask: "If this variable increases, will the target variable increase or decrease?"
3.  **Set up the Ratio:** 
    *   If **Direct**, use the ratio $\frac{\text{Smaller}}{\text{Larger}}$ or $\frac{\text{Larger}}{\text{Smaller}}$ consistently.
    *   If **Indirect**, invert the ratio.
4.  **Solve for $x$:** Use the cross-multiplication method or the Chain Rule formula to isolate $x$.

## 6. Worked Examples

**Example 1: Calculating Required Resources**
*A canteen requires 105 kgs of wheat for a week (7 days). How many kgs of wheat will it require for 58 days?*
*   **Given:** $W_1 = 105, D_1 = 7, D_2 = 58$. Find $W_2$.
*   **Logic:** More days require more wheat (Direct Proportion).
*   **Solution:** 
    $$\frac{7}{58} = \frac{105}{x}$$
    $$7x = 58 \times 105$$
    $$x = \frac{58 \times 105}{7} = 870 \text{ kg}$$

**Example 2: Calculating Required Manpower**
*35 women can do a piece of work in 15 days. How many women would be required to do the same work in 25 days?*
*   **Given:** $M_1 = 35, D_1 = 15, D_2 = 25$. Find $M_2$.
*   **Logic:** More days available means fewer women are needed (Indirect Proportion).
*   **Solution:**
    $$M_1 \times D_1 = M_2 \times D_2$$
    $$35 \times 15 = x \times 25$$
    $$x = \frac{35 \times 15}{25} = 21 \text{ women}$$

## 7. Recognition Clues & Keywords
*   **"Same work":** Signals that $W_1 = W_2$, allowing you to cancel $W$ from the formula.
*   **"More/Less":** Always check if the change in the variable should logically result in a higher or lower answer.
*   **Avoid Confusion:** Do not confuse "Work-Time" with "Speed-Distance-Time." While they share proportionality concepts, "Work" is a cumulative total, whereas "Distance" is a rate-based outcome.

## 8. Common Mistakes
1.  **Ignoring Inverse Proportion:** Students often treat all variables as directly proportional. Always ask: "Does this make the answer bigger or smaller?"
2.  **Mixing Units:** Ensure all time units are consistent (e.g., don't mix hours and days without converting).
3.  **Misplacing Work ($W$):** Remember that $W$ (the work done) is always in the denominator of the Chain Rule formula.
4.  **Calculation Errors:** Always simplify fractions before multiplying to avoid large, error-prone numbers.

## 9. Practice Tips
*   **Master the Logic:** Before using the formula, try to reason out the proportionality (e.g., "If I have more people, I need less time").
*   **Related Patterns:** Study "Pipes and Cisterns" and "Time and Distance," as they utilize the same underlying proportionality logic.
*   **Drill:** Practice problems where one variable is held constant to isolate the effect of the other variables.