// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

const isReduced = window.matchMedia(`(prefers-reduced-motion: reduce)`).matches === true;

// remove static background for non-reduced-motion visitors
// do this at first, to avoid flickering
if (!isReduced) {
    document.body.style.backgroundImage = 'none';
}

var urls = [
    "/camp23/Fisty-sprayed-Stencil_Neonpink.svg",
"/camp23/Mildenberg.svg",
"/camp23/sprayed-23.svg",
];
var imgs = [];
var idx = 0;
var timer_bg = "";
var timer_ray = "";
var timer_shake = "";
var easter_egg_triggered = 0;

// animation timings
const fade_in_t = 50;
const fade_in_step = 0.025;
const fade_out_t = 50;
const fade_out_step = 0.025;
const show_t = 5000;
const hide_t = 1000;
const animate_t = 50;
const wiggle_t = 50;
const base_alpha = 0.25;

function fade_in(element) {
    var op = 0;
    timer_bg = setInterval(function() {
        element.style.opacity = op;
        if (op > 0.99) {
            clearInterval(timer_bg);
            pause();
        }
        op += fade_in_step;
    }, fade_in_t);
}

function fade_out(element) {
    var op = 1;
    timer_bg = setInterval(function() {
        element.style.opacity = op;
        if (op < 0.01) {
            clearInterval(timer_bg);
            next();
        }
        op -= fade_out_step;
    }, fade_out_t);
}

function pause() {
    timer_bg = setInterval(function() {
        clearInterval(timer_bg);
        fade_out(imgs[idx]);
        idx = (idx + 1) % imgs.length;
    }, show_t);
}

function next() {
    timer_bg = setInterval(function() {
        clearInterval(timer_bg);
        fade_in(imgs[idx]);
    }, hide_t);
}

function degToRad(degrees) {
    return (degrees * Math.PI) / 180;
}

function ray(x, y, n, a) {
    var length = canvas.width + canvas.height;
    var width = 5;

    var x1 = Math.cos(degToRad(a - width / 2)) * length;
    var y1 = Math.sin(degToRad(a - width / 2)) * length;
    var x2 = Math.cos(degToRad(a + width / 2)) * length;
    var y2 = Math.sin(degToRad(a + width / 2)) * length;

    ctx.beginPath();
    ctx.moveTo(x * n, y);
    ctx.lineTo((x + x1) * n, y - y1);
    ctx.lineTo((x + x2) * n, y - y2);
    ctx.moveTo(x * n, y);
    ctx.fill();
}

function animation(angle, alpha, rgb) {
    // clear background
    ctx.clearRect(-canvas.width / 2, -canvas.height, canvas.width, canvas.height);

    steps = canvas.height / 100 * 3;
    x_step = -10;
    y_step = 40;
    x_off = canvas.width / 2;
    y_off = (y_step + 1) * steps / 3 * 2;

    for (i = 1; i <= steps; i++) {
        ctx.fillStyle = "rgba(" + rgb + ", " + base_alpha * alpha + ")";

        x = x_off + (x_step * i);
        y = y_off - (y_step * i);

        for (n of [-1, 1]) {
            ray(x, y, n, angle);
        }
    }
}

function animate() {
    var start = Date.now();

    timer_ray = setInterval(function() {
        const millis = Date.now() - start;

        //var angle = millis / 1000 * 360;
        var angle = 45;
        var alpha = 1.0;
        var rgb = "63, 255, 33";

        const min = millis % 60000;
        if (min < 5000) {
            // first 5 seconds of a minute
            // default state
        } else if (min < 8000) {
            // 5sec - 8sec: 3sec
            // move to 180deg
            t = (min - 5000) / 3000;
            angle += (180 - angle) * t;
        } else if (min < 10000) {
            // 8sec - 10sec: 2sec
            // stay at 180deg
            angle = 180;
        } else if (min < 11000) {
            // 10sec - 11sec: 1sec
            // fade out
            t = (min - 10000) / 1000;
            alpha = 1 - t;
            angle = 180;
        } else if (min < 15000) {
            // 10sec - 15sec: 5sec
            // lights off
            alpha = 0;
            angle = 180;
        } else if (min < 16000) {
            // 15sec - 16sec: 1sec
            // fade in
            t = (min - 15000) / 1000;
            alpha = t;
            angle = 180;
        } else if (min < 18000) {
            // 16sec - 18sec: 2sec
            // stay at 180deg
            angle = 180;
        } else if (min < 20000) {
            // 18sec - 20sec: 2sec
            // move to 0deg
            t = (min - 18000) / 2000;
            angle = 180 * (1 - t);
        } else if (min < 25000) {
            // 20sec - 25sec: 5sec
            // stay at 0deg
            angle = 0;
        } else if (min < 26000) {
            // 25sec - 26sec: 1sec
            // fade out
            t = (min - 25000) / 1000;
            alpha = 1 - t;
            angle = 0;
        } else if (min < 30000) {
            // 26sec - 30sec: 4sec
            // lights off
            alpha = 0;
            angle = 0;
        } else if (min < 31000) {
            // 30sec - 31sec: 1sec
            // fade in with move to 10deg
            t = (min - 30000) / 1000;
            alpha = t;
            angle = 10 * t;
        } else if (min < 33000) {
            // 31sec - 33sec: 2sec
            // color change with move to 66deg
            t = (min - 31000) / 2000;
            angle = 10 + (66 - 10) * t;

            r_from = 63;
            g_from = 255;
            b_from = 33;

            r_to = 251;
            g_to = 72;
            b_to = 196;

            r = r_from + (r_to - r_from) * t;
            g = g_from + (g_to - g_from) * t;
            b = b_from + (b_to - b_from) * t;
            rgb = r + ", " + g + ", " + b;
        } else if (min < 35000) {
            // 33sec - 35sec: 2sec
            // stay at 66deg
            angle = 66;
            rgb = "251, 72, 196";
        } else if (min < 36000) {
            // 35sec - 36sec: 1sec
            // move to 90deg
            t = (min - 35000) / 1000;
            angle = 66 + (90 - 66) * t;
            rgb = "251, 72, 196";
        } else if (min < 40000) {
            // 36sec - 40sec: 4sec
            // stay at 90deg
            angle = 90;
            rgb = "251, 72, 196";
        } else if (min < 42000) {
            // 40sec - 42sec: 2sec
            // color change to deep purple
            angle = 90;
            t = (min - 40000) / 2000;

            r_from = 251;
            g_from = 72;
            b_from = 196;

            r_to = 58;
            g_to = 50;
            b_to = 178;

            r = r_from + (r_to - r_from) * t;
            g = g_from + (g_to - g_from) * t;
            b = b_from + (b_to - b_from) * t;
            rgb = r + ", " + g + ", " + b;
        } else if (min < 52000) {
            // 42sec - 52sec: 10sec
            // stay at 90deg
            angle = 90;
            rgb = "58, 50, 178";
        } else if (min < 53000) {
            // 52sec - 53sec: 1sec
            // fade out
            t = (min - 52000) / 1000;
            alpha = 1 - t;
            angle = 90;
            rgb = "58, 50, 178";
        } else if (min < 59000) {
            // rest of the minute
            // lights off
            alpha = 0;
        } else {
            // final second
            // fade in
            t = (min - 59000) / 1000;
            alpha = t;
        }

        animation(angle, alpha, rgb);
    }, animate_t);
}

function disable_animations() {
    // stop all animations
    clearInterval(timer_bg);
    clearInterval(timer_ray);
    clearInterval(timer_shake);

    // enable easter-egg again
    easter_egg_triggered = 0;

    // hide button to stop animations
    btn = document.getElementById("disable_bg_block");
    btn.style.display = "none";

    // clear canvas
    ctx.clearRect(-canvas.width / 2, -canvas.height, canvas.width, canvas.height);

    // hide all background images
    for (img of imgs) {
        img.style.opacity = "0.0";
    }

    // show static background image
    document.body.style.backgroundImage = 'url("/camp23/Fisty-sprayed-Stencil_Neonpink.svg"), url("/camp23/Mildenberg.svg"), url("/camp23/sprayed-23.svg")';
}

function bg() {
    // container for background elements
    div = document.createElement("div");
    div.id = "bg-img";
    document.body.append(div);

    // add static images
    for (url of urls) {
        img = document.createElement("img");
        img.src = url;
        div.append(img);
        imgs.push(img);
    }

    // add canvas for animations
    canvas = document.createElement("canvas");
    ctx = canvas.getContext("2d");
    div.append(canvas);

    // fit to container size
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    //console.log("canvas: " + canvas.width + "x" + canvas.height);

    // set viewport origin of canvas
    ctx.translate(canvas.width / 2, canvas.height);

    // show button to stop animations
    btn = document.getElementById("disable_bg_block");
    btn.style.display = "block";
    link = document.getElementById("disable_bg_link");
    link.onclick = disable_animations;

    // start showing first background image
    fade_in(imgs[idx]);

    // trigger first and future animation steps
    animation();
    animate();
}

function shake(element) {
    shake_n = 0;
    timer_shake = setInterval(function() {
        switch (shake_n++) {
            case 0:
                element.style.marginLeft = "5px";
                break;

            case 1:
                element.style.marginLeft = "-5px";
                break;

            default:
                element.style.marginLeft = "0px";
                clearInterval(timer_shake);
        }
    }, wiggle_t);
}

// prepare easter-egg for reduced-motion visitors
// click 5 times on the main heading to trigger animations
easter_egg_triggered = 5; // but disable it for now
headings = document.querySelectorAll("h1");
for (h of headings) {
    h.onclick = function() {
        if (easter_egg_triggered <= 5) {
            easter_egg_triggered++;
        }
        if (easter_egg_triggered < 5) {
            console.log("still " + (5 - easter_egg_triggered) + " to go");
            shake(h);
        } else if (easter_egg_triggered == 5) {
            console.log("animations activated");
            shake(h);

            // remove static background image
            document.body.style.backgroundImage = 'none';
            bg();
        }
    };
}

if (!isReduced) {
    // trigger animated background for non-reduced-motion visitors
    window.onload = bg;
} else {
    easter_egg_triggered = 0; // enable easter-egg
}

// @license-end
