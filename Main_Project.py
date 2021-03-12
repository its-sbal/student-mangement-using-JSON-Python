
import json

s_lst = []
t_lst = []
def add_Student(id,name,grade,m1,m2,m3,m4,m5):
    f = open("STUDENT.txt","a")
    l = {"id":id,"name":name,"grade":grade,"m1":m1,"m2":m2,"m3":m3,"m4":m4,"m5":m5}
    d = json.dumps(l)
    f.write(d)
    f.write("\n")
    f.close()
def add_Teacher(id,name,grade,subject):
    f = open("TEACHER.txt","a")
    l = {"id":id,"name":name,"grade":grade,"subject":subject}
    d = json.dumps(l)
    f.write(d)
    f.write("\n")
    f.close()
def search_Student():
    with open("STUDENT.txt",'r') as file:
        for data in file:
            d = json.loads(data)
            s_lst.append(d)
    id = int(input("Enter id of student : "))
    i=-1
    for student in s_lst:
        i+=1
        if(student["id"]==id):
            print("Name : ",student["name"],"Grade : ",student["grade"], "Marks : ",student["m1"],student["m2"],student["m3"],student["m4"],student["m5"])
            return i
def search_Teacher():
    with open("TEACHER.txt",'r') as file:
        for data in file:
            d = json.loads(data)
            t_lst.append(d)
    id = int(input("Enter id of student : "))
    i=-1
    for teacher in t_lst:
        i+=1
        if(teacher["id"]==id):
            print("Teacher found")
            return i
def update_S():
    l = search_Student()
    print("l = ",l)
    s_lst[l]["m1"]=int(input("Enter marks for m1: "))
    s_lst[l]["m2"]=int(input("Enter marks for m2: "))
    s_lst[l]["m3"]=int(input("Enter marks for m3: "))
    s_lst[l]["m4"]=int(input("Enter marks for m4: "))
    s_lst[l]["m5"]=int(input("Enter marks for m5: "))

    with open("STUDENT.txt",'w') as file:
        d = json.dumps(s_lst)
        d=d.replace('[',"")
        d=d.replace(']',"")
        d= d.replace("}, ","}\n")
        file.write(d)
    print("Data Updated Successfully\n")
def delete_S():
    with open("STUDENT.txt",'r') as file:
        s_lst=[]
        for data in file:
            d = json.loads(data)
            s_lst.append(d)
        id = int(input("Enter id of student : "))
    i=-1
    for student in s_lst:
            i+=1
            if(student["id"]==id):
                break
    s_lst.pop(i)
    with open("STUDENT.txt",'w') as file:
            d = json.dumps(s_lst)
            d=d.replace('[',"")
            d=d.replace(']',"")
            d= d.replace("}, ","}\n")
            file.write(d)
    print("Data Updated Successfully\n")
def password(p):
    flag = True
    d = ["At least 1 letter between [a-z]","At least 1 number between [0-9]","At least 1 letter between [A-Z]","At least 1 special chacter from [!@\#$%&]","Minimum length of pword: 6","Maximum length of pword: 12"]
    s_char = "!@#$%&"
    if not any(ch.islower() for ch in p):
        print(d[0])
        flag=False
    if not any(ch.isupper() for ch in p):
        print(d[2])
        flag=False
    if not any(ch.isdigit() for ch in p):
        print(d[1])
        flag=False
    if not any(ch in s_char for ch in p):
        print(d[3])
        flag=False
    if(len(p)<6):
        print(d[4])
        flag=False
    if(len(p)>12):
        print(d[5])
        flag=False
    if(flag):
        return "Valid"
    else:
        return "notValid"
def login():
    print("--------------------------------Welcome to STUDENT MANGEMENT Portal-------------------------------")
    n = int(input("Choose Options\n1.Log In\n2.Sign Up\n"))
    if(n==1):
        un = input("Enter username : ")
        pa = input("Enter Password : ")
        for line in open("login.txt","r").readlines():
            data = line.strip().split(",")
            if( un==data[0] and pa==data[1] and data[2]=="A"):
                return 1
            elif(un==data[0] and pa==data[1] and data[2]=='T'):
                return 2
            elif(un==data[0] and pa==data[1] and data[2]=='S'):
                return 3
        print("Invalid Login")
    elif(n==2):
        v = input("Who are you :\n[T] - Teacher\n[S] - Student ")
        id = input("Enter new username : ")
        while(True):
            pa = input("Enter new password : ")
            p = password(pa)
            if(p=="Valid"):
                print("Account Created ")
                with open("login.txt","a") as file:
                    file.write(id+","+pa+","+v)
                login()
                break
            else:
                pass

def main():
    l = login()
    if(l==1):
        print("\nWelcome Admin\n")
        while(True):
            n = int(input("Choose :\n1.Add new Student\n2.Add new teacher\n3.Search Student\n4.Search teacher\n5.Update Student Data\n6.Update Teachers Data\n7.Delete Student Data\n8.Delete Teachers Data\n9.Quit"))
            if n ==1:
                id = int(input("\nId : "))
                name = input("\nName : ")
                grade = int(input("\nGrade : "))
                m1 = int(input("Marks 1 -"))
                m2 = int(input("Marks 2 -"))
                m3 = int(input("Marks 3 -"))
                m4 = int(input("Marks 4 -"))
                m5 = int(input("Marks 5 -"))
                add_Student(id,name,grade,m1,m2,m3,m4,m5)
            elif n==2:
                id = int(input("\nId : "))
                name = input("\nName : ")
                grade = int(input("\nGrade : "))
                subject = input("\nSubject - ")
                add_Teacher(id,name,grade,subject)
            elif n==3:
                search_Student()
            elif n==4:
                search_Teacher()
            elif n==5:
                update_S()
            elif n==7:
                delete_S()
            elif n==9:
                exit()

    elif(l==2):
        print("Welcome Teacher\n")
        while(True):
            n = int(input("Choose Options : \n1.Search Student\n2.Search Teacher\n3.Update Student Data\n4.Delete Student Data\n5.Quit"))
            if n ==1:
                search_Student()
            elif n==2:
                search_Teacher()
            elif n==3:
                update_S()
            elif n==4:
                delete_S()
            elif n==5:
                exit()
    elif(l==3):
        print("Welcome Student\n")
        while(True):
            n = int(input("Choose Options : \n1.Search Student\n2.Quit"))
            if n ==1:
                search_Student()
            elif n ==2:
                exit()
            else:
                print("Invalid Input")

main()

