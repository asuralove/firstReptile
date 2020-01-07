import codecs
import frida
import os

def adbforward():
    os.system("adb forward tcp:27042 tcp:27042")
    os.system("adb forward tcp:27043 tcp:27043")

hook_code = '''
rpc.exports = {
    gethello: function(str){
        send('heelo');
        Java.perform(function(){

            //拿到context上下文
            var currentApplication = Java.use('android.app.ActivityThread').currentApplication();
            var context = currentApplication.getApplicationContext();


            var AuthUtils = Java.use('com.coolapk.market.util.AuthUtils');
            //f = tt.$new();
            var sig = AuthUtils.getAS(context, str);
            send(sig);
        }
    )
    }
};
'''

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])

process = frida.get_usb_device(1).attach('com.coolapk.market')
script = process.create_script(hook_code)
script.on('message', on_message)
script.load()

print(script.exports.gethello('weuhhfb345684533sde6jkfg'))


# device_manager = frida.get_device_manager()
# device = device_manager.add_remote_device("192.168.0.107")

# #s = frida.get_remote_device("192.168.0.107")
# session = device.attach('com.coolapk.market')
# #with codecs.open('./agent.js', 'r', 'utf-8') as f:
# #    source = f.read()
# script = session.create_script(hook_code)
# script.on('message', on_message)
# script.load()
# script.exports.getH('code')
# session.detach()