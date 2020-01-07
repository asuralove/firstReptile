import frida, sys

hook_getUserInfo = """
Java.perform(
    function(){
        var UserInfo = Java.use('com.ss.android.common.applog.UserInfo');
        UserInfo.getUserInfo.overload('int', 'java.lang.String', '[Ljava.lang.String;', 'java.lang.String').implementation = function(v1, v2, v3, v4){
            send(v1);
            send(v2);
            send(v3);
            send(v4);
            var usr = this.getUserInfo(v1, v2, v3, v4);
            send(usr);
            return usr;
        }
    }
)
"""


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_usb_device().attach('com.ss.android.ugc.aweme.lite')
script = process.create_script(hook_getUserInfo)
script.on('message', on_message)
script.load()
sys.stdin.read()