title: Projects
parent: main
position: 10
---

This page lists all of my projects that are documented on this website.
Some bigger topics that are on-going are listed first.
Other projects have a specific date and time where I worked on them, so they are listed by date below.

To receive my latest updates you can subscribe to the <a href="rss.xml"><img src="img/rss.png">RSS Feed</a>.

<!--%
printProjectsMenu()
%-->

<script>
// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
    var coll = document.getElementsByClassName("collapse_menu");
    var i;
    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("collapseactive_menu");
            var content = this.parentElement.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
// @license-end
</script>
