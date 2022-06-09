# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 12:25
# @Author  : Jaywatson
# @File    : AES.py
# @Soft    : backend_flask
import os
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES

key = os.getenv('AES_SECRET_KEY').encode('utf-8')
mode = AES.MODE_CBC

# aes加密
def encrypt(text):
    try:
        cryptor = AES.new(key, mode, key)
        length = 16
        count = len(text)
        add = 0
        if count < length:
            add = (length - count)
        elif count > length:
            add = (length - (count % length))
        text_new = (text + ('\0' * add)).encode('utf-8')
        ciphertext = cryptor.encrypt(text_new)
        return bytes.decode(b2a_hex(ciphertext), encoding='utf8')
    except Exception as e:
        return ''

# aes解密
def decrypt(text):
    try:
        cryptor = AES.new(key, mode, key)
        plain_text = bytes.decode(cryptor.decrypt(a2b_hex(bytes(text, encoding='utf8'))), encoding='utf8')
        return plain_text.rstrip('\0')
    except Exception as e:
        return ''
