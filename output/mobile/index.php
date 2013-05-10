<?
// Auto generated xyCMS compatibility mobile/index.php
$loc = 'index.de.mob.html';
if (isset($_GET['p'])) {
    if (isset($_GET['lang'])) {
        $_GET['p'] .= 'EN';
    }
    switch($_GET['p']) {
        case "blog":
            $loc = "/blog.de.mob.html";
            break;

        case "blogEN":
            $loc = "/blog.mob.html";
            break;

        case "kontakt":
            $loc = "/contact.de.mob.html";
            break;

        case "kontaktEN":
            $loc = "/contact.mob.html";
            break;

        case "home":
            $loc = "/index.de.mob.html";
            break;

        case "homeEN":
            $loc = "/index.mob.html";
            break;

        case "avrserlib":
            $loc = "/avrserial.de.mob.html";
            break;

        case "avrserlibEN":
            $loc = "/avrserial.mob.html";
            break;

        case "c250":
            $loc = "/c250.de.mob.html";
            break;

        case "c250EN":
            $loc = "/c250.mob.html";
            break;

        case "cube":
            $loc = "/ledcube.de.mob.html";
            break;

        case "cubeEN":
            $loc = "/ledcube.mob.html";
            break;

        case "ledmatrix":
            $loc = "/ledmatrix.de.mob.html";
            break;

        case "ledmatrixEN":
            $loc = "/ledmatrix.mob.html";
            break;

        case "nas":
            $loc = "/nas.de.mob.html";
            break;

        case "nasEN":
            $loc = "/nas.mob.html";
            break;

        case "serialdebug":
            $loc = "/serialdebug.de.mob.html";
            break;

        case "serialdebugEN":
            $loc = "/serialdebug.mob.html";
            break;

        case "serialhelper":
            $loc = "/serialhelper.de.mob.html";
            break;

        case "serialhelperEN":
            $loc = "/serialhelper.mob.html";
            break;

        case "ssop28":
            $loc = "/ssop28.de.mob.html";
            break;

        case "ssop28EN":
            $loc = "/ssop28.mob.html";
            break;

        case "notifier":
            $loc = "/ultimatenotifier.de.mob.html";
            break;

        case "notifierEN":
            $loc = "/ultimatenotifier.mob.html";
            break;

        case "yasab":
            $loc = "/yasab.de.mob.html";
            break;

        case "yasabEN":
            $loc = "/yasab.mob.html";
            break;

        case "bt":
            $loc = "/bluetooth.de.mob.html";
            break;

        case "btEN":
            $loc = "/bluetooth.mob.html";
            break;

        case "sram":
            $loc = "/k6x4008.de.mob.html";
            break;

        case "sramEN":
            $loc = "/k6x4008.mob.html";
            break;

        case "rrem":
            $loc = "/rremote.de.mob.html";
            break;

        case "rremEN":
            $loc = "/rremote.mob.html";
            break;

        case "rob":
            $loc = "/xyrobot.de.mob.html";
            break;

        case "robEN":
            $loc = "/xyrobot.mob.html";
            break;

        case "xyrobotremote":
            $loc = "/xyrobotremote.de.mob.html";
            break;

        case "xyrobotremoteEN":
            $loc = "/xyrobotremote.mob.html";
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