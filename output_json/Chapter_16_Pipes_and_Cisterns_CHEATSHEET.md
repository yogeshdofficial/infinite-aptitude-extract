# Pipes And Cisterns — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Pipe Roles:** Label each pipe as "Inlet" (positive rate) or "Outlet" (negative rate).
2. **Define Capacity:** If total volume is unknown, assume it is the LCM of all given time values.
3. **Calculate Rates:** Determine the unit rate (work per unit time) for every pipe individually.
4. **Determine Net Rate:** Sum the rates: $\text{Net Rate} = \sum \text{Inlets} - \sum \text{Outlets}$.
5. **Apply Time Formula:** Use $\text{Time} = \frac{\text{Remaining Work}}{\text{Net Rate}}$ to find the duration.
6. **Sanity Check:** Ensure the sign of the result matches the physical outcome (filling vs. emptying) and units (hours/minutes) are consistent.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Basic Tank Filling | "both opened", "all pipes" | Individual times | Combined time |
| Efficiency Variations | "twice as efficient", "diameter" | Efficiency ratios/diameters | Time taken |
| Partial Operation | "closed after", "already full" | Sequence of events | Time to finish |

---

## Formula Bank

**[Basic Tank Filling]**
$$\text{Net Rate} = \sum \text{Inlet Rates} - \sum \text{Outlet Rates}$$
→ *produces: total work per unit time*
→ *use when: multiple pipes act simultaneously*

$$\text{Time} = \frac{\text{Total Volume}}{\text{Net Rate}}$$
→ *produces: total time to complete*
→ *use when: finding duration for full task*

$$\text{Combined Time} = \frac{xy}{x+y}$$
→ *produces: time for two pipes together*
→ *use when: only two pipes filling*

**[Efficiency Variations]**
$$\text{Rate} \propto \text{Diameter}^2$$
→ *produces: relative speed of pipes*
→ *use when: pipe diameter is given*

$$\text{Time} = \frac{\text{Capacity}}{\text{Net Efficiency}}$$
→ *produces: time taken to fill*
→ *use when: pipes have different efficiencies*

**[Partial Operation]**
$$\text{Work} = \text{Rate} \times \text{Time}$$
→ *produces: amount of work completed*
→ *use when: calculating work in intervals*

$$\text{Time} = \frac{\text{Remaining Work}}{\text{Net Rate}}$$
→ *produces: time to finish remainder*
→ *use when: pipes are closed mid-process*

---

## Step Sequences

**Basic Tank Filling:** Find LCM → Calculate individual rates → Sum net rate → Divide capacity by rate.
**Efficiency Variations:** Determine efficiency ratios → Calculate net efficiency → Divide capacity by net efficiency.
**Partial Operation:** Calculate work done → Find remaining work → Divide by active pipe rate.

---

## Fastest Tricks

**Basic Tank Filling:** Use LCM of times as total capacity to avoid fractions.
**Efficiency Variations:** If diameter doubles, rate increases by factor of 4.
**Partial Operation:** Treat closed pipes as having 0 rate after their closing time.

---

## Trap Watch

**Basic Tank Filling:** Subtracting outlet rate → Always use negative sign.
**Efficiency Variations:** Diameter vs Rate → Square the diameter ratio.
**Partial Operation:** Current tank status → Use remaining capacity, not total.

---

## Last-Minute Reminders

Always convert all time units to a single standard (e.g., all minutes) before calculating rates.
An outlet pipe's rate must always be subtracted from the total inlet rate.
If a tank is partially full, subtract the existing volume from the total capacity before calculating time.
When diameter is mentioned, remember that area (and thus flow rate) scales with the square of the diameter.
If the net rate is negative, the tank is emptying, not filling.