## 数据库设计
### 1.用户表(users)
CREATE TABLE users (
	id VARCHAR(36) NOT NULL, 
	name VARCHAR(36), 
	password_hash VARCHAR(128), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

### 2.路途表(traces)
CREATE TABLE traces (
	id VARCHAR(36) NOT NULL, 
	positions TEXT, 
	PRIMARY KEY (id)
);

### 3.会话表(session)
CREATE TABLE sessions (
	id VARCHAR(36) NOT NULL, 
	user_id VARCHAR(36), 
	time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);


### 4.足迹表(foot_prints)
CREATE TABLE foot_prints (
	id VARCHAR(36) NOT NULL, 
	title VARCHAR(100), 
	time DATETIME, 
	description TEXT, 
	images TEXT, 
	trace_id VARCHAR(36), 
	PRIMARY KEY (id), 
	FOREIGN KEY(trace_id) REFERENCES traces (id)
);

### 参考
https://www.json.org/json-zh.html
https://stackoverflow.com/questions/28525203/how-to-get-current-date-time-format-in-sqlite
http://jsoneditoronline.org/
