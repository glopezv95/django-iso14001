const baseUrl = window.location.origin;
const fetchProjectsUrl = baseUrl + "/api/iso14001/fetch-project-list";
const fetchProjectNameUrl = baseUrl + "/api/iso14001/fetch-project-names";

let tBody = document.querySelector("tbody");
let previousButton = document.querySelector("#btn-previous");

let nextButton = document.querySelector("#btn-next");
let pageP = document.querySelector(".table-desc p")
let start = 0;
let pageNum = 1;

let newProjectInput = document.querySelector("#id_name")
let projectListDiv = document.querySelector("#name-list")

// newProjectInput.addEventListener("change", function (event) {
//     let string = event.target.value;
//     fetch(`${fetchProjectNameUrl}?name=${string}`)
//     .then(response => {return response.json()})
//     .then(data => {
//         console.log(data);
//         data.forEach(element => {
//             let p = document.createElement("p")
//             p.textContent = element

//             projectListDiv.appendChild(p)
//         });

//     })
// })

let fetchList = function (json) {

    let bodyChildren = Array.from(tBody.children);

    bodyChildren.forEach(child => {
        tBody.removeChild(child);
    });

    json.forEach(project => {

        let tr = document.createElement("tr");

        tr.innerHTML =
            `
            <td><a href="${baseUrl}/iso14001/projects/${project.slug}/form">${project.name}</a></td>
            <td>${project.created_at}</td>
            <td>${project.updated_at}</td>`;

        tBody.appendChild(tr);
    });
};

pageP.innerHTML = `Page ${pageNum} of ${numPages}`

fetch(fetchProjectsUrl)
.then(response => {return response.json()})
.then(data => {fetchList(data);})

nextButton.addEventListener("click", function () {

    start += 15;
    pageNum += 1;

    fetch(`${fetchProjectsUrl}?start=${start}`)
    .then(response => {return response.json()})
    .then(data => {
        fetchList(data);
    })

    pageP.innerHTML = `Page ${pageNum} of ${numPages}`
})

previousButton.addEventListener("click", function () {
    
    if (start !== 0) {

        start -= 15;
        pageNum -= 1;

        fetch(`${fetchProjectsUrl}?start=${start}`)
        .then(response => {return response.json()})
        .then(data => {
            fetchList(data);
        })

        pageP.innerHTML = `Page ${pageNum} of ${numPages}`
    }
})