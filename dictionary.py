#Q1-Basic Access
#Create a dictionary called person with keys "name", "age", and "city".
#Fill them with your own details.
#Print the value of "city".
person = {"name":"Fiza","age":19,"city":"london"}
print(person["city"])

#Q2 — Add & Update
#You have this dictionary:
#student = {"name": "Ali", "age": 20}
#Add a key "course" with value "Python".
#Update "age" to 21.
#Print the updated dictionary.

student = {"name": "Ali", "age": 20}
student["age"]=21    #updating
student["course"]="python"  #add

#Q3 — Counting Words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_dict = {}
for word in words:
    if word not in count_dict:
        count_dict[word] = 1
    else:
        count_dict[word] += 1
print(count_dict)

#Q4 — Loop Through Dictionary
marks = {"Math": 90, "Science": 85, "English": 88}
for key,value in marks.items():
    print(key,":",value)