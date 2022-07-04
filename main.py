import calc_class as mycalc

s = int(input("0 : 정수 모드, 1 : 실수 모드 => "))
ninput = int(input("숫자 입력 : "))
c = mycalc.calc(ninput,s)

menu = 1
while menu:
    
    szcmd = input("연산 입력 : ")
    
    ninput = int(input("숫자 입력 : "))

    if szcmd == '+' :
        c.add(ninput)
    elif szcmd == '-' :
        c.sub(ninput)
    elif szcmd == '*' :
        c.mul(ninput)
    elif szcmd == '/' :
        c.div(ninput)

    

    
    