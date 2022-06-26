title: OpenChrono
description: Airsoft Chronograph and Tracer Unit made with Arduino and 3D Printing
parent: projects
git: https://git.xythobuz.de/thomas/OpenChrono
github: https://github.com/xythobuz/OpenChrono
date: 2022-06-26
comments: true
---

Over the past years I've been kinda getting into gas-driven Airsoft guns.
They are interesting from a technical perspective and they are fun toys, as well! 😊

Of course it didn't take much time for me to get some ideas on how to combine this with my other interests.
So I decided to build a chronograph that can measure the speed and energy of BBs shot out of an Airsoft gun.
Two infrared light-barriers detect when a BB passes so an Arduino can measure the speed and display it on an OLED display.

The project was great fun.
It combines different aspects of making, like 3D printing, electronics, low-level microcontroller code and shooting stuff! 🤣

<!--%
lightgallery([
    [ "img/chrono_m11.jpg", "OpenChrono on M11 Airsoft gun" ],
    [ "img/chrono_m11_measurement_4.jpg", "Graph of first M11 magazine" ],
    [ "img/chrono_complete_1.jpg", "Front view of completed unit" ],
    [ "img/chrono_complete_2.jpg", "Back view of completed unit" ],
    [ "img/chrono_complete_3.jpg", "Top view of unit without adapter" ],
])
%-->

The housing for OpenChrono is 3D printed and was designed in OpenSCAD.

<!--%
lightgallery([
    [ "img/openchrono_open.png", "Inside view of 3D model" ],
    [ "img/openchrono_closed.png", "Assembled 3D model" ],
    [ "img/openchrono_lipo.png", "LiPo compartment in 3D model" ],
])
%-->

As usual the project is released as free and open-source software / hardware.
You can find everything you need to build it yourself in [the git repository](https://git.xythobuz.de/thomas/OpenChrono)!

### Table Of Contents

 * [Prototype](openchrono.html#prototype)
 * [Mounting Options](openchrono.html#mounting_options)
 * [Test Results](openchrono.html#test_results)
 * [Build Guide](openchrono.html#build_guide)
 * [Firmware](openchrono.html#firmware)
 * [Possible Future Improvements](openchrono.html#possible_future_improvements)
 * [Potential Other Uses](openchrono.html#potential_other_uses)
 * [Links](openchrono.html#links)
 * [License](openchrono.html#license)
 * [More Pictures](openchrono.html#more_pictures)

## Prototype
<a class="anchor" name="prototype"></a>

Because the optical sensing is dependent on environment conditions I decided to not do any breadboard prototyping and immediately went ahead and designed a case to test with.
In this initial attempt I used an Arduino Nano, an SSD1306 128x64 OLED LCD and an AA-battery holder, all of which I still had left from other projects.
For the IR phototransistor and LED I had to order some parts on eBay.
This got me the [SFH 309 FA-5](https://www.osram.com/ecat/Radial%20T1%20SFH%20309%20FA/com/en/class_pim_web_catalog_103489/prd_pim_device_2219658/) as well as some no-name 940nm IR LEDs.

<!--%
lightgallery([
    [ "img/chrono_proto_1.jpg", "First Prototype and some notes" ],
    [ "img/chrono_proto_2.jpg", "First Prototype (sensors missing)" ],
    [ "img/chrono_proto_3.jpg", "First Prototype, front" ],
    [ "img/chrono_proto_4.jpg", "First Prototype, back" ],
])
%-->

The circuit to connect the phototransistors to the Arduino is pretty simple.
You can find [details here](https://www.electronics-notes.com/articles/electronic_components/transistor/phototransistor-circuits-applications.php).
Signal processing with the Arduino is quick and easy when we have a binary signal available from the sensors, so the phototransistors are used in switch-mode.
To achieve this, proper resistor values need to be selected.
The current passed by the transistors is dependent on the amount of light hitting it, which is difficult for me to calculate, so I determined the proper values experimentally.

<!--%
lightgallery([
    [ "img/chrono_proto_5.jpg", "Prototype with potis" ],
    [ "img/chrono_proto_6.jpg", "Potis and dispaly with data" ],
    [ "img/chrono_proto_7.jpg", "Batteries and potis" ],
    [ "img/chrono_proto_8.jpg", "Scope measurement setup" ],
    [ "img/chrono_proto_9.jpg", "Closer look at phototransistor" ],
    [ "img/chrono_scope.bmp", "Scope view of falling BB" ],
])
%-->

To do this I added external potis outside the case instead of resistors.
You can also see a scope screenshot of both sensors triggering with a BB falling through the device.

The resistor value for the IR LEDs needs to be low enough that the transistors properly switch to a low-value when the light beam is uninterrupted.
This was the case for me at around 50Ω to 100Ω, depending on the supply voltage.
I think it makes sense to drive the LEDs at their current limit, so ~20mA.

Also the pull-up resistors for the transistors need their value to be low enough to quickly drive the signal to near supply voltage when the BB interrupts the light beam.
A value of 1kΩ seems to work well there.

## Mounting Options
<a class="anchor" name="mounting_options"></a>

Unfortunately the OpenChrono IR photo-sensing is a bit constrained in regards to the path of the BB.
The sensors are only 3mm wide, and the BBs are 6mm wide commonly.
So there can not be much deviation of the position of the BB in the light beam, otherwise the beam would not be fully interrupted and the speed measurement can not work.
So we can not just add a big hole in the front of the unit which the user shoots through free-hand, like with standard commercial chronographs.
We need to make sure the gun barrel is centered well in line with the sensor axis.

I already did some experiments in the past with [3D-printed silencer imitations](https://www.printables.com/model/230609-asg-m11-silencer-handgrip) for airsoft use.
So printing matching threaded adapters was not completely new to me.

<!--%
lightgallery([
    [ "img/airsoft_silencers.jpg", "Silencers and adapters I printed in the past" ],
])
%-->

In my first prototype I printed a matching thread into the body of the device itself, split into two halves.
This was not a great idea, when screwing both halves back together the threads did not align well enough to screw something in the top.

So I slightly re-designed it, making the threaded adapter plate a separate part that screws onto the body of the device.
In this way it can also more easily be fitted to different guns.
For my M11 I had to also add an extension plate because it has some length of barrel sticking out past the threaded part.

<!--%
lightgallery([
    [ "img/chrono_threads_m14.jpg", "Adapter for default 14mm thread" ],
    [ "img/chrono_threads_mac11.jpg", "Threaded adapter for Mac11" ],
])
%-->

The 3D models are made using the [OpenSCAD threads library by Dan Kirshner](https://dkprojects.net/openscad-threads/).

<!--%
lightgallery([
    [ "img/openchrono_m14.png", "Adapter for default 14mm thread" ],
    [ "img/openchrono_m11.png", "Threaded adapter for Mac11" ],
    [ "img/openchrono_1911.png", "Threaded adapter for 1911" ],
])
%-->

## Test Results
<a class="anchor" name="test_results"></a>

Attaching the whole unit to a airsoft gun barrel turned out to be a bit tricky.

The first gun I wanted to test with is a full-metal TM 1911 clone with a gas blowback system.
The repetition imparts a big impulse on any barrel attachment, big enough to break my self-made silencer adapters in the past after a single-digit number of shots.
Of course OpenChrono is much heavier than a plastic silencer imitation, so predictably it broke after only three test shots, even though I supported the weight with my hand.
Additionally the impulse in combination with the inertia of the AA batteries caused the supply voltage to cut out in the moment of shooting.
So no usable measurements could be obtained.

<!--%
lightgallery([
    [ "img/chrono_threads_1911.jpg", "Broken threaded adapter for 1911" ],
])
%-->

For the second test run I tried to use a non-blowback ASG Ingram M11 Co2 gun.
Besides some unrelated problems with the magazines it worked relatively well.
Even without blowback the impulse on firing is still big enough to cut out the AA battery power.
But this time it was easily possible to hold the batteries in place by hand while shooting, avoiding the problem.
The measurement results looked mostly realistic, ranging from nearly zero with an empty gas capsule, up to ~1.5J with a full one, which roughly matches the specs of the gun (which hopefully was to be expected, as it is completely unmodified).
With one magazine I got some faulty readings, counting a single shot multiple times with ridiculously high velocities.
I suspect this was caused by oil droplets from a maintenance capsule that was in the magazine previously.
But because of the aforementioned magazine problems I was only able to shoot about 20 BBs for this test.

<!--%
lightgallery([
    [ "img/chrono_m11.jpg", "OpenChrono on M11 Airsoft gun" ],
    [ "img/chrono_m11_test.mp4", "video/mp4", "img/chrono_m11_test_thumb.png", "img/chrono_m11_test_poster.png", "Video of magazine shot through M11" ],
])
%-->

To be able to properly measure anything I next redesigned the hardware to use a soldered-in LiPo battery that won't disconnect on firing.
For the next test with the M11 I went through about 200 shots or more without seeing a single false measurement.

<!--%
lightgallery([
    [ "img/chrono_m11_measurement_1.jpg", "Data for last shot of first magazine" ],
    [ "img/chrono_m11_measurement_4.jpg", "Graph of first magazine" ],
    [ "img/chrono_m11_measurement_7.jpg", "Graph of later magazine" ],
    [ "img/chrono_m11_measurement_23.jpg", "Graph of later magazine" ],
])
%-->

The results are interesting, you can see the behaviour of the Co2 capsule well.
With the first shots with a fresh capsule the speed is about 105m/s, which is 1.39J at 0.25g BB weight.
The speed then reduces with each shot and goes back up again when waiting long enough between shots, as the capsule slowly heats up again.
With the last couple of shots I took only 0.23J were left.

I also want to continue testing with the blowback 1911.
But I first need to get a metal threaded adapter that can withstand the forces.
A female printed thread should do much better than my first test run.

## Build Guide
<a class="anchor" name="build_guide"></a>

Also take a look at [the "Hardware" section of the README.md](https://git.xythobuz.de/thomas/OpenChrono/src/branch/master/README.md#hardware).
You can find detailed parts lists, schematic and wiring plan there as well.

Before starting the build you need to acquire the following parts.

<!--%
tableHelper([ "align-right", "align-right", "align-right monospaced", "align-left" ],
    [ "Description", "Type", "Count", "Link" ], [
        [ "Arduino Nano", "", "1x", "<a href=\"https://store.arduino.cc/products/arduino-nano\">Arduino Store</a>, <a href=\"https://www.aliexpress.com/item/1005002998391675.html\">AliExpress</a>" ],
        [ "LCD 128x64 I2C", "SSD1306 0.96\"", "1x", "<a href=\"https://www.aliexpress.com/item/32638662748.html\">AliExpress</a>, <a href=\"https://www.ebay.de/itm/353351582659\">eBay.de</a>" ],
        [ "Slide Switch", "", "1x", "<a href=\"https://www.aliexpress.com/item/32765155281.html\">AliExpress</a>, <a href=\"https://www.ebay.de/itm/334211625913\">eBay.de</a>" ],
        [ "IR Phototransistor", "<a href=\"https://www.osram.com/ecat/Radial%20T1%20SFH%20309%20FA/com/en/class_pim_web_catalog_103489/prd_pim_device_2219658/\">SFH 309 FA</a>-5", "2x", "<a href=\"https://www.reichelt.de/de/de/fototransistor-npn-730-1120nm-24-tht-3mm-sfh-309-fa-p60553.html\">Reichelt</a>, <a href=\"https://www.ebay.de/itm/353899814039\">eBay.de</a>" ],
        [ "IR LED 3mm", "940nm", "2x", "<a href=\"https://www.aliexpress.com/item/32660252297.html\">AliExpress</a>, <a href=\"https://www.ebay.de/itm/321558979835?var=510446659784\">eBay.de</a>" ],
        [ "LiPo Battery", "600mAh", "1x", "<a href=\"https://www.aliexpress.com/item/1005004340664249.html\">AliExpress</a>, <a href=\"https://www.ebay.de/itm/193560287247\">eBay.de</a>" ],
        [ "Charging Module", "TP4056", "1x", "<a href=\"https://www.aliexpress.com/item/32930640893.html\">AliExpress</a>, <a href=\"https://www.ebay.de/itm/154034193943?var=454147761245\">eBay.de</a>" ],
        [ "Resistor SMD", "4kΩ, 0603", "1x", "<a href=\"https://www.ebay.de/itm/373651719055?var=642713852109\">eBay.de</a>" ],
        [ "Resistor", "1kΩ", "2x", "<a href=\"https://www.ebay.de/itm/352540072577\">eBay.de</a>" ],
        [ "Resistor", "50Ω", "1x", "<a href=\"https://www.ebay.de/itm/372813822157?var=642490601730\">eBay.de</a>" ],
        [ "Screws (Display)", "M2 10mm", "4x", "<a href=\"https://www.ebay.de/itm/261298209327?var=560230293993\">eBay.de</a>" ],
        [ "Screws (Switch)", "M2.5 10mm", "2x", "<a href=\"https://www.ebay.de/itm/261298209327?var=560230293999\">eBay.de</a>" ],
        [ "Screws (Body)", "M3 16mm", "8x", "<a href=\"https://www.ebay.de/itm/261298209327?var=560230294009\">eBay.de</a>" ],
        [ "Screws (Lid)", "M3 <= 6mm", "4x", "<a href=\"https://www.ebay.de/itm/261298209327?var=560230294003\">eBay.de</a>" ],
        [ "Heatmelt Insert", "M3 <= 10mm", "8x", "<a href=\"https://www.ebay.de/itm/184650202586?var=692369947868\">eBay.de</a>" ],
    ]
)
%-->

For the UV tracer option you also need the following parts.

<!--%
tableHelper([ "align-right", "align-right", "align-right monospaced", "align-left" ],
    [ "Description", "Type", "Count", "Link" ], [
        [ "UV LED 3mm", "", "2x", "<a href=\"https://www.ebay.de/itm/373071970513\">eBay.de</a>" ],
        [ "Resistor", "50Ω", "1x", "<a href=\"https://www.ebay.de/itm/372813822157?var=642490601730\">eBay.de</a>" ],
    ]
)
%-->

Next you need to generate the STL files with [OpenSCAD](https://openscad.org/) using [the script in the repository](https://git.xythobuz.de/thomas/OpenChrono/src/branch/master/hardware/openchrono.scad).
You can set `include_uv_leds` to `true` or `false` in there.
At the bottom, comment out the proper parts you need to print.
Besides the `left_half`, you need to select the proper `right_half_xxx` depending on your power source.
For LiPo battery use, also print the `lipo_lid`.
Then select the proper threaded adapter for your gun.
You will most likely need to print either `thread_profile_m14_cw` or `thread_profile_m14_ccw` for standard 14mm diameter, 1mm pitch threads.
Other thread profiles can be added easily.

Print the parts, remove supports and do some sanding as needed.
Then put in the heat-melt inserts.
I recommend using a spare thick soldering iron tip.
Also I put in a small grub screw and place it at the bottom of the insert.
This way, any plastic that gets pushed down will not clog the thread.
Push them in, use a hard flat surface to align them with the printed part, let it cool and remove the grub screw.

<!--%
lightgallery([
    [ "img/chrono_insert_1.jpg", "Heat-melt insert with grub screw" ],
    [ "img/chrono_insert_2.jpg", "Heat-melt insert on soldering iron" ],
    [ "img/chrono_insert_3.jpg", "Putting in heat-melt insert" ],
])
%-->

To connect all the parts I recommend using a thin stranded wire.
I used the cores of an old ethernet cable.
First solder wires with enough length to the OLED display and power switch.
Feed these through the printed `left_half` before screwing on both parts from the outside.

<!--%
lightgallery([
    [ "img/chrono_wiring_4.jpg", "Wiring of power switch" ],
    [ "img/chrono_wiring_5.jpg", "Wiring of OLED display" ],
])
%-->

On the inside of the `left_half` you should next add the IR LEDs and phototransistors (and UV LEDs, if needed).
Pre-bend the wires of the parts to a 90 degree shape that fits the slots in the parts.
If you'd like, add some heat-shrink tubing to insulate agains potential shorts.

Next use a small amount of hotglue to fix the LEDs and transistors into their respective slots.

You need to take care to align the phototransistors and the LEDs properly.
They need to look at each other as straight as possible.
If there is too much deviation, and you maybe also have a resistor that limits the LED current too much, the transistor will not switch properly!

<!--%
lightgallery([
    [ "img/OpenChrono_LiPo_bb.png", "LiPo 'Breadboard' wiring plan" ],
    [ "img/OpenChrono_LiPo_schem.png", "LiPo Schematics" ],
])
%-->

Connect the LEDs in series, as shown on the schematics.
For ease of soldering place the resistor in between the two IR LEDs.
To connect the IR LEDs to the Arduino, feed two wires through their canal in the `left_half` to bring them over to the other side.

For the UV LED option, you can simply route the wires along the existing channels for the IR LED wires.
Only fitting the additional resistor in can be a little bit tricky.

Do the same for the phototransistors.
I recommend connecting both of their Emitters, as well as all the other Ground connections (battery, OLED display, phototransistors, LEDs) together in one spot, wrapping their connection point in heat-shrink tubing.
For the pull-up resistors of the phototransistors, I soldered them on top over the Arduino to the +5V pad, with heat-shrink tubing to prevent any shorts.
I think this is the most space efficient solution.

Also beware to not leave too long dangling wires.
This will make later putting both halves together difficult.

You should be able to build all this with 0.25W THT resistors and everything can fit if you take care to not use up too much space.
If you can I recommend using SMT parts to greatly ease assembly.
But just to make sure it can be done, I used THT parts.

Now everything should be connected to the Arduino.
As the final step for the left half, solder two wires to +5V and GND of the Arduino respectively and leave them dangling for maybe 10mm or more.
This will later connect to the right half.

<!--%
lightgallery([
    [ "img/chrono_wiring_1.jpg", "Wiring below Arduino" ],
    [ "img/chrono_wiring_2.jpg", "Arduino and phototransistors" ],
    [ "img/chrono_wiring_3.jpg", "IR LEDs and Arduino" ],
])
%-->

Next we're going to prepare the right half.

**Beware:** If you use the TP4056 LiPo charger board, they normally come with the charge current set to 1A with a 1.2kΩ resistor on position R3.
You need to put in a higher valued resistor instead, otherwise the small battery will be charged with far too much current and the charger will get very hot.
I recommend 4kΩ or more.
See [this page](https://www.best-microcontroller-projects.com/tp4056.html#TP4056_Current_Programming_Resistor) and [this video](https://www.youtube.com/watch?v=M88e1r8nvYk) for more info.

<!--%
lightgallery([
    [ "img/chrono_lipo_r_1.jpg", "Swapping the current resistor" ],
])
%-->

Next either solder the battery directly to the proper charging board pads, or, if you have it, use the connector that's probably already fitted to your battery, like I did.
Also connect two wires to the OUT+ and OUT- pads, and feed them through the hole next to the charger board hole.
Now first see if the board properly fits into its slot.
If that is the case take it out again, put some dabs of hotglue in the hole, and push the board back in.
You should be able to easily remove hotglue in the USB connector area while it is still warm.
Then secure the board with some more glue on the sides and on top.
This should hold the board firmly in place even when pushing in a USB connector!

<!--%
lightgallery([
    [ "img/chrono_lipo_3.jpg", "LiPo charger prepared" ],
    [ "img/chrono_lipo_6.jpg", "LiPo compartment of device" ],
    [ "img/chrono_lipo_7.jpg", "LiPo battery in device" ],
])
%-->

**Beware:** If you are using the LiPo charger make sure to _always_ keep the power switch in the off position while having a charging USB cable connected.

Turn the right half to the inside and cut the power supply wires to an appropriate length.
Then solder them to the power supply wires of the Arduino, insulating with some heat-shrink tubing.

To flash the firmware onto your Arduino please also take a look at [the "Software" section of the README.md](https://git.xythobuz.de/thomas/OpenChrono/src/branch/master/README.md#software).

**Beware:** _Always_ leave the power switch in the off position when connecting a USB cable to flash the Arduino.

Finally screw both halves together, put in the battery and turn your device on.
Test it by dropping a BB through the device (but beware, depending on your firmware setting this may be too low a speed to measure properly).

<!--%
lightgallery([
    [ "img/chrono_done_1.jpg", "LiPo battery compartment lid" ],
    [ "img/chrono_done_2.jpg", "Front of unit with USB charging port" ],
])
%-->

Attach the threaded adapter for your gun and in turn attach all this to your airsoft gun.
For the first tests, I recommend supporting the weight of the device from below with your hand, depending on how your gun works and if the excess weight may damage the mechanism.
Also be careful for the first test shots!
If for some reason the hole through the device is not perfectly aligned with your gun barrel, the BB may skip off from the side walls and come out of the front in unpredictable directions.
In that case, you will not hit what you are aiming at!
So beware of your environment, wear proper safety gear and start out with a short distance to your bullet stop, increasing only slowly as you are sure everything works as expected.

## Firmware
<a class="anchor" name="firmware"></a>

To achieve high measurement accuracy I used some of the hardware features of the AtMega328p MCU included in standard Arduinos.

To measure the impulses I'm using the two available external interrupts, INT0 and INT1.
They are connected to the phototransistors and usually are on a low level when the LED shines on them as no BB passes through.
When the BB passes the transistor the interrupt pins are pulled high.

So I'm triggering them on rising edges and measure the current time in the interrupt routines and set a flag.

<pre class="sh_cpp">
void interrupt_init() {
    // trigger both on rising edge
    EICRA = (1 << ISC00) | (1 << ISC01);
    EICRA |= (1 << ISC10) | (1 << ISC11);

    // enable interrupts
    EIMSK = (1 << INT0) | (1 << INT1);
}

/*
 * this is supposed to be the "input" sensor,
 * the one that triggers first on firing.
 */
ISR(INT0_vect) {
    time_a = timer_get();
    trigger_a = 1;
}

/*
 * this is supposed to be the "output" sensor,
 * the one that triggers after the other sensor.
 */
ISR(INT1_vect) {
    time_b = timer_get();
    trigger_b = 1;

    // we now need to turn on the UV led
    // and make sure it will only be on shortly!
    timer_start();
    digitalWrite(UV_LED_PIN, HIGH);
}
</pre>

For `timer_get()` and `timer_start()` I'm using another feature of AVR MCUs, their internal Timers.
The 328p has three timers.
Timer0 and Timer2 are 8bit, but Timer0 is already used by the Arduino framework to keep track of the passed milliseconds.
Timer1 is 16bit and can therefore count for the longest time, so I'm using that to measure the speed of the BBs.

To keep the interrupt routines as short and as equal-length as possible, I'm running the Timer1 all the time.
It simply counts from 0x0000 to 0xFFFF and on overflow rolls back to the beginning.
The clock source prescaler determines the maximum and minimum possible measurement speeds.
When the external interrupts fire, they simply record the current value of Timer1.
Later when both have fired and the UI code is not busy, both stored timer values will be used to calculate the time it took for the BB to travel the distance between the measurements.

<pre class="sh_cpp">
static void timer1_init() {
    // normal mode
    TCCR1A = 0;

    // prescaler
#if TIMER_PRESCALER == 1
    TCCR1B = (1 << CS10);
#elif TIMER_PRESCALER == 8
    TCCR1B = (1 << CS11);
#elif TIMER_PRESCALER == 64
    TCCR1B = (1 << CS11) | (1 << CS10);
#elif TIMER_PRESCALER == 256
    TCCR1B = (1 << CS12);
#elif TIMER_PRESCALER == 1024
    TCCR1B = (1 << CS12) | (1 << CS10);
#else
#error Invalid Prescaler for Timer1
#endif
}

uint16_t timer_get() {
    return TCNT1;
}

// ...

void calculate(uint16_t a, uint16_t b) {
    uint16_t ticks = 0;

    if (b >= a) {
        // simple case - just return difference
        ticks = b - a;
    } else {
        // the timer overflowed between measurements!
        int32_t tmp = ((int32_t)b) - ((int32_t)a);
        tmp += 0x10000;
        ticks = (uint16_t)tmp;
    }

    // ...
}
</pre>

From this the speed and (given the BB weight) the energy can be calculated easily.

<pre class="sh_cpp">
double tick_to_metric(uint16_t ticks) {
    // v = d / t
    double period = 1000.0 / ((double)(F_CPU / TIMER_PRESCALER));
    double time = period * (double)ticks;
    double speed = (double)SENSOR_DISTANCE / time;
    return speed;
}

double metric_to_imperial(double speed) {
    // convert m/s to f/s
    speed *= 3.28084;
    return speed;
}

double metric_to_joules(double speed, double mass) {
    // e = 0.5 * m * v^2
    double energy = 0.5 * mass * speed * speed / 1000.0;
    return energy;
}
</pre>

Timer2 is used for the tracer feature, to turn on the UV LEDs only for as long as needed.
This could enable a future improvement where the UV LEDs could be pulsed with a far higher current to achieve more light output.
To pulse the LEDs I'm only connecting the timer to a clock source when the LEDs have been turned on, with an initial value of the timer that determines how long it will take to count up to 0xFF.
Then in the overflow interrupt I'm turning off both the LEDs and the Timer again.

<pre class="sh_cpp">
static void timer2_init() {
    // normal mode, no clock source
    TCCR2A = 0;
    TCCR2B = 0;

    // enable overflow interrupt
    TIMSK2 = (1 << TOIE2);
}

void timer_start() {
    /*
     * the distance between the second IR sensor
     * and the UV LEDs is 7.5mm.
     * Our bullet will travel with a speed of
     * ~10m/s up to ~300m/s approximately.
     * So it will move the 7.5mm in
     * 750us to 25us respectively.
     * So it makes sense to keep the UV LED
     * on for 1ms.
     *
     * We reach exactly 1ms when counting to 250
     * with a prescaler of 64 at 16MHz.
     *
     * If you __really__ want to increase the brightness
     * of the tracer, reduce the pulse length here.
     * Then you can also reduce the UV LED resistor for
     * higher currents, according to the datasheet of
     * your UV LED.
     * Make sure to keep within 40mA the AVR GPIO can provide.
     * Otherwise you need to add a transistor for switching.
     */
    const static uint8_t pulse_length = 250;

    // initial value we count up from
    TCNT2 = 0xFF - pulse_length;

    // prescaler 64
    TCCR2B = (1 << CS22);
}

ISR(TIMER2_OVF_vect) {
    // turn off UV LED
    digitalWrite(UV_LED_PIN, LOW);

    // and also stop timer
    TCCR2B = 0;
}
</pre>

In the main-loop I'm simply updating the LCD to show the measured values.
This is very easy to implement using the great [u8g2 library](https://github.com/olikraus/u8g2).

If you're interested I recommend taking a look at [the code](https://git.xythobuz.de/thomas/OpenChrono/src/branch/master/firmware/OpenChrono).
I think it should be relatively easy to understand and well commented 😅

## Possible Future Improvements
<a class="anchor" name="possible_future_improvements"></a>

As usual I was mostly using parts that I already had.
That explains some strange design decisions, like using cylindrical screws for the battery compartment lid, which honestly look and feel ugly and stand out from the device.

I'm sure it is also possible to make better use of the space inside the device and make wiring much easier that way.

Also the tracer feature has been kind of an afterthought.
I have no real use for it and have not really tested it.
So I'm not sure how well it will work in practice under different conditions.
I also don't think it's realistic to take this bulky device onto a field, but who knows, I'm not really into that.

To be quite honest, I'm happy with the device as it is now.
But I'm always open to feedback and pull requests of course 😉

## Potential Other Uses
<a class="anchor" name="potential_other_uses"></a>

One thing I'd like to talk about is using this device for measuring other things besides Airsoft BBs.
It is definitely feasible to use OpenChrono to measure the speed of air rifle pellets, and this is something I would be interested in as well.
Unfortunately my air rifle does not have a threaded barrel, so attaching the device with proper alignment will be difficult.

Speaking from a measurement perspective, the phototransistors and the Arduino are easily able to measure higher speeds.
500m/s or more should be no problem.
So it is possible to measure much faster projectiles, like real bullets for example.
Beware however about the 3D printed housing.
I'm not sure if it would be able to survive either the pressures involved or the impulse of firing.
This could maybe partly be fixed by adding depressurization holes to the device.
All the hot gases coming out of a real gun will probably also be problematic, both for the plastic and for the optical measurement method.

But all this is not something I can or want to test, and I also do not recommend you do it, either! 👮

## Links
<a class="anchor" name="links"></a>

You can find [all the source code and design files for OpenChrono](https://git.xythobuz.de/thomas/OpenChrono) on my [Gitea instance](https://git.xythobuz.de).
The project is also [mirrored on GitHub](https://github.com/xythobuz/OpenChrono).

If you decide to build it yourself I would be interested in any kind of feedback!

## License
<a class="anchor" name="license"></a>

OpenChrono is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

    Copyright (c) 2022 Thomas Buck <thomas@xythobuz.de>

    OpenChrono is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenChrono is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with OpenChrono.  If not, see <https://www.gnu.org/licenses/>.

## More Pictures
<a class="anchor" name="more_pictures"></a>

Here are some more photographs I didn't use above.

<!--%
lightgallery([
    [ "img/OpenChrono_bb.png", "AA 'Breadboard' wiring plan" ],
    [ "img/OpenChrono_schem.png", "AA Schematics" ],
    [ "img/chrono_lipo_1.jpg", "Battery and charger on their own" ],
    [ "img/chrono_lipo_2.jpg", "Fitting test of charger and LiPo" ],
    [ "img/chrono_lipo_4.jpg", "LiPo charger with cable" ],
    [ "img/chrono_lipo_5.jpg", "Glued-in LiPo charger" ],
    [ "img/chrono_m11_measurement_2.jpg", "Minimum for first magazine" ],
    [ "img/chrono_m11_measurement_3.jpg", "Maximum for first magazine" ],
    [ "img/chrono_m11_measurement_5.jpg", "" ],
    [ "img/chrono_m11_measurement_6.jpg", "" ],
    [ "img/chrono_m11_measurement_8.jpg", "" ],
    [ "img/chrono_m11_measurement_9.jpg", "" ],
    [ "img/chrono_m11_measurement_10.jpg", "" ],
    [ "img/chrono_m11_measurement_11.jpg", "" ],
    [ "img/chrono_m11_measurement_12.jpg", "" ],
    [ "img/chrono_m11_measurement_13.jpg", "" ],
    [ "img/chrono_m11_measurement_14.jpg", "Graph of later magazine" ],
    [ "img/chrono_m11_measurement_15.jpg", "" ],
    [ "img/chrono_m11_measurement_16.jpg", "" ],
    [ "img/chrono_m11_measurement_17.jpg", "" ],
    [ "img/chrono_m11_measurement_18.jpg", "" ],
    [ "img/chrono_m11_measurement_19.jpg", "Graph of later magazine" ],
    [ "img/chrono_m11_measurement_20.jpg", "" ],
    [ "img/chrono_m11_measurement_21.jpg", "" ],
    [ "img/chrono_m11_measurement_22.jpg", "" ],
    [ "img/chrono_m11_measurement_24.jpg", "" ],
    [ "img/chrono_m11_measurement_25.jpg", "" ],
    [ "img/chrono_m11_measurement_26.jpg", "" ],
])
%-->
