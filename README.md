1.用户表(users)
ID varchar(36)
用户名 name varchar(50)
密码哈希值 password_hash varchar(128) 哈希算法使用SHA512

2.足迹表(foot_prints)
ID varchar(36)
标题 title varchar(100)
时间 time datetime
文字 description text
图片 images json_array list<string>
路径ID trace_id varchar(36)
同步 sync boolean

3.路途表(traces)
ID varchar(36)
定位 position json_array 时间戳 time datetime 经度 longitude float 纬度 latitude float
同步 sync boolean

create table traces(id varchar(36) primary key, position json_array, sync bool);

参考
https://www.json.org/json-zh.html
https://stackoverflow.com/questions/28525203/how-to-get-current-date-time-format-in-sqlite
http://jsoneditoronline.org/
