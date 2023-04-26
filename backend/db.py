# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:56:28 2023
@author: theja
"""

import sqlite3

conn = sqlite3.connect("dormagoo.db")

print("Databased opened")

conn.execute('''CREATE TABLE ACCOUNTS
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         ACCNAME           TEXT    NOT NULL,
         ACCPW           TEXT    NOT NULL);''')   
  
#MCO = Multiple Choice Option         
conn.execute('''CREATE TABLE QUESTIONS
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         QUEST           TEXT    NOT NULL,
         MCO1           TEXT    NOT NULL,
         MCO2           TEXT    NOT NULL,
         MCO3           TEXT    NOT NULL,
         MCO4           TEXT    NOT NULL,
         ANSWER           TEXT    NOT NULL);''')
       
conn.execute('''CREATE TABLE PUZZLES
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         ROW0           TEXT    NOT NULL,
         ROW1           TEXT    NOT NULL,
         ROW2           TEXT    NOT NULL,
         ROW3           TEXT    NOT NULL,
         ROW4           TEXT    NOT NULL,
         ROW5           TEXT    NOT NULL,
         ROW6           TEXT    NOT NULL,
         ROW7           TEXT    NOT NULL,
         ROW8           TEXT    NOT NULL,
         ROW9           TEXT    NOT NULL,
         ROW10           TEXT    NOT NULL);''')

print("table created successfully")
