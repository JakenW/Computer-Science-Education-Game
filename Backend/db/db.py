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
         DIFFICULTY           TEXT    NOT NULL,
         QUEST           TEXT    NOT NULL,
         MCO1           TEXT    NOT NULL,
         MCO2           TEXT    NOT NULL,
         MCO3           TEXT    NOT NULL,
         MCO4           TEXT    NOT NULL,
         ANSWER           TEXT    NOT NULL);''')

print("table created successfully")