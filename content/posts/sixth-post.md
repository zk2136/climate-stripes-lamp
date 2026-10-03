---
title: "🧮 Loading and Normalising the Data"
date: 2026-09-11
weight: 6
math: true
draft: false
description: "Store climate data in an array and use an index loop to step through it."
tags: ["programming", "arrays", "loops"]
---

To process 12 decades of historical records, we will store them in a single array and iterate over each value using a loop.

---

<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 24px; margin: 24px 0;">
  <div style="flex: 1;">

### Step 1: Create the Data Array
1. Open **Variables** and make a variable named `raw_data`.
2. From **Arrays**, drag `set list to array of` and attach it inside `on start`. Rename `list` to `raw_data`.
3. Click the **(+)** button to expand the list to 12 items.
4. Fill the slots with your 12 temperature anomalies:
   * `-11`, `-17`, `-2`, `15`, `29`, `-1`, `-3`, `-11`, `21`, `81`, `84`, `127`
   
</div>
  <div style="flex: 1; text-align: center;">
    <img src="/images/microbit-2.png" alt="Setting the variables in Makecode" style="max-width: 100%; border-radius: 8px;" />
  </div>
</div>

---

<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 24px; margin: 24px 0;">
  <div style="flex: 1;">

### Step 2: Loop Through Each Decade
1. Under **Loops**, grab `for index from 0 to 4` and snap it under the data block.
2. Change the `4` to **`11`** (since array indices run from `0` to `11`).
3. In **Variables**, create a variable named `current_val`.
4. Inside the loop, snap in:
   * `set current_val to raw_data get value at (index)`

This allows the micro:bit to inspect each decade's temperature one by one.

</div>
  <div style="flex: 1; text-align: center;">
    <img src="/images/microbit-3.png" alt="Creating the loop for the array" style="max-width: 100%; border-radius: 8px;" />
  </div>
</div>

