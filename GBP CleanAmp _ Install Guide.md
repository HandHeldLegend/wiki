---
title: GBP CleanAmp | Install Guide
slug: FbwX-gbp-cleanamp-or-install-guide
description: Learn how to increase the volume of your Game Boy Pocket console with step-by-step instructions. Test the sound, replace the old speaker with a CleanAmp, and solder wires for optimal performance. Troubleshooting tips included!
createdAt: Fri May 20 2022 19:24:29 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

The following was written by the team at [RetroSix:](https://retrosix.co.uk/)

To begin with it's always best to test your original consoles sound works. It isn't always required, as you have have a dead speaker, but if your console works first its a good sign.&#x20;

Open up the Game Boy Pocket using a Tri-wing screwdriver by removing the 6 screws on the back (2 inside the battery compartment).

Once inside, it is easier to also remove the main circuit board from the shell by removing the 3 Philips screws from the bottom half. Before lifting out the console, push the white tabs on either side of the ribbon connector at the top towards the top of the shell. This releases the pressure on the ribbon cable and you can pull out the cable, leaving the screen stuck down in the front shell. Now remove the circuit board from the shell.

Remove the old speaker from the front PCB by cutting or desoldering the speaker wires.

Use double sided tape (optional) to secure the CleanAmp onto the back side of the speaker, as shown.&#x20;

Take some Kynar/wrapping wire (30awg or 28awg gauge wire - the thin stuff), cut it to length and solder the wires from the points on the Game Boy Pocket to the pads on the CleanAmp as shown.

Be careful when soldering the CleanAmp pads that you do not short the pads together or remove the resistors or capacitors near the pads.

Solder the top right two wires on the CleanAmp to the speaker. Polarity doesn't matter, you can solder either wire to either side.


![](../../assets/oRJW7y4WUFuX95KsN1Q5B_image.png)

### Increase Amp Volume

If you want the audio even louder you can join these two pads together. If you don't like it, just remove the solder joins to restore it to normal.

![](../../assets/T9t-hdsx_HsvD6oATCo9S_image.png)

### Troubleshooting

The bottom right wire is ground, going to pin 4 of the regulator on the right of the console.

The next wire to the left is the audio input. This is the unamplified, volume controlled sound from the console. This is connected to the middle pin of the volume wheel.

The next wire to the left is power in from the Game Boy Pocket. This should be 5 volts.

The send pad up on the right (above the ground wire) is the headphone pin that should be grounded when no headphones are present and floating when headphones are inserted. It is connected to pin 5 of the headphone connector. If you have no audio the first check is to solder the pink wire to the same pad as ground wire (pin 4 of regulator on the right of console). If that makes the audio work, but when its connected to the correct location it doesn't, you have a damaged headphone jack. You can leave the wire where the ground wire is soldered, but your speaker won't turn off if you insert headphones.

![](../../assets/RfWfRemiUcV79ZJ2CM_Y6_image.png)
