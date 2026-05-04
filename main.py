def student(name,rollno,age,branch="CSE"):# mahender
    print("my name is",name)
    print("my rollno is",rollno)
    print("my age is",age)
    print("my branch is",branch)
    print()


student("Mahender",1,21,"AI")
student(rollno=2,name="SIVA",age=19)
student("Shruthi",3,25)


def sum(*arr):
    s=0
    for i in arr:
        s+=i
    print(s)
    print(arr)

sum(10,20,30)
sum(10,20,30,30,23,2,2,3,4,24,2,45,24)
sum(10)


def display(**document):
    print(document)
display(name="anil",age=30,branch="CSE",address="UPPAL")
display(name="siva",age=20)
display(name="shruthi",age=35,pincode=500039)