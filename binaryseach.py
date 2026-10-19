# Question 1: Binary Search
# a=[1,3,5,7,9,11]
# left=0
# right=len(a)-1
# element=int(input('enter element from given list: '))
# found=False
# while (left<=right):
#     mid=(left+right)//2
#     if a[mid]==element:
#         print(f'{element} found at index {mid}')
#         found=True
#         break
#     elif (a[mid]<element):
#         left=mid+1
#     else:
#         right=mid-1
# if found==False:
#     print('element not found')

# Question 2: Binary Search (Lower Bound)
# a=[1,2,4,4,5,7,9]
# left=0
# right=len(a)-1
# element=4
# ans=len(a)
# while (left<=right):
#     mid=(left+right)//2
#     if a[mid]>=element:
#         ans=mid
#         right=mid-1
#     else:
#         left=mid+1
# print(ans)

# Question 3: Binary Search (Upper Bound)
# a=[1,2,4,4,5,7,9]
# left=0
# right=len(a)-1
# element=4
# ans=len(a)
# while (left<=right):
#     mid=(left+right)//2
#     if a[mid]>element:
#         ans=mid
#         right=mid-1
#     else:
#         left=mid+1
# print(ans)

# Question 4: Search Insert Position
# a=[1,3,5,6]
# c=4
# index=0
# for i in range(0, len(a)):
#     if a[i]>=c:
#         index=i
#         break
# print(index)

# Question 5: Floor and Ceil of a Number
# a=[1,2,4,6,8,10]
# x=5
# floor=-1
# ceil=-1
# for i in range(0, len(a)):
#     if a[i]<=x:
#         floor=a[i]
#     if a[i]>=x:
#         ceil=a[i]
#         break
# print(f'floor is {floor} and ceil is {ceil}')
    
# Question 6: First and Last Occurrence of an Element
# a=[1,2,2,2,3,4,5]
# x=2
# left=0
# right=len(a)-1
# first=-1
# while (left<=right):
#     mid=(left+right)//2
#     if a[mid]==x:
#         first=mid
#         right=mid-1
#     elif a[mid]<x:
#         left=mid+1
#     else:
#         right=mid-1
# left=0
# right=len(a)-1
# last=-1
# while (left<=right):
#     mid=(left+right)//2
#     if a[mid]==x:
#         last=mid
#         left=mid+1
#     elif a[mid]>x:
#         right=mid-1
#     else:
#         left=mid+1
# print(f'first occurence {first}')
# print(f'last occurence is {last}')

# Question 7: Search in Rotated Sorted Array
# a=[4,5,6,7,0,1,2]
# x=0
# left=0
# right=len(a)-1
# index=-1
# while(left<=right):
#     mid=(left+right)//2
#     if a[mid]==x:
#         index=mid
#         break
#     if a[left]<=a[mid]:
#         if a[left]<=x<a[mid]:
#             right=mid-1
#         else:
#             left=mid+1
#     else:
#         if a[mid]<x<=a[right]:
#             left=mid+1
#         else:
#             right=mid-1
# print(index)

# Question 8: Search in Rotated Sorted Array with Duplicates
# a=[2,2,2,3,4,2]
# x=4
# left=0
# right=len(a)-1
# found=False
# while(left<=right):
#     mid=(left+right)//2
#     if a[mid]==x:
#         found=True
#         break
#     if a[left]==a[mid]==a[right]:
#              left+=1
#              right-=1
#              continue
#     if a[left]<=a[mid]:
#         if a[left]<=x<a[mid]:
#                 right=mid-1
#         else:
#             left=mid+1
#     else:
#         if a[mid]<x<=a[right]:
#             left=mid+1
#         else:
#             right=mid-1
# print(found)

# Question 9: Binary Search for Smallest Element
# a=[4,5,6,7,0,1,2]
# left=0
# right=len(a)-1
# while left<right:
#     mid=(left+right)//2
#     if a[mid]>a[right]:
#         left=mid+1
#     else:
#         right=mid
# print(a[left])

# Question 10: Binary Search to Find Single Element
# def findSingleElement(arr):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         mid=(left+right)//2
#         if mid%2==1:
#             mid-=1
#         if arr[mid]==arr[mid+1]:
#             left=mid+2
#         else:
#             right=mid
#     return(arr[left])
# print(findSingleElement([1,2,2,3,3,4,4,5,5]))

# Question 11: Nth Root Using Binary Search
# n=3
# m=27
# left=1
# right=27
# while left<right:
#     mid=(left+right)//2
#     if (mid**n)==m:
#         print(f'{mid}')
#         break
#     elif (mid**n)>m:
#         right=mid-1
#     else:
#         left=mid+1

# Question 12: Koko Eating Bananas
# piles=[3,6,7,11]
# h=8
# left=1
# right=max(piles)
# while left<right:
#     mid=(left+right)//2
#     hours=0
#     for pile in piles:
#         hours+=(pile+mid-1)//mid
#         if hours<=h:
#             right=mid
#         else:
#             left=mid+1
# print(left)

# Question 13: Flower Bouquets Problem
# bloomday=[2,5,12,4,13,8,14]
# m=2
# k=2
# left=min(bloomday)
# right=max(bloomday)
# if m*k>len(bloomday):
#     print(-1)
# else:
#     while left<right:
#         mid=(left+right)//2
#         flowers=0
#         bouquets=0
#         for i in bloomday:
#             if i<=mid:
#                 flowers+=1
#                 if flowers==k:
#                     bouquets+=1
#                     flowers=0
#             else:
#                 flowers=0
#         if bouquets>=m:
#             right=mid
#         else:
#             left=mid+1
# print(left)

# Question 14: Smallest Divisor Given a Threshold
# def smallestdivisor(nums, threshold):
#     left=1
#     right=max(nums)
#     while left<right:
#         mid=(left+right)//2
#         total=0
#         for i in nums:
#             total+=(i+mid-1)//mid
#         if total<=threshold:
#             right=mid
#         else:
#             left=mid+1
#     return left
# print(smallestdivisor([1,2,5,9], 6))
# print(smallestdivisor([2,3,7,8], 7))

# Question 15: Capacity to Ship Packages Within D Days
# weights=[1,2,3,4,5,6,7,8,9,10]
# days=5
# left=10
# right=55
# while left<right:
#     mid=(left+right)//2
#     current_weight=0
#     day_used=1
#     for i in weights:
#         if current_weight+i<=mid:
#             current_weight+=i
#         else:
#             day_used+=1
#             current_weight=i
#     if day_used<=days:
#         right=mid
#     else:
#         left=mid+1
# print(mid, day_used)
# print(left)

# kth missing day
# a=[2,3,4,7,11]
# k=5
# left=0
# right=len(a)-1
# while left<=right:
#     mid=(left+right)//2
#     missing=a[mid]-(mid+1)
#     if missing<=k:
#         left=mid+1
#     else:
#         right=mid-1
# print(left+k)

# aggressive cow
# stalls=[0,3,4,7,9,10]
# k=4
# low=1
# high=stalls[-1]-stalls[0]
# while low<=high:
#     mid=(low+high)//2
#     count=1
#     last=stalls[0]
#     for i in range(1, len(stalls)):
#         if stalls[i]-last>=mid:
#             count+=1
#             last=stalls[i]
#     if count>=k:
#         answer=mid
#         low=mid+1
#     else:
#         high=mid-1
# print(answer)

# book allocation method
# a=[10,20,30,40]
# students=2
# low=max(a)
# high=sum(a)
# while low<=high:
#     mid=(low+high)//2
#     students_used=1
#     pages=0
#     for i in a:
#         if pages+i<=mid:
#             pages+=i
#         else:
#             students_used+=1
#             pages=i
#     if students_used<=students:
#         answer=mid
#         high=mid-1
#     else:
#         low=mid+1
# print(answer)

# split array-largest sum
# arr=[3,5,10,5,9]
# k=2
# low=max(arr)
# high=sum(arr)
# while low<=high:
#     mid=(low+high)//2
#     subarray=1
#     current_sum=0
#     for i in arr:
#         if current_sum+i<=mid:
#             current_sum+=i
#         else:
#             subarray+=1
#             current_sum=i
#     if subarray<=k:
#         answer=mid
#         high=mid-1
#     else:
#         low=mid+1
# print(answer)

# painter's partition problem
# boards=[10,20,30,40]
# partition=2
# low=max(boards)
# high=sum(boards)
# while low<=high:
#     mid=(low+high)//2
#     current_painter=1
#     sum_boards=0
#     for i in boards:
#         if sum_boards+i<=mid:
#             sum_boards+=i
#         else:
#             current_painter+=1
#             sum_boards=i
#     if current_painter<=partition:
#         high=mid-1
#     else:
#         low=mid+1
# print(low)

# minimize max distance to gas station
# import math
# stations=[1,2,4,7]
# k=2
# low=0
# high=3
# while high-low>1e-6:
#     mid=(low+high)/2
#     needed=0
#     for i in range(len(stations)-1):
#         gap=stations[i+1]-stations[i]
#         needed+=math.ceil(gap/mid)-1
#     if needed<=k:
#         high=mid
#     else:
#         low=mid
# print(low)

# MEDIAN OF TWO SORTED ARRAYS - BINARY SEARCH ON SMALLER ARRAY
a=[1,2,10]
b=[3,4,5]
if len(a)>len(b):
    a,b=b,a
low=0
high=len(a)
n=len(a)+len(b)
left_elements=(n+1)//2
while low<=high:
    cutA=(low+high)//2
    cutB=left_elements-cutA
    if cutA>0:
        leftA=a[cutA-1]
    else:
        leftA=float('-inf')
    if cutA<len(a):
        rightA=a[cutA]
    else:
        rightA=float('inf')
    if cutB>0:
        leftB=b[cutB-1]
    else:
        leftB=float('-inf')
    if cutB<len(b):
        rightB=b[cutB]
    else:
        rightB=float('inf')

    if leftA<=rightB and leftB<=rightA:
        if n%2 != 0:
            median=max(leftA, leftB)
        else:
            median=(max(leftA,leftB)+min(rightA,rightB))/2
        print(median)
        break

    if leftA>rightB:
        high=cutA-1
    elif leftB>rightA:
        low=cutA+1

    