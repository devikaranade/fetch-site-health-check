# fetch-site-health-check
This repository contains a Python script to monitor and evaluate the health status of various HTTP endpoints specified in a YAML configuration file. The script periodically tests endpoint availability and calculates their respective availability percentages, providing insights into their overall health.

Requirements:
- Python 3.x
- requests library (install using pip install requests)
- PyYAML library (install using pip install PyYAML)

Usage
Clone Repository: Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/devikaranade/fetch-site-health-check.git
Install Dependencies: Make sure you have Python installed. Install the required libraries using pip.

bash
Copy code
pip install requests PyYAML
Run the Script: Execute the Python script with the YAML file path as an argument.

bash
Copy code
python3 assessment.py input.yaml
Output: The script tests endpoint availability every 15 seconds and prints the availability percentage for each domain to the console.

File Structure
assessment.py: Main Python script that checks endpoint health.
input.yaml: Sample YAML file containing a list of HTTP endpoints for testing.

Contributors
Devika Ranade
