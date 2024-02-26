// Define the url to the ccaa/province json
const baseUrl = window.location.origin;
const choicesUrl = baseUrl + "/static/app/json/vars.json";

// Define the date inputs
let startDate = document.querySelector("#id_start_date");
let endDate = document.querySelector("#id_end_date");
let estEndDate = document.querySelector("#id_est_end_date");

// Set the type of the date inputs to "date"
startDate.type = "date";
endDate.type = "date";
estEndDate.type = "date";


let projectInput = document.querySelector("#id_project");
let projects = Array.from(projectInput.children)

if (projectName !== "") {

    projects.forEach(project => {
        projectInput.removeChild(project);
    });

    let newOption = document.createElement("option");
    newOption.textContent = projectName;

    projectInput.appendChild(newOption);
    projectInput.children[0].setAttribute("selected", true);
    projectInput.disabled = true;
}

// Fetch the ccaa/province json
fetch(choicesUrl)
.then(response => response.json())
.then(data => {

    // Define the ccaa and province selects
    let ccaa_dd = document.querySelector("select[name='ccaa']")
    let province_dd = document.querySelector("select[name='province']")

    // Change the value of the province select based on the ccaa value
    ccaa_dd.addEventListener("change", (event) => {

        let choice = event.target.value;
        let options = data[choice];

        // Delete the previous options of the province select
        while (province_dd.firstChild) {
            province_dd.removeChild(province_dd.firstChild)
        };

        // Add the filtered province options
        options.forEach(option => {
            let o = document.createElement("option");
            o.value = option;
            o.textContent = option;

            province_dd.appendChild(o)
        });

        // Select the default value for the province select
        province_dd.children[0].setAttribute("selected", true)

    })
})
.catch(error => console.error("Error fetching json data: ", error))