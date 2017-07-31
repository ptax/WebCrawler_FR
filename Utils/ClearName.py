# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re


def Run(MyStr):
    if MyStr:
        LenMystr = MyStr.split('(')
        if len(LenMystr) <= 2:
            MyStr = re.sub(r'de\s', '', MyStr)
            MyStr = re.sub(r'du\s', '', MyStr)
            MyStr = re.sub(r'des\s', '', MyStr)
            MyStr = re.sub(r'\[.*\]', '', MyStr)
            MyStr = re.sub(r"^d'", '', MyStr)
            MyStr = re.sub(r'canton', '', MyStr)
            return MyStr.strip()
        else:
            return MyStr.strip()
    return MyStr


def Run_2(MyStr):
    if MyStr:
        LenMystr = MyStr.split('(')
        if len(LenMystr) <= 2:
            MyStr = re.sub(r',\(.*\)', '', MyStr)
            MyStr = re.sub(r'\(.*\)', '', MyStr)
            MyStr = re.sub(r'de\s', '', MyStr)
            MyStr = re.sub(r'du\s', '', MyStr)
            MyStr = re.sub(r'des\s', '', MyStr)
            MyStr = re.sub(r'\[.*\]', '', MyStr)
            MyStr = re.sub(r"^d'", '', MyStr)

            return MyStr.strip().lower()
        else:
            return MyStr.strip().lower()
    return MyStr.lower()


def Run_3(MyStr):
    if MyStr:
        LenMystr = MyStr.split('(')
        if len(LenMystr) <= 2:
            MyStr = re.sub(r',\(.*\)', '', MyStr)
            MyStr = re.sub(r'\(.*\)', '', MyStr)
            MyStr = re.sub(r'\[.*\]', '', MyStr)
            MyStr = re.sub(r',', '', MyStr)
            MyStr = re.sub(r"^d'", '', MyStr)


            return MyStr.strip()
        else:
            return MyStr.strip()
    return MyStr


if __name__ == '__main__':
    MyStr = u"Seine-et-Marne,(Melun)"
    print Run_3(MyStr)

    looking_status = re.compile('\(.*\)')
    looking_status = looking_status.findall(MyStr)
    if looking_status:
        status = looking_status[0]
    else:
        pass
    print status

    # MyStr = re.compile('\(.*\)', '', MyStr)
    #print MyStr
