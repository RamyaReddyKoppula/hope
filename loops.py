#x = [1,2,3]
#x_square = []
#for i in x:
    #k = (i**2)
    #x_square.append(k)
#print(x_square)
#for i in range(3, 12, 3):
    #print(i)
#results = []
#for i, r in enumerate(range(1,21)):
   # if i % 2 == 0:
       # print('Current step:', i, '-- Value:', r)
    #results.append(i**2)
#print(results)
#name = ["ramya", "chandu"]
#Age = [25, 21]
#for i, j in zip(name, Age):
    #print("my name is ",i," and age is ",j)
def sum_mul(n=10):
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
            print(s)
#sum_mul(10)
#print(s)