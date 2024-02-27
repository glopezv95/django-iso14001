let scroller = document.querySelector(".scroller");
let primary = document.createElement("div");
primary.classList.add("scroller-primary");

indicatorsList.forEach(element => {
    let div = document.createElement("div");
    div.textContent = element;
    div.classList.add("indicator");
    primary.appendChild(div)
});

let secondary = document.createElement("div");
secondary.classList.add("scroller-secondary");
secondary.innerHTML = primary.innerHTML;

scroller.appendChild(primary);
scroller.appendChild(secondary);