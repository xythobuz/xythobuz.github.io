<?
// Auto generated xyCMS compatibility mobile/index.php
$loc = 'http://www.xythobuz.de/index.de.mob.html';
if (isset($_GET['p'])) {
    if (isset($_GET['lang'])) {
        $_GET['p'] .= 'EN';
    }
    switch($_GET['p']) {
        case "blog":
            $loc = "http://xythobuz.de/blog.de.mob.html";
            break;

        case "blogEN":
            $loc = "http://xythobuz.de/blog.mob.html";
            break;

        case "kontakt":
            $loc = "http://xythobuz.de/contact.de.mob.html";
            break;

        case "kontaktEN":
            $loc = "http://xythobuz.de/contact.mob.html";
            break;

        case "home":
            $loc = "http://xythobuz.de/index.de.mob.html";
            break;

        case "homeEN":
            $loc = "http://xythobuz.de/index.mob.html";
            break;

        case "avrserlib":
            $loc = "http://xythobuz.de/avrserial.de.mob.html";
            break;

        case "avrserlibEN":
            $loc = "http://xythobuz.de/avrserial.mob.html";
            break;

        case "c250":
            $loc = "http://xythobuz.de/c250.de.mob.html";
            break;

        case "c250EN":
            $loc = "http://xythobuz.de/c250.mob.html";
            break;

        case "cube":
            $loc = "http://xythobuz.de/ledcube.de.mob.html";
            break;

        case "cubeEN":
            $loc = "http://xythobuz.de/ledcube.mob.html";
            break;

        case "ledmatrix":
            $loc = "http://xythobuz.de/ledmatrix.de.mob.html";
            break;

        case "ledmatrixEN":
            $loc = "http://xythobuz.de/ledmatrix.mob.html";
            break;

        case "nas":
            $loc = "http://xythobuz.de/nas.de.mob.html";
            break;

        case "nasEN":
            $loc = "http://xythobuz.de/nas.mob.html";
            break;

        case "serialdebug":
            $loc = "http://xythobuz.de/serialdebug.de.mob.html";
            break;

        case "serialdebugEN":
            $loc = "http://xythobuz.de/serialdebug.mob.html";
            break;

        case "serialhelper":
            $loc = "http://xythobuz.de/serialhelper.de.mob.html";
            break;

        case "serialhelperEN":
            $loc = "http://xythobuz.de/serialhelper.mob.html";
            break;

        case "ssop28":
            $loc = "http://xythobuz.de/ssop28.de.mob.html";
            break;

        case "ssop28EN":
            $loc = "http://xythobuz.de/ssop28.mob.html";
            break;

        case "notifier":
            $loc = "http://xythobuz.de/ultimatenotifier.de.mob.html";
            break;

        case "notifierEN":
            $loc = "http://xythobuz.de/ultimatenotifier.mob.html";
            break;

        case "yasab":
            $loc = "http://xythobuz.de/yasab.de.mob.html";
            break;

        case "yasabEN":
            $loc = "http://xythobuz.de/yasab.mob.html";
            break;

        case "bt":
            $loc = "http://xythobuz.de/bluetooth.de.mob.html";
            break;

        case "btEN":
            $loc = "http://xythobuz.de/bluetooth.mob.html";
            break;

        case "sram":
            $loc = "http://xythobuz.de/k6x4008.de.mob.html";
            break;

        case "sramEN":
            $loc = "http://xythobuz.de/k6x4008.mob.html";
            break;

        case "rrem":
            $loc = "http://xythobuz.de/rremote.de.mob.html";
            break;

        case "rremEN":
            $loc = "http://xythobuz.de/rremote.mob.html";
            break;

        case "rob":
            $loc = "http://xythobuz.de/xyrobot.de.mob.html";
            break;

        case "robEN":
            $loc = "http://xythobuz.de/xyrobot.mob.html";
            break;

        case "xyrobotremote":
            $loc = "http://xythobuz.de/xyrobotremote.de.mob.html";
            break;

        case "xyrobotremoteEN":
            $loc = "http://xythobuz.de/xyrobotremote.mob.html";
            break;

        default:
            $loc = "/404.mob.html";
            break;
    }
}
if ($_SERVER['SERVER_PROTOCOL'] == 'HTTP/1.1') {
    if (php_sapi_name() == 'cgi') {
        header('Status: 301 Moved Permanently');
    } else {
        header('HTTP/1.1 301 Moved Permanently');
    }
}
header('Location: '.$loc);
?>