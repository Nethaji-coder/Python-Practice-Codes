file = open('test.txt','r')
#print(file.read())
#print(file.readline())
#print(file.readlines())
file.close()

file1 = open('test2.txt','a')
file1.write('\nHello from Java')
#file1.write('Hello from Python\n')
#file1.write('Hello from Java')
file1.close()