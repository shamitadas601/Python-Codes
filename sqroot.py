
y=24.0
epl=.01
guess=y/2.0#bisection and newton raphson
num=0
while (abs(guess**2-y) >= epl):
    guess=guess-(((guess**2)-y) /(2*guess))
    num=num+1
print (num)
print (guess)




