import frida
import sys


oncreate_script = """
//打印调用堆栈
function printstack() {
    send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
}

//array 转成 string
function array2string(array){
    var buffer = Java.array('byte', array);
    //console.log(buffer.length);
    var result = "";
    for(var i = 0; i < buffer.length; ++i){
        result+= (String.fromCharCode(buffer[i]));
    }
    return result;
}

Java.perform(
    function () {
        var MessageDigest = Java.use('java.security.MessageDigest');

        MessageDigest.update.overload('[B').implementation = function (bytesarray) {
            send('I am here 0:');
            //var String = Java.use('java.lang.String').$new(bytesarray);
            send("ori:"+array2string(bytesarray));
            printstack();
            this.update(bytesarray);
        },
        MessageDigest.update.overload('byte').implementation = function (bytesarray) {
            send('I am here 1:');
            //var String = Java.use('java.lang.String').$new(bytesarray);
            //send("ori:"+array2string(bytesarray));
            //printstack();
            this.update(bytesarray);
        },

        MessageDigest.update.overload('java.nio.ByteBuffer').implementation = function (bytesarray) {
            send('I am here 2:');
            //var String = Java.use('java.lang.String').$new(bytesarray);
            //send("ori:"+array2string(bytesarray));
            //printstack();
            this.update(bytesarray);
        },
        MessageDigest.update.overload('[B', 'int', 'int').implementation = function (bytesarray) {
            send('I am here 3:');
            //var String = Java.use('java.lang.String').$new(bytesarray);
            //send("ori:"+array2string(bytesarray));
            //printstack();
            this.update(bytesarray);
        },
        MessageDigest.getInstance.overloads[0].implementation = function(algorithm) {
            send("call ->getInstance for " + algorithm);
            return this.getInstance.overloads[0].apply(this, arguments);
        };
    }
);
"""

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

#4560
# process = frida.get_usb_device(1).attach('com.yaotong.crackme')
# script = process.create_script(oncreate_script)
# script.on('message', on_message)
# print('[*] Running CTF')
# script.load()
# sys.stdin.read()

device = frida.get_usb_device(1)
pid = device.spawn(['com.iCitySuzhou.suzhou001'])
process = device.attach(pid)

script = process.create_script(oncreate_script)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
device.resume(pid)
sys.stdin.read()

# device = frida.get_usb_device()
# pid = device.spawn(['com.iCitySuzhou.suzhou001'])
# process = device.attach(pid)

# script = process.create_script(oncreate_script)
# script.on('message', on_message)
# print('[*] Running CTF')
# script.load()
# device.resume(pid)
# sys.stdin.read()