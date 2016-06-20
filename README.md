# 用途
把dirname文件夹下所有文件都以相同的结构同步到sae云存储中
比如，在dirname下有如下文件：
*    dirname/a/test.txt
*    dirname/test.txt

推送到sae的云存储中的文件结构就是：
*    /a/test.txt
*    /test.txt

注意空文件夹不推送

# 用法
有三个环境变量需要设置：
* SAE_STORAGE_ACCESS_KEY 
* SAE_STORAGE_SECRET_KEY
* SAE_BUCKET_NAME

顾名思义，他们分别是sae云存储的accessKey, secretKey, bucket名字

在程序中，用起来也很简单：

    from push import push
    push(dirname)

# 注意
sae云存储中的文件结构将和dirname中的文件结构相同，也就是说，如果dirname中的删除了或者没有某个文件，在sae中有这个文件，push过程会删除掉这个“多余”的文件。