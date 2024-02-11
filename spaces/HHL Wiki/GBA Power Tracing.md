---
title: GBA Power Tracing
slug: EHlK-gba-power-tracing
createdAt: Wed Jan 31 2024 19:58:47 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Jan 31 2024 20:03:37 GMT+0000 (Coordinated Universal Time)
---

*Article/original post by *[*retroreconstruct *](https://www.instagram.com/retroreconstruct?igsh=MXYya2d3ZHE0OTd5Yg%3D%3D)*on Instagram.*

Do you really know the GBA?

Let’s take a look at your board. Below is a list that will hopefully point you in the right direction. Just like the GBC guild, this isn’t an exhaustive guide as it’s limited by characters on IG but it will cover the most common issue. It also assumes you have a multimeter, a “tri-wing” screwdriver, and can open the Game Boy Advance.

*Batteries*
We know it’s obvious but are the batteries good? If so, check the battery contacts for any corrosion. When cleaning corrosion you want to brush White Distilled Vinegar on the affected area then clean off with Isopropyl Alcohol (IPA) preferably 97-99% pure. 70% from the drugstore has too much water in it and may short something when you add the batteries.

*Power Switch*
Using a multimeter, set it to continuity mode (icon with the waves), remove the batteries, and put the switch in the OFF position. Touch a probe to Pin 1 & Pin C. “Beep”?, you got a connection. Repeat in the ON position, probing Pin 2 & Pin C. If no beeps, then load a cotton swab with IPA dripping it into the switch opening by the nub. Moving the switch back and forth will scratch up the internal plates. Recheck the pins. Beep? You should fully clean the switch more. If not, you need to replace the switch. We recommend watching a video on both as it's something better seen than described.

*Fuse*
Check F1 with the multimeter and get a beep. If it’s blown you’ll need to replace it but it likely blew for a reason so check your board fully for shorts.

*Common/3v/VCC*
Enters through the BT+ terminal and goes to L1, CP1, R33, U4, T1, Audio(R37, U6\[AMP]), & Low Battery (R10, R18, R26)

*T1 & U4*
These do most of the heavy lifting by prepping the high-voltage lines and are located on the back right at the top and bottom of the board

Pushing the character limit so remember these test points: VCC is 3v from the switch and VDD is 3v used by the system, VDD5 is the 5v plain, VDD13 & VDD-15 go to the screen.&#x20;

![](../../assets/ZBBS--O-4nC7IbYHeADae_img1942.PNG)

![](../../assets/fw_tY5tS1OCi4VlAlukYr_img1943.PNG)

![](../../assets/Cu949UhwxCzy_GPmojHM4_img1944.PNG)

![](../../assets/wfgSVz4-DZVp-4YuzH4u5_img1945.PNG)

![](../../assets/zUMW65nMBHci_Dyx-XcSK_img1946.PNG)

![](../../assets/BjSsWMh8eU0xCgQu7Ut7T_img1947.PNG)

