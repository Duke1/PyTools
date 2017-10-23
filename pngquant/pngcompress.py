#! python3
# coding=utf-8
__author__ = 'Duke'

import getopt
import sys
import os

import shutil

from decimal import getcontext, Decimal
from termcolor import *

RATE_THRESHOLD=0 #1%

def compressDir(oriDir, outDir, result):
    if os.path.exists(outDir):
        shutil.rmtree(outDir)
    os.makedirs(outDir)

    if not os.path.exists(oriDir):
        print ('directory not found !!!')
        return
    for file in os.listdir(oriDir):
        sourceFile = os.path.join(oriDir, file)
        if os.path.isfile(sourceFile):
            compressFile(sourceFile, outDir, result)


def compressFile(fileName, outDir, result):
    fileNames = os.path.splitext(fileName)
    if 2 == len(fileNames) and not '.png' == fileNames[1]:
        return ""

    oriSize = os.path.getsize(fileName)

    outputName = ''.join([outDir, '/', os.path.basename(fileName)])
    cmd = 'pngquant -o {outputName} --quality 50-50 {intputFile}'.format(intputFile=fileName,
                                                                         outputName=outputName)
    os.system(cmd)
    compressSize = os.path.getsize(outputName)

    rate = Decimal(float((oriSize - compressSize) / oriSize * 100)).quantize(Decimal('0.00'))
    if rate > RATE_THRESHOLD:
        printString = '{fileName} {oriSize}-->{nowSize}  [COMPRESSED]~{rate}%'
        printString = printString.format(fileName=os.path.basename(fileName), oriSize=oriSize,
                                         nowSize=compressSize, rate=rate)
    else:
        printString = "".join([fileName, "  Skip ##~", str(rate), "%"])

    result.append(printString)


def main():
    ori_dir = ""
    out_dir = ""
    result = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:o:', ["src="])
        for op, value in opts:
            if op in ("-s", "--src"):
                ori_dir = value
    except getopt.GetoptError:
        print(sys.argv[0] + " : params are not defined well!")

    out_dir = ''.join([ori_dir, '_out'])
    compressDir(ori_dir, out_dir, result)

    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            vj = result[j]
            vj1 = result[j + 1]
            size = float(vj[vj.index("~") + 1:len(vj) - 1])
            size1 = float(vj1[vj1.index("~") + 1:len(vj1) - 1])
            if size < size1:
                result[j], result[j + 1] = result[j + 1], result[j]
    for data in result:
        if data.find("##") >= 0:
            print(colored(data, "green"))
        else:
            print (data)


if __name__ == "__main__":
    main()


#python3 pngcompress.py -s 路径