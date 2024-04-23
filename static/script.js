const bar = document.getElementById('bar');
const nav= document.getElementById('navbar');
const close = document.getElementById('close');

if (bar){
    bar.addEventListener('click',() => {
        nav.classList.add('active');
    })
}

if (close){
    close.addEventListener('click',() => {
        nav.classList.remove( 'active');
    })
}

//ajax request to insert review to the review model

let form = document.getElementById('feedback-form');
let commentContainer = document.getElementById('new-comment');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log("Script loaded");
    let commenter = document.createElement('h5');
    let comment = document.createElement('p');
    commenter.classList.add('mt-0');
    let url = form.getAttribute('data-url');
    $.ajax({
        type: 'POST',
        url: url,
        data: $("#feedback-form").serialize(),
        dataType: "json",
        success: function (data) {
            let commenter = document.createElement('h5');
            commenter.innerText = data.commenter;
            let commentText = document.createElement('p');
            commentText.innerText = data.msg;
            let commentDiv = document.createElement('div');
            commentDiv.appendChild(commenter);
            commentDiv.appendChild(commentText);
            commentContainer.appendChild(commentDiv);
            form.reset();
        }
    });
});

//EDIT FUNCTION ON PROFILE PAGE


function editProfile() {
    // Enable input fields for editing
    document.getElementsByName("address")[0].disabled = false;
    document.getElementsByName("phone_number")[0].disabled = false;
    // Change button text and onclick action
    var btn = document.querySelector('button');
    btn.innerHTML = 'Save Changes';
    btn.setAttribute('onclick', 'saveChanges()');
}

function saveChanges() {
    // Submit the form to save changes
    document.querySelector('form').submit();
}


// Using EXTERNAL API FOR FUNCTION CALL :

function initMap() {
    // Coordinates for the map center
    var center = { lat: 12.898725116470926, lng: 77.65275327554157 };

    // Create a map object and specify the DOM element for display.
    var map = new google.maps.Map(document.getElementById('map'), {
      center: center,
      zoom: 15 // Adjust zoom level as needed
    });

    // Add a marker at the specified location
    var marker = new google.maps.Marker({
      position: center,
      map: map,
      title: 'Royal East, Bengaluru'
    });
  }