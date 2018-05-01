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

#### 2.2 登出

1) 方法：DELETE

2) 路径：/api/sessions/{session_id}

3) 用户验证：header中添加「键」session，「值」{session_id}

### 3 路途

路径：/api/traces

#### 3.1 创建路途

1) 方法：POST

2) 请求体：
```
[   //列表
  { //点一
    "time": "2018-04-20 23:11:11",  //时间
    "longitude": 111.11,    //经度
    "latitude": 111.11      //纬度
  },
  { //点二
    "time": "2018-04-20 23:11:11",
    "longitude": 111.11,
    "latitude": 111.11
  }
]
```

3) 用户验证：header中添加「键」session，「值」{session_id}

4) 返回体：
```
{
    "id": "184b626a-44bd-4f8c-a4a4-d42ea2c15312",   //路途ID
    "positions": [  //位置点列表，结构与【请求体】相同
        {
            "time": "2018-04-20 23:11:11",
            "longitude": 111.11,
            "latitude": 111.11
        },
        {
            "time": "2018-04-20 23:11:11",
            "longitude": 111.11,
            "latitude": 111.11
        }
    ]
}
```

#### 3.2 获取路途

1) 路径：/api/traces/{trace_id}

2) 方法：GET

3) 用户验证：header中添加「键」session，「值」{session_id}

4) 返回体：
```
{
    "id": "184b626a-44bd-4f8c-a4a4-d42ea2c15312",
    "positions": [
        {
            "time": "2018-04-20 23:11:11",
            "longitude": 111.11,
            "latitude": 111.11
        },
        {
            "time": "2018-04-20 23:11:11",
            "longitude": 111.11,
            "latitude": 111.11
        }
    ]
}
```

### 4 足迹

路径：/api/foot-prints

#### 4.1 创建足迹

1) 方法：POST

2) 请求体

```
{
  "title": "test-title-0",  //标题
  "description": "这是测试的描述",  //描述
  "images": [   //图片URL列表
    "image1",   //图片一
    "image2"    //图片二
  ],
  "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2" //路途ID
}
```

3) 用户验证：header中添加「键」session，「值」{session_id}

4) 返回体：
```
{
    "id": "9be3f953-32cc-4090-9ce2-07cff0114335",   //足迹ID
    "title": "test-title-0",    //标题
    "time": "2018-04-30T14:43:02.909629", //创建时间
    "description": "这是测试的描述",
    "images": [
        "image1",
        "image2"
    ],
    "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2"
}
```

5) 示例：
```
curl -X POST \
  http://localhost:8005/api/foot-prints \
  -H 'content-type: application/json' \
  -H 'session: c7023e6a-44fa-4200-a0c1-8677b23a4839' \
  -d '{
  "title": "test-title-0",
  "description": "这是测试的描述",
  "images": [
    "image1",
    "image2"
  ],
  "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2"
}'
```

#### 4.2 获取足迹

1) 方法：GET

2) 路径：/api/foot-prints/{foot-print-id}

3) 用户验证：header中添加「键」session，「值」{session_id}

4) 返回体：
```
{
    "id": "91673780-cbb6-4b0a-a100-8f14012079b8",
    "title": "test-title-0",
    "time": "2018-04-30T14:52:43.600842",
    "description": "这是测试的描述",
    "images": [
        "image1",
        "image2"
    ],
    "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2"
}
```

#### 4.3 修改足迹

1) 方法：PUT

2) 路径：/api/foot-prints/{foot-print-id}

3) 用户验证：header中添加「键」session，「值」{session_id}

4) 请求体：
```
{
    "title": "五一节，峨眉山",
    "description": "劳动节，我和小伙伴一起去了峨眉山",
    "images": [
        "image1",
        "image2"
    ],
    "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2"
}
```

5) 返回体：
```
{
    "id": "91673780-cbb6-4b0a-a100-8f14012079b8",
    "title": "五一节，峨眉山",
    "time": "2018-04-30T14:52:43.600842",
    "description": "劳动节，我和小伙伴一起去了峨眉山",
    "images": [
        "image1",
        "image2"
    ],
    "trace_id": "e5f39cd5-89a3-4972-97b2-02f8f532a2c2"
}
```

#### 4.4 删除

1) 方法:DELETE

2) 路径:/api/foot-prints/{foot_print_id}

3) 用户验证：header中添加「键」session，「值」{session_id} 

### 5 足迹列表
#### 5.1 获取某个用户的足迹列表

1) 方法：GET

2) 路径：/api/foot-print-lists

3) 查询参数：user_id={user_id}

4) 用户验证：header中添加「键」session，「值」{session_id}

5) 示例：
URL：http://localhost:8005/api/foot-print-lists?user_id=59a2cc93-8812-4fcc-abb9-908b758f1e22

响应体：
```
[
    "f0034b36-efcb-4f36-8ab2-45f9c8b97a9a",
    "91673780-cbb6-4b0a-a100-8f14012079b8"
]
```
