#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Mail: haha@haha.com
# @File: mini_toolbox/pip_list.py
# @Date: 2024-03-19 15:01:33
# @Desc: 用于显示pip库安装日期

__all__ = ['gen_pip_list']

import os
import sys
import time
from typing import List, Tuple

import pkg_resources


def gen_pip_list() -> Tuple[List[str], List[int]]:
    """ 用于查找并返回pip库信息，包含：库名/版本/安装时间
    
    Returns:
        Tuple[List[str], List[int]]: data(List[str])为所有pip库的信息, 结构为\
        ``[库名, 版本, 安装时间]``, size(List[int])为各字段所有值的最大长度，用于后续格式化输出
    """

    data = [['Package', 'Version', 'InstallTime']]
    size = [len(x) for x in data[0]]

    time_format = '%Y-%m-%d %H:%M:%S'
    for package in pkg_resources.working_set:
        pkg_dir, pkg_name, pkg_ver = package.location, package.key, package.version

        # 计算时间
        pkg_path = os.path.join(pkg_dir, package.egg_name().split(pkg_ver)[0] + pkg_ver)
        if os.path.exists(pkg_path + '.egg-info'):
            pkg_path = pkg_path + '.egg-info'
        elif os.path.exists(pkg_path + '.dist-info'):
            pkg_path = pkg_path + '.dist-info'
        else:
            pkg_path = pkg_dir
        pkg_ctime = time.strftime(time_format, time.localtime(os.path.getctime(pkg_path)))

        # 插入数据
        tmp_data = [pkg_name, pkg_ver, pkg_ctime]  # 与header对应
        for num in range(len(tmp_data)):
            if size[num] < len(tmp_data[num]):
                size[num] = len(tmp_data[num])
        data.append(tmp_data)

    # 插入行首与数据之间的分隔符
    data.insert(1, list(map(lambda x: '-' * x, size)))

    return data, size


def main():
    """ 用于命令行直接调用输出, 格式化显示pip库安装日期, ``-n`` 按名称排序, ``-t`` 按日期排序 """

    data, size = gen_pip_list()

    # 数据排序
    if '-n' in sys.argv:
        pkgs_data = sorted(data[2:], key=lambda x: x[0])
    elif '-t' in sys.argv:
        pkgs_data = sorted(data[2:], key=lambda x: x[2])
    else:
        pkgs_data = data[2:]

    for item in data[:2] + pkgs_data:
        print("%-*s %-*s %-*s" % (size[0], item[0], size[1], item[1], size[2], item[2]))

    sys.exit(0)


def _test():
    main()


if __name__ == '__main__':
    _test()
