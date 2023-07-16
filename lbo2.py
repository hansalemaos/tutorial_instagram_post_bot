import os

import pandas as pd
from adbkit import ADBTools
from time import sleep
import glob


def get_uiautomator_frame(screenshotfolder="c:\\ttscreenshots"):
    df = pd.DataFrame()
    while df.empty:
        adb.aa_update_screenshot()
        df = adb.aa_get_all_displayed_items_from_uiautomator(
            screenshotfolder=screenshotfolder,  # screenshots will be saved here
            max_variation_percent_x=10,
            # used for one of the click functions, to not click exactly in the center - more information below
            max_variation_percent_y=10,  # used for one of the click functions, to not click exactly in the center
            loung_touch_delay=(
                1000,
                1500,
            ),  # with this settings longtouch will take somewhere between 1 and 1,5 seconds
            swipe_variation_startx=10,  # swipe coordinate variations in percent
            swipe_variation_endx=10,
            swipe_variation_starty=10,
            swipe_variation_endy=10,
            sdcard="/storage/emulated/0/",
            # sdcard will be used if you use the sendevent methods, don't pass a symlink - more information below
            tmp_folder_on_sd_card="AUTOMAT",  # this folder will be created in the sdcard folder for using sendevent actions
            bluestacks_divider=32767,
            # coordinates must be recalculated for BlueStacks https://stackoverflow.com/a/73733261/15096247 when using sendevent
        )
    return df


ADBTools.aa_kill_all_running_adb_instances()
adb_path = r"C:\ProgramData\chocolatey\bin\adb.exe"
deviceserial = "localhost:5555"
adb = ADBTools(adb_path=adb_path, deviceserial=deviceserial)

adb.aa_start_server()
sleep(3)
adb.aa_connect_to_device()
adb.aa_activate_adb_keyboard()
jafeito = []
files = sorted(set(glob.glob(r"C:\instaposts\*.jpg")) - set(jafeito), reverse=True)
arquivo_para_postar = files[-1]
jafeito.append(arquivo_para_postar)
adb.aa_push_file_to_path(arquivo_para_postar, "/sdcard/DCIM/")
adb.aa_execute_multiple_adb_shell_commands(
    [
        f"""am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE """
        f'''-d \"file:///mnt/sdcard/DCIM/{arquivo_para_postar.split(os.sep)[-1]}\"'''
    ]
)
adb.aa_execute_multiple_adb_shell_commands(
    [
        'am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" '
        '-n "com.instagram.lite/com.facebook.lite.MainActivity"'
    ]
)
sleep(4)
df = get_uiautomator_frame()
df.loc[
    df.bb_keys_hierarchy
    == ("node", "node", 0, "node", "node", "node", "node", 1, "node", 7)
].ff_bb_tap_exact_center_long.iloc[0]()
sleep(2)
df = get_uiautomator_frame()
df.loc[(df.bb_height == df.bb_width) & (df.bb_area > 100000)].sort_values(
    by=["bb_x_start", "bb_y_start"]
).iloc[0].ff_bb_tap_exact_center()
sleep(1)
df2 = df.loc[(df.bb_class == "android.view.ViewGroup") & df.bb_clickable]
sleep(2)
df2.loc[df2.bb_center_y == df2.bb_center_y.value_counts().index[0]].sort_values(
    by="bb_center_x", ascending=False
).iloc[0].ff_bb_tap_exact_center()
sleep(2)
df2.loc[df2.bb_center_y == df2.bb_center_y.value_counts().index[0]].sort_values(
    by="bb_center_x", ascending=False
).iloc[0].ff_bb_tap_exact_center()
sleep(2)
df = get_uiautomator_frame()
df.loc[df.bb_text.str.contains("rite")].iloc[0].ff_bb_tap_exact_center()
adb.bb_adbkeyboard.activate_adb_keyboard()
sleep(1)
with open(arquivo_para_postar[:-3] + "txt", encoding="utf-8") as f:
    texto = f.read()
adb.bb_adbkeyboard.send_unicode_text_with_delay(texto)
adb.bb_adbkeyboard.disable_adb_keyboard()
