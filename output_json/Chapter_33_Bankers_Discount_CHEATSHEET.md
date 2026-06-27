# Bankers Discount — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Variables:** Extract Face Value (Sum), Time (convert to years), Rate, and any known Discount (B.D. or T.D.).
2. **Check Time:** Always add 3 days of grace to the bill period before calculating time in years.
3. **Select Pattern:** Use the Quick-Recognition Table to match your knowns/unknowns to a pattern.
4. **Apply Relation:** Use the B.D./T.D./B.G. relationship formulas to bridge missing values.
5. **Calculate:** Solve the algebraic equation.
6. **Sanity Check:** Ensure $B.D. > T.D.$ and $B.G. = B.D. - T.D.$

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| **Basic Relations** | "due date", "discounted on" | Face Value, Rate, Time | B.D., T.D., B.G. |
| **Sum & Rate** | "due a certain time", "rate percent" | B.D., T.D., Time | Sum, Rate |
| **Time Equivalence** | "B.D. equals T.D.", "same time" | Two amounts, Rate | Time |

---

## Formula Bank

**[Basic Discount Relations]**

$$B.D. = \text{S.I. on Face Value}$$
→ *produces: Banker's Discount*
→ *use when: Calculating discount on face value*

$$T.D. = \frac{\text{Face Value} \times R \times T}{100 + (R \times T)}$$
→ *produces: True Discount*
→ *use when: Finding T.D. from Face Value*

$$B.G. = B.D. - T.D.$$
→ *produces: Banker's Gain*
→ *use when: Both discounts are known*

$$B.G. = \frac{(T.D.)^2}{P.W.}$$
→ *produces: Banker's Gain*
→ *use when: T.D. and P.W. are known*

$$T.D. = \sqrt{P.W. \times B.G.}$$
→ *produces: True Discount*
→ *use when: P.W. and B.G. are known*

**[Sum and Rate Calculation]**

$$Sum = \frac{B.D. \times T.D.}{B.D. - T.D.}$$
→ *produces: Face Value (Sum)*
→ *use when: Both discounts are known*

$$Rate = \frac{100 \times B.D.}{Sum \times Time}$$
→ *produces: Annual Rate %*
→ *use when: Sum, B.D., and Time known*

$$Rate = \frac{B.G. \times 100}{T.D. \times T}$$
→ *produces: Annual Rate %*
→ *use when: B.G., T.D., and Time known*

**[Time Equivalence]**

$$Interest = \text{Difference between amounts}$$
→ *produces: Interest on P.W.*
→ *use when: B.D. equals T.D. for different sums*

$$Time = \frac{Interest \times 100}{P.W. \times R}$$
→ *produces: Time in years*
→ *use when: Finding duration for equivalence*

---

## Step Sequences

**Basic Relations:** Identify Face Value → Add 3 days grace → Calculate B.D. → Calculate T.D. → Subtract for B.G.
**Sum & Rate:** Identify B.D./T.D. → Apply Sum formula → Apply Rate formula → Simplify fraction.
**Time Equivalence:** Find difference of amounts → Treat as S.I. → Apply S.I. formula → Solve for T.

---

## Fastest Tricks

* **Basic Relations:** $B.D. = T.D. \times (1 + \frac{RT}{100})$.
* **Basic Relations:** $B.G. = \frac{T.D. \times R \times T}{100}$.
* **Sum & Rate:** If $B.D. = 10\%$ of amount, effective rate is $\frac{10}{90} = 11.11\%$.
* **Time Equivalence:** Difference between amounts is the interest on the smaller amount.

---

## Trap Watch

* **Basic Relations:** Forgetting 3 days grace → Add 3 days.
* **Sum & Rate:** Confusing Sum with P.W. → Use Sum formula.
* **Time Equivalence:** Using wrong principal → Use smaller amount.

---

## Last-Minute Reminders

* Always convert months to years by dividing by 12.
* Banker's Discount is always calculated on the Face Value.
* True Discount is always calculated on the Present Worth.
* Banker's Gain is the interest on the True Discount.
* The Face Value is the sum of Present Worth and True Discount.