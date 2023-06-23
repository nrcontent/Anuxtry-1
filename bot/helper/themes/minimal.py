#!/usr/bin/env python3
class style:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/WZML_X'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>'''
    # ---------------------

    # async def stats(client, message):
    STATS = '''⌬ <b>BOT VERSION :</b>
 <b>Bot Updated :</b> {last_commit}
 <b>Bot Version :</b> {bot_version}
 <b>Last ChangeLog :</b> {commit_details}

⌬ <b><i>BOT SYSTEM :</i></b>
┠ <b>Bot Uptime :</b> {bot_uptime}
┠ <b>OS Uptime :</b> {os_uptime}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>BOT ANALYSIS :</i></b>
┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┖ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core} ( <b>T :</b> {total_core} )

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>Disk Storage :</i></b>
┃ {disk_bar} {disk}%
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}

⌬ <b><i>BOT DATA :</i></b>
┖ <b>UP Data:</b> {up_data} | <b>DL Data:</b> {dl_data}'''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    L_PM_START =            "➲ <b><u>Leech Started :</u></b>\n┃\n┖ <b>Source :</b> {msg_link}"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( {uid} )\n┖ <b>Source :</b> {msg_link}"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '┠ <b>Size: </b>{Size}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┖ <b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '➲ <b><i>Files are Send Above</i></b>'
    L_BOT_MSG =             '➲ <b><i>Files are Send to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>Files are Send. Access via Links...</i></b>'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>Files: </b>{Files}\n'
    RCPATH =                '┠ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Links are Send to Bot PM (Private)</i></b>'
    
    # ----- BUTTONS -------
    CLOUD_LINK =      'Cloud Link'
    SAVE_MSG =        'Save Message'
    RCLONE_LINK =     'Rclone Link'
    DDL_LINK =        '{Serv} Link'
    INDEX_LINK =      'Index Link'
    VIEW_LINK =       'View Link'
    CHECK_PM =        'View in Bot PM'
    CHECK_LL =        'View in Leech Log'
    MEDIAINFO_LINK =  'MediaInfo'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>Processed:</b> {Processed}'
    STATUS =            '\n┠ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '\n┠ <b>Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┠ <b>Engine:</b> {Engine}'
    SEEDERS =           '\n┠ <b>Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>Size: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n┠ <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>Size: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    CANCEL = '''\n┖ {Cancel}\n\n'''

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>Bot Stats</i></b>\n'
    PAGE = '┠ <b>Page:</b> {Page} | '
    TASKS =                       '<b>Tasks:</b> {Tasks}\n'
    Cpu = '┠ <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>FREE:</b> {free}'
    Ram = '\n┠ <b>RAM:</b> {ram}% | '
    uptime =                     '<b>UPTIME:</b> {uptime}'
    DL = '\n┖ <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = '♺ Refresh'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n'
    COUNT_SIZE = '┠ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<code>No Active Downloads!</code>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>FREE:</b> {free}
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dump :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
