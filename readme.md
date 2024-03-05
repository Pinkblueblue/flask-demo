# flask-demo

## 创建虚拟环境

### python 3.3之前

pip install virtualenv
virtualenv --no-site-packages flask-venv

> --no-site-packages 创建一个纯净的虚拟环境，没有主环境中的第三方包
> --clear 清楚当前目录中的其他虚拟环境

### python 3.3之后

#### mac & linux

1. python3 -m venv flask-env
2. . flask-env/bin/activate

> --clear 清楚当前目录中的其他虚拟环境

#### window

1. python -m venv falsk-env
2. env\Scripts\activate

> 也可以在git bash中安装

## 退出虚拟环境

deactivate

## 导出项目依赖

pip freeze > requirements.txt

## 安装依赖

1. 创建一个虚拟环境
2. pip install -r requirements.txt

## 修改端口号

### 命令行

flask run --port 8088

### 代码方式

在代码中准备好， app.run(port = 8088)，然后使用命令行执行该文件python hello.py

## 线上部署

使用gunicorn, 优秀的server组件，使用多线程处理高并发请求

1. pip install gunicorn
2. gunicorn -w 4 -b 0.0.0.0:8099 hello:app

> 4个进程
> 指定host，端口号
> 指定运行文件，以及实例


