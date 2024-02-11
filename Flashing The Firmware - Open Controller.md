---
title: Flashing The Firmware - Open Controller
slug: Olj8-flashing-the-firmware
description: Learn how to flash firmware onto an ESP32 controller and USB gamepad with this comprehensive guide. Follow the step-by-step instructions to connect the Micro-USB port, install drivers, and update the firmware. For the USB gamepad, download and extract a Z
createdAt: Wed Apr 05 2023 12:08:08 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

[Open Controller Firmware Page](https://handheldlegend.github.io/opencontroller)



## ESP32 Firmware Flashing

Flashing the initial firmware onto your ESP32 requires you to use the ****Micro-USB**** port on the ESP32. Plug in the ****Micro-USB**** and click connect on the update website linked above.&#x20;

:::hint{type="info"}
You may need to install the CP210x driver provided by Silicon Labs:&#x20;



Windows: <https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip>

Mac:

<https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip>
:::



![](https://i.imgur.com/BYp75r5.png)

You will be asked to select a device, select "CP2102 USB to UART Bridge Controller"&#x20;

![](https://i.imgur.com/slSNLal.png)

It will then prompt you with a box that says "Install Open Controller Classic", click that button

![](https://i.imgur.com/c4EBAZU.png)

&#x20;It will ask you if you want to erase the device; *this is optional and not required.* Click next.&#x20;

![](https://i.imgur.com/00kSEch.png)

It will then ask you to confirm the installation

![](https://i.imgur.com/vGDWPpG.png)

The install will then start, it may take up to two minutes to complete

![](https://i.imgur.com/0JdRSGi.png)

When it finishes you will get a confetti symbol showing that the install is complete! You can then close any pops ups left on the screen, and ****unplug the micro-usb cable****.&#x20;

![](https://imgur.com/tOODtDw.png)

## USB Firmware Flashing

The USB gamepad communications are handled by an EFM8UB1 microcontroller acting as a co-processor as the ESP32 does not have native USB device support. This microcontroller has its own firmware which must be installed.

![](https://imgur.com/ql2ZBE5.png)

Download the ZIP file provided on the firmware page. Extract the ZIP file.&#x20;

Hold down the button labelled **EN **on the ESP32 devkit while plugging in the ****USB-C Cable****. This will put the USB microcontroller into programming mode.

Run the 'LoadEFM8.bat' file.&#x20;

![](https://imgur.com/vaJVrso.png)

You may end up getting a Windows Defender notification, simply click **more info** and **allow access** to for the flasher to run.&#x20;

![](https://imgur.com/3kjyDEL.png)

After a successful update, you will get a message telling you to press any button to exit.&#x20;

![](https://imgur.com/xMDEAbC.png)

Unplug and replug your device to confirm USB Gamepad function is working properly.
