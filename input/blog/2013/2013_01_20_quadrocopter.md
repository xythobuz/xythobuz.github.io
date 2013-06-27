title: Blog
post: Quadrocopter Ueberblick
date: 2013-01-20
comments: true
flattr: true
twitter: xythobuz
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

Wie auf Twitter bereits zu sehen war, arbeite Ich momentan an meiner eigenen Quadrocopter Plattform. Kern der ganzen Geschichte ist [xyControl][1]:

[![Photo 1][2]][3]
[![Photo 2][4]][5]

Alle nötigen Sensoren, also 3D Accelerometer und 3D Gyroskop, sowie 3D Magnetometer, sind in einem Paket untergebracht, dem [MiniMU-9 v2][6]:

[![Photo 3][7]][8]

Verwendung finden außerdem vier [BL-Ctrl v1.2][9] Brushlessregler, welche vier [Robbe Roxxy BL Outrunner 2824-34][10] Motoren antreiben:

[![Photo 4][11]][12]
[![Photo 5][13]][14]

Und alles zusammen schaut momentan so aus:

[![Photo 6][15]][16]

Ich bin zuversichtlich... :)

 [1]: https://github.com/xythobuz/xyControl
 [2]: img/q_control_small.jpg
 [3]: img/q_control.jpg
 [4]: img/q_control2_small.jpg
 [5]: img/q_control2.jpg
 [6]: http://www.watterott.com/de/MinIMU-9-v2
 [7]: img/q_sens_small.jpg
 [8]: img/q_sens.jpg
 [9]: https://www.mikrocontroller.com/index.php?main_page=product_info&products_id=209
 [10]: http://www.conrad.de/ce/de/product/231867
 [11]: img/q_mot_small.jpg
 [12]: img/q_mot.jpg
 [13]: img/q_motprop_small.jpg
 [14]: img/q_motprop.jpg
 [15]: img/q_fin_small.jpg
 [16]: img/q_fin.jpg