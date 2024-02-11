---
title: Implementing OpenJoyPad
slug: ZoXR-implementing-openjoypad
description: This document offers a comprehensive HID descriptor for a versatile gamepad compatible with any USB stack. The descriptor encompasses an array of controls, including ABXY buttons, D-Pad input, dual analog sticks and triggers, quad digital triggers, quad m
createdAt: Wed Feb 01 2023 23:55:04 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

# HID Descriptor

The descriptor below should work with any USB stack without issue. Tested with EFM8 and TinyUSB without issues. Click here to see an example of how you would send joypad data.

The descriptor supports the following

*   ABXY buttons

*   D-Pad input (See D-Pad format)

*   Dual analog sticks

*   Dual analog triggers

*   Quad digital triggers

*   Quad menu buttons

*   Two stick buttons (L3/R3)

```cpp
// Generic Gamepad HID descriptor
const uint8_t openjoypad_hid_report_descriptor[] = {
    0x05, 0x01,        // Usage Page (Generic Desktop Ctrls)

    0x09, 0x05,        // Usage (Game Pad)
    0xA1, 0x01,        // Collection (Application)
        0xA1, 0x01,         // Collection (Application)
            0x85, 0x01,        //   Report ID (1)

            0x05, 0x09,        //   Usage Page (Button)
            0x15, 0x00,        //   Logical Minimum (0)
            0x25, 0x01,        //   Logical Maximum (1)
            0x35, 0x00,        //   Physical Minimum (0)
            0x45, 0x01,        //   Physical Maximum (1)
            0x75, 0x01,        //   Report Size (1)
            0x95, 0x0E,        //   Report Count (14)
            0x19, 0x01,        //   Usage Minimum (0x01)
            0x29, 0x0E,        //   Usage Maximum (0x0E)
            0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
            
            0x95, 0x02,        //   Report Count (2)
            0x81, 0x01,        //   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)

            0x05, 0x01,        //   Usage Page (Generic Desktop Ctrls)
            0x25, 0x07,        //   Logical Maximum (7)
            0x46, 0x3B, 0x01,  //   Physical Maximum (315)
            0x75, 0x04,        //   Report Size (4)
            0x95, 0x01,        //   Report Count (1)
            0x65, 0x14,        //   Unit (System: English Rotation, Length: Centimeter)
            0x09, 0x39,        //   Usage (Hat switch)
            0x81, 0x42,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,Null State)
            0x65, 0x00,        //   Unit (None)
            0x95, 0x01,        //   Report Count (1)
            0x81, 0x01,        //   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)

            0x26, 0xFF, 0x00,  //   Logical Maximum (255)
            0x46, 0xFF, 0x00,  //   Physical Maximum (255)
            0x09, 0x30,        //   Usage (X)
            0x09, 0x31,        //   Usage (Y)
            0x09, 0x32,        //   Usage (Z)
            0x09, 0x35,        //   Usage (Rz)
            0x09, 0x33,        //   Usage (axis)
            0x09, 0x34,         // Usage (axis)

            0x75, 0x08,        //   Report Size (8)
            0x95, 0x06,        //   Report Count (6)
            0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)

        0xc0,

        // This implements the INPUT report for configuration requests
        0xA1, 0x01,         // Collection (Application)
            0x06, 0x00, 0xFF,      //            USAGE_PAGE (Vendor Defined Page 1) 
            0x09, 0x01,            //            USAGE (Vendor Usage 1) 
            0x85, 0x02,            //           Report ID (2)
            0x15, 0x00,            //            LOGICAL_MINIMUM (0) 
            0x26, 0xff, 0x00,       //            LOGICAL_MAXIMUM (255) 
            0x75, 0x08,            //            REPORT_SIZE (8) 
            0x95, 0x08,            //            REPORT_COUNT (8) 
            0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0xc0,

        // This impelements the OUTPUT report for configuration responses
        0xA1, 0x01,         // Collection (Application)
            0x06, 0x00, 0xFF,      //            USAGE_PAGE (Vendor Defined Page 1) 
            0x09, 0x01,            //            USAGE (Vendor Usage 1) 
            0x85, 0x02,            //           Report ID (2)
            0x15, 0x00,            //            LOGICAL_MINIMUM (0) 
            0x26, 0xff, 0x00,       //            LOGICAL_MAXIMUM (255) 
            0x75, 0x08,            //            REPORT_SIZE (8) 
            0x95, 0x08,            //            REPORT_COUNT (8) 
            0x91, 0x02,            //            OUTPUT (Data,Var,Abs)
        0xc0,
    // 125 bytes
    0xC0
};
```

