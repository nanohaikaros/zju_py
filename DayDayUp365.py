import math
dayup = math.pow((1.0 + 0.001), 365)
daydown = math.pow((1.0 - 0.001), 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))


dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("向上5天向下2天的力量：{:.2f}".format(dayup))

def dayUp(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while (dayUp(dayfactor) < 37.78):
    dayfactor += 0.001
print("每天的努力参数是：{:.3f}.".format(dayfactor))