## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## lockdown_check.rpy
# This file is mainly designed to warn new modders about bugs with certain Ren'Py 
# versions or warn them about QA issues with running Ren'Py versions higher than 
# the one the mod template was tested for.
# New in 4.0.0: Add lockout for Ren'Py 6/7 on Py 3 templates.

## DO NOT MODIFY THIS FILE! ##

# Checks if we are on Ren'Py 8
python early:

    if renpy.version_tuple < (8, 0, 0, 22062402):
        raise NotRenPyEight

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple > (8, 0, 3, 22083102):

        scene black
        "{b}警告：{/b}您目前用于开发 DDLC 模组的 Ren'Py SDK 未经过模组兼容性测试。"
        "目前最新的适用于 DDLC 模组的 Ren'Py 8 版本为{a=https://www.renpy.org/release/8.0.3}“Ren'Py 8.0.3”{/a}。"
        "在过高版本的 Ren'Py 上运行 DDLC 或其模组可能会引发问题，也可能导致游戏功能损坏。"
        
        menu:
            "继续在 Ren'Py [version!q] 版本中运行模组，则代表您同意此免责声明，并接受模组在未经测试的 Ren'Py 版本中运行时可能带来的问题。"
            "我同意。":
                $ persistent.lockdown_warning = True
                return

    else:
        $ persistent.lockdown_warning = True
        return
