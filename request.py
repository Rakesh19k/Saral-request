import requests,os
import json

url=requests.get("http://saral.navgurukul.org/api/courses")

if  os.path.exists("courses.json"):
	f=open("courses.json","r")
	read=f.read()
	load=json.loads(read)
else:
	response=requests.get("http://saral.navgurukul.org/api/courses")
	new_file=open("courses.json","w")
	new_file.write(response.text)
	file_=open("courses.json","r")
	r=file_.readline(file_)
	load=json.loads(r)

print ("------------------------- Welcome to saral --------------------------")
print ("  ")
print ("-------------------- This is your courses name! -----------------------")
print ("  ")

def Frontcourse():
	number=1
	List_of_Id=[]
	for i in load["availableCourses"]:
		List_of_Id.append(i["id"])
		print(number," ",i["name"])
		number+=1
	return List_of_Id
List_of_Id=Frontcourse()
print ("   ")
user=int(input("Choose your course: "))
print ("  ")
link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercises")
load=link.json()
print ("------------------- This is your Exercises -------------------")
print ("  ")

slug_list=[]
child_Exercise=[]
def FrontExercise():
	count=1
	for j in load["data"]:
		print (count," ",j["name"])
		slug_list.append(j["slug"])
		child_Exercise.append(j["childExercises"])
		count+=1
		# print (child_Exercise)
	return slug_list
FrontExercise()
print ("  ")

user1=int(input("which slug you want: "))
slug_link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercise/getBySlug?slug="+str(slug_list[user1-1]))
slug=slug_link.json()
print ("----------------- This is content ------------------")
print ("   ")
print (slug["content"])

# if childExercises in slug:
def Front_childExercise():
	numbering=1
	child_slug=[]
	for k in child_Exercise[user1-1]:
		child_slug.append(k["slug"])
		print (numbering,k["name"])
		numbering+=1
		# print (child_slug)
		# print (k)
	return child_slug
child_slug=Front_childExercise()
# Front_childExercise()

select_question=int(input("enter the question number: "))
print (child_slug[select_question])

def Front():
	child_link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercise/getBySlug?slug="+str(child_slug[select_question-1]))
	child=child_link.json()
	print (child["content"])
Front()

	

def NextQuestion():
	user_input=int(input("Enter Next question: "))
	Next_link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercise/getBySlug?slug="+str(child_slug[user_input+-1]))
	Next=Next_link.json()
	# print (Next)
	print (Next["content"])
# NextQuestion()

def PreviousQuestion():
	Input=int(input("Enter Previous question: "))
	Previous_link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercise/getBySlug?slug="+str(child_slug[Input+-1]))
	Previous=Previous_link.json()
	# print (Previous)
	print (Previous["content"])
# PreviousQuestion()

while True:
	Choose=input("Enter the letter n  ya  p and e! If you want Next enter n , if you want Previous enter p and if you want Exit enter e: ")
	if "n" == Choose:
		NextQuestion()
	elif "p" == Choose:
		PreviousQuestion()
	elif "n" == Choose:
		print ("\n your current Exercise finished \n")
		break


















































































































































# import requests,os
# import json

# url=requests.get("http://saral.navgurukul.org/api/courses")

# if  os.path.exists("courses.json"):
# 	f=open("courses.json","r")
# 	read=f.read()
# 	load=json.loads(read)
# else:
# 	response=requests.get("http://saral.navgurukul.org/api/courses")
# 	new_file=open("courses.json","w")
# 	new_file.write(response.text)
# 	file_=open("courses.json","r")
# 	r=file_.read(file_)
# 	load=json.loads(r)

# print ("------------------------- Welcome to saral --------------------------")
# print ("  ")
# print ("-------------------- This is your courses name! -----------------------")
# print ("  ")


# number=1
# List_of_Id=[]
# for i in load["availableCourses"]:
# 	List_of_Id.append(i["id"])
# 	print(number," ",i["name"])
# 	number+=1
# print ("   ")
# user=int(input("Choose your course: "))
# print ("  ")
# link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercises")
# load=link.json()
# print ("------------------- This is your Exercises -------------------")
# print ("  ")

# slug_list=[]
# count=1
# for j in load["data"]:
# 	print (count," ",j["name"])
# 	slug_list.append(j["slug"])
# 	count+=1

# print ("  ")
# user1=int(input("which slug you want: "))
# slug_link=requests.get("http://saral.navgurukul.org/api/courses/"+str(List_of_Id[user-1])+"/exercise/getBySlug?slug="+str(slug_list[user1-1]))
# slug=slug_link.json()
# print ("----------------- This is content ------------------")
# print ("   ")
# print (slug["content"])