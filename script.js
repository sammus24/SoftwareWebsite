/*function results() {
  const zipCode = document.getElementById('zip_code').value;
  const provider = document.getElementById('provider').value;
    
  fetch('/SoftwareWebsite/results-', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ zip_code: zipCode, provider: provider }),
    })
    .then(response => response.json())
    .then(data => {
    console.log(data);
        // Handle the API response data as needed
      })
    .catch(error => console.error(error));
  }
*/
