# Django REST API - CSV Upload & Validation  

## Overview  
This Django REST Framework (DRF) API allows users to upload a CSV file, validates the data, and saves valid records into the database. Invalid records are rejected with detailed error messages.  

## Features  
1. Upload a CSV file via a POST request  
2. Validate records (`name`, `email`, `age`)  
3. Skip duplicate emails  
4. Return a JSON response summarizing successful and rejected records  
5. Unit tests for API validation  

---

## Technologies Used  
- **Python** (Django, Django REST Framework)  
- **SQLite**
- **Postman** (for testing API)  

---

## Installation & Setup  

### **1. Clone the Repository**

```
git clone https://github.com/cozyrosy/GI-csv-upload.git

cd csv_api_project
```

### **2. Create a Virtual Environment**
```
python -m venv venv

source venv/bin/activate  # macOS/Linux

venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```
pip install -r requirements.txt
```
### **4. Apply Migrations**
```
python manage.py makemigrations

python manage.py migrate
```
### **5. Create a Superuser (for Admin Panel)**
```
python manage.py createsuperuser

#Follow the prompts to set up a username, email, and password.
```
### **6. Run the Server**
```
python manage.py runserver
```
The API will be available at:
http://127.0.0.1:8000/

 ## API Endpoints
1. Upload CSV File
```
 Endpoint: POST /api/upload/
 
 Request (Form-Data)
 
Key	Value

file	Upload a .csv file
```
2. Sample CSV Format
 ```
name,email,age

John Doe,johndoe@example.com,25

Jane Smith,janesmith@example.com,30

Invalid User,invalidemail,200
```
3. Response Format
   
{

    "success_count": 2,
    
    "failed_count": 1,
    
    "errors": [
    
        {
        
            "line": 3,
            
            "email": "Invalid email format",
            
            "age": "Age must be between 0 and 120."
            
        }
        
    ]
    
}
![API Screenshot](https://github.com/cozyrosy/GI-csv-upload/blob/master/api_response.PNG)


## Running Tests
To run the test cases:
```
python manage.py test
```
![API Screenshot](https://github.com/cozyrosy/GI-csv-upload/blob/master/test.PNG)

## Author
👤 Rose Grace Jacob

📧 gracejacob.rose@gmail.com

🔗 https://www.linkedin.com/in/rose-grace-jacob-b0307822b/
