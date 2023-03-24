⚠️ Now found under the Eupnea umbrella complete with modern SOF UCMs
> https://github.com/eupnea-linux/audio-scripts
--------
<p align="center">
  <b>UCM Files from ChromeOS Overlays for modern Chromebooks</b>
<br>
<br>
  SOF/KBL/APL/GLK/SKL
<br>
<br>
https://chromium.googlesource.com/chromiumos/overlays/board-overlays/+/refs/heads/main/
</p>

The `original` directory contains original UCMs pulled from ChromeOS Board Overlays. Everything else contains handcrafted UCMs optimized for mainline Linux distribtions.

Some notes:
* Legacy Audio drivers
  * These are very important to get your Chromebook's audio working, given that you have the correct kernel configuration and topology
* SOF
  * UCM Files might be helpful for getting headphone jacks and microphones working

These UCM files are directly pulled from ChromeOS's overlays, but they are somewhat disorganized since Google didn't standardize their directory layout.
