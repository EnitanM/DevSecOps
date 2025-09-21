from flask import Flask
app = Flask(__name__)
team_number = 1 
@app.route('/')
def hello_world():
    return f'This is Team {team_number}\'s Flask app!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)