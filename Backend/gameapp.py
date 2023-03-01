# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:31:31 2023

@author: theja
"""

from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3 as sql

#Creating the flask app
app = Flask(__name__)

#Creating a secret key for the flask app. Required when using sessions.
app.secret_key = "thebestsecretkeyintheworldyep100percentthebestnodoubt"


#Route to the homepage of the website
@app.route("/")
def home():
    return render_template("index.html")


#Route to create account with information specified by the user
@app.route("/register/", methods=["POST", "GET"])
def register():
    #If the request method is post, we want to obtain user's account info
    if request.method == "POST":
        
        #These lines extract user data from the form
        accName = request.form["accname"]           #account name
        accPass = request.form["accpass"]           #account password
        confPass = request.form["confpass"]         #confirm password
        
        str(accPass)
        str(confPass)
        
        '''
        Check to see if password fields match, if not direct them to 
        the unsuccessful page
        '''
        if(accPass != confPass):
            return render_template("register_fail.html")
        
        
        '''
        The lines below connect to the database and create a new user login
        in the database based on the user's data. If there is a user with 
        the name already, it will not allow the creation and direct them to
        the unsuccessful page.
        '''
        con = sql.connect("dormagoo.db")
        cur = con.cursor()
        cur.execute("select * from ACCOUNTS where ACCNAME = ?", (accName, ))
        nameResult = cur.fetchone()
        if(nameResult != None):
            return render_template("register_fail.html")
        
        
        '''
        Not in database + password matches, add to database
        '''
        cur.execute("insert into ACCOUNTS(ACCNAME, ACCPW) values (?,?)", (accName, accPass))
        con.commit()
        
        return render_template("register_confirm.html")
    
    else:
        #If the resuest is not a post, go to the original form
        return render_template("register.html")

#Route to login
@app.route("/login/", methods=["POST", "GET"])
def login():
    #If the request method is post, we want to verify input info with account database
    if request.method == "POST":
        #These lines extract user data from the form
        accName = request.form["accname"]           #account name
        accPass = request.form["accpass"]           #account password
        
        str(accPass)
        
        '''
        Connect to the database and pull information from accounts table
        based on the name given through the form. If there is not an account
        with the name, go to unsuccess page. If the password does not match
        the one stored in the database, go to the unsuccess page. Otherwise,
        if the account exists and the password is right, go to confirm page.
        '''
        con = sql.connect("dormagoo.db")
        cur = con.cursor()
        cur.execute("select * from ACCOUNTS where ACCNAME = ?", (accName, ))
        curAccount = cur.fetchone()
        
        if(curAccount == None):
            return render_template("login_fail.html")
        
        elif(accPass != curAccount[2]):
            return render_template("login_fail.html")
        
        else:
            return render_template("login_confirm.html")
    
    return render_template("login.html")
    
    #connect to db, fetch info from db, verify matching (if not go back to login main), let them in 
    
    
#Route to main game
@app.route("/play/")
def play():
    return render_template("balls.html")

#This drives the program by Running the Flask App
if __name__ == "__main__":
    app.run(debug=True)
    