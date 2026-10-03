---
title: "🔌 Wiring the ZIP Circle"
date: 2026-09-11
math: true
weight: 4
draft: false
description: "Wire the 12-LED ring using solderless alligator clip connections."
tags: ["electronics", "wiring", "circuits"]
---

We will now wire the ZIP Circle to the micro:bit using 3 alligator clip leads.

---

### Connection Guide

Ensure your micro:bit is unplugged from your laptop before connecting the clips.

| Alligator Lead | micro:bit Pad | ZIP Circle Pad | Purpose |
| :--- | :--- | :--- | :--- |
| **Red Clip** | **`3V`** | **`+V`** | Power supply (3.3V) |
| **Black Clip** | **`GND`** | **`0V`** | Ground reference |
| **Yellow Clip** | **`0` (Pin 0)** | **`DIN`** | Data Input signal |

> **Safety Tip:** Ensure no metal contacts of each wire are touching each other to avoid short circuiting.

---

### Add the NeoPixel Extension in MakeCode
1. Return to MakeCode and click the **Extensions** category at the bottom of the toolbox.
2. Type **`neopixel`** into the search bar and click on the **neopixel** card.
3. A new cyan **Neopixel** category will appear in your block menu.

---

<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 24px; margin: 24px 0;">
  <div style="flex: 1;">

### Hardware Test Program
Inside your `on start` block:
1. `set strip to Neopixel at pin P0 with 12 leds as RGB (GRB-format)`
2. `strip set brightness to 60`
3. `strip show color Red`

Flash this program to your micro:bit. All 12 LEDs should glow solid red.

</div>
  <div style="flex: 1; text-align: center;">
    <img src="/images/microbit-1.png" alt="Hardware test program in MakeCode" style="max-width: 100%; border-radius: 8px;" />
  </div>
</div>
