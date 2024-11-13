from mulOp import mulValue
from divOp import divValue
''
if __name__ =='__main__':
    print('this is main code')
    val1=int(input('enter first number ='))
    val2=int(input('enter second number ='))
    op = input('which math op you want to do ?')

    if op.lower() == 'mul':
        a1=mulValue(val1,val2)
        print(f'multiplication={a1}')
      
    elif  op.lower() == 'div':
          a2=divValue(val1,val2)
          print(f'division ={a2}')
    else:
        print('please choose correct operation ,mul, div')