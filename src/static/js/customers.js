
const dialogbox = document.querySelector('.dialog-box')
document.addEventListener('click',(event)=>{
    const nameindialog = document.querySelector('.name-in-dialog')
    if (event.target.classList.contains('delete-btn')){
        closeButton.id = event.target.id
        confirmButton.id = event.target.id
        nameindialog.innerText = `You want to delete ${event.target.getAttribute('customer_name')}!`
        dialogbox.showModal()
        document.querySelector('.dialog-overlay').style.display = 'block';
    }
})
const closeButton = document.querySelector('.close-btn')
const confirmButton = document.querySelector('.confirm-btn')


closeButton.addEventListener('click',()=>{
    dialogbox.close()
    document.querySelector('.dialog-overlay').style.display = 'none';
    console.log('removed blur')
})


const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
document.cookie = `csrftoken=${csrftoken}; path=/`;


// Function to get CSRF token from cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

confirmButton.addEventListener('click',(event)=>{
    const customer_id = event.target.id
    fetch(`/delete-customer/${customer_id}`,{
        method : 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message)
        document.getElementById(customer_id).closest('tr').remove();
        document.querySelector('.dialog-overlay').style.display = 'none';
        dialogbox.close()
    })
    .catch(error => console.error("Error :",error));

})