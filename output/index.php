<?
// Auto generated xyCMS compatibility index.php
$loc = 'index.de.html';
if (isset($_GET['p'])) {
    if (isset($_GET['lang'])) {
        $_GET['p'] .= EN;
    }
    switch($_GET['p']) {
        case "blogEN":
            $loc = "/blog.html";
            break;

        case "kontaktEN":
            $loc = "/contact.html";
            break;

        case "home":
            $loc = "/index.de.html";
            break;

        case "homeEN":
            $loc = "/index.html";
            break;

        case "avrserlib":
            $loc = "/avrserial.de.html";
            break;

        case "avrserlibEN":
            $loc = "/avrserial.html";
            break;

        case "c250":
            $loc = "/c250.de.html";
            break;

        case "c250EN":
            $loc = "/c250.html";
            break;

        case "cube":
            $loc = "/ledcube.de.html";
            break;

        case "cubeEN":
            $loc = "/ledcube.html";
            break;

        case "ledmatrix":
            $loc = "/ledmatrix.de.html";
            break;

        case "ledmatrixEN":
            $loc = "/ledmatrix.html";
            break;

        case "nas":
            $loc = "/nas.de.html";
            break;

        case "nasEN":
            $loc = "/nas.html";
            break;

        case "serialdebug":
            $loc = "/serialdebug.de.html";
            break;

        case "serialdebugEN":
            $loc = "/serialdebug.html";
            break;

        case "serialhelper":
            $loc = "/serialhelper.de.html";
            break;

        case "serialhelperEN":
            $loc = "/serialhelper.html";
            break;

        case "ssop28":
            $loc = "/ssop28.de.html";
            break;

        case "ssop28EN":
            $loc = "/ssop28.html";
            break;

        case "notifier":
            $loc = "/ultimatenotifier.de.html";
            break;

        case "notifierEN":
            $loc = "/ultimatenotifier.html";
            break;

        case "yasab":
            $loc = "/yasab.de.html";
            break;

        case "yasabEN":
            $loc = "/yasab.html";
            break;

        case "bt":
            $loc = "/bluetooth.de.html";
            break;

        case "btEN":
            $loc = "/bluetooth.html";
            break;

        case "sram":
            $loc = "/k6x4008.de.html";
            break;

        case "sramEN":
            $loc = "/k6x4008.html";
            break;

        case "rrem":
            $loc = "/rremote.de.html";
            break;

        case "rremEN":
            $loc = "/rremote.html";
            break;

        case "rob":
            $loc = "/xyrobot.de.html";
            break;

        case "robEN":
            $loc = "/xyrobot.html";
            break;

        case "xyrobotremote":
            $loc = "/xyrobotremote.de.html";
            break;

        case "xyrobotremoteEN":
            $loc = "/xyrobotremote.html";
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