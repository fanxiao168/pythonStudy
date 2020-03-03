# 3.根据身高和体重 参照BMI 返回身体状况
# BMI  体重(kg)/身高**2
# 中国参考标准
# BMI < 18.5  体重过低
# 18.5<= BMI < 24  正常
# 24<= BMI < 28  超重
# 28<= BMI < 30  I度肥胖

height = float(input('请输入身高(m):'))
weight = float(input('请输入体重(kg):'))
BMI = weight / height ** 2
if BMI < 18.5:
    print('体重过低')
elif BMI < 24:
    print('正常')
elif BMI < 28:
    print('超重')
else:
    print('肥胖')
