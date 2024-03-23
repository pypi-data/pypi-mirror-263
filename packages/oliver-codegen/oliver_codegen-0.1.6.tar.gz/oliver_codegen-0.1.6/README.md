# oliver-codegen 
oliver-codegen 是一款快速构建项目基础框架的脚手架工具. 其原理是从 Github 下载对应模板到本地, 并没有什么魔法代码. 


## 安装
```bash
$ pipx install oliver-codegen
```
通常第一次使用 `pipx` 安装可执行程序时候, 可执行程序并没有自动添加到系统全局变量中, 导致在命令行无法使用. 这时候可以使用下面命令解决:
```bash
$ pipx ensurepath
```

## 使用方式
```bash
$ codegen create your_project_name -t python
```
其中 `-t` 后的参数是选择什么模板创建项目. 查看支持哪些模板命令 `codegen list template`


## 展示配置
输入以下命令, 将在控制台展示支持哪些模板.
```bash
$ codegen list template
```


## 更新程序
```bash
$ pipx upgrade oliver-codegen
```
如果你使用了国内镜像源, 可能存在同步问题, 无法更新到最新版本. 可以使用命令 `pipx upgrade oliver-codegen -i https://pypi.org/simple/`

## 卸载程序
```bash
$ pipx uninstall oliver-codegen
```

## 模板地址
```yaml
# 项目模板名称和存放地址映射表
template:
# Python 项目
  # python 基本模板
  python:
    repository: "https://github.com/lifefossil/template-python.git"
  # fastapi 模板
  fastapi:
    repository: "https://github.com/lifefossil/template-fastapi.git"
  # pyside6 模板
  pyside6:
    repository: "https://github.com/lifefossil/template-pyside6.git"
  # tkinter 模板
  tkinter:
    repository: "https://github.com/lifefossil/template-tkinter.git"
  # Django + Tailwind 模板
  django-tailwind:
    repository: "https://github.com/lifefossil/template-django-tailwind.git"

# vue 项目
  # vue-tailwindcss
  vue-tailwindcss:
    repository: "https://github.com/lifefossil/template-vue-tailwindcss.git"
  # vue-element-plus
  vue-element-plus:
    repository: "https://github.com/lifefossil/template-vue-element-plus.git"
  # vitepress
  vitepress:
    repository: "https://github.com/lifefossil/template-vitepress.git"
  # electron 模板
  electron:
    repository: "https://github.com/lifefossil/template-electron.git"
```
