---
title: "🕹️ Intro to the BBC micro:bit & ZIP Circle"
date: 2026-09-11
math: true
weight: 2
draft: false
description: "Meet the micro:bit microcontroller and the Kitronik ZIP Circle LED ring."
tags: ["microbit", "hardware", "led"]
---

Before we build the circuit, let's understand the two key electronic components used in this workshop.

---

### The BBC micro:bit

The **BBC micro:bit** is a compact pocket-sized computer designed for physical computing. It includes:
* **Edge Connector Pads:** Large conductive holes at the bottom (`0`, `1`, `2`, `3V`, `GND`) that connect easily to alligator clip leads.
* **Micro-USB Port:** Used to supply power from your laptop and flash programs directly to flash memory.
* **Processor & Memory:** Runs your block code and stores variables, arrays, and loops.

---

### The Kitronik ZIP Circle

The **ZIP Circle** is an array of 12 individually addressable RGB LEDs (often referred to as NeoPixels).

Unlike standard LEDs, which require individual power pins for each light:
* All 12 LEDs share **one single data wire** using a serial communication protocol.
* Each LED contains its own microchip that reads its assigned colour and passes the remaining signal down the line.
* The board connects using only 3 pads:
  * **`+V` / `+5V`:** Power supply.
  * **`0V` / `GND`:** Ground connection.
  * **`DIN`:** Data Input to receive signals from the micro:bit.
