'''Make a program that asks for two grades from a student. Then he must calculate the student's average and give the following result:

    The message "Approved", if the average reached is greater than or equal to seven;
    The message "Fail", if the average is less than seven;
    The message "Passed with Distinction", if the average is equal to ten.'''

autor='__Alex Arlindo__'
n1=float(input('Frist grade:'))
n2=float(input('Secund grade:'))
average=(n1+n2)/2
print('Average: ', average)
if average<7:
    print('Fail')
elif average <10:
    print('Approved')
else:
    print('Passed with Distinction')
