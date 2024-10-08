import re

def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    start = 0
    end = len(word) - 1
    while(start <= end):
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True
    pass

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    if(number_val <= 0):
        return []
    elif (number_val == 1):
        return [0]
    elif (number_val == 2):
        return [0,1]
    else:
        series = [0,1]
        a = series[0]
        b = series[1]
        for i in range(3, number_val+1):
            c = a + b
            a = b
            b = c
            if (c < number_val):
                series.append(c)
            else:
                break
        return series
        pass

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    return str1.lower().count(str2.lower())
    pass

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    sum_list = []
    if(len(list1) != len(list2)):
        return sum_list
    else:
        for i in range(len(list1)):
            sum_list.append(list1[i] + list2[i])
        return sum_list

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = input("Enter the password:- ")
    if(isValidPassword(password)):
        return password
    else:
        lab2Question5()

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    if(len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)):
        return True
    else:
        return False