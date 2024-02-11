---
title: Incoming HID Report Format
slug: wm_G-incoming-hid-report-format
description: Learn about different HID report types and sub-commands for a specific device in this comprehensive document. Get insights into the position of each byte within the incoming data for each report type, including Rumble and Subcommand report type, NFC/IR MC
createdAt: Sat Mar 19 2022 21:07:45 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This page tells you more about the incoming data and the position of each byte as it pertains to the various HID report types and sub-commands.

### 0x01 - Rumble and Subcommand

| Index Range&#x20; | Data      | Description                                                                                                    |
| ----------------- | --------- | -------------------------------------------------------------------------------------------------------------- |
| 0                 | 0x01      | Report type                                                                                                    |
| 1                 | 0x0 - 0xF | Global packet number. Increments each time a packet is sent.                                                   |
| 2 - 9             | {}        | Rumble data                                                                                                    |
| 10                | {}        | Sub-command ID                                                                                                 |
| 11 - X            | {}        | Variable-length depending on the sub-command. Contains all of the data pertaining to the specific sub-command. |

### 0x03 - NFC/IR MCU firmware update packet

This command data is in progress.

| Index Range | Data      | Description                                                  |
| ----------- | --------- | ------------------------------------------------------------ |
| 0           | 0x03      | Report type                                                  |
| 1           | 0x0 - 0xF | Global packet number. Increments each time a packet is sent. |

### 0x10 - Rumble data only

| Index Range | Data      | Description                                                 |
| ----------- | --------- | ----------------------------------------------------------- |
| 0           | 0x10      | Report type                                                 |
| 1           | 0x0 - 0xF | Global packet number. Increments each time a packet is sent |
| 2-9         | {}        | Rumble data                                                 |

### 0x11 - Request NFC/IR MCU data

| Index Range | Data        | Description                                                 |
| ----------- | ----------- | ----------------------------------------------------------- |
| 0           | 0x11        | Report type                                                 |
| 1           | 0x0 - 0xF   | Global packet number. Increments each time a packet is sent |
| 2-9         | {}          | Rumble data                                                 |
| 10          | 0x01 - 0x02 | MCU Sub-command ID                                          |
| 11          | 0x01 - 0x08 | NFC command ID                                              |

