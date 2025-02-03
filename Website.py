from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route to display your name
@app.route('/')
def home():
    return '<h1>Abhiuday Maurya</h1>'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
