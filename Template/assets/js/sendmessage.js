document.addEventListener('DOMContentLoaded', function() {
  const contactForm = document.getElementById('contactForm');

  contactForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(contactForm);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    // Send the contact form data to your backend
    sendEmail(data);
  });

  function sendEmail(data) {
    // Make a POST request to your backend to handle sending email
    // You'll need to implement this part using a backend service, like Node.js, PHP, etc.
    // Example using fetch API:
    fetch('https://backend.nsaworccmedicalcenter.org/api/sendmessage/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => {
      if (response.ok) {
          // Handle success - show a success message to the user
          console.log(response);
        alert('Message sent successfully!');
        contactForm.reset();
      } else {
        // Handle error - show an error message to the user
        alert('Failed to send message. Please try again later.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('An error occurred while sending the message.');
    });
  }
});
