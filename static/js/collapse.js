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
