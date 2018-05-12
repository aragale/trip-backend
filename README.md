# 我的毕设的后端代码

## 1 技术栈
### 1.1 语言
Python 3.6.5，官网地址https://www.python.org/downloads/release/python-365/

Python语言具有简洁的语法、较强的表达能力和巨大而广泛的程序库，便于快速开发，是本课题的后端程序的开发语言。

### 1.2 HTTP库
Flask-RESTful 0.3.6，官网地址https://github.com/flask-restful/flask-restful

Flask-RESTful是一个简单的用于创建RESTful API的框架，开源、免费，是本课题的后端程序的框架。

### 1.3 数据库
SQLite 3.23.1，官网地址https://www.sqlite.org/index.html，是一种嵌入式SQL数据库引擎，使用C语言编写，通常用于在本地、客户端存储数据。Python 2.5以及之后版本的标准库，提供了对SQLite的支持。

### 1.3 ORM框架
ORM（英语：Object Relational Mapping），对象关系映射，是一种程序设计技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换，本课题中用作编程语言和数据库之间的转换，较之直接操作SQL，具有更好的安全性和执行、开发效率。

SQLAlchemy 1.2.7，官网地址https://www.sqlalchemy.org，是Python语言的SQL工具包和对象关系映射器，为应用程序开发人员提供了SQL的全部功能和灵活性，是本课题中的对象关系映射器。

## 2 部署
> 本部分说明如何在Ubuntu 16.04.4 LTS上部署

### 2.1 安装Python 3.6
执行命令：

sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt update
sudo apt install python3.6

### 2.2 安装Git
执行命令：

sudo apt install git

### 2.3 获取源代码
此处假定将源代码程序文件置于家目录，执行命令：
cd ~
git clone https://github.com/yzyzt/trip-backend

### 2.4 安装依赖库
执行命令：

cd ~/trip-backend
sudo pip3.6 sintall -r requirements.txt

### 2.5 设置防火墙
后端程序需要监听TCP端口，所以需要设置防火墙（Ubuntu操作系统防火墙软件为ufw），使外界能够访问后端服务监听的TCP端口，此处假定程序监听8002端口，执行命令：

sudo ufw allow 8002/tcp

### 2.6 启动与停止程序
启动，执行命令：

cd ~/trip-backend
/usr/bin/python3.6 trip.py start

停止，执行命令：
cd ~/trip-backend
/usr/bin/python3.6 trip.py stop

重启，执行命令：
cd ~/trip-backend
/usr/bin/python3.6 trip.py restart

