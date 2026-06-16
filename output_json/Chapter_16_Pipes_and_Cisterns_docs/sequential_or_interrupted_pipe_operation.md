# Pattern Name: Sequential or Interrupted Pipe Operation

## 1. Pattern Overview
This pattern solves problems where multiple pipes operate on a tank under varying conditions, such as pipes being opened at different times, closed mid-process, or working against each other. It is essential for calculating the total time required to fill or empty a reservoir when the flow rate is not constant throughout the entire duration.

## 2. Key Formulas
- **Part filled in 1 hour by an inlet:** 
$$\text{Part} = \frac{1}{x}$$
- **Part emptied in 1 hour by an outlet:** 
$$\text{Part} = \frac{1}{y}$$
- **Net part filled (Inlet > Outlet):** 
$$\text{Net Part} = \left( \frac{1}{x} - \frac{1}{y} \right)$$
- **Net part emptied (Outlet > Inlet):** 
$$\text{Net Part} = \left( \frac{1}{y} - \frac{1}{x} \right)$$
- **Total Time Calculation:** 
$$\text{Time} = \frac{\text{Total Work}}{\text{Rate of Work}}$$

## 3. When to Use This Pattern
- **Keywords:** "Opened after," "Closed after," "Turned off," "Working alternately," "Interrupted."
- **Recognition:** The problem describes a timeline where the state of the pipes changes (e.g., Pipe A starts, then Pipe B joins, or Pipe A is closed after 2 hours).
- **Given:** Individual rates of pipes and the sequence of operation.
- **To Find:** Total time taken to fill/empty the tank or the time a specific pipe was open.

## 4. Core Concept & Theory
The fundamental principle is the **Additivity of Work**. Since work is done at a constant rate, the total work done is the sum of the work done in each distinct time interval. By breaking the problem into segments where the "active" pipes remain constant, we can calculate the work done in each segment and sum them to find the total time.

## 5. Step-by-Step Solution Method
1. **Determine Unit Rates:** Calculate the fraction of the tank filled/emptied by each pipe in 1 hour (or 1 minute).
2. **Identify Time Segments:** Break the problem into intervals based on when pipes are turned on or off.
3. **Calculate Work per Segment:** Multiply the unit rate of the active pipes by the duration of that specific segment.
4. **Determine Remaining Work:** Subtract the work completed in previous segments from the total capacity (1).
5. **Solve for Unknowns:** Divide the remaining work by the combined rate of the pipes active in the final segment to find the remaining time.
6. **Sum the Times:** Add the durations of all segments to get the final answer.

## 6. Worked Examples

**Example 1: Sequential Opening**
*Pipe A fills a tank in 10 hours, Pipe B in 15 hours. Pipe A is opened for 2 hours, then Pipe B is opened. How long to fill the rest?*
- **Given:** A = 1/10 per hr, B = 1/15 per hr.
- **Step 1:** Work done by A in 2 hours = $2 \times \frac{1}{10} = \frac{1}{5}$.
- **Step 2:** Remaining work = $1 - \frac{1}{5} = \frac{4}{5}$.
- **Step 3:** Combined rate (A+B) = $\frac{1}{10} + \frac{1}{15} = \frac{3+2}{30} = \frac{5}{30} = \frac{1}{6}$.
- **Step 4:** Time for remaining work = $\frac{4/5}{1/6} = \frac{4}{5} \times 6 = 4.8$ hours.

**Example 2: Interrupted Operation**
*Pipe A fills in 12 hours, Pipe B empties in 18 hours. Both are open for 3 hours, then B is closed. How long to fill the rest?*
- **Given:** A = 1/12, B = -1/18 (negative because it empties).
- **Step 1:** Net rate (A+B) = $\frac{1}{12} - \frac{1}{18} = \frac{3-2}{36} = \frac{1}{36}$.
- **Step 2:** Work done in 3 hours = $3 \times \frac{1}{36} = \frac{1}{12}$.
- **Step 3:** Remaining work = $1 - \frac{1}{12} = \frac{11}{12}$.
- **Step 4:** Time for A to finish = $\frac{11/12}{1/12} = 11$ hours.

## 7. Recognition Clues & Keywords
- **"After X hours, Pipe Y is closed":** Signals a change in the net rate.
- **"Pipe A and B are opened together, but B is closed after...":** Signals a two-phase calculation.
- **"How much more time...":** Indicates you must subtract the work already done.
- **Do not confuse with:** Simple simultaneous problems where pipes are never turned off.

## 8. Common Mistakes
- **Ignoring the sign:** Forgetting that an outlet pipe must be subtracted from the inlet rate.
- **Mixing units:** Failing to convert all time units to hours or minutes consistently.
- **Calculating total time vs. remaining time:** Answering with the "remaining time" when the question asks for "total time elapsed."
- **Fractional errors:** Adding fractions without finding a common denominator correctly.

## 9. Practice Tips
- **Visualize the Timeline:** Draw a horizontal line and mark the points where pipes are turned on or off.
- **Use LCM Method:** Instead of fractions, use the Least Common Multiple of the times to represent the total capacity of the tank in "units." This often simplifies calculations.
- **Related Patterns:** Study "Work and Wages" and "Time and Distance" as they share the same mathematical structure ($Work = Rate \times Time$).