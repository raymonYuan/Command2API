# Command2API for Localldap Check

**作者**：gh0stkey

#### **原项目链接：**https://github.com/gh0stkey/Command2API



## 简介

​	由于内网环境没有Dnslog等平台使用，通过将LDAP的日志信息输出至HTTP端口，实现无需Dnslog等环境检测log4j2、fastjson等漏洞，检测JNDI请求情况 。



## 使用方法

执行命令：

```shell
- python3 Command2Api.py "执行的命令" Web运行的端口
```
![image-20211216173610942](https://user-images.githubusercontent.com/26023094/146347357-39f06dfa-0301-4804-b211-f9fea7c949d6.png)
- 接着在命令中会输出对应的URL，替换127.0.0.1访问即可获取：

![image](https://user-images.githubusercontent.com/26023094/146347403-e1c1d3c8-cf01-49f5-85ed-438eb942a214.png)
