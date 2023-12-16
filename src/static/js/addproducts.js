var productName = document.querySelector("#productname")
var garmentdropoff = document.querySelector("#garmentdropoff")
var requestedpickup = document.querySelector("#requestedpickup")
var garmentpickup = document.querySelector("#garmentpickup")
var add_product = document.querySelector(".add_product")
var products_list = document.querySelector(".products_list")
var products = document.querySelector('.products')
var price = document.querySelector('#price')
var submit = document.querySelector('.submit')
var customer_id = document.querySelector('#customer_id')

document.addEventListener('DOMContentLoaded', function () {
    console.log("document loaded")
    flatpickr(".datepicker", {
        dateFormat: "Y-m-d", // Set your desired date format
    });
    console.log("flatpickr worked")
});

function highlightField(inputElement) {
    // Apply error style to the input field
    inputElement.classList.add('error');
}

// Get all input elements on the page
const inputElements = document.querySelectorAll('input');

// Add an 'input' event listener to each input element
inputElements.forEach(input => {
    input.addEventListener('input', () => {
        // Remove the 'error' class and reset background color on input
        input.classList.remove('error');
    });
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


document.addEventListener('click',function(event){
    if (event.target.classList.contains('delete')){
        var buttonId = parseInt(event.target.id)
        var indexToRemove = products_data.findIndex(element => element.id === buttonId)
        if (indexToRemove != -1){
            products_data.splice(indexToRemove,1)
            var row = event.target.parentNode.parentNode
            row.parentNode.removeChild(row)
        }
    }
})



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

  fetch(`/add-products/${customer_id.value}/`,{
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
