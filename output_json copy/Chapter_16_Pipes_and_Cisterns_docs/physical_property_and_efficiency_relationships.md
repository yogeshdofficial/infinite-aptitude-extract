# Pattern Name: Physical Property and Efficiency Relationships

## 1. Pattern Overview
- This pattern solves problems involving the interaction between physical dimensions (volume/capacity) and the operational efficiency (inlet/outlet rates) of pipes connected to a reservoir.
- It matters because it bridges the gap between abstract time-based rates and concrete physical measurements, allowing for the calculation of system behavior in real-world engineering or plumbing scenarios.

## 2. Key Formulas
- **Part filled in 1 hour (Inlet):** 
$$\text{Rate}_{\text{in}} = \frac{1}{x}$$
- **Part emptied in 1 hour (Outlet):** 
$$\text{Rate}_{\text{out}} = \frac{1}{y}$$
- **Net rate (Inlet + Outlet, $y > x$):** 
$$\text{Net Rate}_{\text{filled}} = \left( \frac{1}{x} - \frac{1}{y} \right)$$
- **Net rate (Inlet + Outlet, $x > y$):** 
$$\text{Net Rate}_{\text{emptied}} = \left( \frac{1}{y} - \frac{1}{x} \right)$$
- **Volume-based Rate:** 
$$\text{Rate} = \frac{\text{Volume}}{\text{Time}}$$

## 3. When to Use This Pattern
- **Keywords:** "Inlet," "Outlet," "Cistern," "Reservoir," "Pours in," "Drained," "Emptying," "Filling."
- **Recognition:** Use this when a problem provides physical dimensions (length, width, height) or specific flow rates (e.g., cu. inches per minute) alongside time-based capacity.
- **Given:** Tank dimensions, flow rates of individual pipes, or time taken to fill/empty.
- **To Find:** Total time to fill or empty the tank under combined conditions.

## 4. Core Concept & Theory
The fundamental idea is the **Principle of Superposition**. We treat the "work" done by a pipe as a fraction of the total tank capacity per unit of time. By converting all physical properties into a common unit (e.g., cubic inches or total tank capacity), we can add or subtract the rates of multiple pipes to find the net effect on the system.

## 5. Step-by-Step Solution Method
1. **Standardize Units:** Convert all physical dimensions into a single unit (e.g., all to cubic inches).
2. **Calculate Total Capacity:** Determine the total volume of the tank using $V = L \times W \times H$.
3. **Determine Individual Rates:** Calculate the rate of each pipe. If given a flow rate (e.g., 576 cu. in/min), keep it in those units. If given time, convert to $\frac{1}{\text{time}}$.
4. **Calculate Net Rate:** Subtract the outlet rate from the inlet rate (or vice versa) to find the net flow per unit of time.
5. **Solve for Time:** Use the formula $\text{Time} = \frac{\text{Total Volume}}{\text{Net Rate}}$.

## 6. Worked Examples

**Example 1: Tank with Mixed Units**
*Given:* A tank 9ft x 5ft x 2ft. Inlet pours 576 cu. in/min. Exhaust empties full tank in 3 hours.
*Solution:*
1. Volume = $9 \times 5 \times 2 = 90 \text{ cu. ft} = 90 \times 12 \times 12 \times 12 = 155,520 \text{ cu. in}$.
2. Exhaust rate = $\frac{155,520 \text{ cu. in}}{3 \times 60 \text{ min}} = 864 \text{ cu. in/min}$.
3. Net rate = $864 - 576 = 288 \text{ cu. in/min}$ (emptying).
4. Time = $\frac{155,520}{288} = 540 \text{ minutes} = 9 \text{ hours}$.

**Example 2: Combined Filling Pipes**
*Given:* Pipe A fills in 30 hrs, Pipe B in 45 hrs.
*Solution:*
1. Rate A = $\frac{1}{30}$, Rate B = $\frac{1}{45}$.
2. Net Rate = $\frac{1}{30} + \frac{1}{45} = \frac{3+2}{90} = \frac{5}{90} = \frac{1}{18}$.
3. Time = $18 \text{ hours}$.

## 7. Recognition Clues & Keywords
- **"Inlet" vs "Outlet":** Always assign a positive sign to inlets and a negative sign to outlets.
- **"Emptying a full tank":** Signals that the outlet rate is the primary focus.
- **Do not confuse with:** Simple work-rate problems where no physical volume is involved; here, you must account for the physical capacity of the container.

## 8. Common Mistakes
- **Unit Mismatch:** Forgetting to convert feet to inches or hours to minutes. Always check that your rate units match your volume units.
- **Sign Errors:** Subtracting an inlet rate instead of an outlet rate. Remember: Inlets add, Outlets subtract.
- **Inverting the Rate:** Forgetting that if a pipe fills in $x$ hours, the rate is $\frac{1}{x}$. Students often mistakenly use $x$ as the rate.

## 9. Practice Tips
- **Draw a Diagram:** Sketch the tank and label the pipes with arrows (inward for inlet, outward for outlet).
- **Master Fractions:** Since these problems rely heavily on $\frac{1}{x} + \frac{1}{y}$, practice finding common denominators quickly.
- **Related Patterns:** Study "Work and Time" patterns, as they are mathematically identical to "Pipes and Cisterns" problems.