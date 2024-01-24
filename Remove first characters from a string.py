#create user defined variable to remove characters
def remove_character(string_input, n):
    string_output = string_input[n:]
    return string_output

#ask user for string
user_input = input("Enter a word: ")

#ask user for number n 
n = int(input("Enter the value of n: "))

#remove characters based on user input
result = remove_character(user_input, n)

#print result
print(f"New word after removing the first {n} letters:", result)