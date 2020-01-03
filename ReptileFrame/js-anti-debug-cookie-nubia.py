#!/usr/bin/env python3
# coding:utf-8
# Author: veelion

'''
https://bbs.nubia.cn/
'''

import time
import urllib.parse as urlparse
import execjs
import re
import requests
import base64
import urllib.parse as urlparse



def run_js(fp):
    js = open(fp).read()
    ctx = execjs.compile(js)
    print(ctx)
    arg2 = ctx.eval('arg2')
    print(arg2)


def rc4(_0x401af1, _0x532ac0):

    _0x45079a = ['']*256  # 40行的 0x100 == 256
    _0x52d57c = 0x0
    _0x105f59, _0x3fd789 = '', ''
    _0x4a2aed = ''
    _0x401af1 = base64.b64decode(_0x401af1) #atob
    for _0x124d17 in range(len(_0x401af1)):
        _0x4a2aed += '%' + ('00' + hex(_0x401af1[_0x124d17])[2:])[-2:]

    # print('_0x4a2aed:', _0x4a2aed)
    _0x401af1 = urlparse.unquote(_0x4a2aed)
    # print('_0x401af1:', _0x401af1)
    for _0x2d67ec in range(0x100):
        _0x45079a[_0x2d67ec] = _0x2d67ec
    for _0x2d67ec in range(0x100):
        _0x52d57c = (_0x52d57c + _0x45079a[_0x2d67ec] + ord(_0x532ac0[_0x2d67ec % len(_0x532ac0)])) % 0x100
        _0x105f59 = _0x45079a[_0x2d67ec]
        _0x45079a[_0x2d67ec] = _0x45079a[_0x52d57c]
        _0x45079a[_0x52d57c] = _0x105f59
    _0x2d67ec = 0x0
    _0x52d57c = 0x0
    # print('_0x45079a:', _0x45079a)
    # print('len:', len(_0x401af1))
    for _0x4e5ce2 in range(len(_0x401af1)):
        _0x2d67ec = (_0x2d67ec + 0x1) % 0x100
        _0x52d57c = (_0x52d57c + _0x45079a[_0x2d67ec]) % 0x100
        _0x105f59 = _0x45079a[_0x2d67ec]
        _0x45079a[_0x2d67ec] = _0x45079a[_0x52d57c]
        _0x45079a[_0x52d57c] = _0x105f59
        _0x3fd789 += chr(ord(_0x401af1[_0x4e5ce2]) ^ _0x45079a[(_0x45079a[_0x2d67ec] + _0x45079a[_0x52d57c]) % 0x100])
    return _0x3fd789 # 得出'unsbox'

def hexXor_arg2(encode_arg1, _0x4e08d8):
    _0x5a5d3b = ''
    _0xe89588 = -2
    while 1:
        _0xe89588 += 2
        if _0xe89588 >= len(encode_arg1) or _0xe89588 >= len(_0x4e08d8):
            break
        _0x401af1 = int(encode_arg1[_0xe89588:_0xe89588+2], 16)
        _0x105f59 = int(_0x4e08d8[_0xe89588:_0xe89588+2], 16)
        _0x189e2c = hex(_0x401af1 ^ _0x105f59)[2:]
        if len(_0x189e2c) == 0x1:
            _0x189e2c = '0' + _0x189e2c
        _0x5a5d3b += _0x189e2c
    return _0x5a5d3b #通过arg2获得第二个变量

def unsbox_arg1(arg1):
    _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd, 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c, 0x22, 0x25, 0xc, 0x24]
    _0x4da0dc = [''] * len(_0x4b082b)
    _0x12605e = '';
    for _0x20a7bf in range(len(arg1)):
        _0x385ee3 = arg1[_0x20a7bf];
        for _0x217721 in range(len(_0x4b082b)):
            if (_0x4b082b[_0x217721] == _0x20a7bf + 0x1):
                _0x4da0dc[_0x217721] = _0x385ee3;
    _0x12605e = ''.join(_0x4da0dc)
    return _0x12605e;   #通过arg1函数得到变量

    # _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd, 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c, 0x22, 0x25, 0xc, 0x24]
    # _0x4da0dc = [''] * len(_0x4b082b)
    # _0x12605e = ''
    # for _0x20a7bf in range(len(arg1)):
    #     _0x385ee3 = arg1[_0x20a7bf]
    #     for _0x217721 in range(len(_0x4b082b)):
    #         if (_0x4b082b[_0x217721] == _0x20a7bf + 0x1):
    #             _0x4da0dc[_0x217721] = _0x385ee3
    # _0x12605e = ''.join(_0x4da0dc)
    # return _0x12605e


def disorder(_0x4818):
    counter = 0x15b
    while counter:
        counter -= 1
        _0x4818.append(_0x4818.pop(0))


def gen_cookie(js_origin):
    arg1 = re.findall(r"var arg1 = '(.*?)'", js_origin)[0]
    print('get arg1:', arg1)
    _0x4818 = re.findall(r"var _0x4818 = (.*?])", js_origin)[0]
    _0x4818 = eval(_0x4818)
    disorder(_0x4818)
    print('get _0x4818:', len(_0x4818), _0x4818[3])
    assert _0x4818[3] == 'wqhBH8Knw4TDhSDDgMOdwrjCncOWwphhN8KCGcKqw6dHAU5+wrg2JcKaw4IEJcOcwrRJwoZ0wqF9YgAV'
    token = rc4(_0x4818[3], 'jS1Y')
    assert token == '3000176000856006061501533003690027800375'

    encode_arg1 = unsbox_arg1(arg1)
    arg2 = hexXor_arg2(encode_arg1, token)
    print('cookie:', arg2)
    return arg2




if __name__ == '__main__':
    from sys import argv
    opt = argv[1]
    if opt == 'js':
        fp = argv[2]
        run_js(fp)
    elif opt == 'gen':
        js = open('./js-nubia-origin.js').read()
        cookie = gen_cookie(js)
        assert cookie == '5d302cf4838229b0b613ca9dea3709b173e473d7'
        print('gen cookie successfully')
    elif opt == 'arg1':
        # arg1 = 'AAC9EB972FEE8264A7C05F3F4DB32C95F6DF6DF7'
        arg1 = '58E0A36D5D35D56D31DB25405A373C5C71D8F62B'
        encode_arg1 = unsbox_arg1(arg1)
        print('encode_arg1:', encode_arg1)
        # assert encode_arg1 == '6D2FF4ADF2C97BF348BEF707255DAC99AEC366EF'
        assert encode_arg1 == '6D307D56D5D5B3545D3321BD52CA8C603AE71F58'

        xx = rc4(
            "wqhBH8Knw4TDhSDDgMOdwrjCncOWwphhN8KCGcKqw6dHAU5+wrg2JcKaw4IEJcOcwrRJwoZ0wqF9YgAV", 'jS1Y'
        )
        print(xx)
        assert xx == '3000176000856006061501533003690027800375'
        arg2 = hexXor_arg2(encode_arg1, '3000176000856006061501533003690027800375')
        cookie = arg2
        print(cookie)
        assert cookie == '5d2fe3cdf24c1bf54eabf654155ec5998943659a'
        print('done')
    else:
        pass
