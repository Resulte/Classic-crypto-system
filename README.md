# Classic-crypto-system
古典密码加解密系统，置换密码+栅栏密码，python实现

# 置换密码

### 流程介绍

加密：

* 建立随机化的密文字符表（随机置换表）

* 逐个字符进行查表替代

* 输出明文、密文

解密：

* 输入密文字符表

* 逐个字符进行查表替代

* 输出密文、明文

### 流程图

![流程图](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/classic1.png)

### 执行结果截图

![执行结果](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/classic2.png)

# 栅栏密码

### 流程介绍

加密：

* 对待处理消息形成数组或列表

* 生成密文空间

* 读取 0、2、4、6...数据到密文空间的 0、1、2、3,...round(n/2)-1 

* 读 取 1 、 3 、 5 、 7... 数 据 到 密 文 空 间 的 round(n/2) 、 round(n/2)+1 、round(n/2)+2...n-1 

* 输出明文、密文

解密：

* 生成明文空间

* 读取密文的 0、1、2、3...round(n/2)-1 到明文空间的 0、2、4、6、...

* 读取密文的 round(n/2)、round(n/2)+1、round(n/2)+2...n-1 到明文空间的 1、 3、5、7...

* 输出密文、明文

### 流程图

![流程图](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/classic3.png)

### 执行结果截图

![执行结果](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/classic4.png)