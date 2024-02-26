let dropdownButton = document.querySelector("#dropdown-btn")
let liItems = document.querySelectorAll("li:not(#iso14001)")

dropdownButton.addEventListener("click", () => {
    console.log(liItems)
    liItems.forEach(item => {
        if (item.classList.contains("hidden")) {
            item.classList.remove("hidden")
        } else {
            item.classList.add("hidden")
        }
    });
})