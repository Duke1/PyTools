# encoding: UTF-8
__author__ = 'Duke'

import subprocess
import re
import platform
import qrcode
import zbar
from PIL import Image

import os

PORT = 8000

CUR_PATH = os.path.dirname(os.path.abspath(__file__))


def generateQRCode(name, code_content, savepath=CUR_PATH, code_box_size=10, code_border=2,
                   code_version=1, code_error_correction=qrcode.constants.ERROR_CORRECT_H):
    qr = qrcode.QRCode(
        version=code_version,
        error_correction=code_error_correction,
        box_size=code_box_size,
        border=code_border,
    )

    qr.add_data(code_content)
    qr.make(fit=True)

    qrImg = qr.make_image()
    qrImg = qrImg.convert("RGBA")

    if os.path.exists(logo_image):
        icon = Image.open(logo_image)
        # 二维码图片尺寸
        img_w, img_h = qrImg.size

        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        # logo图片的尺寸不能超过二维码图片的1/4
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        # 计算logo图片位置
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        qrImg.paste(icon, (w, h), icon)

    savepath = '{0}/{1}.jpg'.format(savepath, name)

    img_savefile = open(savepath, "wb")
    qrImg.save(img_savefile, "JPEG")
    img_savefile.close()

    return savepath


def getQrContent(path):
    # 创建图片扫描对象
    scanner = zbar.ImageScanner()
    # 设置对象属性
    scanner.parse_config('enable')

    # 打开含有二维码的图片
    img = Image.open(path).convert('L')
    # 获取图片的尺寸
    width, height = img.size

    # 建立zbar图片对象并扫描转换为字节信息
    qrCode = zbar.Image(width, height, 'Y800', img.tobytes())
    scanner.scan(qrCode)

    data = ''
    for s in qrCode:
        data += s.data

    # 删除图片对象
    del img

    # 输出解码结果
    print (data)


if __name__ == "__main__":
    getQrContent('./linkedme.png')
