---
title: GBA SP CleanAmp | Install Guide
slug: luc9-gba-sp-cleanamp-or-install-guide
description: Improve sound quality on your Game Boy Advance console by installing a CleanAmp. This document provides step-by-step instructions, including opening the console, replacing the old speaker, and securing the CleanAmp with double-sided tape. Learn how to sol
createdAt: Tue Mar 29 2022 19:07:58 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

The following was written by the team at [RetroSix:](https://retrosix.co.uk/)

To begin with it's always best to test your original consoles sound works. It isn't always required, as you have have a dead speaker, but if your console works first its a good sign. 

Open up the Game Boy Advance using a tripoint and a JIS screwdriver where needed. Unscrew the screw from the battery cover and remove the cover and battery. Remove the 6 visible screws from around the console perimeter and lift off the back cover. Finally remove the 3 screws from the the motherboard (one in center, and two below the cartridge connector) and lift up the motherboard gently from the bottom side tilting up as the screen is still attached.

Before lifting out the console, push the tabs on either side of the ribbon connector at the top towards the top of the shell. This releases the pressure on the ribbon cable and you can pull out the cable, leaving the screen in the front shell. Now remove the circuit board from the shell.

Remove the old speaker from the front shell by lifting it out.

Use double sided tape (optional) to secure the CleanAmp onto the main circuit board as shown. Position is important to make sure the speaker and shell do not hit the CleanAmp preventing the shell closing.

Trim the shell here to prevent the shell from hitting the CleanAmp.

![](../../assets/K1iX11ax7bLHm88YdFyIG_an49dlipxqjmdqb6lbxmm6cavdgdhcwia.jpg)

Use cutters or a knife blade to trim/peel off the plastic rim from around the speaker lip. This reduces the speaker depth so it does not press on the shell when closed.

Take some Kynar/wrapping wire (30awg or 28awg gauge wire - the thin stuff), cut it to length and solder the wires from the points on the Game Boy Advance SP to the pads on the CleanAmp as shown.

Be careful when soldering the CleanAmp pads that you do not short the pads together or remove the resistors or capacitors near the pads.

Solder the two wires on the top left of the CleanAmp to the outer 2 pads of the speaker. Polarity doesn't matter, you can solder either wire to either side.

![](../../assets/KZcNPDRor14QS706snRg1_shujl7gwxmuynwruamo2cb45iinddohaeg.jpg)

![](../../assets/nUZ4mCg_2_2nZrVgUJz3r_xbxyq2-r9bgo-4fcqwcztkhgqntvswhuhg.jpg)

### Increase Amp Volume

If you want the audio even louder you can join these two pads together. If you don't like it, just remove the solder joins to restore it to normal.

![](../../assets/oW0uqTqBlsdhhymyZ1qvk_image.png)

### Troubleshooting

The top left 2 pins are the speaker. The pin to the right of that (top middle) is the PureSilence pin. It connects to the volume wheel and when its low removes all audio from the speaker for pure silence. If you have issues to narrow down you could remove the wire.

The next wire (second from top right) is the headphone pin that should be grounded when no headphones are present and floating when headphones are inserted. If you have no audio the first check is to solder the headphone pin wire to the same pad as ground wire (shield pin of extension connector) or bridge the two pins together. If that makes the audio work, but when its connected to the correct location it doesn't, you have a damaged headphone jack. You can leave the wire where the ground wire is soldered, but your speaker won't turn off if you insert headphones.

The top right wire is ground, going to the right shield pin of the extension connector.

The bottom right wire above the large capacitor is is power in from the console.

### Alternative Board

If you have a motherboard that looks different, you need to solder the wires slightly different like shown here. Notice the extra wire needed to be soldered to the bottom of the small transistor on the CleanAmp. There is also a bridge between the top 2 right pins to each other.

![](../../assets/6myO2iGOGQntnuDu8FWoH_xi4c1jntwv4xylzg4menj63daqnolg2w.jpg)

![](../../assets/9vrt7x5jrNzlvPha4k-Y3_mkb4teliinvchdjddswowox1g2wdabnqiw.jpg)

