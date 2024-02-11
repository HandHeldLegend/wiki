---
title: AGB Amp (PAM8302A) | Install Guide
slug: 9On3-agb-amp-pam8302a-or-install-guide
description: Boost the volume of your console with the PAM8302A audio amplifier installation guide. Learn how to avoid overwhelming your system while soldering the amplifier wires and making connections to the main board. Test the installation before insulating the bo
createdAt: Tue Mar 29 2022 18:29:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Dec 07 2023 19:22:33 GMT+0000 (Coordinated Universal Time)
---

**Installing the PAM8302A audio amplifier into your console is a sure-fire way to boost the volume to a level that rivals today’s consoles… but it’s not without its challenges. Most notably is that the amplifier has a number of variables which contribute to how much current it draws, meaning it requires a certain knowledge level to put it into your console and know that you wont be overwhelming the console. To that end, we have some resources at the bottom of this article that you’ll find handy.**

### Before getting started...

It will be helpful for you to know the current draw of your current modifications in order to gauge if this amplifier mod will overwhelm your system. The current draw of the PAM8302A is dependent upon multiple factors, including supply voltage. See the datasheet, page 5, for details.

### Parts and materials

*   PAM8302A amplifier module

*   2-watt 23mm speaker

*   Hookup wire

*   Flux

*   Desoldering wick

*   3M VHB (thin) or other double-sided tape

*   Multimeter

### Mod Overview

Lets get acquainted with the PAM8302A… it has 7 solder points, and they’re all straight-forward with what they do… here’s a diagram:

![](../../assets/7T61btKgiOX5W4eMAASLv_jfg9cb4undhr7rpxj4za3rmbhzsugcang.jpg)

Placement on the board for the 8302A is a very convenient spot just above the volume dial on the Game Boy Advance. The following mockup shows the placement for the 8302A module:

![](../../assets/V7l0G9CZ_AnB21OWPAwYa_xokcf-9ocmigqlmmfuhmpm3oqs9-x0cxq.jpg)

The diagram below shows you which connections from the main board we'll be using for this install.

![](../../assets/Yk91WGMCDfc-GZdiND3xp_2i2njsjzo21qhrncwpisjbsllrlzrcmcjq.jpg)

What we’ve found helpful is to attach the amplifier wires first, leaving ‘just enough’ wire attached to each point that you can solder it to the board points shown above.

### Basic installation

1.  With the console still assembled, start it up to ensure everything is working - ensure the volume is all way up and that you hear the startup ‘chime’ when the console it tuned on. If everything is working well, then continue…

2.  Desolder the speaker from the main board
    1.  Use desoldering wick to desolder the two points where the speaker wires are connected to the main board. Desolder the wires from the stock speaker itself, too, as we won’t be needing the speaker by the time we’re done.

3.  As shown in the diagram here, just left of capacitor CP4, you’ll need to put a touch of solder to join just the tops of the two points - you won’t need much. This will be our positive (+) connection point.

4.  The top of capacitor CP4, the one just mentioned above, has it’s negative connection on the top - use your flux and add a touch of solder here as well… this will be for our ground (-) connection.

5.  Next up is the PAM8302A itself. Using the hookup wire you’ll want ‘just enough’ wire to where you can work with the PAM8302A board and the connections that will be made to points underneath it. Four inches should be enough to work with and not be excessive when the installation is done.

6.  Get power to the board
    1.  Solder the wire from VIN on the PAM8302A to the positive (+) point we prepped on the GBA logic board.

    2.  Solder the wire from GND on the PAM8302A to the top of capacitor CP4 as shown in the logic board diagram.

7.  Get audio to the board
    1.  On the left side of the PAM8302A board, wire A+ to the top connection of SP1 (the audio outputs).

    2.  Also on the left side of the PAM8302A board, wire A- to the bottom connection of SP1.

8.  Get audio from the PAM8302A to the 2-watt 23mm speaker
    1.  On the right side of the PAM8302A board, solder + (amplified audio out) to one of the speaker points.

    2.  Also on the right side, solder - (amplified audio out) to the other point on the speaker.

    3.  Note: Polarity for the speaker isn’t important for this installation - it will work either way. If the speaker you’re using has designated + and - then follow that, but otherwise just ensure that + and - are not wired to the same point.

9.  Test it!
    1.  Before we fully insulate the board and connections, lets test it to be sure things work. Put the console back together but without screwing it together in order to get batteries into the unit to test. Using the volume dial, turn up the audio to max. As soon as you turn on the console, you should hear a much louder startup chime now that the amplifier is hooked up, powered, and volume set to maximum.

10. Test successful? Insulate it
    1.  Reopen the console and insulate the bottom of the PAM8302A by covering the underside with the 3M VHB or double-sided tape.

### Troubleshooting

If you run into issues, double-check your solder joints for connectivity, powering down the console and going step-by-step to see where a connection perhaps has failed. Another common thing to check would be that the PAM8302A is getting power - set your multimeter to DC Voltage and test across the power pins on the amplifier to measure how much power the amplifier is getting… that voltage needs to be between 2.5V and 5.5V in order for amplifier to operate.

For further asssitance, please reach out to support\@handheldlegend.com
