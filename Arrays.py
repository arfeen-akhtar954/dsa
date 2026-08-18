#TO FIND THE LARGEST NUMBER IN AN ARRAY
# a=[5, 8, 2, 10, 7]
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest =i
# print("The largest number in the array is:", largest)

#To find smallest number in the list
# a=[5, 8, 2, 10, 7]
# smallest=a[0]
# for i in a:
#     if i<smallest:
#         smallest=i
# print("The smallest number in the list is: ", smallest)

#to find second largest number in the list.
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

#to find second smallest number
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

#to find list is sorted or not
# a=[1,2,6,4,5]
# for i in range(len(a)-1):
#     if(a[i]>a[i+1]):
#         print("unsorted")
#         break 
# else: 
#     print("sorted")

#to reverse a list
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

#counting even number

# a=[3,6,8,2,9]
# count=0
# for i in a:
#     if i%2 == 0:
#         count=count+1
# print(count)

#finding sum of elements
# a=[4,3,5,6,7]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

#count positive and negative num
# a=[-2,5,-1,7,3,-4]
# count=0
# for i in a:
#     if i<0:
#         count =count +1

# print(count)

#find average
# a=[4,6,7,3,2]
# sum=0
# for i in a:
#     sum=sum + i

# avg=sum/len(a)
# print(avg)

#find how many elements are greater than 5
# a=[3,8,2,9,5,7]
# count=0
# for i in a:
#     if (i>5):
#         count = count + 1
# print("no. of elements which greater than 5 is: ", count)

#find how many times a number appears in the list
# a=[2,5,2,8,2,7,5]
# count=0
# n=int(input("enter a number for list for counting: "))
# for i in a:
#     if i==n:
#         count = count+1
# print(f"the number {n} is appered in the given list is {count} times")

#to find duplicates
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

#find largest difference between two numbers
# a=[3,8,2,9,5,1]
# ldif=0
# for i in a:
#     for j in a:
#         if abs(i-j)>ldif:
#             ldif=abs(i-j)
# print(ldif)

#find smallest difference between two numbers
# a=[3,8,2,9,5,1]
# sdif=float('inf')
# for i in a:
#     for j in a:
#         if i!=j and abs(i-j)<sdif:
#             sdif=abs(i-j)
# print(sdif)

#find sum of all elements at even indices:
# a=[10,20,30,40,50,60]
# sum=0
# for i in range(0,6):
#     if i%2==0:
#         sum=sum+a[i]
# print(sum)

#find sum of all elements at odd indices:
# a=[10,20,30,40,50,60]
# sum=0
# for i in range(0,6):
#     if i%2!=0:
#         sum=sum+a[i]
# print(sum)

#find number of elements which are greater than the avg of array
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

#find the unique elements in the list
# a=[4,5,4,2,5,7,2]
# for i in a:
#     count=0
#     for j in a:
#         if i==j:
#             count=count+1
#     if count==1:
#         print(i)

# find pairs of numbers whose sum is equal to target
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

# find the missing number in the list
# a=[1,2,3,5,6]
# n=len(a)+1
# for i in range(1,n+1):
#     if i not in a:
#         print(i)
