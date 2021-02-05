
if __name__ == '__main__':
    n = int(input())
ans=1
for i in range(2,n+1):
    for j in range(1,4):
        if i/pow(10,j)<1:
            ans=(ans*pow(10,j))+i
            break
        
print(ans)






