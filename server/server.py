# encoding: UTF-8
__author__ = 'Duke'

import http.server
import socketserver
import socket
import logging

import subprocess
import re
import platform
import qrcode
from PIL import Image

import os

PORT = 8000

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
logo_image = './logo.png'


# local ip
# socket.gethostbyname(socket.gethostname())
# ipList = socket.gethostbyname_ex(socket.gethostname())
#python -m http.server 8000
class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

def openServer(ip):

    #http.server.SimpleHTTPRequestHandler
    Handler = GetHandler

    socketserver.TCPServer.allow_reuse_address = True
    #ip
    httpd = socketserver.ThreadingTCPServer(('', PORT), Handler)
    socketserver.timeout = 60
    socketserver.request_queue_size = 200;

    print("serving at port ", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('中断')
    finally:
        print ('关闭服务')
        httpd.server_close()



def find_all_ip(platform):
    print(platform);
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if platform == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        ip_pattern = re.compile("IPv4*")
        pattern = re.compile(ipstr)
        # print (output.decode('gb2312'))
        outLines = ipconfig_process.stdout.readlines()
        iplist = []
        for line in outLines:
            lineStr = str(line.decode('gbk'))
            match_ipv4 = ip_pattern.search(lineStr)
            match_ip_number = pattern.search(lineStr)
            if match_ipv4 and match_ip_number:
                iplist.append(match_ip_number.group())

        return iplist
    elif platform =="Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile('(inet %s)' % ipstr)
        if platform == "Linux":
            ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        #print (iplist)
        return iplist        


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
    qrImg=qrImg.convert("RGBA")

    if  os.path.exists(logo_image):
        icon=Image.open(logo_image)
        #二维码图片尺寸
        img_w,img_h=qrImg.size

        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)

        #logo图片的尺寸不能超过二维码图片的1/4
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)

        #计算logo图片位置
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        qrImg.paste(icon,(w,h),icon)

    savepath = '{0}/{1}.jpg'.format(savepath, name)

    img_savefile = open(savepath, "wb")
    qrImg.save(img_savefile, "JPEG")
    img_savefile.close()

    return savepath


if __name__ == "__main__":
    ips = find_all_ip(platform.system())
    print (ips)
    if 0==len(ips):
        inputIp = input('输入ip: ')
        ips.append(inputIp)

    if os.path.exists('./offical.apk'):
        for ip in ips:
            generateQRCode(ip, 'http://{host}:{port}/{filePath}'.format(host=ip, port=PORT,filePath='offical.apk'))

    print ('\r\n生成二维码成功！！\r\n')
    openServer(ips[0])


    #Address already in use --> lsof -i :8000
