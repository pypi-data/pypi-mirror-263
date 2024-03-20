# -*- coding: utf-8 -*-
"""
@Time : 2024/1/10 13:48
@Author : TJF

"""
import os
from datetime import datetime
from pathlib import Path
from requests_toolbelt import MultipartEncoder
import json
import requests
import sweetest.report as report
result = ""

def sendMessage(status, name, sheet_name):
    headers = {'content-type': "application/json"}
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/3c1da9e7-aaca-45f4-92da-2a9ff06db8e9"       # 自动化用例执行结果
    # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/204c7253-0602-4177-aa28-28d50ae476bf'  # 飞书助手

    if status == 0:
        result = '测试通过'
        content = {
            "msg_type": "text",
            "content": {
                "text": f"项目名称： {name}\n功能：{sheet_name}\n测试结果：{result}"
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)
    else:
        result = '测试未通过'
        content = {
            "msg_type": "text",
            "content": {
                "text": f"项目名称： {name}\n功能：{sheet_name}\n测试结果：{result}"
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)


# 飞书  上传文件到空间的文件夹，需要有自建应用
def uploadFile_feishu():
    #获取tenant_access_token
    url_token = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
    headers_token = {
        'Content-Type': 'application/json; charset=utf-8',
    }
    data_token = {
        'app_id': 'cli_a40d6db44c7c100d',
        'app_secret': 'Tyc7UJULt9MBBuzaJVtrBcJclwUcbko1'
    }
    response = requests.request('POST', url_token, headers=headers_token, json=data_token)
    ten_acc_token = json.loads(response.text)['tenant_access_token']
    # print('this is acc_token', ten_acc_token)


    #上传文件到飞书空间的文件夹下
    file_name = report.md_file_name
    file_path = os.path.abspath(report.md_file_path)
    file_size = os.path.getsize(file_path)
    parent_node = 'DKlUfFqNalkEzTd5EJpcGT75nQh'     #文件夹token，抓包可以看到
    url_upload = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"

    payload = {'file_name': file_name,
               'parent_type': 'explorer',
               'parent_node': parent_node,
               'size': file_size}
    files = [
        ('file', (file_name, open(file_path, 'rb'), 'application/json'))
    ]
    headers_upload = {
        'Authorization': f'Bearer {ten_acc_token}'
    }

    response = requests.request("POST", url_upload, headers=headers_upload, data=payload, files=files)
    payload = ''
    print(response.text)

    # 获取上传到飞书文件夹的文件url
    file_url_feishu = f'https://open.feishu.cn/open-apis/drive/v1/files?direction=DESC&folder_token={parent_node}&order_by=EditedTime'
    response = requests.request("GET", file_url_feishu, headers=headers_upload, data=payload)
    all_info = json.loads(response.text)
    files = all_info['data']['files']
    for i in files:
        if file_name in i['name']:
            file_url = i['url']
            return file_url


# 发送卡片类型的消息到飞书群聊中的机器人
def sendMessage_feishu(status, name, sheet_name, faicase, blocase, sc, fc, bc, tc):
    global file_url
    if 'LanTu' in name:
        pr_name = '岚图'
    else:
        pr_name = '名称格式报错'
    if 'api' in name:
        apiorui = '接口'
    elif 'ui' in name:
        apiorui = 'UI'
    else:
        apiorui = '类型格式报错'
    if 'test' in name:
        env = '测试环境'
    elif 'pro' in name:
        env = '生产环境'
    else:
        env = '环境格式报错'

    if type(sheet_name) is list:
        sheet_name = '、'.join(sheet_name)
    if type(faicase) is list:
        faicase = '、'.join(faicase)
    if type(blocase) is list:
        blocase = '、'.join(blocase)

    # print('this is type', faicase, type(faicase))

    headers = {'content-type': "application/json"}
    # url = "https://open.feishu.cn/open-apis/bot/v2/hook/3c1da9e7-aaca-45f4-92da-2a9ff06db8e9" #自动化用例执行结果
    # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/0720c99f-d3d3-4c69-9b98-63c7887d7030'  #飞书-岚图汽车-灵活数采
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/e25eba9a-76fa-412b-a476-06c46293b765'  # 飞书助手

    if status == 0 and bc == 0:
        result = "测试通过"
        content = {
            "msg_type": "interactive",
            "card": {
                "elements": [{
                    "tag": "div",
                    "text": {
                        "content": f'功能模块：{sheet_name}\n成功总数：  {sc}\t条\n失败总数：  {fc}\t条\n用例名称：  {faicase}\n阻塞总数：  {bc}\t条\n用例名称：  {blocase}\n用例总数：  {tc}\t条\n\n测试结果：<font color="green"> **{result}** </font> ',
                        "tag": "lark_md"
                    }
                }, {
                    "actions": [{
                        "tag": "button",
                        "text": {
                            "content": "岚图汽车-灵活数采",
                            "tag": "lark_md"
                        },
                        "url": "http://10.223.105.131:8099/app/acquisitionManagement",
                        "type": "default",
                        "value": {}
                    },
                        {
                            "tag": "button",
                            "text": {
                                "content": "自动化测试报告地址",
                                "tag": "lark_md"
                            },
                            "url": uploadFile_feishu(),
                            "type": "default",
                            "value": {}
                        }
                    ],
                    "tag": "action"
                }],
                "header": {
                    "title": {
                        "content": f'{pr_name}_{apiorui}_{env}',
                        "tag": "plain_text"
                    }
                }
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)
    elif status == 0 and bc != 0:
        content = {
            "msg_type": "interactive",
            "card": {
                "elements": [{
                    "tag": "div",
                    "text": {
                        "content": f'功能模块：{sheet_name}\n成功总数：  {sc}\t条\n失败总数：  {fc}\t条\n用例名称：  {faicase}\n阻塞总数：  {bc}\t条\n用例名称：  {blocase}\n用例总数：  {tc}\t条\n\n测试结果：<font color="grey"> **有用例阻塞，请注意** </font> ',
                        "tag": "lark_md"
                    }
                }, {
                    "actions": [{
                        "tag": "button",
                        "text": {
                            "content": "岚图汽车-灵活数采",
                            "tag": "lark_md"
                        },
                        "url": "http://10.223.105.131:8099/app/acquisitionManagement",
                        "type": "default",
                        "value": {}
                    },
                        {
                            "tag": "button",
                            "text": {
                                "content": "自动化测试报告地址",
                                "tag": "lark_md"
                            },
                            "url": uploadFile_feishu(),
                            "type": "default",
                            "value": {}
                        }],
                    "tag": "action"
                }],
                "header": {
                    "title": {
                        "content": f'{pr_name}_{apiorui}_{env}',
                        "tag": "plain_text"
                    }
                }
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)
    else:
        result = "测试未通过"
        content = {
            "msg_type": "interactive",
            "card": {
                "elements": [{
                    "tag": "div",
                    "text": {
                        "content": f'功能模块：{sheet_name}\n成功总数：  {sc}\t条\n失败总数：  {fc}\t条\n用例名称：  {faicase}\n阻塞总数：  {bc}\t条\n用例名称：  {blocase}\n用例总数：  {tc}\t条\n\n测试结果：<font color="red"> **测试失败** </font> ',
                        "tag": "lark_md"
                    }
                }, {
                    "actions": [{
                        "tag": "button",
                        "text": {
                            "content": "岚图汽车-灵活数采",
                            "tag": "lark_md"
                        },
                        "url": "http://10.223.105.131:8099/app/acquisitionManagement",
                        "type": "default",
                        "value": {}
                    },
                        {
                            "tag": "button",
                            "text": {
                                "content": "自动化测试报告地址",
                                "tag": "lark_md"
                            },
                            "url": uploadFile_feishu(),
                            "type": "default",
                            "value": {}
                        }
                    ],
                    "tag": "action"
                }],
                "header": {
                    "title": {
                        "content": f'{pr_name}_{apiorui}_{env}',
                        "tag": "plain_text"
                    }
                }
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)


'''
企微机器人模版
    if status == 1:
        result = "测试通过"
        content = {
            "msgtype": "markdown",
            "markdown": {
                "content": "<font color=\"green\">%s</font>"%("自动化测试用例：" + name + "\n" + "功能：" + ("'" + "','".join(sheet_name) + "'") + "\n测试结果：" + result)
                # "mentioned_mobile_list": ["18939881330", "17320087073"]
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)
        print(r.text + "test")
    else:
        result = "测试失败"
        content = {
            "msgtype": "markdown",
            "markdown": {
                "content":"<font color=\"red\">%s</font><>"%( "自动化测试用例：" + name + "\n" + "功能：" + ("'" + "','".join(sheet_name) + "'") + "\n测试结果：" + result),
                # "mentioned_mobile_list": ["18939881330","17320087073"]
            }
        }
        r = requests.post(url=url, data=json.dumps(content), headers=headers)
        print(r.text+"test")
        '''


def sendFile(file_id):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/3c1da9e7-aaca-45f4-92da-2a9ff06db8e9"
    # url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6c6335c9-2408-4f3b-9333-bcbaff4f656c"

    headers = {'content-type': "application/json"}
    content = {
        "msgtype": "file",
        "file": {
            "media_id": file_id
        }
    }
    s = requests.post(url=url, data=json.dumps(content), headers=headers)




# 企微
def uploadFile(filepath, filename, access_token):
    post_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={access_token}&type=file"
    # post_file_url =f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=6c6335c9-2408-4f3b-9333-bcbaff4f656c&type=file"

    # m = MultipartEncoder(fields:{filename: ('file', open(filepath + Autotest., 'rb'), 'text/plain')})

    m = MultipartEncoder(
        fields={filename: (filename, open(filepath, 'rb'))},
    )
    print(m)
    r = requests.post(url=post_file_url, data=m, headers={
        'Content-Type': "multipart/form-data"})
    print(r.text)
    return r.json()['media_id']


def sendRequest(serverUrl, result, uuId):
    headers = {'Content-Type': "application/json"}
    content = {
        "uuId": uuId,
        "result": result
    }
    print("更新平台状态成功")
    print(requests.post(serverUrl, json.dumps(content), headers=headers).text)


'''
@allure.feature()
class Test_Qtest():
    @allure.severity("normal")
    @allure.story("xxx测试用例")
    @allure.description("自动化测试")
    @pytest.mark.parametrize('sheet_name',getInfo())
    def test_runTest(self,testcase, sheet_name, messageKey, uuId, mobile,autotest_data):
        with allure.step("1.执行用例；2.断言结果"):
            program = Autotest(testcase, sheet_name,autotest_data,
                               {'platformName': 'Desktop', 'browserName': 'Chrome', 'snapshot': False, 'headless': True,
                                'mobile': mobile}, '')
            # program.fliter(id='LOGIN')
            program.plan()
            print(program.code)
        with allure.step("自动化测试截图"):
            snapshot_folder = snapshot_plan / g.start_time[1:]
            for filename in os.listdir(snapshot_folder):
                if filename.startswith(sheet_name):
                    with open(Path(snapshot_folder) / filename, mode='rb') as f:
                        file = f.read()
                    allure.attach(file, filename, allure.attachment_type.PNG)
                with open(Path(snapshot_folder) / 'sweet.log', mode='rb') as f:
                    word = f.read()
                    word_d = word.decode()
                    # error=re.search('ERROR',line)
                    str = 'ERROR'
                    assert str not in word_d

        if messageKey == "":
            if (program.code) == 0:
                send_test.sendRequest(serverUrl, "测试通过", uuId)
            else:
                send_test.sendRequest(serverUrl, "测试未通过", uuId)

        else:
            if (program.code) == 0:
                # media_id = send.uploadFile(program.report_excel, program.report_filename, messageKey)  # 获取临时文件的media_id
                send_test.sendMessage(messageKey, 1, testcase, sheet_name)  # 推送信息至企业微信
                # send.sendFile(messageKey, media_id)  # 推送文件至企业微信
                send_test.sendRequest(serverUrl, "测试通过", uuId)
            else:
                # media_id = send.uploadFile(program.report_excel, program.report_filename, messageKey)  # 获取临时文件的media_id
                send_test.sendMessage(messageKey, 0, testcase, sheet_name)  # 推送信息至企业微信
     pytest.main(['222test_index.py', '-s', '--alluredir', 'C:\\Autotest\\autotest\\Allure-reports\\temp'])
    os.system(r'allure generate C:\\Autotest\\autotest\Allure-reports\\temp -o  C:\Autotest\\autotest\Allure-reports\\report --clean')
    '''
