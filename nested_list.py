if __name__ == '__main__':
    ip=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = [name,score]
        ip.append(temp)
m=min(ip,key=lambda x: x[1])
new_ip=[new_ip for new_ip in ip if new_ip[1]>m[1]]
m2=min(new_ip,key=lambda x: x[1])
new_ip.sort()
for i in new_ip:
    for j in i:
        if j==m2[1]:
            print(i[0])
