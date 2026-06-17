# Pattern: Simultaneous Operation of Multiple Pipes

## 1. Pattern Overview
This pattern solves problems involving multiple pipes (inlets and outlets) operating concurrently to fill or empty a tank. It is essential for calculating the net rate of work and the total time required to reach a specific state (full or empty) in a system.

## 2. Key Formulas
- **Part filled in 1 hour by an inlet:** 
$$\text{Rate}_{\text{inlet}} = \frac{1}{x}$$
- **Part emptied in 1 hour by an outlet:** 
$$\text{Rate}_{\text{outlet}} = \frac{1}{y}$$
- **Net rate when filling (Inlet $x$ > Outlet $y$):** 
$$\text{Net Rate} = \left( \frac{1}{x} - \frac{1}{y} \right)$$
- **Net rate when emptying (Outlet $y$ > Inlet $x$):** 
$$\text{Net Rate} = \left( \frac{1}{y} - \frac{1}{x} \right)$$
- **Total Time:** 
$$\text{Time} = \frac{1}{\text{Net Rate}}$$

## 3. When to Use This Pattern
- **Keywords:** "Both pipes opened," "simultaneously," "inlet and outlet," "net part filled/emptied."
- **Recognition:** The problem provides individual rates for multiple pipes and asks for the result of their combined action.
- **Given:** Time taken by individual pipes to fill or empty the tank.
- **To Find:** The total time taken to fill or empty the tank when multiple pipes work together.

## 4. Core Concept & Theory
The fundamental principle is the **Additive Property of Rates**. Since work is done at a constant rate, the total work done by multiple pipes is the algebraic sum of their individual rates. Inlets are treated as positive work (+), and outlets are treated as negative work (-). By finding the net rate per unit of time, we can determine the total time by taking the reciprocal of that rate.

## 5. Step-by-Step Solution Method
1. **Identify Pipe Types:** Determine which pipes are inlets (add water) and which are outlets (remove water).
2. **Calculate Individual Rates:** Convert the time taken by each pipe into a fraction of the tank filled/emptied per hour (e.g., $1/x$).
3. **Determine Net Rate:** Add the rates of inlets and subtract the rates of outlets: 
   $$\text{Net Rate} = \sum (\text{Inlet Rates}) - \sum (\text{Outlet Rates})$$
4. **Calculate Total Time:** Take the reciprocal of the net rate. If the result is positive, the tank is filling; if negative, it is emptying.

## 6. Worked Examples

**Example 1: Two Inlets**
*Given:* Pipe A fills in 30 hours, Pipe B fills in 45 hours.
*Solution:*
1. Rate of A = $1/30$; Rate of B = $1/45$.
2. Net Rate = $1/30 + 1/45 = (3+2)/90 = 5/90 = 1/18$.
3. Time = $1 / (1/18) = 18$ hours.

**Example 2: Inlet and Outlet**
*Given:* Inlet fills in 4 hours, Outlet empties in 6 hours.
*Solution:*
1. Rate of Inlet = $1/4$; Rate of Outlet = $1/6$.
2. Net Rate = $1/4 - 1/6 = (3-2)/12 = 1/12$.
3. Time = $1 / (1/12) = 12$ hours to fill.

## 7. Recognition Clues & Keywords
- **"Together" or "Both open":** Signals addition of rates.
- **"Emptying" or "Leak":** Signals subtraction of rates.
- **"Full tank":** Indicates the target volume is 1 (the whole).
- **Distinction:** Do not confuse this with "Work and Time" problems where workers might have different efficiencies; here, pipes are usually assumed to have constant rates.

## 8. Common Mistakes
- **Sign Errors:** Forgetting to subtract the outlet pipe's rate. Always remember: Inlets are (+), Outlets are (-).
- **Reciprocal Neglect:** Calculating the net rate (e.g., $1/18$) but forgetting to flip it to find the time ($18$ hours).
- **Unit Mismatch:** Mixing minutes and hours. Always convert all time units to a single standard (e.g., all to hours) before calculating.
- **Assuming all pipes fill:** Always check if a pipe is an "exhaust" or "leak" pipe.

## 9. Practice Tips
- **Visualize the Tank:** Draw a simple diagram with arrows pointing in for inlets and out for outlets.
- **Use LCM Method:** For complex problems, use the Least Common Multiple of the times as the "Total Capacity" of the tank to avoid working with fractions.
- **Related Patterns:** Study "Work and Time" problems, as the mathematical logic is identical, replacing "people" with "pipes."