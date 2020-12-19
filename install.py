#!/usr/bin/env python3

from os import environ, mkdir, path
from shutil import copytree, rmtree
from sys import platform

def install():
    print('copy resource pack... ', end='')
    MCPYPATH = search_mcpy()
    if not path.isdir(path.join(MCPYPATH, 'resource-pack')):
        mkdir(path.join(MCPYPATH, 'resource-pack'))
    if path.isdir(path.join(MCPYPATH, 'resource-pack', 'default')):
        rmtree(path.join(MCPYPATH, 'resource-pack', 'default'))
    copytree(get_dir('default'), path.join(MCPYPATH, 'resource-pack', 'default'))
    print('done')

def get_dir(d):
    return path.abspath(path.join(path.dirname(__file__), d))

def search_mcpy():
    # 搜索文件存储位置
    if 'MCPYPATH' in environ:
        MCPYPATH = environ['MCPYPATH']
    elif platform.startswith('win'):
        MCPYPATH = path.join(path.expanduser('~'), 'mcpy')
    else:
        MCPYPATH = path.join(path.expanduser('~'), '.mcpy')
    return MCPYPATH

if __name__ == '__main__':
    install()
