from tkinter import *
import os
import requests
import smtplib




def open_File():
    a = False
    try:
        with open("a_file.txt") as file:
            file.read()
    except:
        print("Fail")
