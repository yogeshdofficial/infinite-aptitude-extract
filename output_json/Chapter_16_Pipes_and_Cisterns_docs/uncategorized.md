# 1. Pattern Overview
This pattern provides a systematic approach to solving problems involving the rates at which pipes fill or empty a tank or reservoir. It is essential for calculating the net work done when multiple pipes with different capacities operate simultaneously.

# 2. Key Formulas
**Part filled in 1 hour by an inlet pipe:**
$$\text{Part filled} = \frac{1}{x}$$
*(where $x$ is the time in hours to fill the tank)*

**Part emptied in 1 hour by an outlet pipe:**
$$\text{Part emptied} = \frac{1}{y}$$
*(where $y$ is the time in hours to empty the tank)*

**Net part filled (Inlet $x$ and Outlet $y$, where $y > x$):**
$$\text{Net part filled in 1 hour} = \left( \frac{1}{x} - \frac{1}{y} \right)$$

**Net part emptied (Outlet $y$ and Inlet $x$, where $y < x$):**
$$\text{Net part emptied in 1 hour} = \left( \frac{1}{y} - \frac{1}{x} \right)$$

# 3. When to Use This Pattern
- **Keywords:** "Inlet," "Outlet," "Fill," "Empty," "Cistern," "Reservoir," "Together."
- **Recognition:** The problem involves multiple rates of flow (filling vs. draining) acting on a single container.
- **Given:** Time taken by individual pipes to fill or empty the tank.
- **To Find:** Total time taken to fill/empty the tank when multiple pipes are open, or the net effect of opposing pipes.

# 4. Core Concept & Theory
The fundamental principle is the **Unitary Method**. By converting the total time taken by a pipe into a "rate per hour" (the reciprocal), we can add or subtract these rates to find the "net rate" of the system. If a pipe fills, its rate is positive; if it empties, its rate is negative. The total time is simply the reciprocal of the net rate.

# 5. Step-by-Step Solution Method
1. **Identify Pipe Roles:** Determine which pipes are inlets (add water) and which are outlets (remove water).
2. **Calculate Unit Rates:** Express the work of each pipe as a fraction of the tank per hour ($1/time$).
3. **Determine Net Rate:** 
   - If both fill: Add the fractions.
   - If one fills and one empties: Subtract the outlet rate from the inlet rate.
4. **Calculate Total Time:** Take the reciprocal of the net rate calculated in Step 3 to find the total hours required.

# 6. Worked Examples

**Example 1: Two Inlet Pipes**
*Pipe A can fill a tank in 30 hours and pipe B in 45 hours. If both are opened, how long to fill the tank?*
- **Step 1:** Rate of A = $1/30$; Rate of B = $1/45$.
- **Step 2:** Net rate = $1/30 + 1/45$.
- **Step 3:** Find common denominator (90): $3/90 + 2/90 = 5/90 = 1/18$.
- **Result:** The tank will be filled in 18 hours.

**Example 2: Inlet and Outlet**
*A tank is 90 cu. ft. An inlet pours 576 cu. inch/min. An exhaust empties it in 3 hours. How long to empty a full tank?*
- **Step 1:** Convert volume to inches: $90 \times 12^3 = 155,520$ cu. inches.
- **Step 2:** Exhaust rate per minute: $155,520 / (3 \times 60) = 864$ cu. inch/min.
- **Step 3:** Net rate: $864 (\text{out}) - 576 (\text{in}) = 288$ cu. inch/min (emptying).
- **Step 4:** Time = $155,520 / 288 = 540$ minutes = 9 hours.

# 7. Recognition Clues & Keywords
- **"Inlet"**: Always treat as a positive contribution.
- **"Exhaust/Outlet"**: Always treat as a negative contribution.
- **"Full tank" vs "Empty tank"**: Pay attention to the starting state, as it dictates whether you are filling or emptying.
- **Do not confuse with:** Simple work-time problems where all workers are "positive" contributors; here, some "workers" (outlets) actively undo the work.

# 8. Common Mistakes
1. **Adding instead of Subtracting:** Students often add the rates of an inlet and an outlet. Remember: Outlets subtract from the total.
2. **Forgetting to Reciprocate:** After finding the net rate (e.g., $1/18$), students often state the answer is $1/18$ hours. Always flip the fraction to get the final time.
3. **Unit Mismatch:** Mixing cubic feet, cubic inches, and minutes. Always convert to a single unit system before calculating rates.

# 9. Practice Tips
- **Visualize:** Draw a simple diagram of the tank with arrows pointing in for inlets and out for outlets.
- **Master Fractions:** Practice adding and subtracting fractions with different denominators quickly.
- **Related Patterns:** Study "Work and Time" problems, as the logic of "Rate $\times$ Time = Work" is identical to "Rate $\times$ Time = Volume."