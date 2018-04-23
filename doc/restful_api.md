## RESTful API描述

### 1 用户

路径:/api/users

#### 1.1 注册
描述：创建用户

1) 方法：POST

2) 请求体：
```
{
    "user_name": "hello", //用户名
    "password": "123456" //明文密码
}
```

3) 返回：
若注册成功：
```
{
    "id": "6bd741fd-359e-4077-9717-5d834bd660cc", //用户ID
    "name": "hello" //用户名
}
```

若注册失败：
```
{
    "id": null,
    "name": null
}
```

### 2 会话

路径：/api/sessions

#### 2.1 登入

1) 方法：POST

2) 请求体：
```
{
    "user_name": "hello", //用户名
    "password": "123456" //明文密码
}
```

3) 返回体：
若登入成功：
```
{
    "user_id": "6bd741fd-359e-4077-9717-5d834bd660cc", //用户ID
    "session": "395e406e-d4cf-442f-8d01-930e5310a8fe" //会话ID
}
```

若登入失败：
```
{} //空Json对象
```
