
# with open('devops.txt', 'w') as line:
# 	# Reads a specific line of text in the file.
# 	line_text = c.readline()
# 	print(line_text)
nums = []


with open('text.txt', 'r') as line:
	file_text = line.read()
	for char in file_text:
		num = str(ord(char))
		nums.append(num)


	print(nums)


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

	print(line)
	# file.write(nums)
