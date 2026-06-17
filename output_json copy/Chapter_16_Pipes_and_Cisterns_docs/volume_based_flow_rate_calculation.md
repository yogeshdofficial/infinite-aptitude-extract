# Pattern: Volume-Based Flow Rate Calculation

## 1. Pattern Overview
This pattern provides a systematic method to determine the time required to fill or empty a container when flow rates are given in specific volume units (e.g., cubic inches per minute) alongside time-based capacity constraints. It is essential for solving real-world engineering and plumbing problems where tank dimensions and pipe capacities are provided in mixed units.

## 2. Key Formulas
- **Volume of a Rectangular Tank:** 
$$V = \text{length} \times \text{width} \times \text{height}$$
- **Part filled/emptied in 1 unit of time:** 
$$\text{Rate} = \frac{1}{\text{Total Time}}$$
- **Net Flow Rate (Inlet + Outlet):** 
$$\text{Net Rate} = |\text{Rate}_{\text{in}} - \text{Rate}_{\text{out}}|$$
- **Time to fill/empty:** 
$$\text{Time} = \frac{\text{Total Volume}}{\text{Net Flow Rate}}$$

## 3. When to Use This Pattern
- **Keywords:** "Cistern," "Reservoir," "Pours in," "Drained," "Exhaust pipe," "Cubic units."
- **Recognition Clues:** The problem provides physical dimensions (length, width, height) and a specific flow rate (e.g., gallons/min or cubic inches/min).
- **Given:** Tank dimensions, flow rate of one pipe, and time capacity of another pipe.
- **To Find:** The total time required to reach a specific state (empty or full).

## 4. Core Concept & Theory
The fundamental principle is the **Conservation of Volume**. A tank's capacity is a fixed constant. By converting all flow rates into a common unit (e.g., cubic inches per minute), we can treat the tank as a balance sheet. We calculate the "Net Flow" by subtracting the outflow from the inflow (or vice versa). The total time is simply the total volume divided by this net rate of change.

## 5. Step-by-Step Solution Method
1. **Calculate Total Volume:** Multiply length, width, and height. Ensure all units are consistent (e.g., convert feet to inches if the flow rate is in inches).
2. **Standardize Flow Rates:** Convert all pipe capacities into the same unit of volume per unit of time (e.g., cubic inches per minute).
3. **Determine Net Flow:** If one pipe fills and one empties, subtract the smaller rate from the larger rate to find the net change per minute.
4. **Calculate Final Time:** Divide the total volume by the net flow rate. If the result is in minutes, convert to hours if required by the question.

## 6. Worked Examples

**Example 1: Tank Emptying with Mixed Units**
*Given:* Tank 9ft x 5ft x 2ft. Inlet pours 576 cu. inch/min. Exhaust empties full tank in 3 hours.
*Solution:*
1. **Volume:** $9 \times 5 \times 2 = 90 \text{ cu. ft}$. Convert to inches: $90 \times 12 \times 12 \times 12 = 155,520 \text{ cu. inches}$.
2. **Exhaust Rate:** The tank empties in 3 hours (180 mins). Rate = $155,520 / 180 = 864 \text{ cu. inch/min}$.
3. **Net Rate:** $864 (\text{out}) - 576 (\text{in}) = 288 \text{ cu. inch/min}$.
4. **Time:** $155,520 / 288 = 540 \text{ minutes} = 9 \text{ hours}$.

**Example 2: Combined Filling Time**
*Given:* Pipe A fills in 30 hours, Pipe B in 45 hours.
*Solution:*
1. **Rate A:** $1/30$ of tank per hour.
2. **Rate B:** $1/45$ of tank per hour.
3. **Combined Rate:** $1/30 + 1/45 = (3+2)/90 = 5/90 = 1/18$.
4. **Time:** The reciprocal of the rate is 18 hours.

## 7. Recognition Clues & Keywords
- **"Inlet" vs "Outlet":** Always assign a positive sign to inlets and a negative sign to outlets.
- **"Full Tank":** This implies the starting volume is the total calculated volume.
- **Distinction:** Do not confuse this with "Work-Time" problems; while the math is similar, the inclusion of physical dimensions (volume) requires an extra conversion step.

## 8. Common Mistakes
- **Unit Mismatch:** Forgetting to convert feet to inches (or vice versa). Always check that volume units match flow rate units.
- **Time Unit Mismatch:** Mixing minutes and hours. Always convert the final answer to the requested unit.
- **Ignoring the "Net" concept:** Adding rates when one pipe is actually emptying the tank. Always subtract the outlet rate from the inlet rate.

## 9. Practice Tips
- **Draw a Diagram:** Sketch the tank and label the pipes as "In" or "Out" to visualize the flow.
- **Master Conversions:** Practice converting cubic feet to cubic inches ($1 \text{ ft}^3 = 1728 \text{ in}^3$).
- **Related Patterns:** Study "Work-Time Efficiency" patterns, as they share the same reciprocal logic ($1/x + 1/y$).