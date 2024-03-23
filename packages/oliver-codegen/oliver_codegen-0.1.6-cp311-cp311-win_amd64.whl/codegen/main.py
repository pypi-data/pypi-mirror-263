import argparse
import os
import shutil
from pathlib import Path

from git import Repo
from yaml import safe_load

from codegen.core.log import logger
from codegen.core.params import pyproject_toml_params
from codegen.util.error import error_exit
from codegen.util.file_folder_util import modify_poetry_file, handle_read_only_error


def start():
    """
    项目开始入口
    :return: None
    """
    # 获取命令行参数
    args_parser = ArgumentParser()
    args = args_parser.parse()
    # 处理命令行参数
    handle_args = HandleArgs(args=args)
    handle_args.handle()

class ArgumentParser:
    """
    解析命令行参数主逻辑, 现可以处理 ["create", "add", "list"] 这几种命令

    "create" 用于生成新项目, 可以根据后面传入的模板名称, 从远程下载对应模板到本地.

    "add" 用于添加配置文件.

    "list" 用于查找该工具支持哪些模板和配置文件.
    """

    def __init__(self):
        self.operator: list = ["create", "add", "list"]
        self.parser = argparse.ArgumentParser(description=pyproject_toml_params.description)
        self.add_argument()

    def add_argument(self):
        """
        添加命令行命令和选参
        :return: None
        """
        self.parser.add_argument("--version", "-v", action="version", help="版本信息",
                                 version=pyproject_toml_params.version)
        self.parser.add_argument("operator", type=str, help="执行操作符", choices=self.operator)
        self.parser.add_argument("value", type=str, nargs="?", help="操作值")
        self.parser.add_argument("-t", "--template", help="模板名称")

    def parse(self) -> argparse.Namespace:
        """
        解析命令, 并将解析后的参数用 argparse.Namespace 封装
        :return: argparse.Namespace
        """
        return self.parser.parse_args()


class HandleArgs:
    """
    处理传入参数, 根据操作符(operator)不同选择不同处理函数.
    """

    def __init__(self, args: argparse.Namespace):
        self.args: argparse.Namespace = args

    def handle(self):
        """
        处理分发到不同函数处理
        :return: None
        """
        match self.args.operator:
            case "create":
                self.__handle_create()
            case "add":
                self.__handle_add()
            case "list":
                self.__handle_list()
            case _:
                logger.warn(f"暂不支持 {self.args.operator} 操作符参数")

    def __handle_create(self):
        # 如果项目名称没有输入直接报错退出
        if self.args.value is None:
            error_exit("项目名称必须传入: codegen create your_project_name")

        # 如果模板名称为空, 使用默认模板 "python"
        if self.args.template is None:
            self.args.template = "python"

        # 获得模板和仓库映射表, 并判断用户输入的模板名称是否在映射表中.
        temps: dict = get_templates()
        if self.args.template not in temps:
            error_exit(f"暂时不支持 {self.args.template} 模板. 可以使用 'codegen list template' 查看支持哪些模板")

        # 获取用户输入信息
        project_package_name = input("输入项目存放源码包名 (为空则和项目名称一致):")
        description = input("输入项目介绍: ")
        version = input("输入项目版本: ")
        if project_package_name is None or project_package_name == "":
            project_package_name = self.args.value.replace("-", "_")

        # 下载模板
        url = temps[self.args.template].get("repository")
        to_path = Path.cwd().joinpath(self.args.value).resolve()
        try:
            print("下载远程仓库到本地中...")
            # 克隆仓库到本地
            Repo.clone_from(url=url, to_path=to_path, depth=1)
            # 删除 .git 文件夹
            shutil.rmtree(to_path.joinpath(".git"), onerror=handle_read_only_error)
            # 更改项目存放源码包名
            temp_package_name = temps[self.args.template]["project-name"]
            # 更换模板中的包名
            os.rename(to_path.joinpath(temp_package_name), to_path.joinpath(project_package_name))
            # 更换 pyproject.toml 里面项目参数
            modify_poetry_file(to_path.joinpath('pyproject.toml'),project_package_name, self.args.value, description, version)
            print("项目构建完成.")
        except FileNotFoundError:
            error_exit(f" FileNotFoundError: 修改模板项目包名失败")
        except PermissionError:
            error_exit(f"PermissionError: 删除 .git 文件权限不够, 删除失败")
        except Exception as e:
            error_exit(f"从远程仓库 <{url}> 克隆失败", e)

    def __handle_add(self):
        if self.args.value is None:
            error_exit("添加配置文件参数必须传入: codegen add your_config_file")

    def __handle_list(self):
        """
        列出模板和配置文件
        :return:
        """
        if self.args.value is None or self.args.value == "template":
            repos: dict = get_templates()
            print("模板名称  (模板地址)")
            for key in repos:
                print(f"{key}  ({repos[key].get('repository')})")
        elif self.args.value == "add":
            pass
        else:
            pass


def get_templates() -> dict:
    # 模板名称和仓库映射文件路径
    template_repositories_path = (Path(__file__).parent.
                                  joinpath("conf").joinpath("create").joinpath("create.yaml"))
    # 解析文件成字典
    try:
        with open(template_repositories_path, 'r', encoding='utf-8') as f:
            return safe_load(f)['template']
    except Exception as e:
        error_exit("获取仓库映射 <create.yaml> 文件错误", e)




