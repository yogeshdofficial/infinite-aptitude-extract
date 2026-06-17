# Pattern Name: System of Equations for Pipe Rates

## 1. Pattern Overview
This pattern provides a systematic method to calculate the time required to fill or empty a tank by determining the net rate of work performed by multiple inlet and outlet pipes operating simultaneously. It is essential for solving complex work-rate problems where multiple agents act in opposition or cooperation.

## 2. Key Formulas
- **Rate of an Inlet Pipe:** $$\text{Rate} = \frac{1}{x} \text{ (part per hour)}$$
- **Rate of an Outlet Pipe:** $$\text{Rate} = -\frac{1}{y} \text{ (part per hour)}$$
- **Net Rate (Both filling):** $$\text{Net Rate} = \frac{1}{x} + \frac{1}{y}$$
- **Net Rate (One filling, one emptying):** $$\text{Net Rate} = \left| \frac{1}{x} - \frac{1}{y} \right|$$
- **Time to complete work:** $$\text{Time} = \frac{1}{\text{Net Rate}}$$

## 3. When to Use This Pattern
- **Keywords:** "Inlet," "Outlet," "Emptying," "Filling," "Together," "Simultaneously."
- **Recognition:** The problem involves a container (tank/cistern) and multiple pipes with different capacities.
- **Given:** Time taken by individual pipes to fill or empty the tank.
- **To Find:** The total time taken when pipes are opened together or the capacity of the tank.

## 4. Core Concept & Theory
The fundamental principle is the **Unitary Method applied to Work**. We treat the entire tank as "1 unit" of work. By calculating how much of the tank is filled or emptied in exactly one hour (the "rate"), we can add or subtract these rates based on whether the pipes are working together or against each other. If a pipe empties, its rate is treated as a negative contribution to the total volume.

## 5. Step-by-Step Solution Method
1. **Identify Pipe Roles:** Determine which pipes are inlets (positive rate) and which are outlets (negative rate).
2. **Calculate Individual Rates:** Express each pipe's work as a fraction of the tank per hour ($1/x$).
3. **Determine Net Rate:** Sum the rates. Use addition for inlets and subtraction for outlets.
4. **Calculate Total Time:** Take the reciprocal of the net rate ($1 / \text{Net Rate}$) to find the total time required.
5. **Decision Branch:** If the result is positive, the tank is filling; if negative, the tank is emptying.

## 6. Worked Examples

**Example 1: Two Inlet Pipes**
*Pipe A can fill a tank in 30 hours and pipe B in 45 hours. If both are opened, how long to fill?*
- **Step 1:** Rate of A = $1/30$; Rate of B = $1/45$.
- **Step 2:** Net Rate = $1/30 + 1/45 = (3+2)/90 = 5/90 = 1/18$.
- **Step 3:** Time = $1 / (1/18) = 18$ hours.

**Example 2: Inlet and Outlet**
*A tank is filled by an inlet in 4 hours and emptied by an outlet in 6 hours. How long to fill if both are open?*
- **Step 1:** Rate of Inlet = $1/4$; Rate of Outlet = $-1/6$.
- **Step 2:** Net Rate = $1/4 - 1/6 = (3-2)/12 = 1/12$.
- **Step 3:** Time = $1 / (1/12) = 12$ hours.

## 7. Recognition Clues & Keywords
- **"Inlet" / "Pours in":** Always add this rate.
- **"Outlet" / "Exhaust" / "Emptying":** Always subtract this rate.
- **"Full tank":** Indicates the starting state for emptying problems.
- **"Empty tank":** Indicates the starting state for filling problems.
- **Do not confuse with:** Simple work problems where agents do not have "negative" work (like people building a wall).

## 8. Common Mistakes
- **Forgetting the Negative Sign:** Students often add the rates of outlet pipes. Remember: Outlets remove water, so they must be subtracted.
- **Inverting the Final Fraction:** After finding the net rate (e.g., $1/18$), students often forget to take the reciprocal. The rate is "part per hour," not "hours."
- **Unit Mismatch:** Ensure all time units (minutes vs. hours) are converted to the same unit before calculating rates.

## 9. Practice Tips
- **Visualize the Tank:** Draw a simple diagram with arrows pointing in for inlets and out for outlets.
- **LCM Method:** For complex problems, use the Least Common Multiple (LCM) of the times to represent the total capacity of the tank in "units" rather than fractions. This often simplifies the arithmetic.
- **Related Patterns:** Study "Work and Wages" and "Time and Distance" as they share the same fundamental $Rate \times Time = Work$ structure.