## 文件结构
``` 
├── api                        // 项目所有接口
├── app                        // 功能模块
├── config                     // 项目配置文件
├── libs                       // 公共类库
├── logs                       // 日志文件
├── models                     // 数据库模型
├── requirements               // 所需依赖
├── templates                  // 模板文件
├── test                       // 单元测试
├── .env                       // 特殊配置文件
├── .flaskenv                  // 通用配置文件
├── .env                       // 特殊配置文件
├── manage.py                  // 项目入口

```

## .env文件配置项
```
AES_SECRET_KEY                //AES加解密key
```

##模块蓝图创建或方法注册
```
1.蓝图注册：
    创建相关package，在__init__.py文件中创建蓝图，eg:testBp = Blueprint("test", __name__, url_prefix="/v1"),
    并引入相关路由模块。 在api.router中添加相关蓝图
2.MethodView注册：
    将相关方法以{方法名：访问路径}插入api.router
```

##模块蓝图创建方法

##模块蓝图