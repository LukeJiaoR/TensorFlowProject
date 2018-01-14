'''
初步认识tensorflow的基本调用
'''


'''


使用图 (graph) 来表示计算任务.
在被称之为 会话 (Session) 的上下文 (context) 中执行图.
使用 tensor 表示数据.
通过 变量 (Variable) 维护状态.
使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.
'''

import tensorflow as tf

'''
创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
加到默认图中.
构造器的返回值代表该常量 op 的返回值.
'''
op1 = tf.constant([[3.,3.]]) #matrix

op2 = tf.constant([[2.],[2.]])

'''
创建一个矩阵乘法 matmul op , 把 op1 和 op2 作为输入.
返回值 'product' 代表矩阵乘法的结果.
'''
product = tf.matmul(op1,op2)

'''
上面的constant()和一个matmul()都是tensorflow的op，一个是构造，一个是计算。
感觉op有基本单元的意思，无论是构建一个变量，还是一次计算，都属于一个基本单元，但是直译成操作也有点不妥
后续想一想怎么定义为好
'''
'''
实例化一个图（图和线程有点像。。。。）
可以用申明的方式，也可以用下面实现那种方式，
sess = tf.Session的方式可以手动管理资源的存续和释放，关闭。
'''

'''
调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
矩阵乘法 op 的输出.

'''


with tf.Session() as sess:
    result = sess.run(product)
    print(result)   #[[ 12.]]