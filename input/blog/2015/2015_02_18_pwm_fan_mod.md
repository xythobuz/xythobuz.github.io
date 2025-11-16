title: Blog
post: GA-Z97X-UD5H PWM Fan Mod
date: 2015-02-18
comments: true
flattr: true
---

One of the last remaining problems with my [Hackintosh build](2015_01_31_hackintosh.html) were the case fans. After a quick glance in the Mainboard manual I decided that I could control three PWM fans and one non-PWM fan using the on-board hardware.

So I bought three Silent Wings 2 140mm PWM fans and one Thermaltake Pure 200mm fan. The 200mm fan additionally got a small temperature-sensing PCB mounted directly on it.

After some days, I began to worry. It did not seem as if the fans were really PWM controlled. That’s when I took a deeper look into the Mainboard manual.

<div class="lightgallery">
    <a href="img/fans1.png">
        <img src="img/fans1_small.png" alt="Manual excerpt">
    </a>
    <a href="img/fans2.png">
        <img src="img/fans2_small.png" alt="Mainboard review excerpt">
    </a>
</div>

Turns out, only the two CPU fan headers are PWM controlled. The other three headers, albeit being 4pin headers, do not support PWM and regulate the supply voltage to control the fan. And the remaining 3pin fan header can not be controlled at all, it always gives 12V.

Wow. Now I payed a lot of money to have PWM fans that are not used as PWM fans. This is not acceptable...!

But it should be possible to use the remaining available PWM signal from the CPU-OPT header, route it to all PWM fans, and use it to control a transistor that switches the supply voltage of the non-PWM fan. Additionally, we could combine the PWM signal and the regulated supply voltage from the fan headers to get the fans to rotate even slower.

There is an official [Intel PWM fan specification](http://www.formfactors.org/developer%5Cspecs%5Crev1_2_public.pdf). Following these, others have [already made a circuit](http://www.techpowerup.com/forums/threads/so-you-want-pwm-control-of-your-3-pin-fan.115752/) to use the PWM signal to control a non-PWM fan. This is probably very similar to the circuit inside a PWM fan.

Adapting this circuit, I first tested it on a PCB and then slimmed it down even more to get it into the back of my case. That’s it, works like a charm.

<div class="lightgallery">
    <a href="img/fans3.jpg">
        <img src="img/fans3_small.jpg" alt="First schematic drawings">
    </a>
    <a href="img/fans4.jpg">
        <img src="img/fans4_small.jpg" alt="Final schematic">
    </a>
    <a href="img/fans5.jpg">
        <img src="img/fans5_small.jpg" alt="First PCB test">
    </a>
    <a href="img/fans6.jpg">
        <img src="img/fans6_small.jpg" alt="First PCB, wrapped">
    </a>
    <a href="img/fans7.jpg">
        <img src="img/fans7_small.jpg" alt="Final form">
    </a>
</div>

### Affiliate links

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00K9R1KLW&amp;asins=B00K9R1KLW&amp;linkId=OCW45GIRZOZFZVS2&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00AKO0GRI&amp;asins=B00AKO0GRI&amp;linkId=D6BYOYZ4PQGYKJSV&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00KESSNFM&amp;asins=B00KESSNFM&amp;linkId=QRUOKJX7YXKH42UV&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B005OQIDCC&amp;asins=B005OQIDCC&amp;linkId=XYQ2NBTOZDPGWV77&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00KHU1SOK&amp;asins=B00KHU1SOK&amp;linkId=FASON76UURJMIW4H&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00188K5FI&amp;asins=B00188K5FI&amp;linkId=ELXR5Y4EAO2YNDKC&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

<iframe style="width:120px;height:240px;margin:0px;border-style:none;" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&amp;OneJS=1&amp;Operation=GetAdHtml&amp;MarketPlace=DE&amp;source=ss&amp;ref=ss_til&amp;ad_type=product_link&amp;tracking_id=xythobuzorg-21&amp;marketplace=amazon&amp;region=DE&amp;placement=B00CSM5YJA&amp;asins=B00CSM5YJA&amp;linkId=K6O55EESGTI3BI4H&amp;show_border=true&amp;link_opens_in_new_window=true">
</iframe>

