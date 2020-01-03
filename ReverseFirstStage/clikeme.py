import frida, sys
def on_message(message, data):
     if message['type'] == 'send':
         print("[*] {0}".format(message['payload']))
     else:
         print(message)
jscode = """
Java.perform(function () {
//获取当前安卓设备的安卓版本
var v = java.androidVersion;
send('version:'+v);

//获取改应用加载的类
var classnames = Java.enumerateLoadedClassesSync();
for(var i = 0;i < classnames[i]);
    send('class name:'+classname[i]);
};
})
"""
process = frida.get_usb_device().attach('com.yaotong.crackme')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()