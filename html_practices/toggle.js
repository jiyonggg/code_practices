var toggleBtn = document.querySelector("article>button");
toggleBtn.addEventListener("click", function() {
    var navElem = document.querySelector("nav");
    var navClasses = navElem.classList;
    var artElem = document.querySelector("article");
    var artClasses = artElem.classList;
    
    navClasses.toggle("hide");
    artClasses.toggle("menuon");
});