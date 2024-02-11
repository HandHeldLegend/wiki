---
title: ProGCC User Guide
slug: 9SbW-progcc-user-guide
description: Discover the ProGCC Conversion Kit, the ultimate tool for competitive gamers. This document explores how to transform your Pro Controller into a wired powerhouse with five trigger modes. Compatible with GameCube, Wii, and adapters, this controller is a ga
createdAt: Thu Apr 21 2022 02:09:12 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

:::hint{type="info"}
This guide has been updated on 2/23/2023 to more clearly distinguish changes for ProGCC v2. Please reach out to us at [support@handheldlegend.com]() if you have any questions or concerns.
:::

# Product Information

### What is ProGCC?

ProGCC is a conversion kit made in-house designed to take the ergonomics and form-factor of a Pro Controller and turn it into a highly reliable wired controller experience for competitive-level gameplay. This controller sports 5 separate trigger modes to ensure compatibility with a wide library of classic and modern games.

This project is source-available and the documentation/code is free for hobbyist use - [See the github here!](https://github.com/HandHeldLegend/ProCon-GCC-PIC18)

### Compatibility

This controller kit is tested with

*   GameCube

*   Wii

*   GameCube to USB adapter for Wii U/Nintendo Switch

*   Mayflash 4 port adapter

*   [Generic USB GameCube Adapter ](https://handheldlegend.com/products/gamecube-controller-adapter-for-nintendo-switch?_pos=3&_sid=d536a71cf&_ss=r)

Other adapters may work, though your results may vary.

### What is the USB port for?

This product uses a USB type C connector to connect to a GameCube controller port. *This product will not work with a typical USB port and the controller is not wireless.*

:::hint{type="info"}
If you would like to make your own customized USB-C cable, [see our resource guide here!](https://wiki.handheldlegend.com/gamecube-retro-c-cable-information)
:::

[We sell replacement cables on our store.](https://handheldlegend.com/products/switch-pro-controller-usb-c-to-gamecube-cable-progcc?_pos=6&_sid=bbfdc4957&_ss=r)

Alternative cables that are compatible:

[frame1 USB C to GameCube Cable](https://frame1.gg/collections/all/products/extra-usb-c-to-gamecube-wii-cable)

[b0xx USB C to GameCube Cable](https://b0xx.com/collections/all/products/usbc)

# Controls and Settings

Different modes and settings are accessed by holding down a specific button combination while plugging the controller into the console.&#x20;

## Stick Calibration

Stick calibration is identical between V1 and V2.

Unplug the controller. Hold Minus or Capture while plugging in to enable stick calibration mode.

In stick calibration mode, both sticks can be swirled around 5-6 times. Press + (plus) to save the configuration. Controller will connect immediately after saving.

## Software Snapback Adjustment (Left stick only on V2)

The software snapback has 15 levels of adjustment. When you increase the filter, the more that snapback is reduced. When you adjust this value to be very high, your stick may start to feel slow/sluggish. The default value is 0 (no software snapback reduction applied).

We recommend adjusting this one value at a time while using our HHL JoyPad test software to check the results.

With the controller *already plugged in...*

*   Hold Minus and ****single press**** ZL/ZR to decrease/increase snapback filter on X axis.

*   Hold Minus and ****single press**** L/R to decrease/increase snapback filter on Y axis.

## Software Deadzone Adjustment

:::hint{type="info"}
The instructions below are for V2 only. For V1, see the Button Combinations on how to adjust deadzone.
:::

Software deadzone is adjustable on the fly on V2 boards. There are 16 levels of adjustment, with the default level being 4. We recommend decreasing this as much as possible without the joystick becoming jittery.

Stick deadzone is the range in which the analog stick will not put out any values. This specific implementation is a *scaled deadzone*, meaning that you will not lose any analog range by applying deadzone.&#x20;

With the controller *already plugged in...*

*   Hold Minus and ****single press**** Dpad Up/Down to increase/decrease the deadzone by one.

## Button Combinations

While plugging in...

*   Hold ZL/L : Leftmost trigger mode

*   Hold ZR/R : Rightmost trigger mode

*   Hold L/R : Default trigger mode

*   Hold ZL/ZR : Full trigger mode

*   Hold - (minus) : Stick calibration mode

*   Hold + and - : Reset to defaults

*   Hold + (plus) : Enable/disable rumble **(OFF BY DEFAULT)**

*   Hold B : Enable Smash Ultimate mode

*   Hold Y : Enable/Disable Xbox button layout *(ABXY positions changed)*

*For v1 specifically:*

*   Hold D-Up : Increase stick deadzone

*   Hold D-Down : Decrease stick deadzone

## Rumble

Rumble is disabled by default. Hold + while plugging in the controller to enable/disable rumble. The setting is saved each time you toggle the option.

This kit supports LRA rumble motors. The LRA motors found in both Joy Con controllers and Pro Controllers are compatible with this kit. Simply solder the wires to the + and - terminals on each side of the stick board. Hold + or Home while plugging the controller in to enable/disable rumble.

## Trigger Modes

On the original GameCube controller, L and R have analog input, meaning you could do a half press or 'light' press. **The value of the light press is 128. This will not act as light shield in Melee. **

This kit implements different trigger modes to let you experience the entire library of GameCube titles without any compatibility issues.

*   Leftmost trigger mode: ZL is full L trigger press, L is light trigger press.

*   Rightmost trigger mode: ZR is full R trigger press, R is light trigger press.

*   Default trigger mode: ZL/ZR act as full trigger press, L/R are mapped as 'Z'

*   Full trigger mode: ZL/ZR act as full trigger press, L/R act as light analog press

## Smash Ultimate Mode

*   L is mapped to left dpad so it can be re-bound to something else in Smash Ultimate from R being mapped to Z

*   ZL/ZR are mapped as shield presses. It performs both the digital/analog press simultaneously

## Snapback Module

For controllers experiencing snapback *which is not resolved by adjusting software*, there is a snapback module built in to the PCB. These are enabled/disabled through soldering. Bridge the connections together for your desired snapback reduction.

