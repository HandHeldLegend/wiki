---
title: Analog Stick Data
slug: sT5X-analog-stick-data
description: Learn how to interpret and encode joystick data from a controller with this comprehensive document. Discover the format of analog data in both slow mode and standard input mode, including the combination of specific bytes for X and Y axis values. In stand
createdAt: Thu Apr 07 2022 00:40:50 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

## Decode Joystick Data

This is a section detailing how to interpret analog/joystick data coming from the controller.

### Slow Mode/Short Input Report Joystick Data

Starting on *byte 4 *of the incoming report from the controller, you can find the joystick analog data encoded as follows.

| Byte Number | Description          | Example Data |
| ----------- | -------------------- | ------------ |
| 4           | Lower byte of X axis |              |
| 5           | Upper byte of X axis |              |
| 6           | Lower byte of Y axis |              |
| 7           | Upper byte of Y axis |              |

:::hint{type="info"}
To get values for the right stick, add 4 to the byte index.
:::

To get the X or Y axis values, OR the respective bytes together.

```cpp
X_Axis = byte[4] | (byte[5] << 8);
Y_Axis = byte[6] | (byte[7] << 8);
```

### Standard Input Mode Joystick Data

Starting on *byte 6 *of a standard input mode report from the controller, you can find the joystick analog data encoded as follows.

| Byte Number | Description                                                                              | Example Data |
| ----------- | ---------------------------------------------------------------------------------------- | ------------ |
| 6           | Lower byte of X axis. 8 bits.                                                            |              |
| 7           | Lower 4 bits are the Upper byte of X axis. Upper 4 bits are the lower byte of the Y axis |              |
| 8           | Upper byte of Y axis. 8 bits.                                                            |              |

:::hint{type="info"}
For the right stick, add 3 to the byte index.
:::

To get the decoded X or Y axis values, some math is involved.&#x20;

```cpp
X_Axis = byte[6] | ((byte[7] & 0xF) << 8);
Y_Axis = (byte[7] >> 4) | (byte[8] << 4);
```

## Encode Joystick Data

This section details how to take an analog stick value and encode it to be read by the console.

### Slow Mode Joystick Data

In a standard input report, *bytes 4-7* represent the stick data.

For this example, we will use these values and we will only focus on the left stick which is *bytes 4-5*.

*X axis - 0x7D4**** (2004 in decimal)***

*Y axis - 0x6C5 ****(1733 in decimal)***

```cpp
uint8_t input_bytes[4];

uint16_t x_axis = 0x7D4;
uint16_t y_axis = 0x6C5;

// Trim off the top bits.
input_bytes[0] = x_axis & 0xFF;

// Take only the uppermost byte of x_axis and shift right 8 bits.
input_bytes[1] = (x_axis & 0xF00) >> 8;

// Trim off the top bits.
input_bytes[2] = y_axis & 0xFF;

// Take only the uppermost byte of y_axis and shift right 8 bits.
input_bytes[3] = (y_axis & 0xF00) >> 8;

// Final results
// 0 - 0xD4
// 1 - 0x07
// 2 - 0xC5
// 3 - 0x06
```

### Standard Input Mode Joystick Data

In a standard input report, *bytes 6-11* represent the stick data.

For this example, we will use these values and we will only focus on the left stick which is *bytes 6-8*.

*X axis - 0x7D4 ****(2004 in decimal)***

*Y axis - 0x6C5 ****(1733 in decimal)***

```cpp
uint8_t input_bytes[3];

uint16_t x_axis = 0x7D4;
uint16_t y_axis = 0x6C5;

// Trim off the top byte.
input_bytes[0] = x_axis & 0xFF;

// Take only the uppermost 4 bits of x_axis (0x7).
input_bytes[1] = x_axis >> 8;

// Add the lowermost 4 bits of y_axis shifted 4 bits
// to the proper position (0x5).
input_bytes[1] |= (y_axis & 0xF) << 4;

// Take only the uppermost byte of y_axis (0x6C).
input_bytes[2] = y_axis >> 4;

// Final results
// 0 - 0xD4
// 1 - 0x57
// 2 - 0x6C
```

