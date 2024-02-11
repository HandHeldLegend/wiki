---
title: Outgoing HID Report Format
slug: a1Sa-outgoing-hid-report-format
description: Learn the essential formatting requirements for different types of reports to be sent back to the controller. This comprehensive document covers report types like response with rumble and subcommand, NFC/IR MCU firmware update packet, rumble only, and NFC
createdAt: Sat Mar 19 2022 21:08:25 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This page details the formatting of the input report the controller needs to send back to the controller for each of the different reports received.

### 0x01 - Response - Rumble and Subcommand

| Output Index Range | Data                                          | Description          |
| ------------------ | --------------------------------------------- | -------------------- |
| 12                 |                                               | Acknowledgement Byte |
| 13                 |                                               | Sub-Command ID       |
| 14 Onward          | See Section Sub-Command Response Format (WIP) |                      |

### 0x03 - NFC/IR MCU firmware update packet

|    |   |                      |
| -- | - | -------------------- |
| 12 |   | Acknowledgement Byte |
| 13 |   |                      |

### 0x10 - Rumble only

### 0x11 - NFC/IR MCU data request

