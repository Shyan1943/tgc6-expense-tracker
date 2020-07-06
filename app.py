from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)

# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = "pra_expense"

# read in the SESSION_KEY variable from the operating system environment
# SESSION_KEY = os.environ.get('SESSION_KEY')

# set the session key
# app.secret_key = SESSION_KEY

# START WRITING YOUR CODE
@app.route("/")
def home():
    return "Welcome Home"

# C
@app.route("/expense/create")
def expense_create_form():
    return render_template("expense_create_form.template.html")

@app.route("/expense/create", methods=["POST"])
def expense_create_form_process():
    expenditure_name = request.form.get("expenditure_name")
    date = request.form.get("date")
    transaction_type = request.form.get("transaction_type")
    reconciled = request.form.get("reconciled")

    client[DB_NAME].expense.insert_one({
        "expenditure_name" : expenditure_name,
        "date" : datetime.datetime.strptime(date, "%Y-%m-%d"),
        "transaction_type" : transaction_type,
        "reconciled" : reconciled
    })

    return "Created"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
