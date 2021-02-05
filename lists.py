if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
result=[]
a=[a for a in range(x+1)]
b=[b for b in range(y+1)]
c=[c for c in range(z+1)]
for i in a:
    for j in b:
        for k in c:
            result.append([i,j,k])
ans=[ans for ans in result if ans[0]+ans[1]+ans[2]!=n]
print(ans)
