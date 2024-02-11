---
title: AGB CleanAmp Pro | Install Guide
slug: 0oiP-agb-cleanamp-pro-or-install-guide
description: Learn how to improve the sound quality of your Game Boy Advance with this step-by-step installation guide for the CleanAmp. Test the console's sound before starting, then follow instructions on opening the console, removing the circuit board, and disconne
createdAt: Tue Mar 29 2022 18:22:25 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

The following was written by the team at [RetroSix:](https://retrosix.co.uk/)

To begin with it's always best to test your original consoles sound works. It isn't always required, as you have have a dead speaker, but if your console works first its a good sign. 

Open up the Game Boy Advance using a tripoint screwdriver by removing the 6 screws on the back, and 1 more philips screw in the battery compartment.

Once inside, it is easier to also remove the main circuit board from the shell by removing the 3 JIS screws from the centerline of the motherboard (one to the left side, 2 to the right side above power slider switch. Before lifting out the console, push the tabs on either side of the ribbon connector at the top towards the top of the shell. This releases the pressure on the ribbon cable and you can pull out the cable, leaving the screen stuck down in the front shell. Now remove the circuit board from the shell.

Remove the old speaker from the front PCB by cutting or desoldering the speaker wires.

Solder the pads on the Game Boy Advance to the pads on the CleanAmp as shown.

Be careful when soldering the CleanAmp pads that you do not short the pads together or remove the resistors or capacitors near the pads.

Solder the two wires on the top right of the CleanAmp to the speaker wires. Polarity doesn't matter, you can solder either wire to either side.

![Install reference](../../assets/AyzapxtCqrkPLW0IIMorc_image.png)

## Troubleshooting

The bottom left pad is ground, going to pin 4 of the headphone connector.

The top right pad is the audio input. This is the unamplified, volume controlled sound from the console. This is connected to the top original speaker wire pad.

The top left pad that is power in from the Game Boy Advance. Connect this to S1 of the cartridge pins to the top left. This should be around 3 volts.

The middle left pad is the headphone pin that should be grounded when no headphones are present and floating when headphones are inserted. It is connected to pin 5 of the headphone connector. If you have no audio the first check is to solder a wire from this pad to the same pad as ground wire (pin 4 of headphone connector). If that makes the audio work, but when its connected to the correct location it doesn't, you have a damaged headphone jack. You can leave the wire where the ground wire is soldered, but your speaker won't turn off if you insert headphones.

The middle circle pad is the PureSilence pad connected to the "vol" via. When the volume wheel is turned down, it completely cuts off all noise to the speaker and headphones giving you total silence. If you have issues with sound you can remove this solder pad to diagnose issues. Removing it will remove the PureSilence function.

NOTE: The dehum kit is **strongly** recommended to remove the audio noise from the board.

