# Chapter 16: Pipes and Cisterns

## 1. Chapter Introduction
This chapter focuses on the mathematical relationship between the rate of water flow and the time required to fill or empty a container. By understanding how multiple pipes—whether inlets or outlets—interact within a system, you will learn to calculate the net effect of their combined work. Mastering these concepts is essential for solving real-world problems involving efficiency, drainage, and system capacity.

## 2. Core Ideas
The core of this topic lies in treating the capacity of a tank as a whole (1 unit) and determining the "part" of the tank affected by a pipe in a single unit of time (e.g., one hour or one minute). 
*   **Inlets:** Pipes that add water to the tank.
*   **Outlets:** Pipes that remove water from the tank.
*   **Net Work:** When multiple pipes are open, the total work is the sum of the work done by inlets minus the work done by outlets.

## 3. Important Formulas
If a pipe fills a tank in $x$ hours and another empties it in $y$ hours:

*   **Part filled in 1 hour (Inlet):** 
    $$\frac{1}{x}$$
*   **Part emptied in 1 hour (Outlet):** 
    $$\frac{1}{y}$$
*   **Net part filled (when $y > x$):** 
    $$\left( \frac{1}{x} - \frac{1}{y} \right)$$
*   **Net part emptied (when $x > y$):** 
    $$\left( \frac{1}{y} - \frac{1}{x} \right)$$

*Note: Use these formulas to determine the hourly rate of change in the tank's volume before calculating the total time required.*

## 4. Important Facts and Shortcuts
*   **Inlet vs. Outlet:** Always assign a positive value to the work of an inlet and a negative value to the work of an outlet.
*   **Diameter and Efficiency:** The time taken to fill or empty a tank is inversely proportional to the square of the pipe's diameter. If you double the diameter, the pipe's capacity changes significantly.
*   **Negative Results:** If your calculation for the work done by a pipe results in a negative value, it confirms the pipe is acting as an outlet (emptying the tank).
*   **Partial Tanks:** If a tank is already partially full, adjust the "part to be filled" or "part to be emptied" accordingly before calculating the time.

## 5. How to Recognize the Problem Type
*   **"Both pipes opened":** Look for problems involving simultaneous operation; use addition for two inlets or subtraction for an inlet and an outlet.
*   **"Leak in the tank":** Treat the leak as an outlet pipe. Calculate the difference in time between the "normal" fill time and the "leaky" fill time to find the leak's rate.
*   **"Diameter twice as much":** Use the inverse square law of the diameter to find the new rate of flow.
*   **"Already partially full":** Identify the starting fraction (e.g., two-fifths full) to determine if the tank will reach capacity or be emptied first.

## 6. Common Mistakes
1.  **Ignoring the sign:** Forgetting to subtract the work of an outlet pipe from the work of an inlet pipe.
2.  **Mixing units:** Failing to convert all time units (minutes vs. hours) or volume units (cubic feet vs. cubic inches) before performing calculations.
3.  **Misinterpreting "Net":** Assuming all pipes are filling the tank when one or more may be emptying it.
4.  **Incorrectly applying diameter:** Forgetting that the rate of flow is proportional to the *square* of the diameter, not just the diameter itself.

## 7. Chapter Pattern Map
This chapter covers a variety of scenarios, ranging from simple simultaneous operations to complex systems involving leaks and varying pipe diameters. Key patterns include:
*   **Simultaneous Operation:** Combining multiple inlets and outlets.
*   **Efficiency Relationships:** Calculating flow based on physical pipe dimensions.
*   **Sequential/Interrupted Flow:** Handling leaks or changes in pipe status over time.
*   **Volume-Based Calculations:** Converting physical tank dimensions into flow rates.