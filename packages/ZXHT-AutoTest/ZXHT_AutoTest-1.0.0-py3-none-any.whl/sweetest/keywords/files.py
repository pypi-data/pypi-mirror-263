# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 16:39
@Author : TJF

"""
import os

from sweetest.log import logger

def copy(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取源文件路径和目标路径
    source = step['element']
    destination = step['data']['text']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 初始化返回码
    code = 0
    # 根据操作系统类型执行相应的复制命令
    if os.name == 'nt':
        code = os.system(f'COPY /Y {source} {destination}')
    if os.name == 'posix':
        code = os.system(f'cp -f -R {source} {destination}')

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回码不为0，抛出异常
    if code != 0:
        raise Exception(f'COPY {source} {destination} 失败，返回码: {code}')


def move(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取源文件路径和目标路径
    source = step['element']
    destination = step['data']['text']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 初始化返回码
    code = 0
    # 根据操作系统类型执行相应的移动命令
    if os.name == 'nt':
        code = os.system(f'MOVE /Y {source} {destination}')
    if os.name == 'posix':
        code = os.system(f'mv -f {source} {destination}')

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回码不为0，抛出异常
    if code != 0:
        raise Exception(f'MOVE {source} {destination} 失败，返回码: {code}')

def remove(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要删除的路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 初始化返回码
    code = 0
    # 根据操作系统类型执行相应的删除文件命令
    if os.name == 'nt':
        code = os.system(f'del /S /Q {path}')
    if os.name == 'posix':
        code = os.system(f'rm -f {path}')

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回码不为0，抛出异常
    if code != 0:
        raise Exception(f'REMOVE {path} 失败，返回码: {code}')


def rmdir(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要删除的路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 初始化返回码
    code = 0
    # 根据操作系统类型执行相应的删除目录命令
    if os.name == 'nt':
        code = os.system(f'rd /S /Q {path}')
    if os.name == 'posix':
        code = os.system(f'rm -rf {path}')

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回码不为0，抛出异常
    if code != 0:
        raise Exception(f'RMDIR {path} 失败，返回码: {code}')


def mkdir(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要创建的目录路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 初始化返回码
    code = 0
    # 根据操作系统类型执行相应的创建目录命令
    if os.name == 'nt':
        code = os.system(f'mkdir {path}')
    if os.name == 'posix':
        code = os.system(f'mkdir -p {path}')

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回码不为0，抛出异常
    if code != 0:
        raise Exception(f'MKDIR {path} 失败，返回码: {code}')

def exists(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要检查存在性的路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 检查路径是否存在
    result = os.path.exists(path)

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果路径不存在，抛出异常
    if not result:
        raise Exception(f'{path} 不存在')


def not_exists(step):
    try:
        # 尝试执行exists函数
        exists(step)
    except:
        # 如果抛出异常，表示路径不存在，不执行任何操作
        pass
    else:
        # 如果没有抛出异常，表示路径存在，抛出异常
        path = step['element']
        raise Exception(f'{path} 已存在')


def is_file(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要检查的文件路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 检查路径是否为文件
    result = os.path.isfile(path)

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果路径不是文件，抛出异常
    if not result:
        raise Exception(f'{path} 不是文件')


def not_file(step):
    try:
        # 尝试执行is_file函数
        is_file(step)
    except:
        # 如果抛出异常，表示路径不是文件，不执行任何操作
        pass
    else:
        # 如果没有抛出异常，表示路径是文件，抛出异常
        path = step['element']
        raise Exception(f'{path} 是一个文件')


def is_dir(step):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要检查的目录路径
    path = step['element']

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 检查路径是否为目录
    result = os.path.isdir(path)

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果路径不是目录，抛出异常
    if not result:
        raise Exception(f'{path} 不是目录')

def not_dir(step):
    try:
        # 尝试执行is_dir函数
        is_dir(step)
    except:
        # 如果抛出异常，表示路径不是目录，不执行任何操作
        pass
    else:
        # 如果没有抛出异常，表示路径是目录，抛出异常
        path = step['element']
        raise Exception(f'{path} 是一个目录')


def command(step, name=None):
    # 获取当前工作目录
    cwd = os.getcwd()
    # 获取要执行的命令
    cmd = step['element']

    # 如果指定了操作系统名称，并且当前操作系统不匹配，则记录日志并跳过执行命令
    if name and os.name != name:
        logger.info(f'COMMAND: 当前操作系统不是 {name}，"{cmd}" 被跳过')
        return

    # 如果指定了页面，则切换到该页面
    if step['page']:
        os.chdir(step['page'])

    # 执行命令并获取返回代码
    code = os.system(cmd)

    # 如果指定了页面，则恢复到原始工作目录
    if step['page']:
        os.chdir(cwd)

    # 如果返回代码不为0，表示命令执行失败，抛出异常
    if code != 0:
        raise Exception(f'COMMAND: "{cmd}" 执行失败，返回代码: {code}')


def shell(step):
    # 执行shell命令，仅适用于类Unix系统
    command(step, 'posix')


def cmd(step):
    # 执行cmd命令，仅适用于Windows系统
    command(step, 'nt')
