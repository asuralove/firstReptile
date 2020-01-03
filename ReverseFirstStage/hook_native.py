import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


oncreate_script = """
Java.perform(
    function () {
        var TestSig = Java.use('com.yaotong.crackme.MainActivity');

        TestSig.onCreate.overload('android.os.Bundle').implementation = function (v) {
            send('I am here');
            this.onCreate();
        };
    }
);
"""


test_module_script = """
//var walk = Process.enumerateModules();
//for (var i = 0; i<walk.length; i++){
 //   send(walk[i].name);
//}

//var base_address = Module.findBaseAddress("libc.so");
//send('base_address:'+base_address);

var mod_address = Module.findExportByName("libc.so" , "dlopen");
send('mod_address:'+mod_address);


//var lib_module = Process.findModuleByAddress(base_address);
//send("lib_module_name:"+lib_module.name);

Interceptor.attach(mod_address, 
    {
        onEnter: function(args) {
            //send("open("+args[0]+","+args[1]+")");
            var filename = Memory.readUtf8String(args[0]);

            send(filename);
        },
        onLeave:function(retval){
            send("retval:"+retval);
        }
});
"""

hook_sec_native = """
//找到要hook 的函数的内存地址
var securityCheck = Module.findExportByName("libcrackme.so" , "Java_com_yaotong_crackme_MainActivity_securityCheck");

//hook 这个方法
Interceptor.attach(securityCheck, 
    {
        onEnter: function(args) {
        },
        onLeave:function(retval){
            send("retval:"+retval);
            retval.replace(0x1);
        }
});
"""


# process = frida.get_usb_device(1).attach('com.yaotong.crackme')
# script = process.create_script(oncreate_script)
# script.on('message', on_message)
# print('[*] Running CTF')
# script.load()
# sys.stdin.read()

device = frida.get_usb_device(1)
pid = device.spawn(['com.yaotong.crackme'])
process = device.attach(pid)

script = process.create_script(oncreate_script)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
device.resume(pid)
sys.stdin.read()