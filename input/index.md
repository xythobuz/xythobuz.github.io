title: Home
parent: main
position: 1
flattr: true
compat: home
noheader: true
---

# Hi there!

<img id="index-avatar" src="img/ava.jpg">

I'm a <!--% print(own_age()) %--> year old software developer from Germany.
All of my projects are released as free or open-source software on [my Codeberg profile](https://codeberg.org/xythobuz), [my GitHub profile](https://github.com/xythobuz) or here on my website.
Have fun!

To receive my latest updates, you can subscribe to the <a href="rss.xml"><img src="img/rss.png">RSS Feed</a>.

All my projects and all content of this website are proudly made without _any_ generative artificial intelligence.

### Recent Posts and Updates

<!--%
printRecentMenu(10)
%-->

[Show all updates](updates.html).

<script>
// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
    function getRandomInt(max) {
        return Math.floor(Math.random() * max);
    }
    var img = document.getElementById("index-avatar");
    if (getRandomInt(2) == 0) {
        setTimeout(function() {
            img.src = "img/gb_cam.png";
            img.style.width = "150px"; // 128*1.17188
            img.style.height = "131px"; // 112*1.17188
        }, 500 + getRandomInt(10000));
    }
// @license-end
</script>
