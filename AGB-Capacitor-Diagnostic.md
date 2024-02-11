---
title: AGB Capacitor Diagnostic
slug: 49bB-agb-capacitor-diagnostic
description: Learn how to test the voltage of electrolytic capacitors in your GBA console with this comprehensive guide. With step-by-step instructions and accompanying images, you'll easily locate the capacitors and ensure accurate measurements. Find a handy table th
createdAt: Fri May 27 2022 17:34:18 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

If you're unsure about whether your GBA console needs a recap, you can test the voltage at these points associated with each electrolytic capacitor.

Unless you have a power supply, measuring the capacitors can be a difficult task unless you know exactly where to probe. We've laid out these locations below so you can test the voltages with AA batteries in the GBA housing (Which blocks the rear side of the PCB).

Measurements are performed with a multimeter in DC voltage mode. Read your multimeter's manual for full details on setup for your device.

Your black probe can be placed on the negative battery terminal labelled **BT-** on the PCB. Your red probe would go to the point for which you are measuring voltage.

If your readout is significantly less than the voltages listed, the respective capacitor likely needs replacing.

![Located near SELECT/START](../../assets/COgceCPfieEzq89RaeQD4_image.png)

## Measurement Locations

### CP1

![Located near SELECT/START](../../assets/qd-Www_vnUO13AGWvQUh1_image.png)

### CP2

![Located below D-Pad RIGHT](../../assets/yIC4-7PW8dUQ4XzsdwqiP_image.png)

### CP3

![Located just above START](../../assets/id8NKr-XgzOPVvVN_pZzG_image.png)

### CP4

![Located near headphone jack](../../assets/3kxFAefsm9pePLcm_UioT_image.png)

## Capacitor Measurements

The following measurements were performed on a known working board that has been recapped.

:::hint{type="danger"}
Note for CP1 - the measurement should directly correlate with the voltage of your batteries combined. If you have two AA batteries that measure 1.5v, the CP1 measurement would be closer to 3v.

Similarly, if one battery measures 1.2v, and the other measures 1.5v, the total measurement would be expected to be around 2.7v.
:::

| Cap Name | Voltage  |
| -------- | -------- |
| CP1      | 2v to 3v |
| CP2      | 5v       |
| CP3      | 3.33v    |
| CP4      | 1v       |

## Citations

Board scans - <https://circuit-board.de/forum/index.php/Thread/13913-STRIP-CLUB-PCB-Scans/?pageNo=1>

