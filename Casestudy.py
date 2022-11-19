def order(n,data):
    first = data[0]
    data= sorted(data)

    for i in range(0,n):
        if data [i] == first:
            return i

def get_position(n,data):
    first = data[0]
    cont = 0 
    for i in range(1,n): 
        if data[i] <= first:
            cont+=1

        return cont

if __name__== '__main__':
    n = int(input())
    data = list(map(int,input().rstrip().split()))

    print(order(n,data))
    print(get_position(n,data))