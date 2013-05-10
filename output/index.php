<?
// Auto generated xyCMS compatibility index.php
$loc = 'http://xythobuz.de/index.de.html';
if (isset($_GET['p'])) {
    if (isset($_GET['lang'])) {
        $_GET['p'] .= 'EN';
    }
    switch($_GET['p']) {
        case "blog":
            $loc = "http://xythobuz.de/blog.de.html";
            break;

        case "blogEN":
            $loc = "http://xythobuz.de/blog.html";
            break;

        case "kontakt":
            $loc = "http://xythobuz.de/contact.de.html";
            break;

        case "kontaktEN":
            $loc = "http://xythobuz.de/contact.html";
            break;

        case "home":
            $loc = "http://xythobuz.de/index.de.html";
            break;

        case "homeEN":
            $loc = "http://xythobuz.de/index.html";
            break;

        case "avrserlib":
            $loc = "http://xythobuz.de/avrserial.de.html";
            break;

        case "avrserlibEN":
            $loc = "http://xythobuz.de/avrserial.html";
            break;

        case "c250":
            $loc = "http://xythobuz.de/c250.de.html";
            break;

        case "c250EN":
            $loc = "http://xythobuz.de/c250.html";
            break;

        case "cube":
            $loc = "http://xythobuz.de/ledcube.de.html";
            break;

        case "cubeEN":
            $loc = "http://xythobuz.de/ledcube.html";
            break;

        case "ledmatrix":
            $loc = "http://xythobuz.de/ledmatrix.de.html";
            break;

        case "ledmatrixEN":
            $loc = "http://xythobuz.de/ledmatrix.html";
            break;

        case "nas":
            $loc = "http://xythobuz.de/nas.de.html";
            break;

        case "nasEN":
            $loc = "http://xythobuz.de/nas.html";
            break;

        case "serialdebug":
            $loc = "http://xythobuz.de/serialdebug.de.html";
            break;

        case "serialdebugEN":
            $loc = "http://xythobuz.de/serialdebug.html";
            break;

        case "serialhelper":
            $loc = "http://xythobuz.de/serialhelper.de.html";
            break;

        case "serialhelperEN":
            $loc = "http://xythobuz.de/serialhelper.html";
            break;

        case "ssop28":
            $loc = "http://xythobuz.de/ssop28.de.html";
            break;

        case "ssop28EN":
            $loc = "http://xythobuz.de/ssop28.html";
            break;

        case "notifier":
            $loc = "http://xythobuz.de/ultimatenotifier.de.html";
            break;

        case "notifierEN":
            $loc = "http://xythobuz.de/ultimatenotifier.html";
            break;

        case "yasab":
            $loc = "http://xythobuz.de/yasab.de.html";
            break;

        case "yasabEN":
            $loc = "http://xythobuz.de/yasab.html";
            break;

        case "bt":
            $loc = "http://xythobuz.de/bluetooth.de.html";
            break;

        case "btEN":
            $loc = "http://xythobuz.de/bluetooth.html";
            break;

        case "sram":
            $loc = "http://xythobuz.de/k6x4008.de.html";
            break;

        case "sramEN":
            $loc = "http://xythobuz.de/k6x4008.html";
            break;

        case "rrem":
            $loc = "http://xythobuz.de/rremote.de.html";
            break;

        case "rremEN":
            $loc = "http://xythobuz.de/rremote.html";
            break;

        case "rob":
            $loc = "http://xythobuz.de/xyrobot.de.html";
            break;

        case "robEN":
            $loc = "http://xythobuz.de/xyrobot.html";
            break;

        case "xyrobotremote":
            $loc = "http://xythobuz.de/xyrobotremote.de.html";
            break;

        case "xyrobotremoteEN":
            $loc = "http://xythobuz.de/xyrobotremote.html";
            break;

        default:
            $loc = "/404.html";
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