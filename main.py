# Importing Flask
from flask import Flask

# Create a flask instance
app = Flask(__name__)

# Load all of the routes
import routes

# Launching the server in debug mode
if __name__ == '__main__':
    app.run(debug=True)