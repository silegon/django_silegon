django_silegon 博客
===================

软件环境
--------

* django:1.4.1
* python:2.7.2
* nginx + uwsgi 部署
* nginx.conf [配置文件](https://github.com/silegon/django_silegon/blob/master/extra/server/nginx.conf)参考
* django_silegon.xml [uwsgi配置文件](https://github.com/silegon/django_silegon/blob/master/extra/server/django_silegon.xml)
* 以及各种相关的python包 

运行方式
--------
1. 下载源码，安装相关所需的文件。做过的都知道，Python错误提示很人性化。看缺少什么，一搜索就有了。
1. 准备settings.py:也许有同学注意到了，django_silegon项目中没有settings.py。为了不同的环境方便配置起见，可以用[settings.py.template](https://github.com/silegon/django_silegon/blob/master/extra/config/settings.py.template)其中可能需要更改的变量你可以仿照django模板变量的格式，加上{{variable}}。
1. 运行[generate_context.py](https://github.com/silegon/django_silegon/blob/master/extra/config/generate_context.py)生成填充文件settings.py.c
1. 按照自己的需求修改填充文件，然后按需修改[generate_conf.py]并运行。生成所需的settings.py
1. 将settings.py移动到项目中

* 运行开发服务器：python manage.py runserver {ip}:{port}
* 运行生产服务器：uwsgi -x django_silegon.xml

开发、生产帮助
--------------

需要指出的是，开发和生产的过程中状态的切换非常频繁。在延迟很高的外部服务器上添加大量数据是严酷的自残行为。为此可以先在本地测试服务器上添加好数据，然后同步到生产服务器上即可。

有款很好用的python运维工具[fabric](http://docs.fabfile.org/en/1.4.3/index.html)

比如本人用来同步开发服务器与生产服务器代码和数据的脚本[fabfile.py](https://gist.github.com/3415290)

这又会牵扯到新的知识点，比如ssh密钥登陆，sudo不用输入密码操作等等。请自行google了解吧，这也是linux环境的魅力所在。

Todo
----
* 添加定制搜索
* 中文数据的问题
* i18n自动翻译
* 生产服务器优化
* 内部添加缓存
