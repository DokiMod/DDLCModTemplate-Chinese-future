
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

python early:
    
    class NotRenPyEight(Exception):
        def __str__(self):
            return "您使用的模板分支仅支持 Ren'Py 8。\n请您在使用该版本模板开发模组之前切换到 Ren'Py 8 进行开发，或者，请等待针对 Ren'Py 6 / 7 的 python-2 分支版本开发完毕。"

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "未在游戏目录中找到 '" + self.archive + ".rpa' 文件。请检查你的 DDLC 游戏副本，引入丢失文件后重试。"

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC Mod 及其工程无法运行于 OneDrive 等云端文件夹。请移动您的工程文件夹，然后重试。"
