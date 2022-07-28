# DDLC 中文 Mod 模板 4.0

文思泉涌，再度归来。

这里是全新的 DDLC 中文 Mod 模板 4.0，基于 Azariel Del Carmen (GanstaKingofSA) 制作的 [DDLC Mod Template 4.0](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/tree/python-3)，并得到了汉化。整个模板遵循 [Team Salvato 的知识产权（IP）准则](http://teamsalvato.com/ip-guidelines/) 针对饭制 Mod 的规定，并完美支持 Ren'Py 8。

> 本模板目前处于实验性阶段（进展为 1%），且将 **不再支持 Ren'Py 6 / 7**。

> 请注意，本模板仅允许用于制作 DDLC 饭制 Mod，请勿将此模板用于制作非官方 DDLC 补丁。

## **署名要求**

从 DDLC 中文 Mod 模板 4.0 开始，按照原模版规定，您必须在 Mod 的制作人员名单或 `credits.txt` 文件中对模板的原作及翻译团队署名。

> 本 Mod 借助由 GanstaKingofSA 开发、DokiMod 翻译的 DDLC 中文 Mod 模板 4.0 制作。  
> https://github.com/DokiMod/DDLCModTemplate-Chinese-future

默认情况下，制作人员名单已经在游戏中启用。它可能在“额外功能”屏幕的“关于”按钮，也可能是游戏内的其他按钮（如果额外功能屏幕被禁用了）。

这里还有一些备选（但也十分欢迎）的署名方案（在改）：
   1. A custom splash screen that features the Team Salvato logo (and/or your mod logo) and a `GanstaKingofSA` logo (which can be found [here](.github/IMAGES)).
   2. A small mention in the game's disclaimer saying that this mod was not possible without using GanstaKingofSA's mod template.
   3. A presplash screen that contains a `GanstaKingofSA` logo (which can be found [here](.github/IMAGES)).
   4. Present a custom idea to me for approval either through Discord or Reddit.

（README 还没写完，再等等）

### Team Salvato 免责声明
> 本模板内含的代码 / 文件仅针对需要使用 DDLC 原版素材与 Ren'Py 的 DDLC 饭制游戏或模组。本项目并不适用于与 DDLC 无关的项目。
原版 DDLC Mod Template 与 DDLC 中文 Mod 模板均与 Team Salvato 没有任何关联。

### 绝赞功能
1. 在 Ren'Py 8 上尽情打包 Mod！
2. 兼容 Team Salvato 准则的启动屏幕。
3. DDLC 的原版 RPY 文件，辅以注释。
4. macOS `.app` 及 Linux（通过 `LinuxLauncher.sh`）平台支持。
5. Android 平台支持！将您的模组带到移动平台游玩！\*
    > If your mod uses simple code or DDLC functions. More complex code or non-mobile friendly features may require some adjustments to get working. See *guide.pdf* or visit the DDMC Discord for additional help.
6. Xcode 支持！Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)
7. [BETA] 人称支持！Allow players to identify with the pronoun they go by!
    > See *mod_extras/pronouns.rpy* in the `game` folder for a example on how to use this feature.
8. 绝赞·完美“蓝屏死机”画面！Make your own BSOD easily in-game on every operating system! 
9. “遮羞布解除”模式！Allow more sensitive content to be shown in-game.
10. “实况共玩”模式！A better alternative to hide streamer information and more!
11. 图库菜单！Allow players to see the work you have done in-game and export it!
12. 成就菜单！Set up achievements in your mod for players to complete your mod in full!
13. 菜单按钮颜色定制！Have different colored buttons in the menu prompt to your hearts content.
14. 全自动界面配色！Color the GUI in the game to whatever you like without editing the asset files themselves! 
15. 额外功能菜单！Add additional button options to your game for additional button options!
16. Terra's in-depth Poem Game guide!
17. 由 Yagamirai01 贡献的 NVL 支持！
18. Patches for several Ren'Py releases and Windows features.
19. 现更使用 Python 3 代码！
20. [BETA] Discord Rich Presence 绝赞支持！

### Returned Features
1. Ghost Menu. (Dan's spooky easter egg)
2. Sayori Kill Script. (If you delete Sayori before the game starts, a new screen takes over)
3. Monika Kill Script. (If you delete Monika after the game loads, a new script plays out)
4. Special Poems! (The random poems in DDLC that appear in Act 2)
5. Poem Responses! (The Doki's respond to your poems!)

### Getting Started
Follow the steps listed [here](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Recent.html) in order to install the mod template.
> Once you finished writing your script, select *Build Distributions*. Uncheck all the options, check only `Ren'Py 8 DDLC Compliant Mod` and click <u>Build</u>. This will create a cross-platform *Renpy8-DDLCMod* ZIP file with your mod files.

### Getting Started For Android Porting/Modding
Refer to [*guide.pdf*](guide.pdf) for more in-depth information about making your mod work on Android.
> For older templates, refer to the PDF in your templates' ZIP file as the latest guide may not match your current template.

Copyright © 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.  
Template translated by DokiMod.

Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.
