var toggleBtn = document.querySelector("article>button");
toggleBtn.addEventListener("click", function() {
    var navElem = document.querySelector("nav");
    var navClasses = navElem.classList;
    var artElem = document.querySelector("article");
    var artClasses = artElem.classList;
    
    if (navClasses.contains("hide")) {
        navClasses.remove("hide");
        artClasses.add("menuon");
    } else {
        navClasses.add("hide");
        artClasses.remove("menuon");
    }
});