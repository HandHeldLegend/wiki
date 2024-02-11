---
title: MCU/NFC Sub-commands
slug: 63Kd-mcunfc-sub-commands
description: Learn about the different command types for MCU and NFC systems with this comprehensive document. Discover how to request the status and NFC data with MCU commands, and explore the functionalities of NFC commands, such as starting tag polling, discovery, 
createdAt: Sat Mar 19 2022 22:52:41 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

### MCU Sub-command types

| Command ID | Meaning            | Details               |
| ---------- | ------------------ | --------------------- |
| 0x01       | Request MCU status | N/A                   |
| 0x02       | Request NFC data   | See NFC command chart |

### NFC command types

| Command ID | Meaning                 | Details |
| ---------- | ----------------------- | ------- |
| 0x01       | Start NFC tag polling   |         |
| 0x02       | N/A                     |         |
| 0x04       | Start NFC tag discovery |         |
| 0x06       | Read NFC tag            |         |
| 0x08       | Write NFC tag           |         |

## NFC command actions

### 0x01 - Start NFC tag polling

