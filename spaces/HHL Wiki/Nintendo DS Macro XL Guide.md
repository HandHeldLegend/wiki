---
title: Nintendo DS Macro XL Guide
slug: y11v-nintendo-ds-macro-xl-guide
description: Learn how to transform your DS Lite console into a Macro XL console with this comprehensive guide. Follow the step-by-step instructions to remove the back shell, disconnect cables, solder new components, and trim the shell. Additionally, discover how to r
createdAt: Mon Jul 31 2023 12:04:56 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

# Video

<https://www.youtube.com/watch?v=ejKU-x3AnLE>

# Guide

:::hint{type="info"}
Required Tools and Parts:&#x20;

Triwing Screw Driver

J1 Screw Driver

330ohm 0603 Resistor&#x20;


:::



Converting the DS Lite to a Macro XL console is a relatively simple process, let's jump right into the process. Start by removing the seven triwing screws from the back of the console that holds the shell on.&#x20;

![](../../assets/lS1mLhM3rfF1tEmwETcHn_screws.jpg)

Once those are removed, the back shell can be lifted off of the console, revealing two ribbon cables and an antenna cable.

![](../../assets/MbCq6uW7yIYa_hGDEB8Hv_motherboard.jpg)

We can start by removing the antenna cable, just pull up. From there we can unclip the right ribbon cable, this will reveal two smaller ribbon cables for the touchscreen and screen. We can unlatch those and remove them as well.&#x20;

![](https://i.imgur.com/4yMBOWk.jpeg)

Now the top ribbon cable can be removed, this is for the top screen and will no longer be needed.&#x20;

![](https://i.imgur.com/jVSQMqE.jpeg)

Now there are four silver J1 screws securing the motherboard into the shell, we can remove them.

![](https://i.imgur.com/UvsWEj4.jpeg)

From here the motherboard can be removed from the console, it should lift away and leave the touchscreen and screen in place. Now we can start to disassemble the rest of the console. Starting with the four screws holding the top screen in place.

![](../../assets/CO0H_Awvoj_E66TIHXWvL_top-screen.jpg)

Now we can pry the top screen off, revealing the two PCBs holding the speakers in. We can remove the two screws and pull the two PCBs out of the console, the antenna wire should just feed through the shell.&#x20;

![](../../assets/toJUARLt0VUniiELshK_z_top-screen-mbs.jpg)

Once the two PCBs are removed, you can remove the speakers and top screen. This will now allow us to remove the one hinge from the console, all we have to do is push inwards with a pair of tweezers or a screw driver.&#x20;

![](https://i.imgur.com/STrqu31.jpeg)

You will get it partially out, you then need to open the screen and push it the rest of the way out.&#x20;

![](https://i.imgur.com/6FmkUJ0.jpeg)

We then need to remove the one screw that is holding the hinge cover in to remove the other hinge.&#x20;

![](https://i.imgur.com/atXVAzy.jpeg)

The hinge cover should just pull right off, allowing the other hinge to be removed just like the first.&#x20;

![](https://i.imgur.com/9xGubaj.jpeg)

From here the top screen should fall away from the console, we are now prepared to start modifying the motherboard of the console. We need to solder a speaker to the motherboard as well as a 330ohm resistor to trick the console into thinking the top screen is attached.&#x20;

![](../../assets/mnSZ6x5R59YE2Gol47Cbs_solder-points.jpg)

We recommend keeping the speaker wires long as you will need to feed it through to the back of the console, start by soldering the wires to the speaker.&#x20;

![](https://i.imgur.com/pNVUQyj.jpeg)

Position the speaker in this location and run the wires through the slot in the motherboard for the touchscreens ribbon cables.&#x20;

![](https://i.imgur.com/MJcXMwW.jpeg)

Now solder the wires to U1-GND and SPLO, this will give you a functioning speaker for your build.&#x20;

![](https://i.imgur.com/Z60W5vD.jpeg)

Now we need to solder the 330ohm resistor to the motherboard to trick the console into thinking theres a top screen attached. The resistor will connect LEDC2 and LEDA2, an 0603 resistor is the perfect size to bridge the gap.&#x20;

![](https://i.imgur.com/5uKJHG9.jpeg)

From here we can go ahead and trim the plastic on the back half of the shell for the speaker to fit. All the red highlighted plastic needs to be trimmed down flat with flush cutters.&#x20;

![](https://i.imgur.com/hPBwjTa.jpeg)

Finally you can remove the ribbon cable for the top screen by either cutting it off or removing it from the glue tab holding it to the screen.&#x20;

![](https://i.imgur.com/0CfBKUK.jpeg)

Once that is done you can go ahead and reassemble your console minus the top screen, the console should boot and allow you to play any Gameboy Advance games!&#x20;
