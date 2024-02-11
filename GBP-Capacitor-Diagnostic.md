---
title: GBP Capacitor Diagnostic
slug: O_qB-gbp-capacitor-diagnostic
description: Learn how to test the voltage of electrolytic capacitors in your Game Boy Pocket console with this comprehensive document. Using a multimeter in DC voltage mode, you'll uncover step-by-step instructions and specific measurement locations for capacitors C3
createdAt: Tue Jun 07 2022 16:53:49 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

If you're unsure about whether your Game Boy Pocket console needs a recap, you can test the voltage at these points associated with each electrolytic capacitor.

Unless you have a power supply, measuring the capacitors can be a difficult task unless you know exactly where to probe. We've laid out these locations below so you can test the voltages with AA batteries in the Game Boy Color housing (Which blocks the rear side of the PCB).

Measurements are performed with a multimeter in DC voltage mode. Read your multimeter's manual for full details on setup for your device.

Your black probe can be placed on the negative battery terminal labelled **BT-** on the PCB. Your red probe would go to the point for which you are measuring voltage. An alternate location for the black probe is also shown here.

If your readout is significantly less than the voltages listed, the respective capacitor likely needs replacing.

![](../../assets/PfcpizBcdjF-0ODurU_W3_image.png)

## Measurement Locations

### C30

![](../../assets/GXAmZ9AoM-yaPlbpATDSy_image.png)

### C32

![](../../assets/dUV4wrvnTDoPYPfy2mo0b_image.png)

### C29

![](../../assets/vQ9Q637KG6s_fPk5-wVeg_image.png)

### C31

:::hint{type="danger"}
If you do not get a voltage read out, you may also have a dead speaker. Test the speaker as well to be sure.
:::

![](../../assets/JrjeTH5SXJZ-CRnhqy3MA_image.png)

## Capacitor Measurements

The following measurements were performed on a known working board that has been recapped.

| Cap Name | Voltage |
| -------- | ------- |
| C30      | 5v      |
| C32      | 2.93v   |
| C29      | -18v    |
| C31      | 1.25v   |

## Citations

Board scans originated at [](https://circuit-board.de/forum/index.php/Thread/13913-STRIP-CLUB-PCB-Scans/?pageNo=1)[](https://commons.wikimedia.org/wiki/File\:Nintendo-Game-Boy-Color-Motherboard-Top.jpg)<https://commons.wikimedia.org/wiki/File:Nintendo-Game-Boy-Pocket-Motherboard-Top.jpg> - Evan-Amos, Public domain, via Wikimedia Commons

