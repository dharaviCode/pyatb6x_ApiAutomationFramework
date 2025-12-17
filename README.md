# Python API Automation testing Framework
![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)
A Hybrid Custom API Automation Framework built using Python and PyTest, designed for scalable, maintainable, and high-quality API testing.
This framework supports parallel execution, data-driven testing, schema validation, and rich reporting using Allure.

📌 Key Features

Modular and scalable framework design

Hybrid approach (data-driven + reusable utilities)

Supports REST API testing

Parallel execution for faster feedback

Schema validation for response contracts

Allure reporting for rich test insights

Easy integration with CI/CD pipelines

🗂️ Project Structure

The framework follows a clean and industry-standard folder structure to ensure maintainability and extensibility.

.
├── tests/
│   ├── crud/
│   │   ├── test_create_booking.py
│   │   ├── test_update_booking.py
│   │   └── test_delete_booking.py
│   ├── conftest.py
│
├── utils/
│   ├── api_client.py
│   ├── config_reader.py
│   ├── data_loader.py
│   └── logger.py
│
├── test_data/
│   ├── csv/
│   ├── excel/
│   └── json/
│
├── schemas/
│   └── booking_schema.json
│
├── allure_results/
│
├── requirements.txt
└── README.md

📷 Refer to the attached screenshot for a visual overview of the structure.

🧰 Tech Stack
Tool / Library	Purpose
Python 3.12	Programming Language
Requests	HTTP client for API calls
PyTest	Test execution framework
Allure PyTest	Advanced test reporting
Faker	Dynamic test data generation
JSONSchema	API response validation
PyTest-xdist	Parallel test execution
📦 Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd python-api-automation-framework

2️⃣ Install Required Packages
pip install requests pytest pytest-html faker allure-pytest jsonschema

3️⃣ Install Parallel Execution Plugin
pip install pytest-xdist

▶️ How to Run Tests
🔹 Run a Single Test
pytest tests/tests/crud/test_create_booking.py -s

🔹 Run Tests with Allure Reporting
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s

🔹 Generate & View Allure Report
allure serve allure_result

⚡ Parallel Execution

Run tests in parallel to reduce execution time:

pytest -n 4 --alluredir=allure_result


-n 4 → Runs tests using 4 parallel workers

📊 Reporting

Allure Reports provide:

Step-wise execution details

Request & response logs

Failure screenshots/logs (if integrated)

Test trends and history

🧪 Test Data Management

This framework supports data-driven testing using:

📄 CSV files

📊 Excel files

🧾 JSON files

🎲 Dynamic data using Faker

✅ Advanced API Validation

JSON Schema validation using jsonschema

Status code verification

Response payload assertions

Header and contract validation

🔄 CI/CD Ready

The framework is designed to be easily integrated with:

GitHub Actions

Jenkins

Azure DevOps

GitLab CI

👨‍💻 Author

Avinash Kumar
Senior Software Test Engineer | Quality Engineering
Python • API Automation • Test Architecture

📌 Future Enhancements

OAuth & token-based authentication handling

Retry mechanism for flaky APIs

Environment switching (QA / Stage / Prod)

Docker support

Custom HTML reporting

⭐ Contributing

Contributions, improvements, and suggestions are welcome.
Please follow best coding and testing practices while contributing.

📄 License

This project is for learning and internal automation practice purposes.