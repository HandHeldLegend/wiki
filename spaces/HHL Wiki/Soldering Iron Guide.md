---
title: Soldering Iron Guide
slug: 82dm-soldering-iron-guide
description: Learn everything you need to know about soldering with this comprehensive guide. From soldering irons and recommended temperatures to using flux and cleaning with isopropyl alcohol, this document covers it all. Discover the importance of a temperature-con
createdAt: Fri Feb 04 2022 21:06:14 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Dec 05 2023 19:55:42 GMT+0000 (Coordinated Universal Time)
---

This guide is all about soldering, recommended gear, recommended temperatures, and more.&#x20;

## Introduction

**Example of soldering joints:**

![](../../assets/tjTa4_KOcSLCGQNuLNHsg_image.png)

### Soldering Iron Choice

Choosing your soldering iron can be a daunting task. Using a temperature-controlled soldering iron is an absolute must when performing precision work or modding. **Your fire stick from 10 years ago that plugs straight into the wall is not recommended and will likely result in burnt pads and regret!**&#x20;

:::hint{type="info"}
Hand Held Legend earns commissions for Amazon purchases made through links in this post.
:::

Here are a few recommendations, though it is not a comprehensive list by any means and you should do your own research before purchasing:

*   [Hakko FX888D](https://www.amazon.com/dp/B00C2BHTBI?tag=hanhelleg-20)

*   [Pinecil Soldering iron](https://www.amazon.com/dp/B096X6SG13?tag=hanhelleg-20)

*   [Miniware TS80P](https://www.amazon.com/dp/B07HP1P51J?tag=hanhelleg-20)

*   [Weller WE-1010](https://www.amazon.com/Weller-WE1010NA-Digital-Soldering-Station/dp/B077JDGY1J/ref=sr_1_5?crid=NK14USP8AZQ6\&keywords=weller+we1010\&qid=1644263236\&sprefix=Weller+WE%2Caps%2C131\&sr=8-5)

*   [Ersa i-con Nano](https://www.amazon.com/dp/B01KP7ZA34?tag=hanhelleg-20)

Below is a great comparison video from Thomas Sanladerer going over these exact soldering irons.

<https://www.youtube.com/watch?v=R2sPDQeGlj8>

### Materials and supplies

Here's a short list of materials you'll want to pick up:

*   [Leaded solder (63/37 composition recommended)](https://www.amazon.com/dp/B075WBDYZZ?tag=hanhelleg-20)

*   [Low-melt solder (for large component removal)](https://www.amazon.com/dp/B015RV4NBS?tag=hanhelleg-20)

*   [Solder braid/wick](https://www.amazon.com/dp/B09NXBZBFT?tag=hanhelleg-20)

*   [Flux (Gel or paste recommended)](https://www.amazon.com/dp/B07JYLV381?tag=hanhelleg-20)

*   [Isopropyl alcohol for cleanup](https://www.amazon.com/dp/B08JZJ5QV2?tag=hanhelleg-20)

*   [Nitrile work gloves](https://www.amazon.com/dp/B074XCXVCM?tag=hanhelleg-20)

*   [Cotton swabs](https://www.amazon.com/dp/B09498GV6R?tag=hanhelleg-20)

*   [0.1mm Jumper Wire (enameled)](https://www.amazon.com/dp/B075RCMCTF?tag=hanhelleg-20)

*   [Brass sponge (never use wet sponge!)](https://www.amazon.com/dp/B08FQBS97L?tag=hanhelleg-20)

*   Extra soldering tips compatible with your iron

*   [Fume extractor](https://www.amazon.com/dp/B07VWDN29F?tag=hanhelleg-20)

*   [Magnetic board holder](https://www.amazon.com/dp/B09B73XL33?tag=hanhelleg-20)

*   [Desktop USB Microscope](https://www.amazon.com/dp/B081F64YLB?tag=hanhelleg-20)

*   [Flush cutters](https://www.amazon.com/dp/B00FZPDG1K?tag=hanhelleg-20)

*   [Heat resistant silicone mat](https://www.amazon.com/dp/B075M7PQZX?tag=hanhelleg-20)

*   [Kapton tape (heat resistant tape)](https://www.amazon.com/dp/B07RZYY2T1?tag=hanhelleg-20)

*   [Eye protection](https://www.amazon.com/dp/B00FA4RB12?tag=hanhelleg-20)

*   [Silicone Mat](https://www.amazon.com/Magnetic-Soldering-Electronics-Cellphone-Resistant/dp/B01N10MA2O/ref=asc_df_B01N10MA2O/?tag=hyprod-20\&linkCode=df0\&hvadid=242007122763\&hvpos=\&hvnetw=g\&hvrand=6964047050416917009\&hvpone=\&hvptwo=\&hvqmt=\&hvdev=c\&hvdvcmdl=\&hvlocint=\&hvlocphy=9007231\&hvtargid=pla-440907892743\&psc=1)

## Setup

### Iron temperature

The first thing you should know about soldering iron temps is that there is never going to be one single temperature you should stick to. The required temperature will change depending on several factors including:

*   Board thickness

*   Copper weight/thickness

*   Board layer count

*   Trace thickness

*   Component size

*   Soldering tip size

*   Solder type (leaded/unleaded)

If you're unsure about where to start, a safe starting temperature to try is 365c. For thicker boards, you may end up going as high as 400c if you're dealing with a component soldered to a large ground plane as all the copper acts as a huge heat sink.&#x20;

If the component or joint you are trying to heat does not turn molten within 1 second of iron contact, evaluate the situation carefully. If you are using a small tip on a large component, there may not be enough surface area contact to sufficiently transfer heat. Trying a larger tip in these situations may help!

If you still have trouble; either your *temperature could be too low or your soldering iron may not be capable of putting out the required power to heat the area.*&#x20;

### Temperature calibration

Refer to the user manual for your specific soldering iron to utilize any calibration features. A well-calibrated soldering iron will take out much of error associated with incorrect temperatures. Calibrating properly could mean the difference of 10 degrees celcius or more.&#x20;

If you are unable to properly calibrate your iron, you may find that your temperature settings need to be higher or lower compared to the typical temperatures listed in this guide. The more you work with a soldering iron, the less important the calibration becomes as you'll be able to understand when it's appropriate to raise/lower your iron temps.&#x20;

## Work Guide

### Tinning iron

Every time you turn your iron on, wait until it reaches the target temperature before starting any work. Once it is at temperature, clean the tip of your iron by scraping it against your brass sponge. This will clean off any oxides (non-conductive layer formed by contact with oxygen).&#x20;

Add some fresh solder to the tip of your iron, then scrape with your brass sponge again. A fume extractor is recommended at this stage to protect your lungs and eyes from irritants.&#x20;

### Desoldering

Most electronics nowadays are manufactured using unleaded solder. Solder with of this composition typically has a **much** higher melting temperature, in the 380c range or higher. For this reason, it's always recommended to mix in some leaded solder **or **low-melt solder according to the situation at hand. Use flux whenever applying solder for the best results. [See the necessity of flux below.](https://wiki.handheldlegend.com/soldering-iron-guide#nv-necessity-of-flux)

### Wicking

Solder wick or braid is one of the best tools for removing solder from a component or board. Using a quality flux in conjunction with a quality wick can product some incredible results. It is recommended to cut off only the amount of wick you'll need to complete the job. The wick is made of copper, and can act as a heat sink, drawing heat away from the work area.&#x20;

Avoid scraping pads with the wick if you're applying pressure using your soldering iron. The goal is to heat the wick sufficiently that it will absorb any solder. This works due to the [surface tension properties of solder (see below)](https://wiki.handheldlegend.com/soldering-iron-guide#9m-surface-tension). If you perform any movement with the wick beneath your soldering iron, it should be *gliding* on the surface of your pads with barely any pressure.&#x20;

### Cleanup

Even solder flux marked as 'no-clean' **should be cleaned**. Don't take the name at face value-- it simply indicates that it will not become corrosive if left unchecked.&#x20;

Cleanup with isopropyl alcohol is recommended:

*   before you begin working in any area on a board

*   in regular intervals while working to avoid flux becoming 'spent' or burnt up

*   after you work to ensure connectors and other sensitive areas remain clean

Clean your soldering iron tip as necessary throughout your work process. If your tip ever becomes dull, clean with brass sponge and re-apply a small amount of solder to bring it back to a shiny state.&#x20;

When finishing your work process, clean your iron tip one last time, apply some fresh solder to the tip, then holster your iron and shut off power. The extra solder will act as a barrier to prevent oxides from building directly on the tip of your iron. Your tips will last *years if not longer *using this technique.

## Technical Information

### Soldering philosophy

A simple philosophy can be compressed into this phrase: *touch and go*.

This has a straightforward meaning-- you only want to hold the soldering iron in place for as little time as necessary. Your temperature should be hot enough to enable quick work, but not too hot to instantly burn your work area. The longer you heat a component, the higher chance you have of damaging a component or the board itself.&#x20;

### Physical properties of solder

Solder, in its molten form, is attracted to *heat*. Use this to your advantage! What this means is when you are trying to solder a component, the ideal place for your soldering iron tip is one which contacts both the component *and* the pad on the PCB. By heating both at the same time, you can ensure the molten solder will flow across both and create a solid connection.

### Surface tension

If you've ever done experiments in grade school relating to liquid tension, many of those principles apply to soldering. You may find that in some situations, you can use this to your advantage. As an example, when trying to align nearly microscopic components, you'll find that the molten solder sucks the component perfectly into place on the pad.

In other situations, you may find that this surface tension works against you, requiring more precision to hold a component in place as you solder a connection. Being aware of this phenomenon will go a long way to helping you understand when to use specific techniques.&#x20;

### Necessity of flux

Flux is necessary for soldering; Without it, soldering would not be possible. If you see that a roll of solder is marked as 'rosin core', that indicates there is flux built in to the solder itself. This should not persuade you that additional flux is not necessary. While the flux inside the solder is sufficient for tinning pads and wires, it will quickly burn off and leave you with dull, oxidized joints.&#x20;

Flux helps to create a separation from *oxygen* when soldering. This ensures the molten solder does not have the opportunity to mix with oxygen when it's hardening. Molten solder + oxygen = a cold joint!

By keeping all of these tips in mind when working on your next soldering project, you'll have a much higher chance of success. There are many advanced techniques to learn (not to mention the use of hot air stations and the like), however nailing these fundamentals with a soldering iron is a great first step to completing any modding project!

## Recommended Resources

### Soldering Practice Kits

*   [Kit for beginner level (Through-hole components)](https://www.amazon.com/dp/B0711MHKDZ?tag=hanhelleg-20)

*   [Kit for advanced level (Surface mount components)](https://www.amazon.com/dp/B00VWB8F8K?tag=hanhelleg-20)

### YouTube Playlists

If you are interested in learning more about soldering, or seeing soldering in action in many day-to-day situations, check out some of the YouTube playlists below. They feature complex soldering jobs performed by professionals with years of experience.&#x20;

*   [NorthRidge Fix Repair Videos](https://www.youtube.com/c/NorthridgeFix/videos)

*   [Art of Repair - Microsoldering 101 - Basic Course](https://www.youtube.com/watch?v=M8zhfgiToQ8\&list=PLBw4PoJ3vXec0lvJZ5N8Y5vwvf3Qma3A_)

*   [Art of Repair - Microsoldering 102 - Advanced Course](https://www.youtube.com/watch?v=M8zhfgiToQ8\&list=PLBw4PoJ3vXec0lvJZ5N8Y5vwvf3Qma3A_)

*   [Soldering Crash Course - by Wermy](https://www.youtube.com/watch?v=6rmErwU5E-k)

