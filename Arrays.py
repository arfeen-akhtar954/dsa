# Question 1: TO FIND THE LARGEST NUMBER IN AN ARRAY
# a=[5, 8, 2, 10, 7]
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest =i
# print("The largest number in the array is:", largest)

# Question 2: To find smallest number in the list
# a=[5, 8, 2, 10, 7]
# smallest=a[0]
# for i in a:
#     if i<smallest:
#         smallest=i
# print("The smallest number in the list is: ", smallest)

# Question 3: to find second largest number in the list.
# a=[10,9,8,7]
# largest=a[0]
# slargest=float('-inf')
# for i in a:
#     if i>largest:
#         slargest=largest
#         largest=i
#     elif i>slargest and i!=largest:
#         slargest=i
# print("The second largest number in the list is: ", slargest)

# Question 4: to find second smallest number
# a=[8,3,6,2,9,4]
# smallest=a[0]
# ssmallest=float('inf')
# for i in a:
#     if i<smallest:
#         ssmallest=smallest
#         smallest=i
#     elif i<ssmallest and i!=smallest:
#         ssmallest=i

# print("the second smallest element is : ", ssmallest)

# Question 5: to find list is sorted or not
# a=[1,2,6,4,5]
# for i in range(len(a)-1):
#     if(a[i]>a[i+1]):
#         print("unsorted")
#         break 
# else: 
#     print("sorted")

# Question 6: to reverse a list
# 1:
# a=[1,2,3,4,5]

# temp=[]
# for i in range(len(a)-1, -1, -1):
#     temp.append(a[i])
# print(temp)
# 2:
# a=[1,2,3,4,5]
# temp=0
# for i in range(0,1):
#     temp=a[0]
#     a[0]=a[4]
#     a[4]=temp
#     temp=a[1]
#     a[1]=a[3]
#     a[3]=temp

# print(a)

# 3:
# a=[1,2,3,4,5]
# temp=a[0]
# a[0]=a[4]
# a[4]=temp
# temp=a[1]
# a[1]=a[3]
# a[3]=temp

# print(a)

# Question 7: counting even number

# a=[3,6,8,2,9]
# count=0
# for i in a:
#     if i%2 == 0:
#         count=count+1
# print(count)

# Question 8: finding sum of elements
# a=[4,3,5,6,7]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# Question 9: count positive and negative num
# a=[-2,5,-1,7,3,-4]
# count=0
# for i in a:
#     if i<0:
#         count =count +1

# print(count)

# Question 10: find average
# a=[4,6,7,3,2]
# sum=0
# for i in a:
#     sum=sum + i

# avg=sum/len(a)
# print(avg)

# Question 11: find how many elements are greater than 5
# a=[3,8,2,9,5,7]
# count=0
# for i in a:
#     if (i>5):
#         count = count + 1
# print("no. of elements which greater than 5 is: ", count)

# Question 12: find how many times a number appears in the list
# a=[2,5,2,8,2,7,5]
# count=0
# n=int(input("enter a number for list for counting: "))
# for i in a:
#     if i==n:
#         count = count+1
# print(f"the number {n} is appered in the given list is {count} times")

# Question 13: to find duplicates
# a=[2,5,2,8,5,7,2]
# duplicates=[]
# for i in a:
#     count=0
#     for j in a:
#         if i==j:
#             count=count+1
#         if count>1:
#             if i not in duplicates:
#                 duplicates.append(i)
# print(duplicates)

# Question 14: find largest difference between two numbers
# a=[3,8,2,9,5,1]
# ldif=0
# for i in a:
#     for j in a:
#         if abs(i-j)>ldif:
#             ldif=abs(i-j)
# print(ldif)

# Question 15: find smallest difference between two numbers
# a=[3,8,2,9,5,1]
# sdif=float('inf')
# for i in a:
#     for j in a:
#         if i!=j and abs(i-j)<sdif:
#             sdif=abs(i-j)
# print(sdif)

# Question 16: find sum of all elements at even indices:
# a=[10,20,30,40,50,60]
# sum=0
# for i in range(0,6):
#     if i%2==0:
#         sum=sum+a[i]
# print(sum)

# Question 17: find sum of all elements at odd indices:
# a=[10,20,30,40,50,60]
# sum=0
# for i in range(0,6):
#     if i%2!=0:
#         sum=sum+a[i]
# print(sum)

# Question 18: find number of elements which are greater than the avg of array
# a=[2,4,6,8,10]
# sum=0
# for i in a:
#     sum = sum + i
# avg=sum/len(a)
# count=0
# for i in a:
#     if i>avg:
#         count=count+1
# print(count)

# Question 19: find the unique elements in the list
# a=[4,5,4,2,5,7,2]
# for i in a:
#     count=0
#     for j in a:
#         if i==j:
#             count=count+1
#     if count==1:
#         print(i)

# Question 20: find pairs of numbers whose sum is equal to target
# from itertools import count

# a=[2,4,3,5,7]
# target=7
# count=0
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j]==target:
#             count=count+1
#             print(a[i], a[j])
# print(count)

# Question 21: find the missing number in the list
# a=[1,2,3,5,6]
# n=len(a)+1
# for i in range(1,n+1):
#     if i not in a:
#         print(i)

# Question 22: inserting all zeros at the end of the list
# a=[0,1,0,3,12]
# b=[]
# count=0
# for i in a:
#     if i!=0:
#         b.append(i)
#     if i==0:
#         count=count+1
# for i in range(count):
#     b.append(0)
# print(b)


# Question 23: removing duplicates from the list
# a=[2,5,2,8,5,7,2]
# b=[]
# count=0
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# Question 24: find the frequency of each element in the list
# a=[2,3,2,5,3,2,7]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         count=0
#         for j in a:
#             if i==j:
#                 count=count+1
#         print(f"the frequency of {i} is: {count}")
        
# question 25: max element found
# a=[2,3,2,5,3,2,7]
# b=[]
# max=0
# for i in a:
#     if i not in b:
#         b.append(i)
#         count=0
#         for j in a:
#             if i==j:
#                 count=count+1
#         if count>max:
#             max=count
#             print(f'max element is {i} = {max}')

# question 27:first duplicate element
# a=[5,3,4,3,2,5,7]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(f'{a[i]} is first repeating elment') 
#     break 

# question 28: first duplicate element
# a=[5,3,4,3,2,5,7]
# b=[]
# for i in range(len(a)):
#     if a[i] in b:
#         print(f'found first element {a[i]} at index {i}')
#         break
#     else:
#         b.append(a[i])      

# question 29: first non repeating element               
# a=[5,3,4,3,2,5,7]
# for i in range(len(a)):
#     count=0
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             count+=1
#     if count==1:
#         print(f'first non repeating element is {a[i]}')
#         break