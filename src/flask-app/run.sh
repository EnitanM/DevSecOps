#create virtual environment
python3 -m venv venv
source venv/bin/activate

#install dependencies
pip install -r requirements.txt

#run tests
pytest tests.py

#run the app
python app.py