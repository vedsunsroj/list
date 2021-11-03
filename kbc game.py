question_list = [
    "How many continents are there?",       
    "What is the capital of India?",    
    "NG mei kaun se course padhaya jaata hai?" 
]
options_list = [
["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
    ]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
	print(question_list[i])
	j=0
	while j<len(options_list):
		print(options_list[i][j])
		j+=1
	n=int(input("enter a solution"))
	if n==solution_list[i]:
		print("your answer is correct")
	else:
		print("your answer is wrong")
		break
	i+=1