(function($) {
    $.fn.autoscroll = function(options) {
        var settings = $.extend({}, $.fn.autoscroll.defaults, options);
        return this.each(function() {
            var $this = $(this);
            if ($this.length > 0 &&
                $this[0].scrollHeight > $this[0].clientHeight) {
                var scrollTimer,
                    scrollLeft = 0;

                function scrollList() {
                    var itemHeight = $this.children().eq(1).outerWidth(true);
                    scrollLeft++;
                    if (scrollLeft >= itemHeight) {
                        $this.scrollLeft(0).children().eq(0).appendTo($this);
                        scrollLeft = 0;
                    } else {
                        $this.scrollLeft(scrollLeft);
                    }
                }
                $this.hover(function() {
                    clearInterval(scrollTimer);
                    $this.css("overflow-y", "auto");
                    if (settings.hideScrollbar) {
                        $this.addClass("hide-scrollbar");
                    }
                    if($.type(settings.handlerIn) === "function") {
                        settings.handlerIn();
                    }
                }, function() {
                    $this.css("overflow-x", "hidden");
                    scrollTimer = setInterval(function() {
                        scrollList();
                    }, settings.interval);
                    if($.type(settings.handlerOut) === "function") {
                        settings.handlerOut();
                    }
                }).trigger("mouseleave");
            }
        });
    }
    $.fn.autoscroll.defaults = {
        interval: 50, 
        hideScrollbar: true, 
        handlerIn: null, 
        handlerOut: null 

    };
    $(function() {
        $("[data-autoscroll]").autoscroll();
    });
})(jQuery);

let header = document.querySelector("header");
window.onscroll = () =>{
    let pos = document.documentElement.scrollTop
    if (pos > 0 ){
        header.classList.add("sticky");
    }
    else{
        header.classList.remove("sticky");
    }
    if (pos >300){
        scrollTopBtn.style.display = "grid";
    }
    else{
        scrollTopBtn.style.display = "none";
    }
    scrollTopBtn.addEventListener("click", () =>{
        document.documentElement.scrollTop = 0

    })
}

let hamMenuIcone = document.getElementById("ham-menu");
let navBar = document.getElementById("nav-bar");
let navLink = navBar.querySelectorAll("li");
let scrollTopBtn = document.getElementById("scroll-top")


hamMenuIcone.addEventListener("click", ()=> {
    navBar.classList.toggle("active")
    hamMenuIcone.classList.toggle("fa-times")
})



 navLink.forEach((navLink) =>{
     navLink.addEventListener("click", ()=>{
         navBar.classList.remove("active");``
         hamMenuIcone.classList.toggle("fa-times")
     })
 })