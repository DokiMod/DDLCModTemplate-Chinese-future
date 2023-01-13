## splash.rpy

# This is where the splashscreen, disclaimer and menu code reside in.

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None:
                if onedrive_path in config.basedir:
                    raise IllegalModLocation

## Splash Message
# This python statement is where the splash messages reside in.
init python:
    # This variable is the default splash message that people will see when
    # the game launches.
    splash_message_default = "本游戏为非官方性质的饭制游戏，与 Team Salvato 无关。"
    # This array variable stores different kinds of splash messages you can use
    # to show to the player on startup.
    splash_messages = [
        "文学部需要你的支持。",
        "莫妮卡在看着代码哦。"
    ]

    ### New in 3.0.0
    ## This recolor function allows you to recolor the GUI of DDLC easily without replacing
    ## the in-game assets.
    ##
    ## Syntax to use: recolorize("path/to/your/image", "#color1hex", "#color2hex", contrast value)
    ## Example: recolorize("gui/menu_bg.png", "#bdfdff", "#e6ffff", 1.25)
    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), 
            im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

    def process_check(stream_list):
        if not renpy.windows:
            for index, process in enumerate(stream_list):
                stream_list[index] = process.replace(".exe", "")
        
        for x in stream_list:
            for y in process_list:
                if re.match(r"^" + x + r"\b", y):
                    return True
        return False

# This image text shows the splash message when the game loads.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Main Menu Images
# These image transforms store the images and positions of the game logo,
# the menu character sprites and main menu/pause menu screen images.

# This image shows the DDLC logo in the normal DDLC position.
image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"
    # im.Composite((512, 512), (0, 0), recolorize("mod_assets/logo_bg.png"), (0, 0), "mod_assets/logo_fg.png")
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# This image shows the main menu polka-dot image.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_move

# This image shows the pause menu polka-dot image.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_loop

# This image transform shows the white fading effect in the main menu.
image menu_fade:
    "white"
    menu_fadeout

# These images show each respective characters' menu sprite and positions/animations.
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# These images are the same as above but ghost themed for the secret ghost menu
# that appears rarely in-game .
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# This image sprite shows a glitched Sayori menu sprite after Act 1 finishes.
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

# This image shows the main menu screen in the main/pause menu.
image menu_nav:
    "gui/overlay/main_menu.png"
    #recolorize("gui/overlay/main_menu.png", "#ffbde1")
    menu_nav_move

## Main Menu Effects
# These transforms and image transform store the effects that appear in the
# main menu on startup.

# This image transform shows a particle burst effect image to the main menu when
# the game starts.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

# This transform fades out the particle effects of the main menu
transform particle_fadeout:
    easeout 1.5 alpha 0

# This transform moves the polka-dot menu background to the upper-left.
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

# This transform loops the polka-dot moving effect.
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

# This transform moves the menu logo down to it's intended placement in-game.
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

# This transform moves the main menu screen in-game to be visible.
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

# This transform fades out the main menu screen. 
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

# This transform takes in a z-axis, x-axis and zoom numbers and moves the menu
# sprites to where they appear in the game.
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

## Team Salvato Splash Screen
# This image stores the Tean Salvato logo image that appears when the game starts.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# This image is a left over from DDLC's development that shows the splash message
# when the game starts.
image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

## This init python statement checks if the character files are present in-game
## and writes them to the characters folder depending on the playthrough.
init python:
    if not persistent.do_not_delete:
        if renpy.android:
            if not os.path.exists(os.path.join(os.environ['ANDROID_PUBLIC'], "characters")):
                os.mkdir(os.path.join(os.environ['ANDROID_PUBLIC'], "characters"))
        else:
            if not os.path.exists(os.path.join(config.basedir, "characters")):
                os.mkdir(os.path.join(config.basedir, "characters"))
        restore_all_characters()

## These images are the background images shown in-game during the disclaimer.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## This sets the persistent to false in order to choose a language.
default persistent.has_chosen_language = False

## This sets the first run variable to False to show the disclaimer.
default persistent.first_run = False

## This sets the lockdown check variable to False to show the warning for developers.
default persistent.lockdown_warning = False

## Startup Disclaimer
## This label calls the disclaimer screen that appears when the game starts.
label splashscreen:
    ## This python statement grabs the username and process list of the PC.
    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try: process_list = subprocess.run("wmic process get Description", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n")
            except subprocess.CalledProcessError:
                try:
                    process_list = subprocess.run("powershell (Get-Process).ProcessName", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").strip().split("\n") # For W10/11 builds > 22000
                    
                    for i, x in enumerate(process_list):
                        process_list[i] = x + ".exe"
                except: 
                    pass            
        else:
            try: process_list = subprocess.run("ps -A --format cmd", check=True, shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n") # Linux
            except subprocess.CalledProcessError: process_list = subprocess.run("ps -A -o command", check=True, shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n") # MacOS
                
            process_list.pop(0)

        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                currentuser = user

    ## This if statement checks if we have passed the disclaimer and that the
    ## current version of the mod equals the old one or the autoload is set to 
    ## the post-credit loop.
    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black

        menu:
            "检测到先前的存档文件，请问您希望删除存档数据并重新开始游玩吗？"
            "是，删除现有存档数据。":
                "正在删除存档数据...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "不，请从我上次游玩的地方继续。":
                $ restore_relevant_characters()

    if not persistent.lockdown_warning:
        if config.developer:
            call lockdown_check
        else:
            $ persistent.lockdown_warning = True

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        ## Switch to language selector. Borrowed from Ren'Py
        if not persistent.has_chosen_language and translations:

            if _preferences.language is None:
                call choose_language
        
        $ persistent.has_chosen_language = True

        ## You can edit this message but you MUST declare that your mod is 
        ## unaffiliated with Team Salvato, requires that the player must 
        ## finish DDLC before playing, has spoilers for DDLC, and where to 
        ## get DDLC's files."
        "[config.name] 是 Doki Doki Literature Club 的饭制模组，与 Team Salvato 完全无关。"
        "本模组需要在通关原版游戏后再进行游玩，且本模组包含原版游戏的剧透。"
        "游玩本模组需要原版 Doki Doki Literature Club 的文件。您可以在 {a=https://ddlc.moe}https://ddlc.moe{/a} 或者 Steam 免费获取。"

        menu:
            "如果继续游玩 [config.name] 将视为你已经通关原版游戏，并接受任何剧透内容。"
            "我同意。":
                pass
            "我不同意，退出。":
                $ renpy.quit()
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        ## （需要启用额外选项）自动检测设备是否正在运行直播 / 录屏类软件，并自动切换到实况共玩模式，
        ## 提醒用户已经启用该模式。基于原版模板加大了覆盖范围。
        ## （该模式无法解除 DDLC 在中国大陆的屏蔽）
        if extra_settings:
            if process_check(["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe", "dytool.exe", "twitchstudio.exe", "gamecaster.exe", "evcapture.exe", "kk.exe", "streamlabs obs.exe"]):
                $ persistent.lets_play = True
                call screen dialog("实况共玩模式已自动启用。\n该模式允许你跳过包含敏感内容的内容，同时也可以提供备选故事方案。\n设置可用性取决于模组开发者是否在故事线中进行了相应配置。\n\n如需关闭实况共玩模式，请前往设置，并取消选择“实况共玩模式”。\n请注意：实况共玩模式无法改变 DDLC 在中国大陆的屏蔽现状，\n请始终避免在中国大陆平台发布 / 直播与 DDLC 有关的内容。\n同时，无论如何，请注意安全。", 
                    [Hide("dialog"), Return()])
        scene white

    ## 该 Python 脚本包含控制纱世里“提早去世”屏幕展示的脚本。
    ## 为保证模组安全，默认注释该段，但如果有需要，仍可解除注释，再次启用。
    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: renpy.file("../characters/sayori.chr")
    #         except IOError: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: renpy.file("../characters/monika.chr")
    #             except IOError: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: renpy.file("../characters/natsuki.chr")
    #             except IOError: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: renpy.file("../characters/yuri.chr")
    #             except IOError: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: renpy.file("../characters/sayori.chr")
    #             except IOError: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    ## This if statement controls which special poems are shown to the player in-game.
    if not persistent.special_poems:
        python hide:
            # This variable sets a array of zeroes to assign poem numbers.
            persistent.special_poems = [0,0,0]
            
            # This sets the range of poem numbers to pick from.
            a = list(range(1,12))

            # This for loop loops 3 times (array number of special_poems) and
            # assigns a random number to the array.
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                # This line makes sure we remove the number chosen from the range
                # list to avoid duplicates.
                a.remove(b)

    ## This variable makes sure the path of the base directory is Linux/macOS/Unix 
    ## based than Windows as Python/Ren'Py prefers this placement.
    $ basedir = config.basedir.replace('\\', '/')

    ## This if statement checks whether we have a auto-load set to load it than
    ## start the game screen as-new.
    if persistent.autoload:
        jump autoload

    ## This variable sets skipping to False for the splash screen.
    $ config.allow_skipping = False

    ## This if statement checks if we are in Act 2, have not seen the ghost menu
    ## before and a random number is 0 from 0-63.
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        # These variables set the splash and menu screen to be a ghost menu.
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    ## This if statement checks if 'sayori.chr' was deleted after the disclaimer
    ## was made. This feature has been commented out for mod safety reasons but
    ## can be used if needed.
    # if s_kill_early:
    #     show black
    #     play music "bgm/s_kill_early.ogg"
    #     $ pause(1.0)
    #     show end with dissolve_cg
    #     $ pause(3.0)
    #     scene white
    #     show expression "images/cg/s_kill_early.png":
    #         yalign -0.05
    #         xalign 0.25
    #         dizzy(1.0, 4.0, subpixel=False)
    #     show white as w2:
    #         choice:
    #             ease 0.25 alpha 0.1
    #         choice:
    #             ease 0.25 alpha 0.125
    #         choice:
    #             ease 0.25 alpha 0.15
    #         choice:
    #             ease 0.25 alpha 0.175
    #         choice:
    #             ease 0.25 alpha 0.2
    #         choice:
    #             ease 0.25 alpha 0.225
    #         choice:
    #             ease 0.25 alpha 0.25
    #         choice:
    #             ease 0.25 alpha 0.275
    #         choice:
    #             ease 0.25 alpha 0.3
    #         pass
    #         choice:
    #             pass
    #         choice:
    #             0.25
    #         choice:
    #             0.5
    #         choice:
    #             0.75
    #         repeat
    #     show noise:
    #         alpha 0.1
    #     with Dissolve(1.0)
    #     show expression Text("现在大家都高兴了。", style="sayori_text"):
    #         xalign 0.8
    #         yalign 0.5
    #         alpha 0.0
    #         600
    #         linear 60 alpha 0.5
    #     pause
    #     $ renpy.quit()

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    $ pause(1.5)
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ pause(0.5)
    $ config.allow_skipping = True
    return

## This label is a left-over from DDLC's development that hides the Team Salvato
## logo and shows the splash message.
label warningscreen:
    hide intro
    show warning
    pause 3.0

## 本 label 用于在一周目第一天，monika.chr 文件被删除后触发。
## 本功能默认被注释，以确保模组安全，但如果你有使用需求，也可以随时取消该段注释。

# label ch0_kill:
#     $ s_name = "纱世里"
#     show sayori 1b zorder 2 at t11
#     s "..."
#     s "..."
#     s "什...什么......"
#     s 1g "..."
#     s "这..."
#     s "这是哪里......?"
#     s "哦......"
#     s 1u "不......"
#     s "不可能。"
#     s "绝对不可能。"
#     s 4w "这又是哪跟哪？"
#     s "我又是谁？"
#     s "停下来！"
#     s "快点停下来！！！"

#     $ delete_character("sayori")
#     $ delete_character("natsuki")
#     $ delete_character("yuri")
#     $ delete_character("monika")
#     $ renpy.quit()
#     return

## 该 label 检测即将读取的存档是否与目前存档的反作弊码一致。
label after_load:
    $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    ## This 'if' statement makes sure if we are in Yuri's death CG in
    ## Act 2 to bring us back to the scene at a given time.
    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     if persistent.yuri_kill >= 1380:
    #         $ persistent.yuri_kill = 1440
    #     elif persistent.yuri_kill >= 1180:
    #         $ persistent.yuri_kill = 1380
    #     elif persistent.yuri_kill >= 1120:
    #         $ persistent.yuri_kill = 1180
    #     elif persistent.yuri_kill >= 920:
    #         $ persistent.yuri_kill = 1120
    #     elif persistent.yuri_kill >= 720:
    #         $ persistent.yuri_kill = 920
    #     elif persistent.yuri_kill >= 660:
    #         $ persistent.yuri_kill = 720
    #     elif persistent.yuri_kill >= 460:
    #         $ persistent.yuri_kill = 660
    #     elif persistent.yuri_kill >= 260:
    #         $ persistent.yuri_kill = 460
    #     elif persistent.yuri_kill >= 200:
    #         $ persistent.yuri_kill = 260
    #     else:
    #         $ persistent.yuri_kill = 200
    #     jump expression persistent.autoload

    ## 如果你取消注释了上方的代码，请将下面的 “if” 修改为 “elif”。
    ## This statement checks if the anticheat number is equal to the 
    ## anticheat number in the save file, else it errors out.
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "存档文件加载失败。"
        "您是不是想作弊呢？"
        $ m_name = "莫妮卡"
        show monika 1 at t11
        if persistent.playername == "":
            m "真有意思啊。"
        else:
            m "真有意思啊，[persistent.playername]。"
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("提示：您可以使用“快进”按钮来快速跳过您阅读过的文字。", ok_action=Return())
    return

## This label loads the label saved in the autoload variable. 
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

## 该 label 用于游戏开始时直接加载三周目优里灾厄画面并“快进”。
# label autoload_yurikill:
#     if persistent.yuri_kill >= 1380:
#         $ persistent.yuri_kill = 1440
#     elif persistent.yuri_kill >= 1180:
#         $ persistent.yuri_kill = 1380
#     elif persistent.yuri_kill >= 1120:
#         $ persistent.yuri_kill = 1180
#     elif persistent.yuri_kill >= 920:
#         $ persistent.yuri_kill = 1120
#     elif persistent.yuri_kill >= 720:
#         $ persistent.yuri_kill = 920
#     elif persistent.yuri_kill >= 660:
#         $ persistent.yuri_kill = 720
#     elif persistent.yuri_kill >= 460:
#         $ persistent.yuri_kill = 660
#     elif persistent.yuri_kill >= 260:
#         $ persistent.yuri_kill = 460
#     elif persistent.yuri_kill >= 200:
#         $ persistent.yuri_kill = 260
#     else:
#         $ persistent.yuri_kill = 200
#     jump expression persistent.autoload

## This label sets the main menu music to Doki Doki Literature Club before the
## menu starts. (This is not my favor.)
label before_main_menu:
    # $ config.main_menu_music = audio.t1 # 所以为什么要默认重置主菜单 bgm 啊（恼
    return

## 该 label 控制游戏退出后会发生的事件。
## 但是如果此时处于“ghost menu”，退出游戏时会显示一瞬间的莫妮卡跳杀。
label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
