// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(document).ready(function() {
    var coll = document.getElementsByClassName("collapse");
    var i;
    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("collapseactive");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;

                setTimeout(function() {
                    content.style.borderWidth = null;
                    content.style.display = "none";
                }, 120);
            } else {
                content.style.display = "block";
                content.style.maxHeight = content.scrollHeight + "px";
                content.style.borderWidth = "2px";
            }
        });
    }
});
// @license-end
