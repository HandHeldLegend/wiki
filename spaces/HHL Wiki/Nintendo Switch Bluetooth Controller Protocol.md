---
title: Nintendo Switch Bluetooth Controller Protocol
slug: g6FX-nintendo-switch-bluetooth-controller-protocol
description: Learn how to implement the Nintendo Switch controller protocol using Bluetooth and the Bluedroid Bluetooth stack in the ESP-IDF development environment. This document covers HID reports, sub-commands, and how to extract necessary information from incoming
createdAt: Sat Mar 19 2022 05:45:53 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This page details all things Nintendo Switch controller protocol (Bluetooth only) related.

:::hint{type="info"}
**This article is still a work in progress! It was last updated June 24, 2022 and may have information that is missing or incomplete.**
:::

On top of this, specific details are given on how this looks implemented using the **Bluedroid** Bluetooth stack in the **ESP-IDF** development environment.

### Sources

This work would not be possible without the following sources put together by community modding members.

*   [dekuNukem Nintendo Switch Reverse Engineering - GitHub](https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering)

*   [JoyConDroid Project - GitHub](https://github.com/YouTubePlays/JoyConDroid/)

*   [NathanReeves BlueCubeMod - GitHub](https://github.com/NathanReeves/BlueCubeMod/tree/master/Firmware/BlueCubeModv2)

## HID Reports and Sub-Commands

### HID Reports from Nintendo Switch

Once a report comes in from the Nintendo Switch, it must be interpreted. The **report type **determines what type of data the Nintendo Switch will expect back from the controller. As far as I can tell, these reports are only sent through **HID interrupt reports**.

### Obtaining Report Type

**To obtain the report type, see the example below.**

In this code example, we are acting on the callback event of a **esp\_hidd\_cb\_param\_t** type. The report type is specified by *byte 0*.

```cpp
// This is the callback event that's already registered
void hidd_cb(esp_hidd_cb_event_t event, esp_hidd_cb_param_t *param)
{
    switch(event)
    {
        case ESP_HIDD_INTR_DATA_EVT:
            // In this event case, we are handling an interrupt event
            // We'll grab the HID command type and set it as 'report_type'.
            uint8_t report_type = param->intr_data.data[0];
            break;
    }
}
```

### HID report types and meanings

| Report ID | Meaning                               | Details                                                                                                                                         |
| --------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x01      | Rumble data AND a Subcommand          | The event data contains data to animate the linear actuators for HD rumble. This event data also contains a sub-command. Read on to learn more. |
| 0x03      | NFC and IR MCU firmware update packet | N/A                                                                                                                                             |
| 0x10      | Rumble data                           | Only event data to animate the linear actuators for HD rumble.                                                                                  |
| 0x11      | Request NFC/IR MCU data               | Read data from the IR sensor or NFC memory buffer from the controller.                                                                          |

### Sub-Commands from Nintendo Switch

Sub-commands will interface with the various hardware built in to the controller to perform many functions. The Nintendo Switch controllers have SPI flash built in to hold firmware patches, controller colors, calibration data, and more.&#x20;

### Obtaining Sub-Command

In this code example, we are acting on the callback event of a **esp\_hidd\_cb\_param\_t** type. The sub-command is *byte 10* of the incoming data.

```cpp
// This is the callback event that's already registered
void hidd_cb(esp_hidd_cb_event_t event, esp_hidd_cb_param_t *param)
{
    switch(event)
    {
        case ESP_HIDD_INTR_DATA_EVT:
            // This is the same as the previous example... we got report ID
            uint8_t report_type = param->intr_data.data[0];

            // We'll get the sub command as 'sub_cmd'
            uint8_t sub_cmd = param->intr_data.data[10]
            break;
    }
}
```

### Sub-Command types and meanings

| Sub-Command | Meaning                      | Details |
| ----------- | ---------------------------- | ------- |
| 0x00        | Get ONLY Controller State    |         |
| 0x01        | Bluetooth manual pairing     |         |
| 0x02        | Request device info          |         |
| 0x03        | Request input report mode    |         |
| 0x04        | Trigger buttons time elapsed |         |
| 0x05        | Get page list state          |         |
| 0x06        | Set HCI state                |         |
| 0x07        | Reset pairing info           |         |
| 0x08        | Set low power shipping state |         |
| 0x10        | SPI Flash read               |         |
| 0x11        | SPI Flash write              |         |
| 0x12        | SPI Sector erase             |         |
| 0x20        | Reset NFC/IR MCU             |         |
| 0x21        | Set NFC/IR MCU config        |         |
| 0x22        | Set NFC/IR state             |         |
| 0x30        | Set player number (lights)   |         |
| 0x31        | Get player number (lights)   |         |
| 0x38        | Set "Home" button LED        |         |
| 0x40        | Enable 6-axis IMU            |         |
| 0x41        | Set 6-axis sensitivity       |         |
| 0x42        | Write IMU registers          |         |
| 0x43        | Read IMU registers           |         |
| 0x48        | Enable vibration             |         |



