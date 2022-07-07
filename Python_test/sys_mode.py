# coding: utf-8
__author__ = 'www.py3study.com'
import sys

class showSysmodule(object):
    '''这个类用于展示python标准库中的sys模块'''
    def __init__(self):
        print(u'sys模块最常用的功能就是获取程序的参数')
        self.getArg()
        print(u'其次就是获取当前的系统平台')
        self.getOs()

    def getArg(self):
        print(u'开始获取参数的个数')
        print(u'当前参数有{}个'.format(len(sys.argv)))
        print(u'这些参数分别是{}'.format(sys.argv))

    def getOs(self):
        print(u'sys.platform返回值对应的平台:')
        print('System\t\t\tPlatform')
        print('Linux\t\t\tlinux2')
        print('Windows\t\t\twin32')
        print('Cygwin\t\t\tcygwin')
        print('Mac OS X\t\tdarwin')
        print('OS/2\t\t\tos2')
        print('OS/2 EMX\t\tos2emx')
        print('RiscOS\t\t\triscos')
        print('AtheOS\t\t\tatheos')
        print('\n')
        print(u'当前的系统为:{}'.format(sys.platform))

if __name__ == '__main__':
    ssm = showSysmodule()