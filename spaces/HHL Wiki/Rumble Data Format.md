---
title: Rumble Data Format
slug: r96W-rumble-data-format
description: Learn about the rumble data layout for controllers like Joy-Cons and Pro Controllers, including its division into sections based on frequencies and amplitudes. This document presents a comprehensive table detailing the specific values for each section. Ad
createdAt: Sat Mar 19 2022 21:26:57 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

The rumble data is split up between left and right. This is for the splitting of Joy-Cons but also for Pro Controllers which have two linear resistance actuators (LRA) that can be controlled independently.

### Rumble data layout

| Index array (based on real report) | Data        | Description                                                                                        |
| ---------------------------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| 2 - HF Low Range Mode              | 0x04 - 0xFC | Left side - Encoded High Frequency. 81.75Hz - 313.14Hz. &#xA;Requires LSB of byte 3 to be cleared. |
| 2 - HF High Range Mode             | 0x00 - 0xC8 | Left side - Encoded High Frequency 320Hz - 1252.57Hz. &#xA;Requires LSB of byte 3 to be set.       |
| 3                                  | 0x00 - 0xC8 | Left side - High Frequency Amplitude. Increments of 0x0200.                                        |
| 4 - LF                             | 0x01 - 0x7F | Left Side - Low Frequency. 40.87Hz - 626.28Hz.                                                     |
| 5 - LF Amplitude Low Mode          | 0x40 - 0x72 | Left Side - Encoded Low Frequency Amplitude.&#xA;Requires MSB of byte 4 to be cleared.             |
| 5 - LF Amplitude Intermediate Mode | 0x40 - 0x71 | Left Side - Encoded Low Frequency Intermediate Amplitude.&#xA;Requres MSB of byte 4 to be set.     |

Bytes 6-9 are repeated but for the Right controller/LRA.

### Decoding rumble data

:::hint{type="info"}
**Under construction**
:::

