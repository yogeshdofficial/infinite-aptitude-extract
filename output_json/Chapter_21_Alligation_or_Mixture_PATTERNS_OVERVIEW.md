# Alligation Or Mixture — Chapter Overview

## What This Chapter Is About

This chapter deals with the mathematical techniques used to determine the proportions in which two or more ingredients of different values (prices, concentrations, or qualities) must be combined to achieve a specific target value. The central relationship is the "Alligation Rule," which balances the differences between individual component values and the final mixture's mean value. You will encounter problems ranging from simple price blending to complex scenarios involving repeated replacements, profit-based adjustments, and mixing multiple vessels.

---

## Core Concepts

**[The Mean Price Principle]** — This is the "anchor" of the mixture. It represents the cost or value of one unit of the final mixture. You must always ensure that the values of the individual components and the mean price are in the same units (e.g., all per kg or all per litre) before performing any calculations.

**[The Balancing Act (Alligation)]** — Alligation is essentially a shortcut for a weighted average. It works on the principle that the ratio of the quantities of two ingredients is inversely proportional to the difference between their individual values and the mean value. If you have a "cheaper" item and a "dearer" item, the quantity of the cheaper item is determined by the distance of the dearer item from the mean, and vice versa.

**[Unit Consistency]** — Because alligation relies on comparing values, you cannot mix "apples and oranges." If one component is given as a price per kg and another as a price per litre, or if one is a cost price and the other is a selling price, you must convert them all to a common base (usually cost price per unit) before starting.

**[Replacement Logic]** — When a portion of a mixture is removed and replaced with a pure substance, the concentration of the original liquid decreases geometrically. This is not a simple subtraction problem; it is a process of repeated dilution where the total volume remains constant, but the composition changes with every operation.

---

## Key Terms Glossary

**Alligation** — A rule used to find the ratio in which two or more ingredients at different prices must be mixed to produce a mixture of a desired price.

**Mean Price** — The cost price per unit of the final mixture. It must always lie numerically between the prices of the two individual ingredients being mixed.

**Cheaper/Dearer** — Terms used to denote the ingredient with the lower unit price and the higher unit price, respectively.

**Replacement** — The process of withdrawing a specific quantity of a mixture from a container and substituting it with an equal quantity of another liquid (usually water).

---

## Pattern Map

1. **Alligation Basics** (4 questions) — The foundational setup: finding the ratio of two ingredients given their individual prices and the target mean price.
2. **Missing Component Price** (3 questions) — Requires finding the price of one ingredient when the ratio and the other prices are already known.
3. **Profit-Based Alligation** (8 questions) — The target price is given as a selling price with a profit percentage; you must first calculate the cost price (mean price) before applying alligation.
4. **Quantity Adjustment** (6 questions) — Involves scaling the calculated ratio to match a specific total quantity or a specific amount of one ingredient.
5. **Vessel Mixing** (4 questions) — Deals with combining two different mixtures (each with its own internal ratio) to create a third mixture with a specific target ratio.
6. **Mixture Replacement** (6 questions) — The "repeated dilution" scenario: calculating the remaining quantity of a pure liquid after $n$ cycles of removing and replacing.

---

## Core Formulas

### The Rule of Alligation
$$
\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{\text{Price of Dearer} - \text{Mean Price}}{\text{Mean Price} - \text{Price of Cheaper}}
$$
**Variables:** Prices must be per unit quantity.
**When to use:** Whenever you need to find the ratio of two ingredients to reach a target mean price.
**Key insight:** The mean price must always be between the cheaper and dearer prices; if it isn't, the mixture is physically impossible.

### Repeated Replacement Formula
$$
\text{Final Quantity of Pure Liquid} = \text{Initial Quantity} \times \left(1 - \frac{y}{x}\right)^n
$$
**Variables:** $x$ = total volume of container, $y$ = quantity replaced in each operation, $n$ = number of operations.
**When to use:** When a fixed amount of mixture is repeatedly removed and replaced with pure water.
**Key insight:** This formula calculates the amount of the *original* liquid remaining, not the amount of water added.

---

## Suggested Study Order

1. **Alligation Basics** — Master the core ratio calculation first; it is the foundation for everything else.
2. **Missing Component Price** — A simple algebraic rearrangement of the basic rule.
3. **Profit-Based Alligation** — Introduces the necessity of converting Selling Price to Cost Price, a common exam requirement.
4. **Quantity Adjustment** — Teaches you how to apply the ratio to real-world volume constraints.
5. **Vessel Mixing** — A more advanced application of the basic rule using fractions/ratios.
6. **Mixture Replacement** — A distinct logic (geometric decay) that stands apart from the standard alligation grid.

---

## Chapter-Wide Traps

**Unit Mismatch:** Using a selling price as the mean price without converting it to cost price → Always calculate the cost price of the mixture first if a profit percentage is involved.

**Ratio Inversion:** Confusing the position of the cheaper and dearer quantities in the final ratio → Always remember that the "cheaper" quantity is associated with the difference from the "dearer" price.

**Replacement Confusion:** Assuming the replacement formula calculates the amount of water added → Remember it calculates the *remaining* original liquid; subtract this from the total to find the water.