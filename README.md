# DDLC 中文 Mod 模板 4.0

文思泉涌，再度归来。

这里是全新的 DDLC 中文 Mod 模板 4.0，基于 Azariel Del Carmen (GanstaKingofSA) 制作的 [DDLC Mod Template 4.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/tree/python-3)，并得到了汉化。整个模板遵循 [Team Salvato 的知识产权（IP）准则](http://teamsalvato.com/ip-guidelines/) 针对饭制 Mod 的规定。

> 本模板目前处于实验性阶段（进展为 2%），因此暂不建议使用于正式工程。

> 此处的模板为 Python 3 版本，是专为 Ren'Py 8 设计的。若有配合 Ren'Py 6 / 7 使用该模板的需求，请使用 [Python 2 版本](https://github.com/DokiMod/DDLCModTemplate-Chinese-future/tree/python-2)。Python 2 版本的开发仍在进行（0%）。

### 免责声明
> 本模板内含的代码 / 文件仅针对需要使用 DDLC 原版素材与 Ren'Py 的 DDLC 饭制游戏或模组。本项目并不适用于与 DDLC 无关的项目。

原版 DDLC Mod Template 与 DDLC 中文 Mod 模板均与 Team Salvato 没有任何关联。

> 请注意，本模板仅允许用于制作 DDLC 饭制模组，请勿将此模板用于制作非官方 DDLC 补丁。

   - <u>Team Salvato</u>
      > The template code/files are designed for original DDLC fan games and mods that use DDLC assets with Ren'Py. It is not meant for non-DDLC projects. The DDLC Mod Template is not afilliated in anyway with Team Salvato.
   - <u>GanstaKingofSA</u>
      > You may not use the template to make unofficial DDLC patchers, fixes, etc.

## **署名要求**

从 DDLC 中文 Mod 模板 4.0 开始，按照原模版规定，您必须在模组的制作人员名单或 `credits.txt` 文件中对模板的原作及翻译团队署名。

> 本 Mod 借助由 GanstaKingofSA 开发、DokiMod 翻译的 DDLC 中文 Mod 模板 4.0 制作。  
> https://github.com/DokiMod/DDLCModTemplate-Chinese-future

默认情况下，制作人员名单已经在游戏中启用。它可能在“额外功能”屏幕的“关于”按钮，也可能是游戏内的其他按钮（如果额外功能屏幕被禁用了）。

这里还有一些备选（但也十分欢迎）的署名方案（在改）：
   1. A custom splash screen that features the Team Salvato logo (and/or your mod logo) and a `GanstaKingofSA` logo (which can be found [here](.github/IMAGES)).
   2. A small mention in the game's disclaimer saying that this mod was not possible without using GanstaKingofSA's mod template.
   3. A presplash screen that contains a `GanstaKingofSA` logo (which can be found [here](.github/IMAGES/Logos)).
   4. Present a custom idea to me for approval either through Discord or Reddit.

### 绝赞功能
1. 轻松地在 Ren'Py 8 启动器里打包模组！
2. 兼容 Team Salvato 准则的启动屏幕。
3. DDLC 的原版 RPY 文件，辅以（中文？）注释。
4. macOS `.app` 及 Linux（通过 `LinuxLauncher.sh`）平台支持。
5. Android 平台支持！将您的模组带到移动平台游玩！\*
    > 前提是您的模组仅使用简单的代码及 DDLC 功能。更复杂的代码及并非为移动端设计的功能可能需要进行微调，才能在移动平台运行。请参阅 *guide.pdf* （中文翻译待提供）。<!-- 或加入 DDMC Discord 以获得更多帮助 -->
6. Xcode 支持！直接在 Xcode 打开项目，无需打开 Ren'Py 启动器即可编辑、运行、构建模组！
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)
7. [BETA] 人称支持！让玩家随心选择符合自己的人称代词！
    > See *mod_extras/pronouns.rpy* in the `game` folder for a example on how to use this feature.
8. 绝赞·完美“蓝屏死机”画面！轻松显示“蓝屏死机”画面，支持各类操作系统！（甚至还有在做的汉化版本！）
9. “遮羞布解除”模式！有些内容不能放，但是至少，这里有个开关。
10. “实况共玩”模式！更好的隐藏主播信息方案，且可以提供适合更多观众的备选剧情方案；支持自动识别部分直播 / 录屏软件（包括 OBS Studio、Twitch Studio、Gamecaster、哔哩哔哩直播姬[^1]、Bandicam 等）并自动启用实况模式。
11. 图库菜单！让玩家随心浏览你的画作，更支持导出。
12. 成就菜单！简单的成就解决方案；立即设置一些成就，让玩家完整体验你的模组作品！
13. 菜单按钮颜色定制！为菜单提示添加不同配色的按钮，满足你的需求。
14. 全自动界面配色！无需修改资源文件，直接修改界面配色。
15. 额外功能菜单！一个按钮，通往更多丰富功能！
16. Terra's in-depth Poem Game guide!
17. 由 Yagamirai01 贡献的 NVL 支持！
18. 针对部分 Ren'Py 版本及 Windows 功能的补丁。
19. 现更使用 Python 3 代码！
20. [测试] Discord Rich Presence 绝赞支持！
21. 新转场特效。

### 中文模板 4.0 新优化

1. 更规范、更完善的中文翻译，包括代码注释。
2. 界面优化。
3. 支持原生 Ren'Py 文件结构方式。

（README 还没写完，再等等）

### Returned Features
1. Ghost Menu (Dan's spooky easter egg).
2. Sayori Kill Script (plays if Sayori is deleted before the game starts).
3. Monika Kill Script (plays if Monika is deleted before a new game starts).
4. Special Poems (The random poems in DDLC that appear in Act 2) <u>[now improved!]</u>.
5. Poem Responses! (The responses the girls give you about your poem).

### 开始制作模组
Follow the steps listed [here](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Recent.html) in order to install the mod template.
> Once you finished writing your script, select *Build Distributions*. Uncheck all the options, check only `Ren'Py 8 DDLC Compliant Mod` and click <u>Build</u>. This will create a cross-platform *Renpy8-DDLCMod* ZIP file with your mod files.

### Getting Started For Android Porting/Modding
Refer to [*The DDLC Android Mod Guide*](./Documentation/Android%20Mod%20Guide.pdf) for more in-depth information about making your mod work on Android.
> For older templates, refer to the PDF in your templates' ZIP file as the latest guide may not match your current template.

Copyright © 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.  
Template translated by DokiMod.

Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.

[^1]: 实况共玩模式无法改变 DDLC 在中国大陆的屏蔽现状，因此请不要在中国大陆平台发布 / 直播与 DDLC 有关的内容。同时，无论如何，请注意安全。