# Number System — Exam Cheat Sheet

## How To Solve Any Question In This Chapter
1. **Identify Structure:** Scan for algebraic expressions (identities), large arithmetic operations (distributive property), or divisibility/remainder keywords.
2. **Classify Pattern:** Match the question structure to the Quick-Recognition Table below.
3. **Select Tool:** Extract the relevant formula from the Formula Bank.
4. **Simplify/Substitute:** Apply the formula or shortcut; use modular arithmetic for remainders or cyclicity for unit digits.
5. **Verify:** Check if the result is a logical integer, matches the sign, and satisfies the divisibility/remainder constraints.

---

## Quick-Recognition Table

| Pattern | Trigger Words | Given | Find |
| :--- | :--- | :--- | :--- |
| Algebraic Identities | "Simplify", "Evaluate", squares/cubes | Expression with variables | Simplified value |
| Basic Arithmetic | "Simplify", "Evaluate", large products | Arithmetic expression | Result |
| Counting/Sequences | "Sum", "Sequence", "Maximum value" | Series or constraints | Term or sum |
| Divisibility Rules | "Divisible by", "Least value" | Number with missing digit | Missing digit |
| Division Problems | "Added to", "Subtracted from", "Nearest" | Dividend, Divisor | Required number |
| Number Properties | "Prime", "Factors", "Zeros" | Integer | Property/Count |
| Remainder Theorems | "Remainder", "Divided by", "Power" | Dividend, Divisor | Remainder |
| Uncategorized | "Unit digit", "Odd number" | Power/Product | Unit digit |

---

## Formula Bank

**[Algebraic Identities]**
$$a^2 - b^2 = (a + b)(a - b)$$
→ *produces: difference of squares result*
→ *use when: two squares are subtracted*

$$a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$$
→ *produces: simplified sum/difference of cubes*
→ *use when: expression matches cube pattern*

$$(x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx)$$
→ *produces: expansion of trinomial square*
→ *use when: three terms are squared*

**[Basic Arithmetic]**
$$a(b \pm c) = ab \pm ac$$
→ *produces: simplified product*
→ *use when: common factor exists*

$$625 = \frac{10000}{16}$$
→ *produces: product with 625*
→ *use when: multiplying by 625*

**[Counting and Sequences]**
$$a_n = a + (n-1)d$$
→ *produces: n-th term of sequence*
→ *use when: finding specific term*

$$S_n = \frac{n}{2}(a + l)$$
→ *produces: sum of arithmetic series*
→ *use when: finding total sum*

**[Divisibility Rules]**
$$\text{Sum of digits} \pmod{3 \text{ or } 9} = 0$$
→ *produces: divisibility check*
→ *use when: checking 3 or 9*

$$\text{Last } k \text{ digits} \pmod{2^k} = 0$$
→ *produces: divisibility check*
→ *use when: checking 2, 4, 8, 16*

**[Division Problems]**
$$\text{Dividend} = \text{Divisor} \times \text{Quotient} + \text{Remainder}$$
→ *produces: missing component*
→ *use when: division components needed*

$$\text{Add} = \text{Divisor} - \text{Remainder}$$
→ *produces: value to make divisible*
→ *use when: finding smallest addition*

**[Number Properties]**
$$\text{Highest power of } p \text{ in } n! = \sum \lfloor \frac{n}{p^k} \rfloor$$
→ *produces: exponent of prime factor*
→ *use when: counting zeros or factors*

**[Remainder Theorems]**
$$a \equiv b \pmod{n} \implies a^k \equiv b^k \pmod{n}$$
→ *produces: reduced remainder*
→ *use when: large powers exist*

**[Uncategorized]**
$$\text{Unit digit of } a^n = \text{Unit digit of } a^{n \pmod 4}$$
→ *produces: unit digit*
→ *use when: finding last digit*

---

## Step Sequences

* **Algebraic Identities:** Identify identity → Substitute values → Simplify → Solve.
* **Basic Arithmetic:** Factor common terms → Distribute → Simplify → Calculate.
* **Counting/Sequences:** Identify sequence type → Apply sum formula → Calculate → Solve.
* **Divisibility Rules:** Sum digits/check last digits → Set equation → Solve for variable → Verify.
* **Division Problems:** Divide dividend → Find remainder → Calculate difference → Add/Subtract.
* **Number Properties:** Prime factorize → Sum exponents → Apply Legendre's formula → Solve.
* **Remainder Theorems:** Reduce base mod divisor → Apply power → Adjust sign → Result.
* **Uncategorized:** Find cyclicity → Reduce exponent mod 4 → Calculate unit digit → Solve.

---

## Fastest Tricks

* **Algebraic:** Use $(a+b)^2 - (a-b)^2 = 4ab$ to solve complex products instantly.
* **Arithmetic:** Multiply by $625$ by appending four zeros and dividing by $16$.
* **Divisibility:** For $99$, check sum of pairs of digits from right to left.
* **Division:** Nearest multiple is $Dividend \pm (\text{Divisor} - \text{Remainder})$.
* **Remainders:** If base is $n-1$, remainder is $(-1)^{\text{power}}$.
* **Unit Digits:** $4^{\text{odd}} \to 4$, $4^{\text{even}} \to 6$; $9^{\text{odd}} \to 9$, $9^{\text{even}} \to 1$.

---

## Trap Watch

* **Algebraic:** Confusing $a^2+b^2$ with $(a+b)^2$ → Check middle term.
* **Divisibility:** Forgetting to include the unknown digit in sum → Add $x$.
* **Division:** Adding remainder instead of difference → Use $Divisor - Remainder$.
* **Number Properties:** Counting 4 as a prime factor → Use $2^2$.
* **Remainders:** Negative remainder $\pmod n$ → Add $n$ to result.

---

## Last-Minute Reminders

1. The number 1 is neither prime nor composite.
2. The only even prime number is 2.
3. A number is divisible by 24 only if it is divisible by both 3 and 8.
4. The number of zeros at the end of $n!$ is the exponent of 5 in its prime factorization.
5. Always check if the remainder is negative before finalizing the answer.