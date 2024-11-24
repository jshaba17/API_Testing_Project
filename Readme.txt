# API Testing Project

This project is designed to test REST APIs and generate test results in HTML format using the `pytest` testing framework. 
The project verifies the functionality of API endpoints such as fetching, creating, updating, and deleting resources.



Before running the project, ensure the following tools are installed on your system:

1. **Python** (version 3.9 or above)
2. **pip** (Python package manager)



 Setup Instructions

1. **Clone the Repository**  
   Download the project files to your local system.

2. **Install Dependencies**  
   Run the following command to install the required Python libraries:  
   pip install -r requirements.txt
 
3. **Verify the Setup**  
Ensure that the project structure is as follows:
API_Testing_Project/ 
├── tests/ │ ├── test_api.py 
├── utils/ │ ├── api_helper.py 
├── reports/ 
├── requirements.txt

 Running Tests

1. **Run All Tests**  
Use the following command to execute all tests and generate an HTML report:  
pytest --html=reports/test_report.html


2. **View the Report**  
After running the tests, open the `test_report.html` file in the `reports/` directory using any web browser to view the results.

---

## Features Tested

1. **Fetch API Endpoints**  
- Retrieve a list of resources.  
- Fetch a resource by ID.

2. **Create API Endpoints**  
- Add new resources with proper validation.

3. **Update API Endpoints**  
- Modify existing resources.

4. **Delete API Endpoints**  
- Remove resources and handle errors for invalid IDs.

---

## Project Files

- `tests/test_api.py`: Contains all test cases for API endpoints.
- `utils/api_helper.py`: Helper functions to make API requests.
- `requirements.txt`: List of required Python libraries.
- `reports/`: Directory where the HTML test reports are saved.

  

