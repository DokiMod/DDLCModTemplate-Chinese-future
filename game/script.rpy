## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # 该变量控制一周目之后的反作弊 ID。
    # 不建议变更本行代码。请考虑在你的游戏剧情脚本里使用下方代码：
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - 最小值 | Y - 最大值
    $ anticheat = persistent.anticheat

    # 该变量将章节数字设置为 0，以供模组使用。
    $ chapter = 0

    # 该变量控制玩家是否能在游戏期间跳过暂停时刻。
    $ _dismiss_pause = config.developer

    ## 角色命名
    # 这些变量控制游戏内角色的命名。
    # 如需添加新角色，请参考下方代码示例：
    #   $ mi_name = "Mike"
    # 不要忘记在 definitions.rpy 添加相应角色！
    $ s_name = "???"
    $ m_name = "女孩 3"
    $ n_name = "女孩 2"
    $ y_name = "女孩 1"

    # 该变量控制文本框展示时是否显示底部文字菜单，以及是否允许使用 Esc 显示菜单。
    $ quick_menu = True

    # 该变量控制文本框内的对话文字样式风格，可定义为常规（style.normal）或干扰（style.edited）风格。
    # 如需干扰风格，您可以使用 style.edited
    $ style.say_dialogue = style.normal

    # 控制纱世里是否去世的变量。
    # 一般不建议修改此项。
    $ in_sayori_kill = None
    
    # 这些变量控制是否允许玩家跳过 / 快进对话或转场。
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## 脚本主体
    # 这里包含脚本的调用（call）逻辑。
    # persistent.playthrough 变量控制游戏的周目数。
    if persistent.playthrough == 0:

        # 该变量将章节数设置为 X。
        # 变量设定应取决于玩家目前所经历的剧情。
        $ chapter = 0

        # This call statement calls your script label to be played.
        call ch0_main
        
        # This call statement calls the poem mini-game to be played.
        call poem

        ## 第一天
        $ chapter = 1
        call ch1_main

        # This call statement calls the poem sharing minigame to be played.
        call poemresponse_start
        call ch1_end

        call poem

        ## 第二天
        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end

        call poem

        ## 第三天
        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        ## 第四天
        $ chapter = 4
        call ch4_main

        # This python statement writes a file from within the game to the game folder
        # or to the Android/data/[modname]/files/game folder.
        python:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
                except IOError: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
            else:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except IOError: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        ## Day 5
        $ chapter = 5
        call ch5_main

        # This call statement ends the game but doesn't play the credits.
        call endgame
        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        
        # This jump statement jumps over to Act 2 from Act 1.
        jump playthrough2


    elif persistent.playthrough == 2:
        ## 二周目 - 第一天
        $ chapter = 0
        call ch20_main
        label playthrough2:
            call poem

            python:
                if renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                else:
                    try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                    except IOError: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            ## 二周目 - 第二天
            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end

            # 调用（call）诗歌小游戏，但不启用转场动画
            call poem(False)

            python:
                if renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                else:
                    try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except IOError: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            ## 二周目 - 第三天
            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            call poem(False)

            ## 二周目 - 第四天
            $ chapter = 3
            call ch23_main

            # This if statement calls either a special poem response game or play
            # as normal.
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start

            # This if statement is leftover code from DDLC where if your game is
            # a demo that it ends the game fully.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "试玩版结束"
                return

            call ch23_end
            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:
        ## 四周目 - 第一天
        $ chapter = 0
        call ch40_main
        jump credits

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
