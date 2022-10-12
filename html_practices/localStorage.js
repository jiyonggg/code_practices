const contentElem = document.querySelector("#content");
const buttons = document.querySelectorAll("button");

function saveContent() {
    let content = contentElem.value;
    localStorage.setItem("content", content);
    alert("Save Completed");
}

function loadContent() {
    let content = localStorage.getItem("content");
    if (content == null) {
        alert("No Saved Data Exists")
    } else {
        contentElem.value = content;
        alert("Load Completed");
    }
}

function alertContent() {
    alert("Content: " + contentElem.value);
}

function clearContent() {
    localStorage.clear();
    alert("Clear Completed");
}

Array.prototype.map.call(buttons, (elem) => elem.addEventListener("click", window[elem.id + "Content"]));