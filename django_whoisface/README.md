# 前言

`django_whoisface` 是一个 django 项目，充当了服务器的作用。

# 环境搭建

想让代码运行起来，是要运行环境的
我们需要一个 Python 环境，建议使用虚拟环境，建议使用 `pipenv` 工具来搭建虚拟环境

首先，在 Repository 的根目录中（即 `whoisface` 文件夹）提供了 `Pipfile` 和 `Pipfile.lock` 文件，我们来靠这个文件来搭建虚拟环境吧！

## 安装 pipenv

安装 `pipenv` ,执行以下命令:

```bash
pip install pipenv
```

输入 pip show pipenv ，获得以下输出说明安装成功了！

```powershell
PS whoisface> pip show pipenv
Name: pipenv
Version: 2020.11.15
Summary: Python Development Workflow for Humans.
Home-page: https://github.com/pypa/pipenv
Author: Pipenv maintainer team
Author-email: distutils-sig@python.org
License: MIT
Location: c:\users\17293\appdata\local\programs\python\python39\lib\site-packages
Requires: setuptools, pip, certifi, virtualenv, virtualenv-clone
Required-by:
```

## 安装虚拟环境

确保此时在在 Repository 的根目录中，执行以下命令:

```bash
pipenv install
```

该命令会根据 `Pipfile.lock` 文件的内容自动化的构建虚拟环境，包括：

- 构建虚拟机的解释器
- 安装依赖的第三方包

## 技术栈阐述

### 数据库

数据库选择的是 SQLite ，这是一个嵌入式数据库，相比于 Mysql、PostgreSql、Oracle 等数据库，SQLite 不需要安装，不需要配置，最适合电脑前的小白们了！

> SQLite 存在伪约束等等问题，如果你要换成其他的数据库也是很简单的

### 缓存

TODO

### Django

选用最新的 `3.2`

> 现在是 `2021年07月 3日 19:10:03`

### Django REST framework

无所谓什么版本

### Pipenv

无所谓什么版本

# 把项目跑起来

开启服务的命令：

```bash
python manage.py runserver
```

> 请确保此时的路径在 django_whoisface 路径中

看到如下的画面说明服务启动成功了

```powershell
\whoisface> cd .\django_whoisface\
\whoisface\django_whoisface> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
July 03, 2021 - 18:01:41
Django version 3.2.4, using settings 'django_whoisface.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

将 `http://127.0.0.1:8000/` 该地址在浏览器中打开

# 各个功能模块的讲解

```bash

```

```python

```

```python

```

```python

```

```python

```
