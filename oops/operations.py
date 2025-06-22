class Operations:
    '''def sub(self,num):
        return -num'''

    def sub(self, num1, num2=0):
        return num1 - num2

    def add(self, num1, num2=0):
        return num1 + num2

    def mul(self, num1, num2=0):
        return num1 * num2
num1=int(input('Enter a number: '))
num2=input('Enter another number: ')

op=Operations()
if num2.strip() == "":
    result=op.sub(num1)
else:
    result=op.sub(num1, num2)

print(op.sub(num1))
print(op.sub(num1, num2))
