---
title: ProGCC 47uF Capacitor Install Guide
slug: nqpA-progcc-47uf-capacitor-install-guide
description: Learn how to fix intermittent disconnects on ProGCC boards caused by voltage dipping with this helpful document. Discover the recommended solution of installing a bulk capacitor, rated at 6v with a capacitance value of 47uF. Find out why ceramic capacitor
createdAt: Mon Feb 06 2023 21:33:08 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

## Issue Description

For some ProGCC boards, there are intermittent disconnects associated with voltage dipping on the 3.3v line. This causes the microcontroller to brown-out or reset.&#x20;

:::hint{type="info"}
Please stay tuned for an email from us if you have purchased a ProGCC detailing how to receive a free capacitor. If you are impacted by this issue and do not receive an email by March 1st, please contact our support team.&#x20;
:::

## Solution Description

Install a bulk capacitor (Electrolytic or Tantalum) **rated for 6v** or so with a capacitance value of **47uF.**

**Ceramic capacitors will not work for this solution.**

:::hint{type="danger"}
**Installing Electrolytic or Tantalum capacitors backwards can result in serious injury or burns. Please take proper precautions to ensure you install the capacitors correctly if you are doing this yourself!**
:::

:::hint{type="warning"}
**Make sure not to flow too much solder onto the pads, excess solder will flow to the pad on the bottom side of the board and has the potential to cause a short to ground. **
:::



## Valid Parts

### Harvest from OEM GameCube board

You can use this capacitor found on an original GameCube controller. Mind the fit as it may require some trimming of the plastic in the controller.

![](../../assets/2X3uKZixGsvTt1iuXAWZc_image.png)

### Component Detail

The capacitor needs to be *tantalum *or *electrolytic*.

*   6.0v to 6.3v rating (not higher, not lower)

*   47uF capacitance rating

*   *2513 *case code (mm) or *1206 *case code (inches)

Here's a list of locations to order the component by country.

### USA

*   [Mouser](https://www.mouser.com/ProductDetail/80-T491A476K006AT)

*   [DigiKey](https://www.digikey.com/en/products/detail/kemet/T491A476K006AT/8614980?s=N4IgTCBcDaICoBYCcBGAggg7ANgNIAZ9s04QBdAXyA)

### Japan

*   [Mouser](https://www.mouser.jp/ProductDetail/KEMET/T491A476K006AT?qs=u%2FajwFXIEhZdcMxuEj9OyA%3D%3D)

### UK

*   [Mouser](https://www.mouser.co.uk/ProductDetail/KEMET/T491A476K006AT?qs=u%2FajwFXIEhZdcMxuEj9OyA%3D%3D)

### Canada

*   [Mouser](https://www.mouser.ca/ProductDetail/KEMET/T491A476K006AT?qs=u%2FajwFXIEhZdcMxuEj9OyA%3D%3D)



## Installation Diagram

We recommend installing this capacitor on the right side of the PCB as shown below.

![](../../assets/AVvgp-xVs1RLqiNWG_gxX_image.png)

## Video Demonstration

<https://www.youtube.com/watch?v=5d46BDS8mCE>

