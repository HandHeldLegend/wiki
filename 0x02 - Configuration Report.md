---
title: 0x02 - Configuration Report
slug: lkwy-0x02-configuration-report
description: Learn about the different sub-commands and their unique IDs for retrieving and configuring settings on a gamepad. Explore various functions such as resetting or saving settings, analog calibration, trigger sensitivity, button remapping, and more. Discover
createdAt: Wed Feb 01 2023 23:50:33 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

# INPUT Configuration Report



# OUTPUT Configuration Report Requests

The first byte after the Report ID of these commands represents a sub-command to tell the gamepad which configuration data it would like to retrieve or what command to apply. Additional bytes represent parameters related to the command. See the table and information below.

| Sub-Command ID (Byte 1) | Meaning                                         |
| ----------------------- | ----------------------------------------------- |
| 0x00                    | Reset or save settings                          |
| 0x01                    | Retrieve all settings                           |
| 0x02                    | Initiate or finalize analog calibration process |
| 0x03                    | Retrieve trigger sensitivity data               |
| 0x04                    | Retrieve trigger mode data                      |
| 0x05                    | Retrieve button remap data                      |
| 0x06                    | Initiate or cancel digital button remap         |

## 0x00 - Reset or Save Settings

| Parameter byte (Byte 2) | Meaning                                    | Notes                          |
| ----------------------- | ------------------------------------------ | ------------------------------ |
| 0x00                    | Reset all configuration options to default | Should not save at this point. |
| 0x01                    | Save all configuration options to storage. | Save all settings              |

## 0x01 - Retrieve all settings

The device (Gamepad) will reply with a number of 0x02 ID Input reports. Each will have its own sub-command ID that will contain the relevant configuration data.&#x20;

## 0x02 - Initiate or finalize analog calibration process

This command requests that the controller either initiate or finalize an analog stick calibration process.

This allows for each axis to be calibrated individually.

### Byte 2 - Function Select

| Parameter byte (Byte 2) | Meaning                    | Notes                                                                                                  |
| ----------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------ |
| 0x00                    | Initiate calibration mode. | This should toggle an internal calibration process in the joypad itself.                               |
| 0x01                    | Finalize calibration mode. | This will tell the joypad to take the current data in its calibration cycle and save it.               |
| 0x02                    | Cancel calibration mode.   | This will tell the joypad to cancel the calibration mode. Analog calibration reverts to original data. |

### Byte 3 - Axis Select

| Parameter byte (Byte 3) | Meaning                                 | Notes                                         |
| ----------------------- | --------------------------------------- | --------------------------------------------- |
| 0x00                    | Left stick, X and Y axis                | Joypad should handle min, max, center values. |
| 0x01                    | Right stick, X and Y axis               |                                               |
| 0x02                    | Analog triggers, Left and Right trigger |                                               |

## 0x03 - Retrieve trigger sensitivity data

This command requests the sensitivity values for the triggers. No additional parameter is needed. See the input description for the response format.

## 0x04 - Retrieve trigger mode data

This command requests the sensitivity values for the triggers. The parameter byte is a mode bank symbol. There are several pre-defined modes which would help to define trigger modes for a few use-case scenarios that are common with USB Gamepads. See this link for more information.

This allows for trigger modes to be customized for different USB Gamepad modes.

| Parameter byte (Byte 2) | Meaning   | Notes                                                     |
| ----------------------- | --------- | --------------------------------------------------------- |
| 0x00 - 0xFF             | Mode bank | Implementation of different mode banks can be customized. |

## 0x05 - Retrieve Button Remap Data

No parameter data required.

## 0x06 - Initiate Or Cancel Digital Button Remap

### Byte 0 - Initiate or Cancel

| Parameter byte (Byte 1) | Meaning        | Notes |
| ----------------------- | -------------- | ----- |
| 0x00                    | Initiate remap |       |
| 0x01                    | Cancel remap   |       |

### Byte 1 - Button to initiate remap

Send a byte value of 0 through 15 to map one of the following buttons.

| Value | Button to remap    | Notes        |
| ----- | ------------------ | ------------ |
| 0     | D-Pad Up           |              |
| 1     | D-Pad Down         |              |
| 2     | D-Pad Left         |              |
| 3     | D-Pad Right        |              |
| 4     | Button Up          | Nintendo "X" |
| 5     | Button Down        | Nintendo "B" |
| 6     | Button Left        | Nintendo "Y" |
| 7     | Button Right       | Nintendo "A" |
| 8     | Trigger L          |              |
| 9     | Trigger ZL         |              |
| 10    | Trigger R          |              |
| 11    | Trigger ZR         |              |
| 12    | Button Start       |              |
| 13    | Button Select      |              |
| 14    | Button Stick Left  |              |
| 15    | Button Stick Right |              |

