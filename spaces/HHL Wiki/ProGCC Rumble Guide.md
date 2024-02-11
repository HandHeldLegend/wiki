---
title: ProGCC Rumble Guide
slug: mHdw-progcc-rumble-guide
description: Learn how to install rumble motors in gaming controllers with this comprehensive video and installation guide. Discover the various types of motors used, such as ERM and LRA, and follow step-by-step instructions for installation. From removing the backing
createdAt: Fri Mar 03 2023 15:39:02 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

# Video Guide

<https://youtu.be/DYedmJaQsrQ>

# Install Guide

## Motor Types

### ERM&#x20;

&#x20;Eccentric Rotating Mass motors are a type of motor that has an offset weight at the end of a spinning rod. They are the type of motors that were used in older controllers like the Xbox 360 and the Playstation 3.&#x20;

![](https://guide-images.cdn.ifixit.com/igi/qaiKdyJ3vSKCYkTc.medium)

We use coin style motors, while they look different they still spin in the same way as other ERM style motors.

![](https://www.ineedmotors.com/Content/uploads/2021349995/20210811152711084b275195554a28aa06e62a84e941de.jpg)

### LRA&#x20;

&#x20;Linear Resonant Actuators are motors that move back and forth on one direction in order to generate the rumble feel. LRA type motors are sometimes used in phones, and other small devices.&#x20;

![](https://cdn.shopify.com/s/files/1/0689/3143/products/RumbleMotorsTransparent.jpg?v=1658257602)

### Motor Styles

It's also important to mention that the motors will not always look the same, for example both ERM and LRA style motors can be made in coin styles. They can both be made into bar shaped versions as well. We use ERM coin style motors in our builds as they fit in our shells with next to no modifications.&#x20;

## ERM Motor Install

First we remove the backing from our rumble motors and use the adhesive on the back to hold them in place.&#x20;

![](../../assets/iGznMSMzMDajUCFyjdoiJ_1-place-motor.jpg)

Next we will solder the rumble motors to the positive and negative pads on the motherboard. The polarity does not matter.

![](../../assets/P0yCXTj8dZCuv2LXR3f2R_motor-points.jpg)

![](../../assets/T4i98H3CoROUpTPwfLgrh_2-solder-pos-an-neg.jpg)

We will need to bridge the ERM pad on the motherboard next.

![](../../assets/Q91LWF92i7akuQwba3Fx7_4-bridge-erm.jpg)

We strongly recommend removing resistor 20 and bridging the connection to allow more power to the ERM motors, allowing them to function better.&#x20;

![](https://i.imgur.com/E0p5M37.jpeg)

We also put optional silicone around the motor to make sure it doesn't rumble off of the adhesive it comes with. We also add 10mm silicone cabinet bumper pads above the motors to increase the surface area the motor has with the shell.

![](https://i.imgur.com/fczUDEC.jpeg)

You can now reassemble your controller, and hold plus (+) while plugging the controller in to enable your rumble motors.

![](https://i.imgur.com/V4TKYNo.jpeg)

## LRA Motor Install

The first thing to do is to swap the wires on the LRA motor as you will need longer wires to reach the pads on the motherboard.&#x20;

![](../../assets/7iuXQmxhaCQTIY5NrHhBZ_solder-new-wires-to-motor.jpg)

Once you finish soldering new wires on, we recommend taking some kapton tape and covering your soldering to prevent shorting.&#x20;

![](../../assets/t--6qialIIGn0xmq-bz1T_kapton.jpg)

If you are using one of the shells that we sell on our store then you will need to trim the shell in order to get the LRA motors that we sell to fit. Trim away the plastic highlighted in red, we use flush cutter and xacto knives. Just take your time and be sure not to hurt yourself.&#x20;

![](../../assets/iwRusxqGkpTMXu2XpP4X3_trim-plastic.png)

![](../../assets/k2yFTFGqV90DWPrq2smuF_trimming.jpg)

Next we will use some double sided tape or anything similar to hold them into the shell. They simply fit into the rectangular area of the shell that we trimmed out.&#x20;

![](../../assets/GFTwgLyfLSS-UX9Vwmbnp_lra-motor-in-shell.jpg)

Next we will solder the motors to the pads on the motherboard located right here

![](../../assets/F2O7Lgu4E6LMfUPKMolXU_motor-points.jpg)

Once you finish soldering your motors you can close up your controller and hold plus (+) while plugging your controller in to enable the rumble motors!&#x20;

![](https://i.imgur.com/V4TKYNo.jpeg)

