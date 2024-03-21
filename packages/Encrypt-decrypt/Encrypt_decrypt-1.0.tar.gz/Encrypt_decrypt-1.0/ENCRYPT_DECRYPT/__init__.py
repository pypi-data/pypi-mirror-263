def encrypt(file):
    
    #Getting the message from user
    print()
    print('------------------------------Incryption Program---------------------------------\n')

    mess = input('Enter message :')

    #Converting the message into ASCII code
    words = [j for i in mess for j in i]

    int_lst = []
    for i in words:
        if isinstance(i, int):  
            int_lst.append(i)
        elif isinstance(i, str):
            if i.isdigit():
                int_lst.append(int(i))
            elif i.isalpha():
                int_lst.append(ord(i))
            elif i.isspace(): 
                int_lst.append(ord(i))

                
    #Encrpting the message
    incryp_lst = []
    increament = 967
    for j in int_lst:
        temp_n_lst = j + increament
        increament +=247
        incryp_lst.append(str(temp_n_lst))

    #Writing the file
    f = open(file,'w')
    w_row = f.write(' '.join(incryp_lst))
    f.close()
    #Printing the file
    print()
    print('Your message is successfully encrypted and stored in',file)
    print()
    print('Message Key : ',end='')
    for list in incryp_lst:
        print(list,end=' ')


def decrypt():

    #User chosing
    print()
    print('------------------------------Decryption Program---------------------------------\n')
    print('1)Enter Message Key \n')
    print('2)Enter file name \n')
    choice = input('Enter your choice:')
    print()
    
    #Decision making: key or file
    #If press 1
    if choice == '1':
        #Converting the Key into list
        f2 = input('Enter the Key :')
        splitted_f2 = f2.split()
        int_splitted_f2 = [int(i) for i in splitted_f2]
        
        #Decrypting : Layers ---> Real value
        decryp_lst_1 = []

        for i in range(len(int_splitted_f2)):
            Decreament_1 = 967 + (247*i)
            temp_de_list_1 = int_splitted_f2[i] - Decreament_1
            decryp_lst_1.append(temp_de_list_1)

        #Decrypting : Real value ---> Words
        de_words_1 = []
        for words in decryp_lst_1:
            int_2_words_1 = chr(words)
            de_words_1.append(int_2_words_1)

        #Printing the Message
        print()
        print('Decrypted Messsage :',end='')
        for i in de_words_1:
            print(i,end='')
        
    #If press 2   
    elif choice == '2':
        #Getting the file
        f1 = input('Enter file name :')
 
        #Reading the file 
        f = open(f1,'r')
        reads = f.read()
        splitted_read = reads.split()
    
        #Converting string elements into integers
        int_list = [int(i) for i in splitted_read]

        #Decrypting : Layers ---> Real value
        decryp_lst = []
    
        for i in range(len(int_list)):
            Decreament = 967 + (247*i)
            temp_de_list = int_list[i] - Decreament
            decryp_lst.append(temp_de_list)
    
        #Decrypting : Real value ---> Words
        de_words = []
        for words in decryp_lst:
            int_2_words = chr(words)
            de_words.append(int_2_words)
    
        #Printing the Message
        print()
        print('Decrypted message :',end='')
        for i in de_words:
            print(i,end='')
    
    #else 
    else:
        print(f"Enter valid operation")

decrypt()