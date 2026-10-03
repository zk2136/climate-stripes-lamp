---
title: "🎨 Mapping Data to Colours"
date: 2026-09-11
weight: 7
math: true
draft: false
description: "Translate temperature anomalies into warming stripe colours using conditional logic."
tags: ["coding", "conditionals", "display"]
---

Now we will translate the anomaly values into distinct colours that represent historical climate shifts.

---

### The Classification Brackets

* **$\le -15$:** Dark Blue (Coldest decades)
* **$\le -6$:** Light Blue / Cyan (Cooler than average)
* **$\le 15$:** White (Stable historical baseline)
* **$\le 82$:** Orange (Noticeable warming)
* **Above $82$:** Red (Extreme record heat)

---

<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 24px; margin: 24px 0;">
  <div style="flex: 1;">

### Step-by-Step Logic Setup
1. Inside your `for index from 0 to 11` loop, right below `set current_val`, add an **`if / else if / else`** block.
2. Use the **(+)** icon on the bottom of the condition block to add branches until you have 5 sections:
   * **If** `current_val <= -15` $\to$ `strip set pixel color at (index) to Blue`
   * **Else if** `current_val <= -6` $\to$ `strip set pixel color at (index) to rgb(0, 150, 255)`
   * **Else if** `current_val <= 15` $\to$ `strip set pixel color at (index) to White`
   * **Else if** `current_val <= 82` $\to$ `strip set pixel color at (index) to Orange`
   * **Else** $\to$ `strip set pixel color at (index) to Red`
3. At the very end of `on start` (outside the loop), attach **`strip show`**.

</div>
  <div style="flex: 1; text-align: center;">
    <img src="/images/microbit-4.png" alt="Setting limits to assign colours to temperatures" style="max-width: 100%; border-radius: 8px;" />
  </div>
</div>

Flash the code to see your LED ring transform into the 120-year climate sequence.

