title: Blog
post: Configuring Marlin Firmware for the Fabrikator Mini
date: 2016-03-24
comments: true
flattr: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

I’ve recently aquired a [Turnigy Fabrikator Mini V1.5](http://www.hobbyking.com/hobbyking/store/__82020__Fabrikator_Mini_3D_Printer_V1_5_Transparent_EU_230V.html) from HobbyKing. This is a very cheap 3D printer with surprisingly good quality.

Many 3D printers are based on an Arduino with some stepper motor drivers, commonly on a [RAMPS shield](http://reprap.org/wiki/RAMPS_1.4). The Fabrikator Mini is using an [MKS-Base board](http://reprap.org/wiki/MKS_BASE), which is basically an Arduino Mega (with an ATmega2560) and a RAMPS 1.4 shield on a single PCB.

I’ve also got the so-called [RepRapDiscount Full Graphic Smart Controller](http://reprap.org/wiki/RepRapDiscount_Full_Graphic_Smart_Controller), a graphic LCD, a beeper, some buttons to control the menu and an SD-card slot. It does, however, not work out-of-the-box, you need to compile a new firmware to get it to run.

As far as I can tell, the most common and actively developed firmware for these boards is the [Marlin Firmware](https://github.com/MarlinFirmware/Marlin/releases), but there are [many alternatives](http://reprap.org/wiki/List_of_Firmware).

The [YouTuber Chuck Hellebuyck](https://www.youtube.com/channel/UCsdc_0ZTXikARFEn2dRDJhg) offers a pre-configured Marlin Firmware on [his website](http://www.elproducts.com/fabrikator-mini.html), but it seems to be a very old version. That’s why I’ve decided to get the newest Marlin Firmware working on the Fabrikator Mini.

At the time of this writing, [Marlin version 1.1.0-RC3](https://github.com/MarlinFirmware/Marlin/releases/tag/1.1.0-RC3) was the newest available firmware release. Clone the repository and check out the corresponding tag:

<pre class="sh_sh">
git clone https://github.com/MarlinFirmware/Marlin.git
cd Marlin
git checkout 1.1.0-RC3
</pre>

The configuration happens in the files `Marlin/Configuration.h` and `Marlin/Configuration_adv.h`. It’s best to read through the whole file to get to know all available options. I’ve listed the important changes in the following section, including the changes required to get the display and SD card working:

<pre class="sh_cpp">
// Configuration.h
#define MOTHERBOARD BOARD_RAMPS_14_EFB
#define TEMP_SENSOR_0 3
#define HEATER_0_MAXTEMP 230
#define HEATER_1_MAXTEMP 230
#define HEATER_2_MAXTEMP 230
#define HEATER_3_MAXTEMP 230
const bool Y_MIN_ENDSTOP_INVERTING = true;
const bool X_MAX_ENDSTOP_INVERTING = true;
const bool Z_MAX_ENDSTOP_INVERTING = true;
#define Y_HOME_DIR 1
#define X_MAX_POS 80
#define Y_MAX_POS 80
#define Z_MAX_POS 80
#define MANUAL_HOME_POSITIONS
#define MANUAL_Y_HOME_POS 80
#define HOMING_FEEDRATE {10*60, 10*60, 2*60, 0}
#define DEFAULT_AXIS_STEPS_PER_UNIT   {201.01,201.01,6366.88,97.11}
#define DEFAULT_MAX_FEEDRATE          {40, 40, 2, 40}
#define DEFAULT_MAX_ACCELERATION      {200,200,50,2000}
#define DEFAULT_ACCELERATION          300
#define DEFAULT_RETRACT_ACCELERATION  2000
#define DEFAULT_TRAVEL_ACCELERATION   300
#define PLA_PREHEAT_HPB_TEMP 0
#define PLA_PREHEAT_FAN_SPEED 127
#define ABS_PREHEAT_HOTEND_TEMP 200
#define ABS_PREHEAT_HPB_TEMP 0
#define ABS_PREHEAT_FAN_SPEED 127
#define SDSUPPORT
#define ENCODER_PULSES_PER_STEP 4
#define ENCODER_STEPS_PER_MENU_ITEM 1
#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER

// Configuration_adv.h
#define EXTRUDER_0_AUTO_FAN_PIN 9
//#define ENDSTOPS_ONLY_FOR_HOMING // Comment this!
</pre>

With its default firmware, the Fabrikator Mini by default runs the fan as soon as the extruder temperature exceeds 50 degrees Celsius. To get this behavior from the Marlin Firmware, `EXTRUDER_0_AUTO_FAN_PIN` is set to the same value as `FAN_PIN`. This leads to a compile error. To fix this, `FAN_PIN` has to be undefined. This can be achieved by modifying the `pins.h` file corresponding to the mainboard used, in this case `Marlin/pins_RAMPS_13_EFB.h`, adding these lines at the end:

<pre class="sh_cpp">
// Disable normal fan to be able to enable auto fan
#undef FAN_PIN
#define FAN_PIN -1

// Reverse encoder direction
#undef BTN_EN1
#define BTN_EN1 33

#undef BTN_EN2
#define BTN_EN2 31
</pre>

That’s it. You can now open the `Marlin/Marlin.ino` file in the Arduino IDE, select `Arduino Mega 2560` as device and the Fabrikator Mini USB port and hit upload. If this is your first time compiling Marlin with Graphic LCD support, you need to install the `u8glib` from the Arduino IDE library manager.

The following is a git patch for all required changes:

<pre class="sh_diff">
From 284c1d4bdeda82c18477f01f99aada0cbfb10de7 Mon Sep 17 00:00:00 2001
From: Thomas Buck <xythobuz@xythobuz.de>
Date: Fri, 25 Mar 2016 00:04:54 +0100
Subject: [PATCH 1/1] Modified configuration for Turnigy Fabrikator Mini with
 RepRapDiscount Full Graphic Smart Controller support.

---
 Marlin/Configuration.h     | 64 +++++++++++++++++++++++-----------------------
 Marlin/Configuration_adv.h |  4 +--
 Marlin/pins_RAMPS_13_EFB.h |  6 ++++-
 3 files changed, 39 insertions(+), 35 deletions(-)

diff --git a/Marlin/Configuration.h b/Marlin/Configuration.h
index c4fa028..c0411cf 100644
--- a/Marlin/Configuration.h
+++ b/Marlin/Configuration.h
@@ -47,7 +47,7 @@ Here are some standard links for getting your machine calibrated:
 // User-specified version info of this build to display in [Pronterface, etc] terminal window during
 // startup. Implementation of an idea by Prof Braino to inform user that any changes made to this
 // build by the user have been successfully uploaded into firmware.
-#define STRING_CONFIG_H_AUTHOR "(none, default config)" // Who made the changes.
+#define STRING_CONFIG_H_AUTHOR "(xythobuz, FabMin)" // Who made the changes.
 #define SHOW_BOOTSCREEN
 #define STRING_SPLASH_LINE1 SHORT_BUILD_VERSION // will be shown during bootup in line 1
 //#define STRING_SPLASH_LINE2 STRING_DISTRIBUTION_DATE // will be shown during bootup in line 2
@@ -62,7 +62,7 @@ Here are some standard links for getting your machine calibrated:
 
 // This determines the communication speed of the printer
 // :[2400,9600,19200,38400,57600,115200,250000]
-#define BAUDRATE 250000
+#define BAUDRATE 115200
 
 // Enable the Bluetooth serial interface on AT90USB devices
 //#define BLUETOOTH
@@ -70,12 +70,12 @@ Here are some standard links for getting your machine calibrated:
 // The following define selects which electronics board you have.
 // Please choose the name from boards.h that matches your setup
 #ifndef MOTHERBOARD
-  #define MOTHERBOARD BOARD_RAMPS_13_EFB
+  #define MOTHERBOARD BOARD_RAMPS_14_EFB
 #endif
 
 // Optional custom name for your RepStrap or other custom machine
 // Displayed in the LCD "Ready" message
-//#define CUSTOM_MACHINE_NAME "3D Printer"
+#define CUSTOM_MACHINE_NAME "Fabrikator Mini"
 
 // Define this to set a unique identifier for this printer, (Used by some programs to differentiate between machines)
 // You can use an online service to generate a random UUID. (eg http://www.uuidgenerator.net/version4)
@@ -145,7 +145,7 @@ Here are some standard links for getting your machine calibrated:
 //#define DUMMY_THERMISTOR_998_VALUE 25
 //#define DUMMY_THERMISTOR_999_VALUE 100
 // :{ '0': "Not used", '4': "10k !! do not use for a hotend. Bad resolution at high temp. !!", '1': "100k / 4.7k - EPCOS", '51': "100k / 1k - EPCOS", '6': "100k / 4.7k EPCOS - Not as accurate as Table 1", '5': "100K / 4.7k - ATC Semitec 104GT-2 (Used in ParCan & J-Head)", '7': "100k / 4.7k Honeywell 135-104LAG-J01", '71': "100k / 4.7k Honeywell 135-104LAF-J01", '8': "100k / 4.7k 0603 SMD Vishay NTCS0603E3104FXT", '9': "100k / 4.7k GE Sensing AL03006-58.2K-97-G1", '10': "100k / 4.7k RS 198-961", '11': "100k / 4.7k beta 3950 1%", '12': "100k / 4.7k 0603 SMD Vishay NTCS0603E3104FXT (calibrated for Makibox hot bed)", '13': "100k Hisens 3950  1% up to 300°C for hotend 'Simple ONE ' & hotend 'All In ONE'", '60': "100k Maker's Tool Works Kapton Bed Thermistor beta=3950", '55': "100k / 1k - ATC Semitec 104GT-2 (Used in ParCan & J-Head)", '2': "200k / 4.7k - ATC Semitec 204GT-2", '52': "200k / 1k - ATC Semitec 204GT-2", '-2': "Thermocouple + MAX6675 (only for sensor 0)", '-1': "Thermocouple + AD595", '3': "Mendel-parts / 4.7k", '1047': "Pt1000 / 4.7k", '1010': "Pt1000 / 1k (non standard)", '20': "PT100 (Ultimainboard V2.x)", '147': "Pt100 / 4.7k", '110': "Pt100 / 1k (non-standard)", '998': "Dummy 1", '999': "Dummy 2" }
-#define TEMP_SENSOR_0 1
+#define TEMP_SENSOR_0 3
 #define TEMP_SENSOR_1 0
 #define TEMP_SENSOR_2 0
 #define TEMP_SENSOR_3 0
@@ -172,10 +172,10 @@ Here are some standard links for getting your machine calibrated:
 // When temperature exceeds max temp, your heater will be switched off.
 // This feature exists to protect your hotend from overheating accidentally, but *NOT* from thermistor short/failure!
 // You should use MINTEMP for thermistor short/failure protection.
-#define HEATER_0_MAXTEMP 275
-#define HEATER_1_MAXTEMP 275
-#define HEATER_2_MAXTEMP 275
-#define HEATER_3_MAXTEMP 275
+#define HEATER_0_MAXTEMP 230
+#define HEATER_1_MAXTEMP 230
+#define HEATER_2_MAXTEMP 230
+#define HEATER_3_MAXTEMP 230
 #define BED_MAXTEMP 150
 
 // If your bed has low resistance e.g. .6 ohm and throws the fuse you can duty cycle it to reduce the
@@ -332,11 +332,11 @@ Here are some standard links for getting your machine calibrated:
 
 // Mechanical endstop with COM to ground and NC to Signal uses "false" here (most common setup).
 const bool X_MIN_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
-const bool Y_MIN_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
+const bool Y_MIN_ENDSTOP_INVERTING = true; // set to true to invert the logic of the endstop.
 const bool Z_MIN_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
-const bool X_MAX_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
+const bool X_MAX_ENDSTOP_INVERTING = true; // set to true to invert the logic of the endstop.
 const bool Y_MAX_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
-const bool Z_MAX_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
+const bool Z_MAX_ENDSTOP_INVERTING = true; // set to true to invert the logic of the endstop.
 const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the logic of the endstop.
 //#define DISABLE_MAX_ENDSTOPS
 //#define DISABLE_MIN_ENDSTOPS
@@ -386,7 +386,7 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 // Sets direction of endstops when homing; 1=MAX, -1=MIN
 // :[-1,1]
 #define X_HOME_DIR -1
-#define Y_HOME_DIR -1
+#define Y_HOME_DIR 1
 #define Z_HOME_DIR -1
 
 #define min_software_endstops true // If true, axis won't move to coordinates less than HOME_POS.
@@ -398,9 +398,9 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 #define X_MIN_POS 0
 #define Y_MIN_POS 0
 #define Z_MIN_POS 0
-#define X_MAX_POS 200
-#define Y_MAX_POS 200
-#define Z_MAX_POS 200
+#define X_MAX_POS 80
+#define Y_MAX_POS 80
+#define Z_MAX_POS 80
 
 //===========================================================================
 //========================= Filament Runout Sensor ==========================
@@ -565,14 +565,14 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 // @section homing
 
 // The position of the homing switches
-//#define MANUAL_HOME_POSITIONS  // If defined, MANUAL_*_HOME_POS below will be used
+#define MANUAL_HOME_POSITIONS  // If defined, MANUAL_*_HOME_POS below will be used
 //#define BED_CENTER_AT_0_0  // If defined, the center of the bed is at (X=0, Y=0)
 
 // Manual homing switch locations:
 // For deltabots this means top and center of the Cartesian print volume.
 #if ENABLED(MANUAL_HOME_POSITIONS)
   #define MANUAL_X_HOME_POS 0
-  #define MANUAL_Y_HOME_POS 0
+  #define MANUAL_Y_HOME_POS 80
   #define MANUAL_Z_HOME_POS 0
   //#define MANUAL_Z_HOME_POS 402 // For delta: Distance between nozzle and print surface after homing.
 #endif
@@ -583,17 +583,17 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
  * MOVEMENT SETTINGS
  */
 
-#define HOMING_FEEDRATE {50*60, 50*60, 4*60, 0}  // set the homing speeds (mm/min)
+#define HOMING_FEEDRATE {10*60, 10*60, 2*60, 0}  // set the homing speeds (mm/min)
 
 // default settings
 
-#define DEFAULT_AXIS_STEPS_PER_UNIT   {80,80,4000,500}  // default steps per unit for Ultimaker
-#define DEFAULT_MAX_FEEDRATE          {300, 300, 5, 25}    // (mm/sec)
-#define DEFAULT_MAX_ACCELERATION      {3000,3000,100,10000}    // X, Y, Z, E maximum start speed for accelerated moves. E default values are good for Skeinforge 40+, for older versions raise them a lot.
+#define DEFAULT_AXIS_STEPS_PER_UNIT   {201.01,201.01,6366.88,97.11}  // default steps per unit for Ultimaker
+#define DEFAULT_MAX_FEEDRATE          {40, 40, 2, 40}    // (mm/sec)
+#define DEFAULT_MAX_ACCELERATION      {200,200,50,2000}    // X, Y, Z, E maximum start speed for accelerated moves. E default values are good for Skeinforge 40+, for older versions raise them a lot.
 
-#define DEFAULT_ACCELERATION          3000    // X, Y, Z and E acceleration in mm/s^2 for printing moves
-#define DEFAULT_RETRACT_ACCELERATION  3000    // E acceleration in mm/s^2 for retracts
-#define DEFAULT_TRAVEL_ACCELERATION   3000    // X, Y, Z acceleration in mm/s^2 for travel (non printing) moves
+#define DEFAULT_ACCELERATION          300    // X, Y, Z and E acceleration in mm/s^2 for printing moves
+#define DEFAULT_RETRACT_ACCELERATION  2000    // E acceleration in mm/s^2 for retracts
+#define DEFAULT_TRAVEL_ACCELERATION   300    // X, Y, Z acceleration in mm/s^2 for travel (non printing) moves
 
 // The speed change that does not require acceleration (i.e. the software might assume it can be done instantaneously)
 #define DEFAULT_XYJERK                20.0    // (mm/sec)
@@ -641,12 +641,12 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 
 // Preheat Constants
 #define PLA_PREHEAT_HOTEND_TEMP 180
-#define PLA_PREHEAT_HPB_TEMP 70
-#define PLA_PREHEAT_FAN_SPEED 0   // Insert Value between 0 and 255
+#define PLA_PREHEAT_HPB_TEMP 0
+#define PLA_PREHEAT_FAN_SPEED 127   // Insert Value between 0 and 255
 
-#define ABS_PREHEAT_HOTEND_TEMP 240
-#define ABS_PREHEAT_HPB_TEMP 110
-#define ABS_PREHEAT_FAN_SPEED 0   // Insert Value between 0 and 255
+#define ABS_PREHEAT_HOTEND_TEMP 200
+#define ABS_PREHEAT_HPB_TEMP 0
+#define ABS_PREHEAT_FAN_SPEED 127   // Insert Value between 0 and 255
 
 //==============================LCD and SD support=============================
 // @section lcd
@@ -665,7 +665,7 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 
 //#define ULTRA_LCD  //general LCD support, also 16x2
 //#define DOGLCD  // Support for SPI LCD 128x64 (Controller ST7565R graphic Display Family)
-//#define SDSUPPORT // Enable SD Card Support in Hardware Console
+#define SDSUPPORT // Enable SD Card Support in Hardware Console
 // Changed behaviour! If you need SDSUPPORT uncomment it!
 //#define SDSLOW // Use slower SD transfer mode (not normally needed - uncomment if you're getting volume init error)
 //#define SDEXTRASLOW // Use even slower SD transfer mode (not normally needed - uncomment if you're getting volume init error)
@@ -710,7 +710,7 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 // http://reprap.org/wiki/RepRapDiscount_Full_Graphic_Smart_Controller
 //
 // ==> REMEMBER TO INSTALL U8glib to your ARDUINO library folder: http://code.google.com/p/u8glib/wiki/u8glib
-//#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER
+#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER
 
 // The RepRapWorld REPRAPWORLD_KEYPAD v1.1
 // http://reprapworld.com/?products_details&products_id=202&cPath=1591_1626
diff --git a/Marlin/Configuration_adv.h b/Marlin/Configuration_adv.h
index 51141fc..41d61d2 100644
--- a/Marlin/Configuration_adv.h
+++ b/Marlin/Configuration_adv.h
@@ -107,7 +107,7 @@
 // extruder temperature is above/below EXTRUDER_AUTO_FAN_TEMPERATURE.
 // Multiple extruders can be assigned to the same pin in which case
 // the fan will turn on when any selected extruder is above the threshold.
-#define EXTRUDER_0_AUTO_FAN_PIN -1
+#define EXTRUDER_0_AUTO_FAN_PIN 9
 #define EXTRUDER_1_AUTO_FAN_PIN -1
 #define EXTRUDER_2_AUTO_FAN_PIN -1
 #define EXTRUDER_3_AUTO_FAN_PIN -1
@@ -121,7 +121,7 @@
 
 // @section homing
 
-#define ENDSTOPS_ONLY_FOR_HOMING // If defined the endstops will only be used for homing
+//#define ENDSTOPS_ONLY_FOR_HOMING // If defined the endstops will only be used for homing
 
 // @section extras
 
diff --git a/Marlin/pins_RAMPS_13_EFB.h b/Marlin/pins_RAMPS_13_EFB.h
index c75acd8..aa43d90 100644
--- a/Marlin/pins_RAMPS_13_EFB.h
+++ b/Marlin/pins_RAMPS_13_EFB.h
@@ -6,4 +6,8 @@
 
 #define IS_RAMPS_EFB
 
-#include "pins_RAMPS_13.h"
\ No newline at end of file
+#include "pins_RAMPS_13.h"
+
+#undef FAN_PIN
+#define FAN_PIN -1
+
-- 
2.7.2
</pre>

<pre class="sh_diff">
From 6a5672200c4246a92abe34e7efa8ab3ec52861a8 Mon Sep 17 00:00:00 2001
From: Thomas Buck <xythobuz@xythobuz.de>
Date: Sat, 26 Mar 2016 18:51:30 +0100
Subject: [PATCH 1/1] Slightly improved Fabrikator Mini Configuration.

---
 Marlin/Configuration.h     | 4 ++--
 Marlin/pins_RAMPS_13_EFB.h | 8 ++++++++
 2 files changed, 10 insertions(+), 2 deletions(-)

diff --git a/Marlin/Configuration.h b/Marlin/Configuration.h
index c0411cf..507f36e 100644
--- a/Marlin/Configuration.h
+++ b/Marlin/Configuration.h
@@ -670,8 +670,8 @@ const bool Z_MIN_PROBE_ENDSTOP_INVERTING = false; // set to true to invert the l
 //#define SDSLOW // Use slower SD transfer mode (not normally needed - uncomment if you're getting volume init error)
 //#define SDEXTRASLOW // Use even slower SD transfer mode (not normally needed - uncomment if you're getting volume init error)
 //#define SD_CHECK_AND_RETRY // Use CRC checks and retries on the SD communication
-//#define ENCODER_PULSES_PER_STEP 1 // Increase if you have a high resolution encoder
-//#define ENCODER_STEPS_PER_MENU_ITEM 5 // Set according to ENCODER_PULSES_PER_STEP or your liking
+#define ENCODER_PULSES_PER_STEP 4 // Increase if you have a high resolution encoder
+#define ENCODER_STEPS_PER_MENU_ITEM 1 // Set according to ENCODER_PULSES_PER_STEP or your liking
 //#define ULTIMAKERCONTROLLER //as available from the Ultimaker online store.
 //#define ULTIPANEL  //the UltiPanel as on Thingiverse
 //#define SPEAKER // The sound device is a speaker - not a buzzer. A buzzer resonates with his own frequency.
diff --git a/Marlin/pins_RAMPS_13_EFB.h b/Marlin/pins_RAMPS_13_EFB.h
index aa43d90..aec7aa0 100644
--- a/Marlin/pins_RAMPS_13_EFB.h
+++ b/Marlin/pins_RAMPS_13_EFB.h
@@ -8,6 +8,14 @@
 
 #include "pins_RAMPS_13.h"
 
+// Disable normal fan to be able to enable auto fan
 #undef FAN_PIN
 #define FAN_PIN -1
 
+// Reverse encoder direction
+#undef BTN_EN1
+#define BTN_EN1 33
+
+#undef BTN_EN2
+#define BTN_EN2 31
+
-- 
2.7.2
</pre>

