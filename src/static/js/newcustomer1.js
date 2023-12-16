var next1 = document.querySelector(".next-btn-1");
var next2 = document.querySelector(".next-btn-2");
var next3 = document.querySelector(".next-btn-3");
var back1 = document.querySelector(".back-btn-1");
var back2 = document.querySelector(".back-btn-2");
var back3 = document.querySelector(".back-btn-3");
var submit = document.querySelector(".submit-btn");
var customerinfo = document.querySelector(".customerinfo");
var measurementinfo = document.querySelector(".measurementinfo");
var productsinfo = document.querySelector(".productsinfo");
var checkout = document.querySelector(".checkout");
var CustomerNameInput = document.querySelector("#Name");
var VillageInput = document.querySelector("#Village");
var PhoneInput = document.querySelector("#Phone");
var gmailInput = document.querySelector("#Gmail");
var productName = document.querySelector("#productname");
var garmentdropoff = document.querySelector("#garmentdropoff");
var requestedpickup = document.querySelector("#requestedpickup");
var garmentpickup = document.querySelector("#garmentpickup");
var customer_id = document.querySelector("#customer_id").value;
var add_product = document.querySelector(".add_product");
var products_list = document.querySelector(".products_list");
var products = document.querySelector(".products");
var price = document.querySelector("#price");
var clothimage = document.querySelector('#clothimage')
var design = document.querySelector('#design')


document.addEventListener("DOMContentLoaded", function () {
  console.log("document loaded");
  flatpickr(".datepicker", {
    dateFormat: "Y-m-d", // Set your desired date format
  });
  console.log("flatpickr worked");
});

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
      `/api/check-email-exists/${customer_id}/?gmail=${gmail}`
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

next3.addEventListener("click", function () {
  if (products_list.innerHTML) {
    productsinfo.style.left = "-250%";
    checkout.style.left = "50%";
  } else {
    alert("Please add atleast one product.");
  }
});

add_product.addEventListener("click", loadProduct);

var products_data = [];
var products_count = 0;
console.log(products_count);

function loadProduct() {
  var isvalid = true;
  var inputs = [productName, garmentdropoff, requestedpickup, price, clothimage];
  inputs.forEach(function (input) {
      if (input.value === "") {
        highlightField(input);
        isvalid = false;
      }
      });
      if (!isvalid) {
        alert("Please Correct all fields!");
      }
      if (isvalid) {
        products_count += 1;

  
      var reader = new FileReader()
      reader.onload = function(e){
      const imagepreview = document.createElement('img')
      imagepreview.src = e.target.result
      imagepreview.classList.add('h-20','w-16')

      var newProduct = `<div class="productcard h-20 flex w-96 items-center bg-gray-300 mt-4">
      <div class="productimage">
        ${imagepreview.outerHTML}
      </div>
      <div class="productdetails ml-5">
        <h1>${productName.value}</h1>
        <p class="text-sm">price: ${price.value}</p>
        <p class="text-sm">drop off: ${garmentdropoff.value}</p>
        <p class="text-sm">req. pick up: ${requestedpickup.value}</p>
      </div>
      <div  class="flex justify-center items-center ml-16">
        <button
        id="${products_count}"
          class=" delete flex justify-center items-center border border-black "
          type="button"
        >
          delete
        </button>
      </div>
    </div>`
      
    products_list.innerHTML += newProduct;
      var productData = {
        id: products_count,
        product_name: productName.value,
        garment_drop_off: garmentdropoff.value,
        requested_pick_up_date: requestedpickup.value,
        price: price.value,
        clothimage : clothimage.files[0],
        design : design.files[0],
      };
      console.log(productData);
      products_data.push(productData);
      productName.value = "";
      price.value = "";
      clothimage.value = "";
      design.value = "";
    }
  reader.readAsDataURL(clothimage.files[0])
}}

const form = document.querySelector('form')

form.addEventListener("submit", function (event) {
  event.preventDefault();
  var formData = new FormData(form)

  products_data.forEach(function(product,index){
    formData.append(`product_name_${index}`,product.product_name)
    formData.append(`garment_drop_off_${index}`, product.garment_drop_off);
    formData.append(`requested_pick_up_date_${index}`, product.requested_pick_up_date);
    formData.append(`price_${index}`, product.price);
    //add image files
    formData.append(`cloth_image_${index}`,product.clothimage)
    formData.append(`design_${index}`,product.design)
  })

  fetch('/newCustomer1/',{
    method : 'POST',
    body : formData,
  })
  .then(response => {
    if(response.ok){
      window.location.href = '/'
    }
  })
  .catch(error => {
    console.error("Error",error)
  })
});

document.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete")) {
    var buttonId = parseInt(event.target.id);
    var indexToRemove = products_data.findIndex(
      (element) => element.id === buttonId
    );
    if (indexToRemove != -1) {
      products_data.splice(indexToRemove, 1);
      var row = event.target.parentNode.parentNode;
      row.parentNode.removeChild(row);
    }
  }
});

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
next2.addEventListener("click", function () {
  measurementinfo.style.left = "-200%";
  productsinfo.style.left = "50%";
});
back2.addEventListener("click", function () {
  productsinfo.style.left = "250%";
  measurementinfo.style.left = "0";
});
// next3.addEventListener('click', function () {

//     productsinfo.style.left = "-250%"
//     checkout.style.left = "50%"
// })
back3.addEventListener("click", function () {
  checkout.style.left = "250%";
  productsinfo.style.left = "50%";
});