# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re


def Run(MyStr):
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
            MyStr = re.sub(r'canton', '', MyStr)
            MyStr = MyStr.replace(u'arrondissement', '')

            return MyStr.strip()
        else:
            return MyStr.strip()
    return MyStr


if __name__ == '__main__':
    MyStr = u"  la sfdsf "
    print Run(MyStr)