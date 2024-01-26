from __main__ import app 
from flask import render_template, request, redirect, url_for
from database import database
from datetime import datetime

# Initialize the database
db = database()

# Define the route
@app.route("/")
def index():
    # Send the HTML page to the user. This file is located in the templates folder
    return render_template("index.html", page="home")

# About page
@app.route("/about")
def about():
    return render_template("about.html", page="about")

# Messages page
@app.route("/messages")
def messages():
    # Get data
    data = db.query("""
                    SELECT message_id, message_title, message_content, message_date
                    FROM message_tbl
                    """)
    # Send to the user
    return render_template("messages.html", data=data, page="messages")

# Adding a new message. Notice how the POST method has been added
@app.route("/messages/add", methods=["GET", "POST"])
def add_message():
    # Only execute if the user is adding an item to the database
    if request.method == "POST":
        # Fetch the details
        title = request.form["title"]
        message = request.form["message"]
        # Add them to the database
        db.update("""
                  INSERT INTO message_tbl (message_title, message_content, message_date) 
                  VALUES (?, ?, ?)""", 
                  [title, message, datetime.now()])

    # Send the user back to the messages page
    return redirect(url_for("messages"))

# Removing a message. The <id> will enable a user to pass in a
# number into the URL. We can crossmatch this to the database
# to remove a specific message.
@app.route("/messages/remove/<id>")
def remove_message(id):
    # Remove the message from the database
    db.update("""
            DELETE FROM message_tbl WHERE message_id = ?"""
            , [id])
    
    # Send the user back to the messages page
    return redirect(url_for("messages"))