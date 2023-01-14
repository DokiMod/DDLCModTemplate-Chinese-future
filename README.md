# DDLC 中文 Mod 模板 4.0

**使用此模板之前请注意！本项目包含对 DDLC 的剧透。我们希望您能在通关 DDLC 原作后使用该模板进行模组开发，以避免影响游戏体验。**

**您仍需为自己的心理健康做周全的考虑。DDLC 本质上为心理恐怖游戏，并不适合所有玩家，且游戏内已经做了充足的提醒。心理健康比一切都重要。**

---

文思泉涌，再度归来。这里是全新的 DDLC 中文 Mod 模板 4.0，基于 Azariel Del Carmen (GanstaKingofSA) 制作的 [DDLC Mod Template 4.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/tree/python-3)，并得到了汉化。整个模板遵循 [Team Salvato 的知识产权（IP）准则](https://teamsalvato.com/ip-guidelines/) 针对饭制模组的规定。

> 本模板目前处于实验性阶段（进展为 2%），且使用了不太稳定的 Python 3 / Ren'Py 8，因此暂不建议使用于正式工程。（虽然硬着头皮用也不是不可以 —— imgradeone）  
> 目前如有需要，我们推荐您使用 [DDLC 中文 Mod 模板 2.0](https://github.com/imgradeone/DDLCModTemplate-Chinese-next) 进行新模组开发。

> Additionaly [here](./CREDITS.md) are all the contributors that contributed to the mod template.

> 此处的模板为 Python 3 版本，是专为 Ren'Py 8 设计的。若有配合 Ren'Py 6 / 7 使用该模板的需求，请等待 [Python 2 版本](https://github.com/DokiMod/DDLCModTemplate-Chinese-future/tree/python-2) 完成开发。Python 2 版本将在之后开始开发，抱歉给您带来不便。

> ~~万一 Dan 鸽把原版游戏升级到 Ren'Py 8 了呢 —— imgradeone~~

### 免责声明

   - <u>Team Salvato</u>
      > 本模板内含的代码 / 文件仅针对需要使用 DDLC 原版素材与 Ren'Py 的 DDLC 饭制游戏或模组。请勿将此模板用于制作与 DDLC 无关的项目。原版 DDLC Mod Template 与 DDLC 中文 Mod 模板均与 Team Salvato 没有任何关联。
   - <u>GanstaKingofSA</u>
      > 请勿将此模板用于制作非官方 DDLC 补丁。
   - <u>DokiMod</u>
      > 使用 DDLC 中文 Mod 模板并不意味着您可以在中国大陆的平台正常发布与 DDLC 有关的内容。

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
1. 使用 Ren'Py 8 构建，且兼容 Team Salvato 内容的模组 + 启动屏幕（免责声明）！
3. DDLC 的原版 RPY 文件，辅以（中文？）注释。
4. 支持 macOS、Linux* 与 Android**！
   > \* - Linux 用户请使用 `LinuxLauncher.sh` 来运行模组。

   > \*\* - 若您的模组使用简易代码与 Mod 模板内置功能。更复杂的代码、手机端不友好的功能可能需要修改。See *Android Mod Guide.pdf* or visit the DDMC Discord for additional help.
6. Xcode 支持！直接在 Xcode 打开工程，无需启动 Ren'Py 启动器即可编辑、构建、测试模组！
    > 备注：您需要在 Xcode 里修改 `RENPY_TOOL`，使其指向您安装的 Ren'Py SDK 应用位置。[Learn more &rsaquo;](XCODE.md)
7. [BETA] 人称支持！让玩家随心选择符合自己的人称代词！
    > See *mod_extras/pronouns.rpy* in the `game` folder for a example on how to use this feature.
8. 绝赞·完美“蓝屏死机”画面！轻松显示“蓝屏死机”画面，支持各类操作系统！（甚至还有在做的汉化版本！）
9. “遮羞布解除”和“实况共玩”模式！增强内容容许度，同时保护实况主的信息，更支持自动识别部分直播 / 录屏软件（包括 OBS Studio、Twitch Studio、Gamecaster、哔哩哔哩直播姬[^1]、Bandicam 等）并自动启用实况模式。
10. 图库菜单、成就菜单！让玩家欣赏您的画作，并且在游玩过程中获得更多成就！
12. 全自动界面配色 + 菜单按钮颜色定制！随心为游戏内界面与菜单按钮修改配色，无需修改原文件！
13. Terra's in-depth Poem Game guide!
14. 由 Yagamirai01 贡献的 NVL 支持！
15. 针对部分 Ren'Py 版本及 Windows 功能的补丁。
16. Python 3 支持与代码！
17. [BETA] Discord Rich Presence 绝赞支持！
18. 动态超分辨率 (DSR/DSP) + 自定义分辨率！Scale positions and/or your assets higher than they usually can go and display DDLC in different resolution modes. The DDLC Mod Template is now a universal X resolution template!
19. 玩家名称更改！听说你后悔使用原来的名字了？现在可以直接更改了！
20. 新版莫妮卡终端 + 设置菜单！输入命令更加轻松，设置界面更干净。New Monika Console and Settings Menu! - Enjoy a easier console to type commands in and a cleaner settings UI compared to the original game.

### 中文模板 4.0 新优化

1. 更规范、更完善的中文翻译，包括代码注释。
2. 界面优化。
3. 支持原生 Ren'Py 文件结构方式。
4. 拓展了直播 / 录屏软件的识别列表（包括 Twitch Studio、Gamecaster、哔哩哔哩直播姬[^1]、Bandicam 等）。
5. 合入了来自 DDLC Plus 的（新）汉化文本（感谢 Riotloc 团队以及社区汉化参与者）。
6. 整合社区版、Plus 版诗歌内容翻译。

（README 还没写完，再等等）

### 回归功能
1. Ghost Menu (Dan's spooky easter egg).
2. Sayori Kill Script (plays if Sayori is deleted before the game starts).
3. Monika Kill Script (plays if Monika is deleted before a new game starts).
4. 特别诗篇 (The random poems in DDLC that appear in Act 2) <u>[now improved!]</u>.
5. Poem Responses! (The responses the girls give you about your poem).

### 开始制作模组
> 针对模板 4.0 的中文文档仍在制作。

Follow the steps listed [here](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Recent.html) in order to install the mod template.
> Once you finished writing your script, select *Build Distributions*. Uncheck all the options, check only `Ren'Py 8 DDLC Compliant Mod` and click <u>Build</u>. This will create a cross-platform *Renpy8-DDLCMod* ZIP file with your mod files.

### Getting Started For Android Porting/Modding
Refer to [*The DDLC Android Mod Guide*](./Documentation/Android%20Mod%20Guide.pdf) for more in-depth information about making your mod work on Android.
> For older templates, refer to the PDF in your templates' ZIP file as the latest guide may not match your current template.

Copyright © 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.  
Template translated and modified by DokiMod.

Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.

[^1]: 实况共玩模式无法改变 DDLC 在中国大陆的屏蔽现状，因此请不要在中国大陆平台发布 / 直播与 DDLC 有关的内容。同时，无论如何，请注意安全。