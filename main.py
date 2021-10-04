n=input()
evensum=0
oddsum=0
for i in range(0,len(n)):
    if i%2==0:
        evensum+=int(n[i])
    else:
        oddsum+=int(n[i])
print(evensum)
print(oddsum)
print(int(abs(evensum-oddsum)))