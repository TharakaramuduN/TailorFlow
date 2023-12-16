document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname.includes('orders')) {
        var title = document.querySelector('#orders');
        title.style.color = "yellow";
    }
    else if (window.location.pathname.includes('customers')) {
        var title = document.querySelector('#customers');
        title.style.color = "yellow";
    }
    else{
        var title = document.querySelector('#home');
        title.style.color = "yellow";
    }
});