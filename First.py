import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100)) # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# 构造一个线性模型
# 
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

x = []
y = []
# 拟合平面
for step in range(0, 201):
    sess.run(train)
    x.append(sess.run(W).tolist())
    y.append(sess.run(b).tolist())
    if step % 20 == 0:
        print (step, sess.run(W), sess.run(b))

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]
print(x)
print(y)
list1 = []
list2 = []
for l in x:
    list1.append(l[0][0])
    list2.append(l[0][1])
print(x)
print(list1)
plt.scatter(list1,list2 )

plt.show()
'''
这个基础的例子比上一个例子更直观也更符合实际。看起来更加的顺畅
总的来说，开头用极客学院的文档是一个比较错误的选择，因为感觉不维护了，时间比较久了
下面应该会想办法跟官方文档。
主要方向还是做 machine reading 好了
'''