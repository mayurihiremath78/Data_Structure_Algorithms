list=[]
def insert():
    n=int(input("Enter no elements to be inserted:"))
    for i in range(n):
        ele=int(input())
        list.append(ele)
    print("Element inserted successfully!")
def remove():
    print("Enter elements to be removed:")
    key=int(input())
    list.remove(key)
    print("Element removed successfully!")
def search():
    key=int(input("Enter element to be search:"))
    for i in list:
        if(key==i):
            print("Element Found!")
        else:
            print("Not found")
def size():
   print("Elements of list:",len(list))

def intersection(list1,list2):
    #intersect=[]
    # list1=[]
    # list2=[]
    n = int(input("Enter no of elements you want to add in list1:"))
    for i in range(n):
        key = int(input("Enter ele:"))
        list1.append(key)
    n2 = int(input("Enter no of elements you want to add in list2:"))
    for i in range(n2):
        key = int(input("Enter ele:"))
        list2.append(key)

    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i]==list2[j]):
                print("Intersection of list 1 and list 2:",list1[i])

def union():
    list3=[]
    n = int(input("Enter no of elements you want to add in list1:"))
    for i in range(n):
        key = int(input("Enter ele:"))
        list1.append(key)
    n2 = int(input("Enter no of elements you want to add in list2:"))
    for i in range(n2):
        key = int(input("Enter ele:"))
        list2.append(key)
    for i in range(len(list1)):
        list3=list1+list2
    print(list3)

def diff():
    list3=[]
    n = int(input("Enter no of elements you want to add in list1:"))
    for i in range(n):
        key = int(input("Enter ele:"))
        list1.append(key)
    n2 = int(input("Enter no of elements you want to add in list2:"))
    for i in range(n2):
        key = int(input("Enter ele:"))
        list2.append(key)
    list3=list1-list2
    print(list3)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ch=1
    list1 = []
    list2 = []
    while(ch!=8):
        print('1.Insert')
        print('2.Remove')
        print('3.Search')
        print('4.Size')
        print('5.Intersection of 2 list')
        print('6.Union')
        print('7.Difference')
        print('8.Exit')
        ch=int(input('Enter choice:'))

        if(ch==1):
            insert()
        elif(ch==2):
            remove()
        elif(ch==3):
            search()
        elif(ch==4):
            size()
        elif(ch==5):

            intersection(list1,list2)

        elif(ch==6):

            union()

        elif(ch==7):

            diff()

        else:
            print("Enter valid choice!!")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
