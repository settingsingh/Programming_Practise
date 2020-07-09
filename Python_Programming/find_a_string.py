'''
Output the integer number indicating the total number of 
occurrences of the substring in the original string.

Solution : Sliding Window Method 
'''
#taking the main string and the sub-string as input
#strip() method removes the white spaces from both the ends
string, sub_string = (input().strip(), input().strip())
count = 0

#taking a window of length equal to length of the sub-string
#and sliding it through the main string to count the occurences
for i in range(len(string) - len(sub_string) + 1):
    if string[i : i + len(sub_string)] == sub_string:
        count = count + 1

print("Total number of occurences of {} is {}".format(sub_string, count))
