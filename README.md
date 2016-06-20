# 用途
把dirname文件夹下所有文件都以相同的结构同步到sae云存储中
比如，在dirname下有如下文件：
*    dirname/a/test.txt
*    dirname/test.txt
推送到sae的云存储中的文件结构就是：
*    /a/test.txt
*    /test.txt
注意空文件夹不推送
