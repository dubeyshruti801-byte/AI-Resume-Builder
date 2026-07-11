/*
=========================================
validation.js
AI Resume Builder
=========================================
*/

"use strict";

/* --------------------------------------
   Show Toast Message
-------------------------------------- */

function showToast(message, isError = true) {
    const toast = document.getElementById("toast");
    const text = document.getElementById("toastMessage");

    text.textContent = message;

    toast.style.backgroundColor = isError
        ? "#dc2626"
        : "#16a34a";

    toast.classList.remove("hidden");

    setTimeout(() => {
        toast.classList.add("hidden");
    }, 3000);
}


/* --------------------------------------
   Email Validation
-------------------------------------- */

function isValidEmail(email) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
}


/* --------------------------------------
   Phone Validation
   Same as backend:
   + optional
   7-15 digits
-------------------------------------- */

function isValidPhone(phone) {
    const pattern = /^\+?\d{7,15}$/;
    return pattern.test(phone);
}


/* --------------------------------------
   URL Validation
-------------------------------------- */

function isValidURL(url) {

    if (url.trim() === "") {
        return true;
    }

    try {
        new URL(url);
        return true;
    }
    catch {
        return false;
    }
}


/* --------------------------------------
   Required Field Validation
-------------------------------------- */

function validateRequired(id, fieldName) {

    const value = document
        .getElementById(id)
        .value
        .trim();

    if (value === "") {

        showToast(fieldName + " is required.");

        return false;
    }

    return true;
}


/* --------------------------------------
   Complete Form Validation
-------------------------------------- */

function validateForm() {

    if (!validateRequired("name", "Name"))
        return false;

    if (!validateRequired("email", "Email"))
        return false;

    if (!validateRequired("phone", "Phone"))
        return false;

    const email =
        document.getElementById("email").value.trim();

    if (!isValidEmail(email)) {

        showToast("Invalid email address.");

        return false;
    }

    const phone =
        document.getElementById("phone").value.trim();

    if (!isValidPhone(phone)) {

        showToast("Phone must contain 7-15 digits.");

        return false;
    }

    const linkedin =
        document.getElementById("linkedin").value.trim();

    if (!isValidURL(linkedin)) {

        showToast("Invalid LinkedIn URL.");

        return false;
    }

    const github =
        document.getElementById("github").value.trim();

    if (!isValidURL(github)) {

        showToast("Invalid GitHub URL.");

        return false;
    }

    const portfolio =
        document.getElementById("portfolio").value.trim();

    if (!isValidURL(portfolio)) {

        showToast("Invalid Portfolio URL.");

        return false;
    }

    return true;
}


/* --------------------------------------
   Loading Overlay
-------------------------------------- */

function showLoading() {

    document
        .getElementById("loadingOverlay")
        .classList
        .remove("hidden");

}


function hideLoading() {

    document
        .getElementById("loadingOverlay")
        .classList
        .add("hidden");

}