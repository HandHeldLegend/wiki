---
title: Analog Stick Calibration Data
slug: F7yu-analog-stick-calibration-data
description: Learn how to interpret and generate calibration data for analog sticks in Nintendo Joy-Con and Pro Controllers with this comprehensive document. Discover the structure of the calibration data, including the magic bytes signaling valid data, and gain acces
createdAt: Wed Apr 06 2022 06:57:40 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

## Interpreting Analog Stick Calibration

Calibration data is stored on the SPI flash onboard the Joy-Con or Pro Controller as a series of 22 bytes at *address 0x00008010*.

For these examples, the byte numbers correspond to the 11 bytes corresponding to each stick axis. There are two 'Magic Bytes' followed by 9 byte segments. The first segment is for the left stick.

:::hint{type="info"}
To obtain data for the right stick, increase the index by 11.
:::

This section is based on real calibration data read from a real Pro Controller after it has been calibrated through the Nintendo Switch OS. Processing requires that these bytes be cast to 16 bit unsigned integers. This is basically a way for Nintendo to compress 32 bytes into just 22* bytes*.

The data captured for left stick calibration data:&#x20;

*0xB2 0xA1 0x04 0xF6 0x6A 0xD7 0x77 0x75 0x13 0x06 0x60*

### Magic Bytes

If the Magic bytes equals 0xA1B2, it means data is stored by the calibration process and can be read. Otherwise, this is ignored.

| Byte Number | Description            | Data Example |
| ----------- | ---------------------- | ------------ |
| 0           | Magic byte lower byte. | 0xB2         |
| 1           | Magic byte upper byte. | 0xA1         |

The byte is read as *big endian* as *0xA1B2 *altogether.

### Center Value X Axis

| Byte Number | Description                      | Data Example           |
| ----------- | -------------------------------- | ---------------------- |
| 6           | Lower 4 bits. Shift left 8 bits. | 0x7**7** --> 0x**7**00 |
| 5           | The entire 8 bits.               | 0xD7                   |

Bytes get OR'd and the result is the X axis center.

*Example result: 0x7D7.*

### Minimum Value X Axis

This value is a *distance. *I.E. it's the amount of units away from the center point that the minimum value is. Math must be done to determine the exact minimum value.

| Byte Number | Description                                   | Data Example           |
| ----------- | --------------------------------------------- | ---------------------- |
| 9           | Get shifted lower 4 bits. Upper bits ignored. | 0x0**6** --> 0x**6**00 |
| 8           | The entire 8 bits.                            | 0x13                   |

1.  Bytes get OR'd.
    0x600 |= 0x013 --> *0x613.*

2.  Formula is applied
    (X Center - Result) = Minimum Value&#x20;
    (0x7D7 - 0x613)

*Example result: 0x1C4.*

### Maximum Value X Axis

This value is a *distance. *I.E. it's the amount of units away from the center point that the maximum value is. Math must be done to determine the exact maximum value.

| Byte Number | Description                                   | Data Example           |
| ----------- | --------------------------------------------- | ---------------------- |
| 3           | Get shifted lower 4 bits. Upper bits ignored. | 0xF**6** --> 0x**6**00 |
| 2           | The entire 8 bits.                            | 0x04                   |

1.  Bytes get OR'd.
    0x600 |= 0x004 --> *0x604.*

2.  Formula is applied
    (X Center + Result) = Maximum Value&#x20;
    (0x7D7 + 0x604)

*Example result: 0xDDB.*

### Center Value Y Axis

| Byte Number | Description                                     | Data Example           |
| ----------- | ----------------------------------------------- | ---------------------- |
| 7           | Shift left 4 bits.                              | 0x**75** --> 0x**75**0 |
| 6           | The upper 4 bits of byte 4. Lower bits ignored. | 0x**7**7 --> 0x**7**   |

Bytes get OR'd and the result is the Y axis center.

*Example result: 0x756.*

### Minimum Value Y Axis

This value is a *distance. *I.E. it's the amount of units away from the center point that the minimum value is. Math must be done to determine the exact minimum value.

| Byte Number | Description                                     | Data Example           |
| ----------- | ----------------------------------------------- | ---------------------- |
| 10          | Shift left 4 bits.                              | 0x**60** --> 0x**60**0 |
| 9           | The upper 4 bits of byte 4. Lower bits ignored. | 0x**0**6 --> 0x**0**   |

1.  Bytes get OR'd.
    0x600 |= 0x000 --> *0x600.*

2.  Formula is applied
    (Y Center - Result) = Minimum Value&#x20;
    (0x756 - 0x600)

*Example result: 0x156.*

### Maximum Value Y Axis

This value is a *distance. *I.E. it's the amount of units away from the center point that the maximum value is. Math must be done to determine the exact maximum value.

| Byte Number | Description                                     | Data Example           |
| ----------- | ----------------------------------------------- | ---------------------- |
| 4           | Shift left 4 bits.                              | 0x**6A **--> 0x**6A**0 |
| 3           | The upper 4 bits of byte 4. Lower bits ignored. | 0x**F**6 --> 0x**F**   |

1.  Bytes get OR'd.
    0x6A0 |= 0x00F --> *0x6AF.*

2.  Formula is applied
    (Y Center + Result) = Maximum Value&#x20;
    (0x756 + 0x6AF)

*Example result: 0xE05.*

## Generating Calibration Data

For this example, we will use the following calibration values. The index should be adjusted to match the proper address locations.

| Name                 | Hex   | Decimal |
| -------------------- | ----- | ------- |
| X axis minimum value | 0x1C4 | 452     |
| X axis center value  | 0x7D7 | 2007    |
| X axis maximum value | 0xDDB | 3547    |
| Y axis minimum value | 0x157 | 343     |
| Y axis center value  | 0x757 | 1879    |
| Y axis maximum value | 0xE06 | 3590    |

```cpp
// X axis demo values
uint16_t x_min = 0x1C4;
uint16_t x_center = 0x7D7;
uint16_t x_max = 0xDDB;

// Some basic math needs to be done ot get the proper
// storage value. The value that gets stored is technically
// the 'distance' from center.
uint16_t x_min_store = x_min + x_center;
uint16_t x_max_store = x_max - x_center;

// Y axis demo values
uint16_t y_min = 0x157;
uint16_t y_center = 0x757;
uint16_t y_max = 0xE06;

uint16_t y_min_store = y_min + y_center;
uint16_t y_max_store = y_max - y_center;

uint8_t cal_data[11];

// Set magic byte.
cal_data[0] = 0xB2;  
cal_data[1] = 0xA1;

// Lower byte of x_max_store.
cal_data[2] = x_max_store & 0xFF;

// Upper 4 bits of x_max_store shifted to right 8 bits.
cal_data[3] = (x_max_store & 0xF00) >> 8;

// Lower 4 bits of y_max_store shifted to the left 4 bits.
// Gets 'OR'd against the current value.
cal_data[3] |= (y_max_store & 0xF) << 4;

// Upper byte of y_max_store shifted right 4 bits.
cal_data[4] = (y_max_store & 0xFF0) >> 4;

// Lower byte of x_center.
cal_data[5] = x_center & 0xFF;

// Upper 4 bits of x_center shifted right 8 bits.
cal_data[6] = (x_center & 0xF00) >> 8;

// Lower 4 bits of y_center shifted left 4 bits.
// Gets 'OR'd against the current value.
cal_data[6] |= (y_center & 0xF) << 4;

// Upper byte of y_center shifted right 4 bits.
cal_data[7] = (y_center & 0xFF0) >> 4;

// Lower byte of x_min_store.
cal_data[8] = x_min_store & 0xFF;

// Upper 4 bits of x_min_store shifted right 8 bits.
cal_data[9] = (x_min_store & 0xF00) >> 8;

// Lower 4 bits of y_min_store shifted left 4 bits.
// Gets 'OR'd against the current value.
cal_data[9] |= (y_min_store & 0xF) << 4;

// Upper byte of y_min_store shifted right 4 bits.
cal_data[10] = y_min_store >> 4;

```



