---
title: OpenJoyPad HID USB Specification
slug: J4vc-openjoypad-hid-usb-specification
description: Learn about the USB HID specification for gamepads, enabling multiple gamepads to be easily configured with a single application. Explore a comprehensive list of commands for input and output, covering gamepad input reports and configuration reports. Addi
createdAt: Wed Feb 01 2023 23:47:32 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This article details a USB HID specification that can be implemented across gamepads to allow configuration of many gamepads with one application.

# Commands (INPUT)

These are sent from the device (Gamepad) to the host.

| Report ID | Meaning                                  |
| --------- | ---------------------------------------- |
| 0x01      | Gamepad input report                     |
| 0x02      | Configuration report                     |
| 0x03      | Reserved (Maybe future motion controls?) |

# Commands (OUTPUT)

These are sent from the host to the device (Gamepad).

| Report ID | Meaning                      |
| --------- | ---------------------------- |
| 0x02      | Request Configuration Report |

