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
    return render_template("game.html")


#Route play the nonogram puzzles 
@app.route("/puzzletest/")
def puzzletest():
    con = sql.connect("dormagoo.db")
    cur = con.cursor()
    cur.execute("select * from PUZZLES where ID = ?", (1, ))
    testPuzzle = cur.fetchone()
    
    #Obtain data from the db and make it integer lists
    puzzleRowList = []
    for i in range(len(testPuzzle)):
        if(i == 0):
            continue
        else:
            currentRow = testPuzzle[i].split(" ")
            currentRow = list(map(int, currentRow))
            puzzleRowList.append(currentRow)
            
    return render_template("puzzletest.html", puzzle = puzzleRowList)

#This route allows the user to create questions which get added to the database
@app.route("/createquestion/", methods=["POST", "GET"])
def createquestion():
    #If the request method is post, we want to verify input info with account database
    if request.method == "POST":
        #These lines extract user data from the form
        question = request.form["question"]           #question
        mco1 = request.form["mco1"]                   #option 1
        mco2 = request.form["mco2"]                   #option 2
        mco3 = request.form["mco3"]                   #option 3
        mco4 = request.form["mco4"]                   #option 4
        answer = request.form["answer"]               #correct answer
        
        #remove potential trailing white space on the answer to check if it is an acceptable answer
        answer = answer.strip()
        
        '''
        Iterate through a list of the possible correct answer choices a user
        could input. If the user's input is not a valid answer, redirect them
        to an unsuccessful page telling them they entered an invalid answer.
        
        Otherwise, continue to adding to the database
        '''
        possibleAnswers = ["1", "2", "3", "4"]
        isPossibleAnswer = False
        for i in range(len(possibleAnswers)):
            if(answer == possibleAnswers[i]):
                isPossibleAnswer = True
        
        if(isPossibleAnswer == False):
            return render_template("question_unsuccessans.html")

        #if we have nade it to this line, now add question to database with user input information
        con = sql.connect("dormagoo.db")
        cur = con.cursor()
        cur.execute("insert into QUESTIONS(QUEST, MCO1, MCO2, MCO3, MCO4, ANSWER) values (?,?,?,?,?,?)", (question, mco1, mco2, mco3, mco4, answer))
        con.commit()
        
        return render_template("question_confirm.html")
    
    return render_template("createquestion.html")
    
#This route tests the visual novel aspect created by Christina
@app.route("/VNtest")
def VNtest():
    return render_template("vntest.html")

#This route tests the question proposal aspect created by Christina
@app.route("/MCtest")
def MCtest():
    return render_template("mctest.html")

@app.route("/puzzletest2/")
def puzzletest2():
    con = sql.connect("dormagoo.db")
    cur = con.cursor()
    cur.execute("select * from PUZZLES where ID = ?", (1, ))
    testPuzzle = cur.fetchone()
    
    #Obtain data from the db and make it integer lists
    puzzleRowList = []
    for i in range(len(testPuzzle)):
        if(i == 0):
            continue
        else:
            currentRow = testPuzzle[i].split(" ")
            currentRow = list(map(int, currentRow))
            puzzleRowList.append(currentRow)
    
    #Generate the labels needed for the puzzle
    xLabels = createXLabels(puzzleRowList)
    yLabels = createYLabels(puzzleRowList)
    
    return render_template("puzzletest2.html", puzzle = puzzleRowList, xLabs = xLabels, yLabs = yLabels)




#These functions are used to generate the text labels for the puzzle
'''
Given a nonogram puzzle, this function dynamically
creates the necessary Y-axis labels for the puzzle
'''    
def createYLabels(p):
    YLabels = []
    for row in p:
        #print(row)
        curRowLab = ""
        curLabVal = 0
        for i in range(len(row)):
            #print(row[i])
            if(row[i] == 1):
                curLabVal += 1
            if(row[i] == 0):
                if(curLabVal != 0):
                    curRowLab += str(curLabVal) + " "
                    curLabVal = 0
            #do something here to remove any potential extra spaces on end
            if(i == len(row)-1 and curLabVal == 0):              
                rowLength = len(curRowLab)
                if(rowLength == 0):
                    curRowLab += str(curLabVal)
                else:
                    rowLength -= 1
                    if(curRowLab[rowLength] == " "):
                        curRowLab = curRowLab[:rowLength]
            
            if(i == len(row)-1 and curLabVal != 0):
                curRowLab += str(curLabVal)
                
        YLabels.append(curRowLab)
    #print("Y Labels:", YLabels)
    return YLabels

'''
Given a nonogram puzzle, this function dynamically
creates the necessary X-axis labels for the puzzle
'''    
def createXLabels(p):
    XLabels = []
    #print(len(p))
    #print(p[0][0])

    for i in range(len(p)):
        curRowLab = ""
        curLabVal = 0
        for j in range(len(p[i])):
            #print(p[j][i], i, j)
            if(p[j][i] == 1):
                curLabVal += 1
            if(p[j][i] == 0):
                if(curLabVal != 0):
                    curRowLab += str(curLabVal) + " "
                    curLabVal = 0
            
            #do something here to remove any potential extra spaces on end
            if(j == len(p[i])-1 and curLabVal == 0):
                rowLength = len(curRowLab)
                if(rowLength == 0):
                    curRowLab += str(curLabVal)
                else:
                    rowLength -= 1
                    if(curRowLab[rowLength] == " "):
                        curRowLab = curRowLab[:rowLength]
            
            if(j == len(p[i])-1 and curLabVal != 0):
                curRowLab += str(curLabVal)
                
        XLabels.append(curRowLab)
        
    #print("X Labels:", XLabels)
    return XLabels


#This drives the program by Running the Flask App
if __name__ == "__main__":
    app.run(debug=True)
