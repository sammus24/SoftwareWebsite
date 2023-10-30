from flask import Flask, render_template, request
import requests

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def search():
    zip_code = request.form['zip_code']
    provider = request.form['provider']
    parameters = {
        "postal_code": zip_code,
        "taxonomy_description": provider
    }

    response = requests.get("https://npiregistry.cms.hhs.gov/api/?pretty=on&enumeration_type=NPI-1&version=2.1", params=parameters)

    if response.status_code == 200:
        data = response.json()
        results = data.get("result", [])

        doctors = []  # Create a list to store the doctor information

        for result in results:
            first_name = result.get("basic", {}).get("first_name", "")
            last_name = result.get("basic", {}).get("last_name", "")
            
            address_data = result.get("addresses", [{}])[0]
            address = ", ".join(filter(None, [address_data.get("address_1", ""), address_data.get("address_2", ""), address_data.get("city", ""), address_data.get("state", ""), address_data.get("postal_code", "")]))
            
            doctor_info = {
                "first_name": first_name,
                "last_name": last_name,
                "address": address
            }
            
            doctors.append(doctor_info)
    else:
        return "Request failed with status code: " + str(response.status_code)
    return render_template('results.html', doctors=doctors)

    
if __name__ == '__main__':
    app.run(debug=True)
