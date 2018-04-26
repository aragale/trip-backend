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
#### 1.2 获取
描述：获取用户信息

1) 方法：GET

2) 路径：/api/users/{user_id}

3) 用户验证：header中添加「键」session，「值」{session_id}

代码实例：
```
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"password\": \"6faa7cb35dbb\",\"user_name\": \"sasdf\"\n}");
Request request = new Request.Builder()
  .url("http://localhost:8005/api/users/ab31e73d-6ca0-434b-8221-ae0896459cce")
  .get()
  .addHeader("session", "e883651f-c641-4e43-a4e5-2e2d869b585b") //注意此句
  .build();

Response response = client.newCall(request).execute();
```

4) 返回体
```
{
    "id": "ab31e73d-6ca0-434b-8221-ae0896459cce", //用户ID
    "name": "sasdf" //用户名称
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
