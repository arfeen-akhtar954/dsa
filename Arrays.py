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