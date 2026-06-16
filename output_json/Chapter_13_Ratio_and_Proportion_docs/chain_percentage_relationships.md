# Pattern: Chain Percentage Relationships

## 1. Pattern Overview
- This pattern solves problems involving successive percentage changes or sequential ratio-based transformations applied to a single initial quantity.
- It matters because it allows you to calculate the final state of a value without needing to track every intermediate step individually, saving time and reducing calculation errors.

## 2. Key Formulas
- **Successive Percentage Change:** If a quantity $P$ undergoes successive changes of $a\%$, $b\%$, and $c\%$, the final value $V$ is:
$$V = P \times \left(1 \pm \frac{a}{100}\right) \times \left(1 \pm \frac{b}{100}\right) \times \left(1 \pm \frac{c}{100}\right)$$
- **Replacement/Dilution Formula (from Context VII):** If $x$ is the initial volume, $y$ is the amount replaced, and $n$ is the number of operations:
$$\text{Final Pure Liquid} = x \left(1 - \frac{y}{x}\right)^n$$

## 3. When to Use This Pattern
- **Keywords:** "Successive," "Compounded," "Replaced," "After $n$ operations," "Increased by $x\%$ then decreased by $y\%$."
- **Recognition:** Look for a sequence of events where the output of one percentage change becomes the input for the next.
- **Given:** Initial value, sequence of percentage changes or replacement ratios.
- **To Find:** Final value after all operations or the initial value given the final result.

## 4. Core Concept & Theory
The fundamental idea is **Multiplicative Scaling**. Instead of adding or subtracting percentages (which is a common error), we treat each percentage change as a multiplier. A $10\%$ increase is a multiplier of $1.10$; a $10\%$ decrease is a multiplier of $0.90$. By multiplying these factors together, we create a "chain" that represents the total net effect of all operations.

## 5. Step-by-Step Solution Method
1. **Identify the Initial Value ($P$):** Determine the starting quantity. If unknown, assign it as $x$.
2. **Convert Percentages to Multipliers:** For each change, calculate $(1 + \frac{r}{100})$ for increases or $(1 - \frac{r}{100})$ for decreases.
3. **Set up the Chain:** Multiply the initial value by the sequence of multipliers.
4. **Solve for the Unknown:** Isolate the variable to find the final value or the initial value.
5. **Verify:** Check if the final value makes logical sense relative to the initial value (e.g., if all changes were increases, the final value must be larger).

## 6. Worked Examples

**Example 1: Successive Price Changes**
Given: A product costs $\$200$. Its price increases by $10\%$ and then decreases by $20\%$.
Solution:
1. Initial $P = 200$.
2. Multipliers: $10\%$ increase $\rightarrow 1.10$; $20\%$ decrease $\rightarrow 0.80$.
3. Chain: $200 \times 1.10 \times 0.80$.
4. Calculation: $200 \times 0.88 = 176$.
Final Price: $\$176$.

**Example 2: Liquid Replacement**
Given: A container has $100$ liters of milk. $10$ liters are removed and replaced with water. This is done $2$ times.
Solution:
1. $x = 100, y = 10, n = 2$.
2. Formula: $100 \times (1 - \frac{10}{100})^2$.
3. Calculation: $100 \times (0.9)^2 = 100 \times 0.81 = 81$.
Final Pure Milk: $81$ liters.

## 7. Recognition Clues & Keywords
- **Signals:** "Successive discounts," "Population growth over years," "Depreciation of assets."
- **Distinction:** Do not confuse this with **Simple Interest** or **Additive Change**. In this pattern, the percentage is always applied to the *current* value, not the *original* value.

## 8. Common Mistakes
1. **Adding Percentages:** Students often calculate $10\% + 20\% = 30\%$ change. This is wrong because the second percentage applies to the *new* value, not the original.
2. **Ignoring the Base:** Forgetting that the base changes after every step. Always use the multiplier method to avoid this.
3. **Incorrect Replacement Formula:** Applying the replacement formula when the amount replaced ($y$) changes each time. The formula only works if $y$ is constant.

## 9. Practice Tips
- **Mastery:** Practice converting percentages to fractions (e.g., $25\% = 1/4$, so multiplier is $5/4$) to make mental math faster.
- **Related Patterns:** Study **Compound Interest** (which is essentially a chain percentage problem over time) and **Ratio Compounding** (Section IV-ii of your context).