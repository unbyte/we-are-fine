# We Are Fine

> 「安安静静 不要说话」

# 构建与运行

```shell script
# clone repo
git clone https://github.com/unbyte/we-are-fine
cd we-are-fine

# 供参考的配置文件
cat config.example.py

# 创建自己的配置文件
vim config.py

# 构建并运行
docker-compose up -d --build
```

查看运行日志

```shell script
docker logs we-are-fine
```

# 用法

## 简介

本系统会在每天的8点给所有注册的账号自动填报信息并发送邮件。

接下来每隔两个小时会重新填报先前填报失败的账号，直到16点。

如果自动填报任务本身发生故障，管理员会收到邮件(管理员邮箱在`config.py`中设置)

## 注册

所以一般而言只需要注册即可自动填报

注册接口如下

`POST /api/user/register`

```json
{
  "username": "学号",
  "password": "stuinfo.neu.edu.cn的密码",
  "ip": "你想要用来填报信息的ip",
  "email": "你想要用来接收填报情况的邮箱"
}
```
ip可以是空字符串，填报时不会对ip进行伪装。其他都不可为空。

## 登陆

登陆之后可以修改账号信息或是查看自动填报日志

登陆接口如下

`POST /api/user/login`

```json
{
  "username": "学号",
  "password": "之前注册的时候填的密码"
}
```
注意，因为本系统不提供前端（提高使用门槛），所以通过`curl`等方式调用接口的用户必须为之后的操作手动保存cookie

## 信息

登陆后可以查看并设置学号，密码，ip，邮箱以及是否启用自动填报(注册时是默认开启的)

查看信息接口`GET /api/user/info`

修改信息接口

`POST /api/user/info`
```json
{
  "username": "新的学号",
  "password": "新的密码",
  "ip": "新的ip",
  "email": "新的邮箱",
  "enable": true
}
```

`enable`字段，true为开启自动填报，false为关闭

## 日志

登陆后可以查看自动填报日志

接口`GET /api/record/list`

# 其他

所有的数据保存在`./data/database.db`中，如果需要备份，直接备份宿主机上的`git clone`下来的`./data/database.db`
就可以了

# 开源协议

MIT License.