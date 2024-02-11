---
title: AGB CleanAmp v1.2 | Install Guide
slug: AJuP-agb-cleanamp-v12-or-install-guide
description: Upgrade the sound system of your Game Boy Advance console with ease using the CleanAmp device. This comprehensive document offers step-by-step instructions for disassembling your console, removing the old speaker, and seamlessly connecting the CleanAmp to
createdAt: Tue Mar 29 2022 18:34:52 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

The following was written by the team at [RetroSix:](https://retrosix.co.uk/)

To begin with it's always best to test your original consoles sound works. It isn't always required, as you have have a dead speaker, but if your console works first its a good sign. 

Open up the Game Boy Advance using a tripoint screwdriver by removing the 6 screws on the back, and 1 more philips screw in the battery compartment.

Once inside, it is easier to also remove the main circuit board from the shell by removing the 3 JIS screws from the centerline of the motherboard (one to the left side, 2 to the right side above power slider switch. Before lifting out the console, push the tabs on either side of the ribbon connector at the top towards the top of the shell. This releases the pressure on the ribbon cable and you can pull out the cable, leaving the screen stuck down in the front shell. Now remove the circuit board from the shell.

Remove the old speaker from the front PCB by cutting or desoldering the speaker wires.

Use double sided tape (optional) to secure the CleanAmp onto the main circuit board as shown. Position is important to make sure the speaker and shell do not hit the CleanAmp preventing the shell closing

Take some Kynar/wrapping wire (30awg or 28awg gauge wire - the thin stuff), cut it to length and solder the wires from the points on the Game Boy Advance to the pads on the CleanAmp as shown.

Be careful when soldering the CleanAmp pads that you do not short the pads together or remove the resistors or capacitors near the pads.

Solder the two wires on the top left of the CleanAmp to the speaker wires. Polarity doesn't matter, you can solder either wire to either side.


![](../../assets/C4vWtw8i63igalaeE3tAs_plnwxndvid1bippishmvnnled988shyea.jpg)

### Increase Amplification

If you want the audio even louder you can join these two pads together. If you don't like it, just remove the solder joins to restore it to normal.

![](../../assets/mVl4n6Y-tUeXLFFFmJ2HO_image.png)

## Troubleshooting

The top right wire is ground, going to pin 4 of the headphone connector.

The middle right wire below that is the audio input. This is the unamplified, volume controlled sound from the console. This is connected to the top original speaker wire pad.

The bottom right wire below that is power in from the Game Boy Advance. Connect this to S1 of the cartridge pins to the top left. This should be around 3 volts.

The second wire on the top right is the headphone pin that should be grounded when no headphones are present and floating when headphones are inserted. It is connected to pin 5 of the headphone connector. If you have no audio the first check is to solder the wire to the same pad as ground wire (pin 4 of headphone connector). If that makes the audio work, but when its connected to the correct location it doesn't, you have a damaged headphone jack. You can leave the wire where the ground wire is soldered, but your speaker won't turn off if you insert headphones.

The top middle wire to the right of the speaker wires is the PureSilence wire connected to the "vol" via. When the volume wheel is turned down, it completely cuts off all noise to the speaker and headphones giving you total silence. If you have issues with sound you can remove this wire to diagnose issues. Removing it will remove the PureSilence function.

**NOTE**: The dehum/dehiss kit is strongly recommended to remove the audio noise from the board.

![](../../assets/eJnySEASA86clzpouYQDa_-d52c4o-5fnefnzj6dz0acy95jxw4humya.jpg)
