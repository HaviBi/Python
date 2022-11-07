# enter data
personHeight = input('please enter your height(m):')
personHeight = float(personHeight)

personWeight = input('please enter your weight(kg):')
personWeight = float(personWeight)

personAge = input('please enter your age:')
personAge = int(personAge)

personSex = input('please enter your sex:')
personSex = int(personSex)

# verify data
if (0 < personHeight < 3) and (0 < personWeight < 300) and (0 < personAge < 150) and (personSex == 0 or personSex == 1):
    print('continue')

# analysis data
BMI = personWeight / (personHeight * personHeight)
TZL = 1.22 * BMI + 0.23 * personAge - 5.4 - 18.8 * personSex

TZL /= 100

minNum = 0.15 * 0.10 * (1 - personSex)
maxNum = 0.18 * 0.10 * (1 - personSex)

result = minNum < TZL < maxNum

# output result
# print('your TZL is : %f' % TZL)
# print('your TZL is ', result)

# distinguish between man and woman
if personSex == 1:
    # TZL for man
    result = 0.15 < TZL < 0.18
elif personSex == 0:
    # TZL for woman
    result = 0.25 < TZL < 0.28

if personSex == 1:
    print('Sir,')
elif personSex == 0:
    print('Ms.')

print('your sex is %d' % personSex)
print('your TZL is', result)

