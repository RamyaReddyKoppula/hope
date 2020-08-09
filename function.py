#def world(name):
    #print("my world is my brother "+ name)
#world("chandu")
#def add(a, b):
    #return a+b
#c = add(3, 5)
#print(c)

def underline(text):
    "\n" + text + "\n"+"=" *len(text)+ "\n"
def person(student, format):
    text = " "
    for i in student:
        name = i["name"]
        rollnum = i["rollnum"]
        text += underline(name)+rollnum+"\n"
        return text.strip()
qualities = [{
    "name" : "Ramya",
    "rollnum" : 25
},
{
    "name" : "chandu",
    "rollnum" : 21
}]
person(qualities, format=underline)
print(person)
