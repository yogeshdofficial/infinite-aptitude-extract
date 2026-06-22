# Successive Change

## Overview
This pattern involves scenarios where a value undergoes multiple percentage changes, either sequentially or simultaneously. The central idea is to treat the initial value as a base (usually 100) and apply each percentage change as a multiplier to find the final value.

---

## Recognition Clues
* **Keywords:** "Increased by", "Reduced by", "Percentage change", "Next year", "Again".
* **Given:** Initial values (or a base of 100) and multiple percentage rates.
* **Asked:** Final percentage change, or the final value after all changes.
* **Structure:** Look for a chain of events (e.g., wage reduced then increased) or compound effects (e.g., hours and wages both changing).

---

## Key Formulas

### [Net Percentage Change]
$$
\text{Net \%} = x + y + \frac{xy}{100}
$$
**Variables:**
- $x$ = first percentage change (use negative for reduction)
- $y$ = second percentage change (use negative for reduction)

**When to use:** When two successive percentage changes are applied to the same base.

**Worked example:** Wage reduced by 50% ($x = -50$) and then increased by 50% ($y = +50$).
Net % = $-50 + 50 + \frac{(-50 \times 50)}{100} = 0 - 25 = -25\%$.

### [Percentage Increase/Decrease]
$$
\text{\% Change} = \left( \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \right) \times 100
$$
**Variables:**
- $\text{New Value}$ = value after changes
- $\text{Old Value}$ = initial value

**When to use:** To find the total percentage shift after calculating the final result.

---

## Solution Framework

**Step 1: Assume a base value** — Use 100 if no initial value is given to make percentage calculations trivial.
**Step 2: Apply changes sequentially** — Multiply the base by $(1 \pm \frac{r}{100})$ for each change to find the new value.
**Step 3: Calculate the difference** — Subtract the original value from the new value to find the absolute change.
**Step 4: Convert to percentage** — Divide the absolute change by the original value and multiply by 100.

---

## Shortcut Tricks

* **Trick:** For two successive changes of $x\%$ and $y\%$, use the formula $x + y + \frac{xy}{100}$.
* **Why it works:** It accounts for the compounding effect of the second percentage acting on the already changed value.
* **When to use it:** When you need the net percentage change of two sequential events.
* **Example:** Hours increased by 20%, wages by 15%. Net change = $20 + 15 + \frac{20 \times 15}{100} = 35 + 3 = 38\%$.

---

## Common Mistakes

* **Mistake:** Adding percentages directly (e.g., 50% reduction + 50% increase = 0%).
* **Why it happens:** Ignoring that the second percentage applies to the *reduced* base, not the original.
* **Fix:** Always calculate the value after the first change before applying the second.
* **Mistake:** Using the new value as the denominator for percentage change.
* **Why it happens:** Forgetting that percentage change is always relative to the *original* value.

---

## Worked Example (Step-by-Step)

**Question:** A man‘s wage was reduced by 50%. Again the reduced wage was increased by 50%. Find his loss in terms of percentage.

**Solution:**
1. **Assume base:** Let original wage = 100.
2. **Apply first change:** Reduced by 50% $\rightarrow 100 - (50\% \text{ of } 100) = 50$.
3. **Apply second change:** Increased by 50% $\rightarrow 50 + (50\% \text{ of } 50) = 50 + 25 = 75$.
4. **Calculate difference:** $100 - 75 = 25$ (Loss).
5. **Calculate %:** $\frac{25}{100} \times 100 = 25\%$.

**Answer:** 25% loss.

---

## Similar Patterns
**Profit and Loss:** Distinguished by the presence of "Cost Price" and "Selling Price" terminology; Successive Change focuses on the *process* of change rather than trade margins.

---

## Revision Summary
* **Key formula:** $x + y + \frac{xy}{100}$ for net change.
* **Spot it by:** Multiple percentage changes applied to a single entity.
* **First move:** Assume 100 as the starting value.
* **Fastest method:** Use the net change formula for two sequential events.
* **Biggest trap:** Adding percentages directly instead of compounding them.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage** — A fraction with 100 as the denominator; $x\% = \frac{x}{100}$.
* **Multipliers** — An increase of $r\%$ is equivalent to multiplying by $(1 + \frac{r}{100})$; a decrease is $(1 - \frac{r}{100})$.

### Formulas You Must Know First
$$
\text{Value} = \text{Base} \times \left(1 \pm \frac{r}{100}\right)
$$
**What it means:** This calculates the new value after a single percentage change.
**Example:** 10% increase on 200 is $200 \times 1.10 = 220$.

### Terms Used In This Pattern
* **Income/Expenditure/Savings** — $Savings = Income - Expenditure$.
* **Wage** — Payment for work, often calculated as $Hours \times Rate$.