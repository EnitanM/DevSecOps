#create virtual environment
python3 -m venv venv
source venv/bin/activate

#install dependencies
pip install -r requirements.txt

#run tests
pytest tests.py

#ENV variables
APP_PORT=8082
APP_NAME="personalproject"
VERSION="latest"

#Build Docker image
docker build -t $APP_NAME:$VERSION .
# #Scan Docker image for vulnerabilities
# docker scout cves $APP_NAME:$VERSION --output report.txt

# #SBOM
# docker scout sbom $APP_NAME:$VERSION --output sbom.txt
