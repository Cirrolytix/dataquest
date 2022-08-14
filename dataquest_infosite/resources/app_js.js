function toggle(element) {
    var x = document.getElementById(element);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
	fbq('trackCustom', element);
	gtag('event', 'select_content', {'event_category': 'engagement', 'event_label': element});
}

function toggleClose(element) {
    var x = document.getElementById(element);
	x.className = x.className.replace(" w3-show", "");
}

function enrollment() {
	fbq('trackCustom', 'enrollment');
	gtag('event', 'select_content', {'event_category': 'engagement', 'event_label': 'enrollment'});
	window.alert('Registration is now closed. Thank you for your interest.');
}

// Toggle
function toggleHide(element) {
    var object = document.getElementById(element);
      if (object.style.display == 'none') {
          object.style.display = 'block';
          } 
      else {
        object.style.display = 'none';
          }	
        }