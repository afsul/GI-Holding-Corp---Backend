Prerequisites
Python 3.11.7

Installation

Clone the repository:
git clone https://github.com/afsul/GI-Holding-Corp---Backend.git

Create a virtual environment:
python -m venv env

Activate the virtual environment:
On Windows:
.\env\Scripts\activate

On macOS and Linux:
source env/bin/activate

Install dependencies:
pip install -r requirement.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application at http://localhost:8000
