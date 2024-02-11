---
title: RetroGlow for GBC | Install Guide

slug: MVFF-retroglow-for-gbc-or-install-guide
description: Installation tutorial for the Game Boy Color (GBC) RetroGlow LED Flex Board/Cable to light up your game boy's buttons!
createdAt: Thu Jan 20 2022 19:16:47 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

:::hint{type="warning"}
It has been brought to our attention that the controls for this kit may conflict with some IPS kits on the market. We recommend soldering to an alternate button for the 'Select' button on IPS kits such as 'Start' or 'Dpad Down' since the IPS kits typically require pressing both buttons simultaneously.

*Noted July 26th, 2022 by Mitch*
:::

## Video Guide

<https://www.youtube.com/watch?v=r8DN1CGnsyI>

## Gathering Tools and Supplies

:::hint{type="info"}
Hand Held Legend earns commissions for Amazon purchases made through links in this post.
:::

### Required&#x20;

1.  [J0 and Y1 screwdriver bits](https://handheldlegend.com/products/screwdriver-kit-for-nintendo-consoles-xbox-sega?_pos=2&_sid=021a47cd1&_ss=r)

2.  [Solder](https://amzn.to/32nTOfo) (Leaded is recommended)

3.  [Soldering iron](https://amzn.to/3nLARef)

4.  [Kapton tape](https://amzn.to/3tQ1UJ0)

5.  Fully charged or new [AA batteries](https://www.amazon.com/dp/B00JHKSMJU?tag=hanhelleg-20)

### Recommended

1.  [Solder flux (paste or gel)](https://www.amazon.com/dp/B09NXBZBFT?tag=hanhelleg-20)

2.  [Isopropyl Alcohol](https://www.amazon.com/dp/B08JZJ5QV2?tag=hanhelleg-20) (70% or higher) for cleaning flux residue - [Dispensing Pump](https://amzn.to/3qRRHd9)

3.  [Plastic spudger](https://handheldlegend.com/products/screwdriver-kit-for-nintendo-consoles-xbox-sega?_pos=2&_sid=021a47cd1&_ss=r)

4.  [Tweezers](https://amzn.to/3fMmp1f)

5.  [Cotton Swabs](https://www.amazon.com/dp/B09498GV6R?tag=hanhelleg-20)

6.  [Solder braid/wick](https://handheldlegend.com/products/solder-wick-2-0mm-1-5m?_pos=1&_sid=b883b203f&_ss=r)

7.  [Solder sucker](https://amzn.to/3GXiPx1)

8.  [Transparent Game Boy Color Buttons](https://handheldlegend.com/collections/game-boy-color-gbc/products/game-boy-color-prestige-buttons-retrosix?variant=39542373122182)

9.  [Transparent Game Boy Color Membranes](https://handheldlegend.com/collections/game-boy-color-gbc/products/game-boy-color-silicone-button-pads?variant=39576237179014)

## Installation Guide

### Fully disassemble your Gameboy Color

[*See this guide on iFixit*](https://www.ifixit.com/Teardown/Game+Boy+Color+Teardown/73017) for full details.

### Remove the power LED

Heat the two legs from the rear side of the board with a soldering iron. Lifting the board up at an angle while heating the LED should result in the LED dropping out. Use solder wick or a solder sucker to help if needed.

![LED rear side location](../../assets/3hObpKNJBGh75186JhdsW_led-removal.png)

![LED fully removed](../../assets/weBkxzYuEHb_AvQPxUmoN_led-removed.png)

### Solder the 5V connection

Align the PCB to the best of your ability. The goal is to ensure all of the gold holes are lined up with the test pads on the main board. Use Kapton tape to hold alignment during soldering. Soldering the 5V connection point will act as an anchor and allow you to fine-tune your PCB positioning by reheating that one area. Use generous flux as needed to get a great connection.&#x20;

*Recommended soldering iron temperature: 365c*

![5V connection point](../../assets/qY4_eH7XJABlFBAbeeCIY_solder-5v-connection.png)

### Solder button vias

You will solder each of the points circled in red. Be sure to check your alignment and take your time before soldering. Kapton tape can help to hold the board in place before soldering.

![All remaining connection points circled](../../assets/JeVHMO5NyPjkXbMACa_yV_solder-remainder.png)



### Optional - Solder IPS control wires

Use the pads along the top portion of the flex pcb (labelled for your convenience) to wire up the controls for your [IPS GBC IPS display](https://handheldlegend.com/collections/game-boy-color-gbc/Displays). This kit will not interfere with those controls and will provide a very clean end result without any wires showing. Use flux as needed. **Be sure to cover all exposed solder connections in this area with Kapton tape. Cover both the IPS control connection points and the cartridge pins for the best protection against short circuits/damage. Trimming the cart cart pins is always recommended to prevent damage to IPS kits. **

![Wires connected to the flex PCB](../../assets/aA9nSE076V2_iU0ZAtNbc_ips-wires-installed.png)

### Test before reassembly

Place the main board into the rear shell. Insert the AA batteries and power on the console. Upon first power up, you should see all LEDs light up with Red, Orange, Yellow, Green, Blue, and Purple from right to left. If you see any issues here, see the troubleshooting at the bottom of this guide.

![LEDs lit up from right to left: ROYGBP](../../assets/TjETY51OXcuIZ6iKVsflX_power-test.png)

:::hint{type="info"}
If your console is particularly noisy, consider replacing capacitor C32 with a larger rating tantalum capacitor. We recommend a 680uF 10v cap based on information from our friends at Console5. At the time of writing this note they are out of stock but you can find the part through Mouser: [Mouser Link](https://www.mouser.com/ProductDetail/Kyocera-AVX/TPSE687M010R0150V?qs=AQlKX63v8RtLz%2Fuark6Orw%3D%3D)
:::

### Final reassembly and second test

At this point, follow the disassembly in reverse to ensure your Game Boy Color is put back together properly. If installing an IPS, refer to the product guide for your kit of choice to ensure it is installed correctly. Install your choice of transparent buttons and membranes.

Power on your Game Boy Color and ensure all LEDs are illuminating properly. Button functionality may vary depending on where you have sourced your buttons and/or membranes. If you are using an aftermarket Game Boy Color housing, you may need to slightly loosen the J0 screws behind the main board to relieve some button pressure.

Quick functionality test: **Hold Select and press Right on the D-Pad. **You should see the lights flash **Green** twice. At this point, you can press D-Pad left or right to lower or increase the LED brightness. If you do not get this result, see the troubleshooting guide at the bottom of this article.

![Fully assembed kit](../../assets/FT3RYfGyNUl_Lh2bwYsht_reassembly-control-test.png)



### LED Customization

[For the full user guide to customize your LED setup, click here!](https://wiki.handheldlegend.com/retroglow-for-gbc-or-user-guide)

## Installation problems and solutions

| Problem                                                                                                   | Solution                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LEDs are flickering                                                                                       | Double check all solder points. Use flux and go over each of the connection points once more.                                                                                                                                                                                                                                              |
| Some or none of the LEDs are not illuminating                                                             | Reach out to us at [support@handheldlegend.com]() along with a photo of your issue.                                                                                                                                                                                                                                                        |
| All LEDs are illuminating, but the controls will not work (Can't get the double green flash when testing) | Clean your button membranes using a q tip. Ensure that all button contacts (gold pads) are clear of flux residue. Scrubbing with IPA is highly recommended to ensure you have a clean and conductive surface. Use a standard #2 pencil to rub some graphite on to the button membranes to increase conductivity and button responsiveness. |
| Select Button / Strange LED behavior                                                                      | If you have soldered a wire from an IPS kit Select Point to the RetroGlow Select Point, please solder the wire to a different point on the RetroGlow such as Start.                                                                                                                                                                        |

