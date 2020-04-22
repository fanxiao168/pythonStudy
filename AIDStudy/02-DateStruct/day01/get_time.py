# 在一个列表中存储100万整数，在第二个位置
# 插入一个数，计算插入所用的时间，100万个呢？
# 0     time: 0.007654905319213867
# 10000 time: 0.013025999069213867

import time
l = [x for x in range(1000000)]

st = time.time()
l.insert(10000,'007')
print('time:',time.time()-st)


