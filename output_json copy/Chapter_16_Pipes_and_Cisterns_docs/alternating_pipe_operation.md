# Pattern Name: Alternating Pipe Operation

## 1. Pattern Overview
The Alternating Pipe Operation pattern solves problems where two or more pipes do not work simultaneously, but instead operate in a sequential, rotating cycle (e.g., Pipe A works for one hour, then Pipe B works for the next). This pattern is essential for calculating the total time required to fill or empty a tank when the rate of work changes periodically rather than remaining constant.

## 2. Key Formulas
- **Work Rate of an Inlet:** If a pipe fills a tank in $x$ hours, its rate is:
$$\text{Rate}_{\text{inlet}} = \frac{1}{x} \text{ units/hour}$$
- **Work Rate of an Outlet:** If a pipe empties a tank in $y$ hours, its rate is:
$$\text{Rate}_{\text{outlet}} = -\frac{1}{y} \text{ units/hour}$$
- **Cycle Work:** If Pipe A and Pipe B work in a 2-hour cycle:
$$\text{Work per cycle} = \text{Rate}_A + \text{Rate}_B$$
- **Total Time Calculation:**
$$\text{Total Time} = (\text{Number of full cycles} \times \text{Cycle duration}) + \text{Remaining time}$$

## 3. When to Use This Pattern
- **Keywords:** "Opened alternately," "opened for one hour each," "in turns," "successively."
- **Recognition:** The problem specifies a sequence of operation (e.g., "A opens first, then B, then A...").
- **Given:** Individual time taken by each pipe to fill/empty the tank.
- **To Find:** The total time taken to fill the tank under the alternating schedule.

## 4. Core Concept & Theory
The fundamental idea is to treat the alternating sequence as a single "block" or "cycle." Because the pipes do not work together, their rates cannot be added directly for the entire duration. By calculating the net work done in one complete cycle, we can determine how many full cycles are needed to get close to the total capacity, then calculate the final fractional time required to finish the job.

## 5. Step-by-Step Solution Method
1. **Calculate Individual Rates:** Determine the fraction of the tank filled/emptied by each pipe per hour.
2. **Define the Cycle:** Identify the duration of one full rotation (e.g., 2 hours if A and B alternate).
3. **Calculate Cycle Work:** Sum the work done by each pipe within that cycle.
4. **Determine Full Cycles:** Divide the total work (1) by the work done per cycle to find the number of full cycles completed.
5. **Calculate Remaining Work:** Subtract the work completed in the full cycles from the total capacity (1).
6. **Final Step:** Calculate the time needed for the remaining work based on the rate of the pipe whose turn it is next.

## 6. Worked Examples

**Example 1: Alternating Fillers**
*Given:* Pipe A fills a tank in 10 hours, Pipe B fills it in 15 hours. They are opened alternately for 1 hour each, starting with A.
*Solution:*
1. Rates: A = 1/10, B = 1/15.
2. Cycle (2 hours): $1/10 + 1/15 = 5/30 = 1/6$ of the tank.
3. In 6 cycles (12 hours): $6 \times (1/6) = 1$ full tank.
4. Result: It takes 12 hours to fill the tank.

**Example 2: Filler and Emptier**
*Given:* Pipe A fills in 12 hours, Pipe B empties in 24 hours. They are opened alternately for 1 hour each, starting with A.
*Solution:*
1. Rates: A = 1/12, B = -1/24.
2. Cycle (2 hours): $1/12 - 1/24 = 1/24$ of the tank.
3. To reach near capacity: After 20 cycles (40 hours), work done = $20 \times (1/24) = 20/24 = 5/6$.
4. Remaining work: $1 - 5/6 = 1/6$.
5. Next turn (A): A fills 1/12 per hour. To fill 1/6, A needs $(1/6) / (1/12) = 2$ hours.
6. Total time: $40 + 2 = 42$ hours.

## 7. Recognition Clues & Keywords
- **"Alternately"**: The primary signal.
- **"Turn by turn"**: Indicates sequential operation.
- **"First hour... second hour"**: Explicitly defines the cycle.
- **Distinction**: Do not confuse this with "simultaneous" operation where you simply add rates ($1/x + 1/y$).

## 8. Common Mistakes
- **Adding rates for the whole time:** Students often calculate $(1/x + 1/y)$ and apply it to the total time. This is wrong because the pipes are never on at the same time.
- **Ignoring the "Next Turn" pipe:** In the final step, students often use the wrong pipe's rate to finish the remaining work. Always check who starts the cycle.
- **Overfilling:** In problems with an outlet, ensure the tank doesn't "overflow" during a cycle before the outlet has a chance to empty it.

## 9. Practice Tips
- **Visualize the Cycle:** Draw a timeline showing "A" then "B" then "A" to keep track of who is working.
- **Use LCM:** Use the Least Common Multiple of the times to represent the total capacity of the tank in "units" rather than fractions; this makes the arithmetic much easier.
- **Related Patterns:** Study "Work and Wages" and "Simultaneous Pipe Operation" to understand the contrast in calculation methods.