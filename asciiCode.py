
from tkinter import *
import os
import requests


#nums = []


def open_file():
	with open('text.txt', 'r') as line:
		nums = []
		file_text = line.read()
		for char in file_text:
			num = str(ord(char))
			nums.append(num)
		return nums

def write_file(nums):
	with open('table.txt', 'w') as file:
		count = 0
		line = "	db.b "
		for num in nums:
			line += num + ","
			count += 1
			if count > 8:
				l = len(line)
				line = line[:l-1]
				file.write(line + "\n")
				line = "	db.b "
				count = 0

def process_file():
	nums = open_file()
	print(nums)
	write_file(nums)

window = Tk()
window.title("ASCII Encoder")
window.config(padx=20, pady=20)


read_button = Button(text="Read File", command=process_file)
read_button.grid(row=2, column=1)

window.mainloop()