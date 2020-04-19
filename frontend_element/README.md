# 技术支撑平台前端

![vue](https://img.shields.io/badge/vue-4.2.2-brightgreen.svg)
![element-ui](https://img.shields.io/badge/element--ui-2.13.0-brightgreen.svg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
> 技术支撑平台前端代码.

## 目录

- [项目描述](#项目描述)
- [文件结构](#文件结构)
- [启动](#启动)

## 项目描述

## 集成第三方控件

- [elementUI](https://element.eleme.cn)


## 文件结构
```
├── build                      // 构建相关  
├── mock                       // 项目mock 模拟数据
├── src                        // 源代码
│   ├── api                    // 所有请求
│   ├── assets                 // 主题 字体等静态资源
│   ├── components             // 全局公用组件
│   ├── directive              // 全局指令
│   ├── filtres                // 全局 filter
│   ├── lang                   // 国际化 language
│   ├── layout                 // 页面模板
│   ├── router                 // 路由
│   ├── store                  // 全局 store管理
│   ├── styles                 // 全局样式
│   ├── utils                  // 全局公用方法
│   ├── vendor                 // 第三方js
│   ├── views                  // 页面
│   ├── App.vue                // 入口页面
│   ├── main.js                // 入口 加载组件 初始化等
│   └── permission.js          // 权限管理
├── static                     // 第三方不打包资源
├── tests                      // 单元测试
├── .babelrc                   // babel-loader 配置
├── eslintrc.js                // eslint 配置项
├── .gitignore                 // git 忽略项
├── favicon.ico                // favicon图标
├── index.html                 // html模板
└── package.json               // package.json
```

## 启动
```
1.npm install

2.npm run serve
```
