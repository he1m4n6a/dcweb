# dcweb
Dependency-Check 是一款分析软件构成的工具，他会检测项目中依赖项的公开披露漏洞，常用于扫描java和.NET项目。本项目就是基于此工具的包装。

# 目标
用于检测项目中使用依赖库的安全性。根据公司业务的情况：

1. 对接代码管理平台，自动化扫描
2. 业务提交扫描工单，安全人员帮助扫描和给修复建议
3. 业务自行提交扫描

如果公司代码发布不多，推荐使用第二种方法，安全人员好跟进并给出针对性建议。

# 安装
1. pip -r requirements.txt
2. 下载本项目到本地
3. 从 https://bintray.com/jeremy-long/owasp/dependency-check 下载dependency-check最新二进制版本，放到dcweb/dependency-check目录下
4. 修改app/views.py的监听地址和端口，默认为localhost:8888
5. 如果不是监听本地，需要添加ip白名单准入，修改dcweb/settings.py中的ALLOWED_HOSTS
6. python manage.py runserver 0.0.0.0:8888 运行即可

# 使用方法
![](screen.png)
把包含三方依赖库的源码打包上传,点击开始扫描即可。

# todo
项目中还有很多地方可以优化和补充，后续如果大家如果有需求或者别的想法可以进行补充。

1. 添加报告结果分析并发送邮件
2. 添加网页接口鉴权
