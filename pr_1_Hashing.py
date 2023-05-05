def initializeHashTable():
    size = int(input('Enter size of hash table: '))
    hashtable = [[-1, 'null'] for i in range(size)]
    print('Hashtable of size', size, 'is successfully created .....')
    return(size, hashtable)

print('Menu')
print('1. Linear Probing')
print('2. Double Hashing')
print('3.Exit')
choice = int(input('Enter your choice: '))
count = 0

if choice == 1:
    size, hashtable = initializeHashTable()
    choice1 = 1
    while(choice1 != 4):
        print('Menu')
        print('1.Insert')
        print('2.Search')
        print('3.Display')
        print('4.Back')
        choice1=int(input('Enter your choice: '))
        if choice1 == 1:
            if(count == size):
                print('Hash table is Full .........')
            else:
                number = int(input('Enter number: '))
                name = input('Enter Name: ')
                hashvalue = number % size
                while(hashtable[hashvalue][0] != -1):
                    print('Collision has occured ..... calculating new hash value....')
                    hashvalue = (hashvalue + 1)%size
                hashtable[hashvalue][0] = number
                hashtable[hashvalue][1] = name
                count += 1
                print('Data is successfully inserted in the hash table ....Total inserted: ', count)
        if choice1 == 2:
            number = int(input('Enter number to search: '))
            hashvalue = number % size
            comparision = 0
            while(hashtable[hashvalue][0] != number and comparision < size):
                hashvalue = (hashvalue + 1)%size
                comparision += 1
            if comparision < size:
                print('The number', number, 'is found at location', hashvalue, 'with comparisions', comparision+1)
            else:
                print('The number is NOT found in the hashtable.... with comparisions', comparision+1)
        if choice1 == 3:
            for i in range(size):
                print('Hash Value ', i, end = " -> ")
                print(hashtable[i])
