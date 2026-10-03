---
title: "📊 What are Climate Warming Stripes?"
date: 2026-09-11
math: true
weight: 5
draft: false
description: "Explore temperature anomalies and how the Ed Hawkins visualisation works."
tags: ["climate", "data", "science"]
---

In 2018, climate scientist Professor Ed Hawkins created the **Warming Stripes** graphic to communicate rising global temperatures without confusing numbers, axis labels, or graphs.

---

### Absolute Temperature vs. Temperature Anomaly

Instead of plotting actual degrees (e.g. $14^\circ\text{C}$), climate scientists use **temperature anomalies**:
* An **anomaly** measures the difference between a recorded temperature and a long-term historical baseline.
* The UK baseline used here is the **1961–1990 average** ($8.29^\circ\text{C}$).
* **Negative values:** Years or decades that were cooler than the historical average.
* **Positive values:** Years or decades that were warmer than the historical average.

---

### The 12-Decade UK Dataset

We are using UK Met Office mean [temperature data](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt) binned into 12 ten-year periods (1904–2023), multiplied by 100 to work cleanly as whole numbers:
[-11, -17, -2, 15, 29, -1, -3, -11, 21, 81, 84, 127]

* Index `0` (1904–1913) was $-0.11^\circ\text{C}$ below average (`-11`).
* Index `5` (1954–1963) was the coldest era in the record at $-0.01^\circ\text{C}$ (`-1`).
* Index `11` (2014–2023) was the hottest decade at $+1.27^\circ\text{C}$ (`127`).


