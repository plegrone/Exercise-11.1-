#Set the count value to zero and open the text file containing the words that will be used as keys in the dictionary
count = 0
with open('words.txt') as listwords:
  words_lines = listwords.readlines()

#Build a table with words from the text file by appending them into the table
words_table = []
for word in words_lines:
    words = word.split()
    for word in words:
      words_table.append(word)

#Create a dictionary and add the words as keys with a value of 1 for each key
#Increase the count by 1 as each key is added to the dictionary to check if all words have been included
dict = {}
for word in words_table:
  if word not in dict:
    dict[word] = 1
    count = count +1
  else:
    dict[word] = 1
    count = count + 1

#Check that the count is equal to the total words in the text file
print(count)

#This function checks if a key is in the dictionary and returns the value associated with it 
def checkKey(dict, key): 
      
    if key in dict: 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  
#Checks for a couple of keys that are word entries in the text file and returns the value sassociated with each if found  
key = 'aa'
checkKey(dict, key) 
  
key = 'zoo'
checkKey(dict, key)

key = 'foo'
checkKey(dict, key) 
