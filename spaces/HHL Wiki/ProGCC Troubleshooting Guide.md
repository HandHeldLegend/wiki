---
title: ProGCC Troubleshooting Guide
slug: zlmo-progcc-troubleshooting-guide
description: Learn about common issues with game controllers, such as drifting sticks and malfunctioning buttons. This document provides potential causes for each issue and offers practical solutions such as cable replacements, support contacts, soldering techniques, 
createdAt: Thu Sep 22 2022 21:30:27 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

## Common Issues

*   Sticks are not centered

*   Sticks are drifting

*   Disconnecting Intermittently&#x20;

See our table below listing common issues and potential causes.

| Issue                                                                | Cause                                                                                      | Solution                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Controller disconnects when the USB Cable is wiggled.                | Defective USB-C Cable.                                                                     | Contact support\@handheldlegend.com to receive a replacement cable.                                                                                                                                                                       |
| Controller does not work when plugged in until Plus/Home is pressed. | Defective ribbon cable or defective soldering on ribbon connector.                         | This is likely a production issue. Take photos of the ribbon cable and the ribbon connectors, send them to support\@handheldlegend.com to receive support.                                                                                |
| Controller is stuck in 'Smash Ultimate' mode.                        | 'Ultimate Mode' is considered a trigger mode, and it is not toggled like Xbox Layout Mode. | Hold one of the button combinations for the listed trigger modes in our [user guide.](https://wiki.handheldlegend.com/progcc-user-guide#eZy98)                                                                                            |
| Intermittent Disconnects while playing games                         | Too much draw on 3.3v line&#x20;                                                           | Solder the 47uF capacitor onto the controller, as described [here](https://wiki.handheldlegend.com/progcc-47uf-capacitor-install-guide)                                                                                                   |
| Home/Minus not pressing right/always pressing right&#x20;            | Membrane isn't connecting correctly with motherboard                                       | You can trim the membrane to fix this issue, as well as adjusting the screw tightness can resolve this issue. See the [guide here](https://wiki.handheldlegend.com/progcc-minus-button-fixes)                                             |
| Bumper buttons feel mushy                                            | Membrane placement/ Brand                                                                  | The membranes dictate the feel of the bumper buttons, you should make sure they are thoroughly seated. If you want a tougher button press then try the ExtremeRate brand membranes as they are springier than other unbranded ones.&#x20; |
| ERM Rumble Motors not firing at all angles/at the correct times      | Not enough power making it to the ERM motors.&#x20;                                        | Remove resistor R20, and bridge the connection with solder to allow more power through to the rumble motors.&#x20;                                                                                                                        |
| Left Stick Acting As Dpad, only activates at edge of stick gate      | Calibration went wrong.                                                                    | Recalibrate the sticks of the controller. Hold minus while plugging the controller in, spin the sticks 5-6 times, and press plus to save. It will automatically reconnect the controller.&#x20;                                           |

