---
title: 0x01 - Input Report
slug: lyUN-0x01-input-report
description: Learn how to implement the OpenJoyPad HID report in C with this comprehensive document. Included is a C struct with 10 bytes length, featuring fields that accurately represent the status of gamepad buttons, triggers, sticks, and D-Pad positions. Don't mis
createdAt: Wed Feb 01 2023 23:50:18 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

# INPUT Format

See the code block example for an implementation of the OpenJoyPad HID report as a C struct.

```cpp
// Structure for OpenJoyPad USB input report Data
// Has a length of 10 bytes
typedef struct
{
    uint8_t report_id;

    union
    {
        struct
        {
            uint8_t button_y    : 1;
            uint8_t button_b    : 1;
            uint8_t button_a    : 1;
            uint8_t button_x    : 1;
            uint8_t trigger_l   : 1;
            uint8_t trigger_r   : 1;
            uint8_t trigger_zl  : 1;
            uint8_t trigger_zr  : 1;
        };
        uint8_t buttons_1;
    };

    union
    {
        struct
        {
            uint8_t button_minus  : 1;
            uint8_t button_plus   : 1;
            uint8_t stick_left    : 1;
            uint8_t stick_right   : 1;
            uint8_t button_home   : 1;
            uint8_t button_capture: 1;
            uint8_t padding       : 2;
        }; 
        uint8_t buttons_2;
    };

  uint8_t dpad_hat;
  uint8_t stick_left_x;
  uint8_t stick_left_y;
  uint8_t stick_right_x;
  uint8_t stick_right_y;
  uint8_t analog_trigger_l;
  uint8_t analog_trigger_r;
} __attribute__ ((packed)) openjoypad_input_s;
```

# D-Pad Hat Formatting

See the enumerator table below for definitions you can use to ensure your D-Pad output values are correct.

```cpp
typedef enum
{
  JP_HAT_TOP          = 0x00,
  JP_HAT_TOP_RIGHT    = 0x01,
  JP_HAT_RIGHT        = 0x02,
  JP_HAT_BOTTOM_RIGHT = 0x03,
  JP_HAT_BOTTOM       = 0x04,
  JP_HAT_BOTTOM_LEFT  = 0x05,
  JP_HAT_LEFT         = 0x06,
  JP_HAT_TOP_LEFT     = 0x07,
  JP_HAT_CENTER       = 0x08,
} jp_input_hat_dir_t;
```

