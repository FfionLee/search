n=int(input("input number of items:"))
list=[]
for i in range(n):
    j=int(input("input number:"))
    list.append(j)

print(list)

item=int(input("input number to find:"))
def linear(list,item):
    for i in range(len(list)):
        if list[i]==item:
            return(i)
    else:
        return("item not found")

result=linear(list,item)
print(result)

def binary(list,item):
    low=0
    found=False
    high=len(list)-1
    while low<=high or found==False:
        mid=(high-low)//2
        if item>list[mid]:
            low=mid+1
        elif item<list[mid]:
            high=mid-1
        else:
            found=True
            return(mid)
            
    return("item not found")

r=binary(list,item)
print(r)