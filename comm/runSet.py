import os
import unittest
import readConfig as readConfig
from comm.Log import MyLog as Log
from comm.webDriver import MyDriver as Driver

log = Log.get_log()
logger = log.get_logger()
driver = Driver.get_browser()
filePath = ''


def set_case_list():
    """
    read case name from 'caseList.txt'
    读取 'caseList.txt'文件
    :return:
    """
    caseList = []
    caseListPath = os.path.join(readConfig.proDir, "caseList.txt")
    fb = open(caseListPath,'r', encoding='UTF-8')
    for case in fb.readlines():
        data = str(case)
        if data != "" and not data.startswith("#"):
            caseList.append(data.replace("\n", ""))
            print(caseList)
    fb.close()
    return caseList


def set_suite():
    """
    set test suite
    :return:
    """
    global filePath
    suite_list = unittest.TestSuite()
    suite_module = []

    case_list = set_case_list()

    for case in case_list:
        name = str(case).split("/")[-1]
        webname = str(case).split("/")[0]
        sitename = str(case).split("/")[1]

        filePath = os.path.join(readConfig.proDir, "case", webname, sitename, "testCase")
        # filePath = os.path.join(readConfig.proDir, "testCase")
        print("case path:" + filePath)

        discover = unittest.defaultTestLoader.discover(filePath, pattern=name+'.py', top_level_dir=None)
        suite_module.append(discover)

    if len(suite_module) > 0:
        for case in suite_module:
            for name in case:
                suite_list.addTest(name)
    else:
        return None

    return suite_list


def set_website():
    """
    Set website by name
    调用方法set_case_list()，并判断从配置文件config.ini获取的参数（url地址）
    :return:
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            web = data.split("/")[0]
            site = data.split("/")[1]
            name = web.upper()
            print(web)
            print(name)
            print(site)
            break
    driver.open_browser(name, site)


def close_browser():
    """
    quite browser
    :return:
    """
    driver.close_browser()


def get_web():
    """
    get web
    :return: web
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            web = data.split("/")[0]
            print("web:",web)
            break
    return web


def get_site():
    """
    get site
    :return:site
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            site = data.split("/")[1]
            break
    return site
