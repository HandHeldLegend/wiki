---
title: Electrolytic Re-Cap Guide
slug: X0MD-electrolytic-re-cap-guide
description: Learn how to safely replace surface mount electrolytic capacitors with this comprehensive reference guide. Discover essential safety precautions, video tutorials, and a list of necessary tools. Follow step-by-step instructions for removing and replacing s
createdAt: Fri Feb 04 2022 21:00:39 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Dec 07 2023 19:09:44 GMT+0000 (Coordinated Universal Time)
---

This is a multi-purpose reference guide for replacing surface mount electrolytic capacitors.
Please exercise safety when working with electrolytic capacitors. Applying too much heat can cause these components to **explode. Always wear eye protection and hand protection when performing this type of work!**

:::hint{type="info"}
Hand Held Legend earns commissions for Amazon purchases made through links in this post.
:::

## Video Guide

<https://www.youtube.com/watch?v=Eg8WZZAjilI>

## Required Tools

*   [Temperature controlled soldering iron](https://www.amazon.com/dp/B00C2BHTBI?tag=hanhelleg-20)

*   [PCB Holder](https://www.amazon.com/dp/B09B73XL33?tag=hanhelleg-20)

*   [Nitrile work gloves](https://www.amazon.com/dp/B074XCXVCM?tag=hanhelleg-20)

*   [Eye Protection](https://www.amazon.com/dp/B00FA4RB12?tag=hanhelleg-20)

*   [Brass sponge](https://www.amazon.com/dp/B08FQBS97L?tag=hanhelleg-20)

*   [Leaded solder](https://www.amazon.com/dp/B075WBDYZZ?tag=hanhelleg-20)

*   [Solder flux (paste or gel)](https://www.amazon.com/dp/B07JYLV381?tag=hanhelleg-20)

*   [Solder wick/braid](https://www.amazon.com/dp/B0195UVWJ8?tag=hanhelleg-20)

*   [99% isopropyl alcohol](https://www.amazon.com/dp/B08JZJ5QV2?tag=hanhelleg-20)

*   [Cotton swabs](https://www.amazon.com/dp/B09498GV6R?tag=hanhelleg-20)

*   [Fume extractor or open window](https://www.amazon.com/dp/B07VWDN29F?tag=hanhelleg-20)

*   [Flush cutters](https://www.amazon.com/dp/B00FZPDG1K?tag=hanhelleg-20)

*   [Tweezers](https://www.amazon.com/dp/B00BAYWOFY?tag=hanhelleg-20)

![](../../assets/moosp60cDJvScHIJevh6W_mpc-hc64iegjcvc7py.jpg)

## Starting Out

This guide assumes that you have a solid grasp on all things soldering. [If you are just starting out, be sure to check out our introductory guide linked here!](https://wiki.handheldlegend.com/soldering-iron-guide)

In this guide, I'll be using a curved soldering tip. With practice and trying different iron tips, you'll likely develop a preference one way or another.

![The curve!](../../assets/N7f2yto7EhukKIT3HXfH2_mpc-hc64f856xg58vu.jpg)

### Note existing placement

Before starting, take a picture of the existing capacitor placement. When you are replacing many capacitors, this can be a useful guide to remember which caps go where, as well as which values each capacitor should be.&#x20;

![Cameraception](../../assets/WQ3J2fsESK7c_INPhdplx_mpc-hc64jok4izbtg5.jpg)

As a rule of thumb, replacement capacitors should match or slightly exceed the original capacitance value (Marked as uF or microfarats), and should match or exceed the original voltage rating.&#x20;
*As an example, if replacing a 200uF 12v capacitor, a 220uF 24v capacitor would substitute just fine in most circumstances.*

### Tin existing connections

Add flux to both exposed connections on either side of the capacitor. If you are removing a through-hole capacitor, perform this step on the connections for the capacitor on the underside of the board.

Use your soldering iron to add leaded solder to each capacitor leg/connection. Adding in leaded solder will cause the original unleaded solder to mix chemistries with the fresh material, resulting in a lower melting temperature. This ensures an easier removal with a lesser risk of ripped pads or burning.

![Through-hole style capacitor](../../assets/mapEw_issOCF5IxAaS1wy_mpc-hc64nzcahnzjfi.jpg)

![Surface mount style capacitor](../../assets/jhdAWFycWjn3Ek3y3-Soa_mpc-hc645ac9mekcxw.jpg)

If you are removing a surface mount capacitor, [see section A. ](https://wiki.handheldlegend.com/electrolytic-re-cap-guide#q2-a-surface-mount-capacitors)
If you are removing a through-hole capaciator, [see section B.](https://wiki.handheldlegend.com/electrolytic-re-cap-guide#km-b-through-hole-capacitors)

## A) Surface Mount Capacitors

### Heat and lift

Heat one leg of the capacitor and gently lift up. The goal is not to pull the capacitor off, but to simply raise the leg up off the board. at this point it may not be completely desoldered, which is okay!

:::hint{type="warning"}
Some electrolytic caps may have adhesive underneath. Use extra precaution when removing these components.

![](../../assets/l-Ujd6gsOmbuezWqyuTY__image.png)
:::

![Firmly grasp it in your... tweezers!](../../assets/oOcli3l9wtBCrzbRevJvT_mpc-hc64qdwwtflobv.jpg)

**Repeat **the same step on the other leg. You will repeat this process going back and forth until the capacitor is fully removed.&#x20;

![Almost there...](../../assets/t1u1FKlpWXmK6CDrxFbCL_mpc-hc64ceqj9g0tgx.jpg)

![Capacitor removed!](../../assets/xcbGREO2U29C5e_FefNqH_mpc-hc64gfe5a17l3d.jpg)

### Clean pads

Clean off any flux residue or burnt flux using cotton swaps and IPA.&#x20;

Cut a small strip of your solder braid/wick using your flush cutters. Apply fresh flux to each of the capacitor pads. Hold the solder braid/wick over the pad using your tweezers.

Apply heat with your soldering iron to the top of the solder braid. Avoid scraping the solder wick against the pad as this can result in a torn/lifted pad. It is advised to only press straight down, or gently glide the wick across the pads until all solder is absorbed into the wick.&#x20;

![](../../assets/5Q1I1h8lUmkOaGaod_rUJ_mpc-hc644wwuzp3zdl.jpg)

Once more, clean any excess flux residue or burnt flux using cotton swabs and IPA.

### Align component

Apply fresh flux to each capacitor pad.

Apply fresh, leaded solder to **only **one of the pads.&#x20;

Paying attention to the correct orientation of the capacitor **(use your photo reference from earlier!)**, heat the pad with the fresh solder and slide the capacitor into place. Do not mind precise placement at this step as we can align this more carefully in the next step.

![Press gently to ensure a nice fit](../../assets/eup1vokHxw-JidGi5CTUf_mpc-hc64r56swfpio0.jpg)

Release the iron and let the solder cool. Observe the placement of the capacitor. If the component requires adjustment, heat the one joint and move the component as needed. Hold the component in place as you release the heat and let the solder cool.

### Finalize capacitor install

Apply fresh leaded solder to the other pad. Do your best to heat both the capacitor leg and the pad at the same time to ensure a proper connection. This should be done quickly to avoid heating the capacitor excessively.

Clean any flux using cotton swabs and IPA.

## B) Through-Hole Capacitors

### Grab and flip

Grab the capacitor you are removing and flip the board over to locate the solder connections you tinned earlier on the rear side of the PCB. Apply flux to the capacitor leg solder points. **Gloves and eye protection are a necessity here!**

### Heat and remove

The goal now is to heat both joints of the capacitor at once while applying a gentle downward force on the capacitor in your grip.  Your choice in soldering iron tip will make this step of the process either easier or more difficult. For larger capacitors you may need to go back and forth between both connections to fully remove the capacitor.

![](../../assets/ASjWqRaMmXlm7r8nD9R13_mpc-hc64axfrodt5pg.jpg)

### Clean vias

Cut a small strip of your solder braid/wick using your flush cutters. Apply fresh flux to each of the capacitor vias (the holes where the capacitor legs were connected). This step will be very difficult without any flux! Hold the solder braid/wick over the pad using your tweezers.

Apply heat with your soldering iron to the top of the solder braid. Avoid scraping the solder wick against the via. It is advised to only press straight down, or gently glide the wick across the vias until all solder is absorbed into the wick. You should be able to clearly see the hole through the via at this point!

![](../../assets/h8NYiBznUi8Gu3RWRb96R_mpc-hc64cxq2aq84cf.jpg)

![](../../assets/AwnyEWjSZWY8pQr2wKFAm_dsc03686.JPG)

Once more, clean any excess flux residue or burnt flux using cotton swabs and IPA.

### Thread capacitor and solder

Thread your new capacitors legs through the now-clean vias. Ensure the capacitor orientation is correct. **(Use your photos from earlier to double check the orientation!). **Bend the legs at an angle to hold the capacitor in place while you solder.

Flip the board over and apply flux to the base of the legs where they stick out of the PCB. Heat the via and the leg simultaneously as you introduce some fresh solder to the connection.&#x20;

![](../../assets/WD_aBOq5XA1C0lkBXJbqy_mpc-hc64a6pqbuvalv.jpg)

After ensuring the connection looks great, use your flush cutters to trim any excess length of the capacitor legs. Clean the connections once more with IPA and cotton swabs.

![](../../assets/1Y9tjrFipMSOEQPLsOsh9_mpc-hc643rgiswncmu.jpg)

## Completion

Repeat these steps for any electrolytic caps you need to replace!&#x20;

![A beautiful, new capacitor](../../assets/Uw25lONKQZW3gHQOVzflj_mpc-hc64ikhqrsta2j.jpg)



