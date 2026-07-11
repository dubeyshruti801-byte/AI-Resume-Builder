"use strict";

/* ==========================================================
   AI Resume Builder
   app.js
   Part 1
========================================================== */


/* ==========================================================
   DOM Elements
========================================================== */

const resumeForm = document.getElementById("resumeForm");

const skillsContainer = document.getElementById("skillsContainer");
const experienceContainer = document.getElementById("experienceContainer");
const educationContainer = document.getElementById("educationContainer");
const projectsContainer = document.getElementById("projectsContainer");
const certificationsContainer = document.getElementById("certificationsContainer");
const languagesContainer = document.getElementById("languagesContainer");

const addSkillBtn = document.getElementById("addSkill");
const addExperienceBtn = document.getElementById("addExperience");
const addEducationBtn = document.getElementById("addEducation");
const addProjectBtn = document.getElementById("addProject");
const addCertificationBtn = document.getElementById("addCertification");
const addLanguageBtn = document.getElementById("addLanguage");

const loadingOverlay = document.getElementById("loadingOverlay");
const toast = document.getElementById("toast");
const toastMessage = document.getElementById("toastMessage");


/* ==========================================================
   Utility Functions
========================================================== */

function createInput(type, placeholder, className = "") {

    const input = document.createElement("input");

    input.type = type;
    input.placeholder = placeholder;

    if (className) {
        input.className = className;
    }

    return input;

}


function createTextarea(placeholder) {

    const textarea = document.createElement("textarea");

    textarea.rows = 4;
    textarea.placeholder = placeholder;

    return textarea;

}


function createRemoveButton() {

    const button = document.createElement("button");

    button.type = "button";

    button.className = "remove-btn";

    button.textContent = "Remove";

    button.addEventListener("click", () => {

        button.parentElement.remove();

    });

    return button;

}


/* ==========================================================
   Toast Notification
========================================================== */

function showToast(message, success = true) {

    toastMessage.textContent = message;

    toast.classList.remove("hidden");

    if (success) {

        toast.classList.remove("error");
        toast.classList.add("success");

    }

    else {

        toast.classList.remove("success");
        toast.classList.add("error");

    }

    setTimeout(() => {

        toast.classList.add("hidden");

    }, 3000);

}


/* ==========================================================
   Loading Overlay
========================================================== */

function showLoader() {

    loadingOverlay.classList.remove("hidden");

}


function hideLoader() {

    loadingOverlay.classList.add("hidden");

}


/* ==========================================================
   Skills
========================================================== */

function addSkill(value = "") {

    const wrapper = document.createElement("div");

    wrapper.className = "dynamic-card";

    const input = createInput(
        "text",
        "Python / FastAPI / MongoDB",
        "skill-input"
    );

    input.value = value;

    wrapper.appendChild(input);

    wrapper.appendChild(createRemoveButton());

    skillsContainer.appendChild(wrapper);

}


/* ==========================================================
   Experience
========================================================== */

function addExperience(data = {}) {

    const wrapper = document.createElement("div");

    wrapper.className = "dynamic-card";

    const title = createInput(
        "text",
        "Job Title"
    );

    title.value = data.title || "";

    const company = createInput(
        "text",
        "Company"
    );

    company.value = data.company || "";

    const start = createInput(
        "date",
        ""
    );

    start.value = data.start || "";

    const end = createInput(
        "date",
        ""
    );

    end.value = data.end || "";

    const description = createTextarea(
        "Describe your responsibilities..."
    );

    description.value = data.description || "";

    wrapper.appendChild(title);
    wrapper.appendChild(company);
    wrapper.appendChild(start);
    wrapper.appendChild(end);
    wrapper.appendChild(description);
    wrapper.appendChild(createRemoveButton());

    experienceContainer.appendChild(wrapper);

}


/* ==========================================================
   Education
========================================================== */

function addEducation(data = {}) {

    const wrapper = document.createElement("div");

    wrapper.className = "dynamic-card";

    const degree = createInput(
        "text",
        "Degree"
    );

    degree.value = data.degree || "";

    const institution = createInput(
        "text",
        "Institution"
    );

    institution.value = data.institution || "";

    const year = createInput(
        "text",
        "Year"
    );

    year.value = data.year || "";

    wrapper.appendChild(degree);
    wrapper.appendChild(institution);
    wrapper.appendChild(year);
    wrapper.appendChild(createRemoveButton());

    educationContainer.appendChild(wrapper);

}
/* ==========================================================
   Projects
========================================================== */

function addProject(data = {}) {

    const wrapper = document.createElement("div");
    wrapper.className = "dynamic-card";

    const title = createInput(
        "text",
        "Project Title"
    );
    title.value = data.title || "";

    const description = createTextarea(
        "Project Description"
    );
    description.value = data.description || "";

    const technologies = createInput(
        "text",
        "Python, FastAPI, MongoDB"
    );
    technologies.value = (data.technologies || []).join(", ");

    wrapper.appendChild(title);
    wrapper.appendChild(description);
    wrapper.appendChild(technologies);
    wrapper.appendChild(createRemoveButton());

    projectsContainer.appendChild(wrapper);

}


/* ==========================================================
   Certifications
========================================================== */

function addCertification(data = {}) {

    const wrapper = document.createElement("div");
    wrapper.className = "dynamic-card";

    const name = createInput(
        "text",
        "Certification Name"
    );
    name.value = data.name || "";

    const issuer = createInput(
        "text",
        "Issuing Organization"
    );
    issuer.value = data.issuer || "";

    const year = createInput(
        "text",
        "Year"
    );
    year.value = data.year || "";

    wrapper.appendChild(name);
    wrapper.appendChild(issuer);
    wrapper.appendChild(year);
    wrapper.appendChild(createRemoveButton());

    certificationsContainer.appendChild(wrapper);

}


/* ==========================================================
   Languages
========================================================== */

function addLanguage(data = {}) {

    const wrapper = document.createElement("div");
    wrapper.className = "dynamic-card";

    const language = createInput(
        "text",
        "Language"
    );
    language.value = data.name || "";

    const proficiency = createInput(
        "text",
        "Beginner / Intermediate / Fluent"
    );
    proficiency.value = data.proficiency || "";

    wrapper.appendChild(language);
    wrapper.appendChild(proficiency);
    wrapper.appendChild(createRemoveButton());

    languagesContainer.appendChild(wrapper);

}


/* ==========================================================
   Event Listeners
========================================================== */

addSkillBtn.addEventListener("click", () => {

    addSkill();

});


addExperienceBtn.addEventListener("click", () => {

    addExperience();

});


addEducationBtn.addEventListener("click", () => {

    addEducation();

});


addProjectBtn.addEventListener("click", () => {

    addProject();

});


addCertificationBtn.addEventListener("click", () => {

    addCertification();

});


addLanguageBtn.addEventListener("click", () => {

    addLanguage();

});


/* ==========================================================
   Default Field Initialization
========================================================== */

window.addEventListener("DOMContentLoaded", () => {

    addSkill();

    addExperience();

    addEducation();

    addProject();

    addCertification();

    addLanguage();

});
/* ==========================================================
   Collect Skills
========================================================== */

function getSkills() {

    return Array.from(

        skillsContainer.querySelectorAll("input")

    )

    .map(input => input.value.trim())

    .filter(skill => skill !== "");

}


/* ==========================================================
   Collect Experience
========================================================== */

function getExperience() {

    return Array.from(

        experienceContainer.querySelectorAll(".dynamic-card")

    )

    .map(card => {

        const inputs =
            card.querySelectorAll("input");

        const textarea =
            card.querySelector("textarea");

        return {

            title: inputs[0].value.trim(),

            company: inputs[1].value.trim(),

            start: inputs[2].value,

            end: inputs[3].value,

            description: textarea.value.trim()

        };

    })

    .filter(exp => exp.title !== "");

}


/* ==========================================================
   Collect Education
========================================================== */

function getEducation() {

    return Array.from(

        educationContainer.querySelectorAll(".dynamic-card")

    )

    .map(card => {

        const inputs =
            card.querySelectorAll("input");

        return {

            degree: inputs[0].value.trim(),

            institution: inputs[1].value.trim(),

            year: inputs[2].value.trim()

        };

    })

    .filter(edu => edu.degree !== "");

}


/* ==========================================================
   Collect Projects
========================================================== */

function getProjects() {

    return Array.from(

        projectsContainer.querySelectorAll(".dynamic-card")

    )

    .map(card => {

        const title =
            card.querySelectorAll("input")[0];

        const technologies =
            card.querySelectorAll("input")[1];

        const description =
            card.querySelector("textarea");

        return {

            title: title.value.trim(),

            description: description.value.trim(),

            technologies:

                technologies.value

                .split(",")

                .map(t => t.trim())

                .filter(t => t !== "")

        };

    })

    .filter(project => project.title !== "");

}


/* ==========================================================
   Collect Certifications
========================================================== */

function getCertifications() {

    return Array.from(

        certificationsContainer.querySelectorAll(".dynamic-card")

    )

    .map(card => {

        const inputs =
            card.querySelectorAll("input");

        return {

            name: inputs[0].value.trim(),

            issuer: inputs[1].value.trim(),

            year: inputs[2].value.trim()

        };

    })

    .filter(cert => cert.name !== "");

}


/* ==========================================================
   Collect Languages
========================================================== */

function getLanguages() {

    return Array.from(

        languagesContainer.querySelectorAll(".dynamic-card")

    )

    .map(card => {

        const inputs =
            card.querySelectorAll("input");

        return {

            name: inputs[0].value.trim(),

            proficiency: inputs[1].value.trim()

        };

    })

    .filter(lang => lang.name !== "");

}


/* ==========================================================
   Form Submission
========================================================== */

resumeForm.addEventListener(

    "submit",

    async function (event) {

        event.preventDefault();

        if (!validateForm()) {

            return;

        }

        const resumeData = {

            name:

                document.getElementById("name").value.trim(),

            email:

                document.getElementById("email").value.trim(),

            phone:

                document.getElementById("phone").value.trim(),

            summary:

                document.getElementById("summary").value.trim(),

            linkedin:

                document.getElementById("linkedin").value.trim(),

            github:

                document.getElementById("github").value.trim(),

            portfolio:

                document.getElementById("portfolio").value.trim(),

            skills:

                getSkills(),

            experience:

                getExperience(),

            education:

                getEducation(),

            projects:

                getProjects(),

            certifications:

                getCertifications(),

            languages:

                getLanguages()

        };

        await createResume(

            resumeData

        );

    }

);


/* ==========================================================
   Optional Clear Form
========================================================== */

function clearResumeForm() {

    if (

        !confirm(

            "Clear all entered information?"

        )

    ) {

        return;

    }

    resumeForm.reset();

    skillsContainer.innerHTML = "";

    experienceContainer.innerHTML = "";

    educationContainer.innerHTML = "";

    projectsContainer.innerHTML = "";

    certificationsContainer.innerHTML = "";

    languagesContainer.innerHTML = "";

    addSkill();

    addExperience();

    addEducation();

    addProject();

    addCertification();

    addLanguage();

    showToast(

        "Form cleared successfully.",

        true

    );

}
document
    .getElementById("clearFormBtn")
    .addEventListener(
        "click",
        clearResumeForm
    );