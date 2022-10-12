const containerElem = document.querySelector(".container");
var skin = localStorage.getItem("skin") || "";
document.querySelector("#toggle").addEventListener("click", () => {
    containerElem.classList.toggle("dark");
    localStorage.setItem("skin", Array.prototype.at.call(containerElem.classList, -1));
});

containerElem.classList.add(localStorage.getItem("skin"));