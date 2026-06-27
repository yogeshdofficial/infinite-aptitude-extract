# Divisibility Rules

## Overview
These questions test your ability to determine if a number is divisible by a specific divisor or to find a missing digit that makes a number divisible. The central idea is to apply specific digit-sum or digit-position rules to avoid long division.

---

## Recognition Clues
* **Keywords:** "divisible by", "least value must be assigned to *", "which of the following numbers is divisible by".
* **Given:** A large number (often with a missing digit like `*` or `$`).
* **Asked:** The missing digit or a confirmation of divisibility.
* **Scan for:** The divisor (e.g., 3, 4, 5, 8, 9, 11, 24).

---

## Key Formulas

### [Divisibility by 3 and 9]
$$ \text{Sum of digits} \div \text{Divisor} = \text{Integer} $$
**Variables:** Sum of digits = total of all individual digits in the number.
**When to use:** When the divisor is 3 or 9.
**Worked example:** For 197*5462 (divisible by 9), sum = $1+9+7+x+5+4+6+2 = 34+x$. Next multiple of 9 is 36. $34+x=36 \implies x=2$.

### [Divisibility by 4 and 8]
$$ \text{Last } n \text{ digits} \div \text{Divisor} = \text{Integer} $$
**Variables:** $n=2$ for 4; $n=3$ for 8.
**When to use:** When the divisor is 4 or 8.
**Worked example:** For 618703572 (divisible by 4), last two digits are 72. $72 \div 4 = 18$. Since 18 is an integer, it is divisible.

### [Divisibility by 11]
$$ (\text{Sum of odd-place digits}) - (\text{Sum of even-place digits}) = 0 \text{ or multiple of } 11 $$
**Variables:** Odd/Even places are counted from the right (ones place is 1st).
**When to use:** When the divisor is 11.
**Worked example:** For 4832718: Odd (8,7,3,4) sum=22; Even (1,2,8) sum=11. $22-11=11$. Divisible.

---

## Solution Framework
1. **Identify the Rule:** Match the divisor to its specific rule (e.g., 3/9 use sum, 4/8 use last digits, 11 uses alternating sum).
2. **Apply the Rule:** Calculate the required sum or isolate the required digits.
3. **Solve for Unknown:** If a digit is missing, set up an equation to reach the nearest multiple of the divisor.
4. **Verify:** Check if the resulting number satisfies the condition.
5. **Composite Divisors:** If the divisor is composite (e.g., 24), split it into co-prime factors (3 and 8) and check both.

---

## Shortcut Tricks
* **Trick:** For divisibility by 9, "cast out nines" (ignore any digits that sum to 9 while adding).
* **Why it works:** Adding 9 to a sum does not change its divisibility by 9.
* **When to use:** When summing a long string of digits.
* **Example:** In 197*5462, ignore 9, ignore (7+2), ignore (5+4). Remaining: $1+6=7$. $7+x$ must be 9, so $x=2$.

---

## Common Mistakes
* **Mistake:** Starting the 11-divisibility count from the left. **Fix:** Always count positions from the right (ones place is 1st).
* **Mistake:** Using 4 and 6 to check for 24. **Fix:** Use co-prime factors (3 and 8).
* **Mistake:** Forgetting to include the unknown digit in the sum. **Fix:** Treat the `*` as a variable $x$ and include it in the addition.

---

## Worked Example (Step-by-Step)

**Question:** What least value must be assigned to * so that 62684*0 is divisible by 8?

**Solution:**
1. **Identify Rule:** Divisibility by 8 requires the last three digits to be divisible by 8.
2. **Apply Rule:** The last three digits are $4*0$.
3. **Solve for Unknown:** We need $4*0$ to be a multiple of 8.
   - If $*=0$, $400 \div 8 = 50$ (Divisible).
   - If $*=4$, $440 \div 8 = 55$ (Divisible).
   - If $*=8$, $480 \div 8 = 60$ (Divisible).
4. **Select Least Value:** The question asks for the *least* value, which is 0.

**Answer:** 0

---

## Similar Patterns
* **Remainder Theorems:** These ask for the remainder when a number is divided, whereas divisibility rules ask if the remainder is 0.

---

## Revision Summary
* **Key formula:** Sum of digits (3, 9) or Last digits (4, 8).
* **Spot it by:** "Divisible by" or missing digit `*`.
* **First move:** Identify the divisor and apply its specific rule.
* **Fastest method:** Use "casting out nines" for 9 and check co-primes for composite divisors.
* **Biggest trap:** Counting positions from the left for 11.

---

## Appendix: Prerequisites
### Concepts You Must Know
* **Co-prime numbers** — Numbers with no common factors other than 1.
* **Multiples** — A number is a multiple of $n$ if it can be divided by $n$ without a remainder.

### Formulas You Must Know First
* **Composite Factorization:** $24 = 3 \times 8$.
* **Place Value:** The rightmost digit is the "ones" place (1st position).

### Terms Used In This Pattern
* **Digit:** The symbols 0-9 used to form a number.
* **Divisor:** The number by which another number is to be divided.