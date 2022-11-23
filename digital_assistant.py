#
##Author: Radhey Ruparel
##Description: This program a very simplistic version of a digital assistant. The interface will be typed text on the python console. 
##Also, it will only be able to recognize to main types of commands. It will also remember and recall something that user asks it to.
#

#Required to import all the os functions and progam is able to locate the file
import os
os.chdir(os.path.dirname(__file__))


def loading_information_input(storage_memory):
    
    '''This function, opens and read the data from the da.txt file. Through reading the file, it stores the important
    data in to the storage_memory dictonary.
    This function has a paramter varable as storage_memory, which is a dictonary'''
    
    #This opens the file da.txt to read
    file_open=open('da.txt','r')
    
    #This for loop reads the content of the file line by line
    for line in file_open:
        #This strips the new line from the line, and makes one line split into three parts in a list
        information=line.rstrip('\n').split('|')
        #This stores a data from the file into a dictonary, with a key and value
        storage_memory[information[0]+' '+information[1]]=information[2]
    
    #This closes the da.txt file
    file_open.close()

def storaging_the_input(storage_memory,user_command):
    
    '''This function stores the data that the users inputs into a dictonary.
    This function has a paramter varable as storage_memory, which is a dictonary
    And another is user_command, which is the information which user is trying to store, which is the a string'''
    
    #This is for the present tense statements
    if 'is' in user_command:
        #This strips the new line from the user's information, and makes one line split into two parts in a list
        information=user_command.rstrip('\n').split('is ')
        #This stores a data from the user into a dictonary, with a key and value
        storage_memory[information[0]+'is']=information[1]
    
    #This is for the past tense statements
    elif 'was' in user_command:
        information=user_command.rstrip('\n').split('was ')
        storage_memory[information[0]+'was']=information[1]
    
    #This is for the future tense statements
    elif 'will be' in user_command:
        #This strips the new line from the user's information, and makes one line split into two parts in a list
        information=user_command.rstrip('\n').split('will be ')
        #This stores a data from the user into a dictonary, with a key and value
        storage_memory[information[0]+'will be']=information[1]

def retrieving_the_information(storage_memory,user_command):
    '''This function retrieves the information from the dictonary, which the user is trying to demand
    This function has a paramter varable as storage_memory, which is a dictonary
    And another is user_command, which is the information which user is trying to demand, which is the a string'''
    
    #This strips the question mark from the user's demand
    user_command=user_command.rstrip('?')
    
    #This is for the present tense statements
    if 'is' in user_command:
        #This strips the new line from the user's information, and makes one line split into two parts in a list
        information=user_command.rstrip('\n').split(' is ')
        #A variable to keep count of all the keys in the dictonary
        key_count_1=0
        #Giving the Key variable, the keys from the main dictonary
        for key in storage_memory:
            #Trying to match the key which the user's demand
            if information[1] in key:
                #Changing the comand to the presetive of DA
                if 'my' in information[1]:
                    #Replacing my to your in a string
                    information[1]=information[1].replace('my','your')
                #Changing the comand to the presetive of user
                elif 'your' in information[1]:
                    #Replacing your to my in a string
                    information[1]=information[1].replace('your','my')
                print('\nDA:',information[1],'is',storage_memory[key])
                break
            key_count_1+=1
        #If the information is not found in the dictonary, which the
        if len(storage_memory)==key_count_1:
            #A message that the DA doesn't know the information which the user is trying to demand
            print('\nDA: I don\'t know.')

    #This is for the past tense statements
    elif 'was' in user_command:
        #This strips the new line from the user's information, and makes one line split into two parts in a list
        information=user_command.rstrip('\n').split(' was ')
        #A variable to keep count of all the keys in the dictonary
        key_count_2=0
        #Giving the Key variable, the keys from the main dictonary
        for key in storage_memory:
            #Trying to match the key which the user's demand
            if information[1] in key:
                #Changing the comand to the presetive of DA
                if 'my' in information[1]:
                    #Replacing my to your in a string
                    information[1]=information[1].replace('my','your')
                #Changing the comand to the presetive of user
                elif 'your' in information[1]:
                    #Replacing your to my in a string
                    information[1]=information[1].replace('your','my')
                print('\nDA:',information[1],'was',storage_memory[key])
                break
            key_count_2+=1
        #If the information is not found in the dictonary, which the
        if len(storage_memory)==key_count_2:
            #A message that the DA doesn't know the information which the user is trying to demand
            print('\nDA: I don\'t know.')
    
    #This is for the future tense statements
    elif 'will be' in user_command:
        #This strips the new line from the user's information, and makes one line split into two parts in a list
        information=user_command.rstrip('\n').split('will be ')
        #A variable to keep count of all the keys in the dictonary
        key_count_3=0        
        #Giving the Key variable, the keys from the main dictonary
        for key in storage_memory:
            #Trying to match the key which the user's demand
            if information[1] in key:
                #Changing the comand to the presetive of DA
                if 'my' in information[1]:
                    #Replacing my to your in a string
                    information[1]=information[1].replace('my','your')
                #Changing the comand to the presetive of user
                elif 'your' in information[1]:
                    #Replacing your to my in a string
                    information[1]=information[1].replace('your','my')
                print('\nDA:',information[1],'will be',storage_memory[key])
                break
            key_count_3+=1
        #If the information is not found in the dictonary, which the
        if len(storage_memory)==key_count_3:
            #A message that the DA doesn't know the information which the user is trying to demand
            print('\nDA: I don\'t know.')

#Declaring the main function
def main():
    #This is the main dictonary, where all the data inputed will be stored
    storage_memory={}
    #Calling the this function, to store the data from the da.txt file into dictonary as a memory 
    loading_information_input(storage_memory)
    #DA Start up message
    print('DA: Hi there, let\'s talk. . .')
    #An infinte loop, so the user can have unlimated conversation with the DA
    while True:
        #User's input, which can be a command to store or recall information
        user_command=input('USER: ')
        #If the user is asking a question, which requries recalling information
        if '?' in user_command:
            #Calling this will print the out the information from the dictonary, which users commands
            retrieving_the_information(storage_memory,user_command)
        #If the user wan't to exit the DA
        elif 'bye' in user_command:
            #A good bye message from the DA
            print('\nDA: bye!')
            break #Breaking the infinite loop will close the program
        #If the user is trying to tell information to the DA
        else:
            #This function will store the infromation which the user is trying to tell
            storaging_the_input(storage_memory,user_command)
            #Telling the user that the infromation has been stored.
            print('\nDA: OK!')

#Calling the main function
main()