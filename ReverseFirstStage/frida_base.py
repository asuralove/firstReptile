import frida,sys

def on_message(message,data):
    if message['type'] == 'send':
        print("[*]{0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function(){
//获取当前安卓设备的安卓版本
var v = Java.androidVersion;
send('version:'+v);

//获取该应用加载的类
var classnames = Java.enumerateLoadedClassesSync();
for(var i = 0;i < classnames.length;i++){
    sned('class name:'+classnames[i]);
};
})
"""

jscode_signature = """
Java.perform(function(){
    var TestSig = Java.use('com.yaotong.crackme.MainActivity');
    var mystr = Java.use('java.lang.String')
    
    TestSig.securityCheck.implementation = function(str){
        send('i am here');
        return true;
    };
});
"""

#hook app启动阶段
oncreate_script = """
Java.perform(function(){
    var TestSig = Java.use('com.yaotong.crackme.MainActivity');  
    
    TestSig.onCreate.implementation = function(){
        send('i am here');
        this.onCreate();
    };
    }
);
"""
oncreate_scripts = """
function printstack(){
    send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
}
function array2string(array){
    var buffer = Java.array('byte',array);
    //console.log(buffer.length);
    var result = "";
    for(var i =0;i < buffer.length;++i){
        result+= (String.formCharCode(buffer[i]));
    }
    return result;
}
Java.perform(
    function(){
        var MessageDigest = Java.use('java.secuity.MessageDigest');
        
        MessageDigest.update.overload('[B').implementation = function(bytesarray){
            send('I am here 0;');
            send("ori:"+array2string(bytesarray));
            printstack();
            this.update(bytesarray);
        },
        MessageDigest.update.overload('byte').implementation = function(bytesarray){
            send('I am here 1;');
            //send("ori:"+array2string(bytesarray));
            //printstack();
            this.update(bytesarray);
        },
        
        MessageDigest.update.overload('java.nio.ByteBuffer').implementation = function(bytesarray){
            send('I am here 2;');
            this.update(bytesarray);
        },
        
        MessageDigest.update.overload('[B','int','int').implementation = function(bytesarray){
            send('I am here 3;');
            this.update(bytesarray);
        },
        MessageDigest.getInstance.overload[0].implementation = function(algorithm){
          send("call ->getInstance for " + algorithm);
          return this.getInstance.overload[0].apply(this,arguments);
        };
    }
);      
"""

test_module_script = """
var base_address = Module.findBaseAddress("libc.so");
send('base_address:'+base_address);

var mod_address = Module.findExportByName("libc.so","dlopen");
send('mod_address:'+mod_address);

var lib_module = Process.findModuleByAddress(base_address);
send("lib_module_name:"+lib_module.name);

Interceptor.attach(mod_address,{
    onEnter:function(args){
        //send("open("+args[0]+","+args[1]+")");
        send("open("+Memory.readUtf8String(args[0])+","+args[1]+")");
    },
    onLeave:function(retval){
        send("retval:"+retval);
    }
});
"""
#在已启动的情况下
# process = frida.get_usb_device(1).attach('com.yaotong.crackme')
# script = process.create_script(jscode_signature)
# script.on('message', on_message)
# print('[*] Running CTF')
# script.load()
# sys.stdin.read()

device = frida.get_usb_device(1)
pid = device.spawn(['com.yaotong.crackme'])
process = device.attach(pid)
script = process.create_script(oncreate_scripts)
script.on('message',on_message)
print('[*]Running CTF')
script.load()
device.resume(pid)
sys.stdin.read()
