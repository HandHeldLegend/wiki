---
title: GCC Snapback Flex PCB | Install Guide
slug: jucg-gcc-snapback-flex-pcb-or-install-guide
description: Looking to reduce snapback on your Gamecube controller? Hand Held Legend's installation guide for their Gamecube Controller Snapback reduction flex pcb has got you covered. This step-by-step guide provides easy instructions for installing the flex pcb wit
createdAt: Thu Mar 31 2022 22:43:14 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This is our install guide for our [Gamecube Controller Snapback reduction flex pcb.](https://handheldlegend.com/products/no-reset-snapback-mod-for-the-gamecube-controller-hand-held-legend?_pos=1&_sid=08a55e3c9&_ss=r) This is the easiest way to reduce snapback on your original Gamecube controller. No trimming or wires are required!

![A brand-new snapback flex pcb](../../assets/L8jdkmYiNYm1wb2N72Vof_dsc03760.JPG)

## Video

<https://www.youtube.com/watch?v=ub7Q0-cH-bc&t=5s>

## Getting Started

### Required Tools

*   Soldering iron and supplies ([See our soldering guide for complete list](https://wiki.handheldlegend.com/soldering-iron-guide))

*   Y1 Tri-point screwdriver

### Disassembly

Disassemble your controller to the point where the rumble bracket is removed. Further disassembly is not required. [See our full controller disassembly guide linked here.](https://wiki.handheldlegend.com/gamecube-controller-disassembly)

## Install Guide

### Line up the board

Optionally apply double sided adhesive to the PCB where the flex cable will reside. Carefully line up the flex PCB with the rear connections for the main joystick and press it into place.

### Solder the connections

Apply solder to each of the 4 gold contact points. Ensure that the joints are not bridged. If you add too much solder, you can remove solder with solder braid and some solder flux. [See our soldering guide for more details.](https://wiki.handheldlegend.com/soldering-iron-guide)

![Soldered flex pcb](../../assets/WSpR0zkoLXyGdDtWUvAEU_dsc03761.JPG)

## Configuring the module

You may see a yellow film covering the 8-pole dip switch. This peels off without any issues. Use a plastic tool or a toothpick to adjust the switch positions.&#x20;

![Bye-bye](../../assets/hTWMP2ywMwDxErXcSAYtz_image.png)



There are 4 values per axes, ranging from **150, 220, 330 and 680 nanofarads**.&#x20;

We recommend starting with a base value of 150 for older controllers. If you have one of the newer Smash Ultimate controllers, you might try 220 or 330. On our module, this would mean **enabling switches 1 and 5 for 150 nanofarads.**

### Switch value chart

| Stick Axis | Switch Number | Value          |
| ---------- | ------------- | -------------- |
| X          | 1             | 150 nanofarads |
| X          | 2             | 220 nanofarads |
| X          | 3             | 330 nanofarads |
| X          | 4             | 680 nanofarads |
| Y          | 5             | 150 nanofarads |
| Y          | 6             | 220 nanofarads |
| Y          | 7             | 330 nanofarads |
| Y          | 8             | 680 nanofarads |

![](../../assets/oos1Ih8iSRmrU2-kpBlzR_dsc03762.JPG)

As you play with and wear down your controller sticks, you may find the need to adjust the capacitance required to maintain the same level of snapback reduction. If you are experiencing stick drift or other issues, it might be time to replace the stick potentiometers altogether. Stay tuned for a guide on that process!

### Test and adjust

Install the rumble bracket and rear shell. Do not install the screws at this time. Take this opportunity to plug in your controller and test. Games like Super Smash Bros Melee are often used to test snapback. This can be done in the main menu or on the character select screen. At the main menu where you can select the game mode, try flicking the stick up or down. If the menu option moves up, then down when you flick the stick up, you still have snapback. At this point, as an example, you may try enabling the switch for 220 nanofarads and disabling the 150 nanofarads. Of course, these values can be combined in any manner to allow for some fine tuning.

## Reassemble

Once you are fully satisfied with the feel of the stick, install the 6 rear Y1 screws and you're finished!

