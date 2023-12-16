var next1 = document.querySelector(".next-btn-1");
// var next2 = document.querySelector(".next-btn-2")
// var next3 = document.querySelector(".next-btn-3")
var back1 = document.querySelector(".back-btn-1");
// var back2 = document.querySelector(".back-btn-2")
// var back3 = document.querySelector(".back-btn-3")
// var submit = document.querySelector(".submit-btn")
var customerinfo = document.querySelector(".customerinfo");
var measurementinfo = document.querySelector(".measurementinfo");
// var productsinfo = document.querySelector(".productsinfo")
// var checkout = document.querySelector(".checkout")
var CustomerNameInput = document.querySelector("#Name");
var VillageInput = document.querySelector("#Village");
var PhoneInput = document.querySelector("#Phone");
var gmailInput = document.querySelector("#Gmail");
// var productName = document.querySelector("#productname")
// var garmentdropoff = document.querySelector("#garmentdropoff")
// var requestedpickup = document.querySelector("#requestedpickup")
// var garmentpickup = document.querySelector("#garmentpickup")
var customer_id = document.querySelector("#customer_id").value;

// document.addEventListener('DOMContentLoaded', function () {
//     flatpickr(".datepicker", {
//         dateFormat: "Y-m-d", // Set your desired date format
//     });
// });

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

function isValidPhoneNumber(phoneNumber) {
  const phoneRegex = /^\d{10}$/;
  return phoneRegex.test(phoneNumber);
}

function resetErrorStyles() {
  // Reset error styles for all input fields
  const inputs = [PhoneInput, gmailInput];
  inputs.forEach((input) => {
    input.classList.remove("error");
  });
}

function highlightField(inputElement) {
  // Apply error style to the input field
  inputElement.classList.add("error");
}

next1.addEventListener("click", async function () {
  var gmail = gmailInput.value.trim();
  var phone = PhoneInput.value.trim();
  resetErrorStyles();
  let isValid = true;
  if (CustomerNameInput.value === "") {
    highlightField(CustomerNameInput);
    isValid = false;
  }
  if (VillageInput.value === "") {
    highlightField(VillageInput);
    isValid = false;
  }

  if (phone) {
    var response = await fetch(
      `/api/check-phone-exists/${customer_id}/?phone=${phone}`
    );
    var data = await response.json();
    if (data.exists) {
      alert("Phone number already exists.");
      isValid = false;
      return;
    }
  }
  if (gmail) {
    var response = await fetch(
      `/api/check-email-exists/${customer_id}?gmail=${gmail}`
    );
    var data = await response.json();
    if (data.exists) {
      alert("Email already exists.");
      isValid = false;
      return;
    }
  }

  if (!isValidEmail(gmail)) {
    highlightField(gmailInput);
    isValid = false;
  }

  if (!isValidPhoneNumber(phone)) {
    highlightField(PhoneInput);
    isValid = false;
  } else if (isValid) {
    customerinfo.style.left = "-250%";
    measurementinfo.style.left = "0";
  } else {
    alert("Please fill out form correctly.");
  }
});

// next3.addEventListener('click', function () {
//     resetErrorStyles()
//     var isvalid = true
//     var inputs = [productName, garmentdropoff, garmentpickup, requestedpickup]
//     inputs.forEach(function (input) {
//         if (input.value === "") {
//             highlightField(input)
//             isvalid = false
//         }
//     })
//     if (!isvalid) {
//         alert("Please Correct all fields!")
//     }
//     else {
//         productsinfo.style.left = "-250%"
//         checkout.style.left = "50%"
//     }

// })

// Get all input elements on the page
const inputElements = document.querySelectorAll("input");

// Add an 'input' event listener to each input element
inputElements.forEach((input) => {
  input.addEventListener("input", () => {
    // Remove the 'error' class and reset background color on input
    input.classList.remove("error");
  });
});

back1.addEventListener("click", function () {
  customerinfo.style.left = "50%";
  measurementinfo.style.left = "200%";
});
// next2.addEventListener('click', function () {

//     measurementinfo.style.left = "-200%"
//     productsinfo.style.left = "50%"
// })
// back2.addEventListener('click', function () {

//     productsinfo.style.left = "250%"
//     measurementinfo.style.left = "0"
// })
// next3.addEventListener('click', function () {

//     productsinfo.style.left = "-250%"
//     checkout.style.left = "50%"
// })
// back3.addEventListener('click', function () {

//     checkout.style.left = "250%"
//     productsinfo.style.left = "50%"
// })
