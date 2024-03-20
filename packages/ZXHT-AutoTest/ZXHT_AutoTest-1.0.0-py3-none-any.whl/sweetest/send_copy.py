# -*- coding: utf-8 -*-
"""
@Time : 2024/1/10 13:48
@Author : TJF

"""
import os
import time

from requests_toolbelt import MultipartEncoder
import json
import requests
import sweetest.report as report


# 飞书  上传文件到空间的文件夹，需要有自建应用
class SendFeishu:
    def __init__(self, code, plan_name, sheet_name, faicase, blocase, sc, fc, bc, tc):
        self.file_url = None
        self.file_name = None
        self.parent_node = None
        self.env = None
        self.apiorui = None
        self.pr_name = None
        self.code = code  # 用例执行状态码
        self.sheet_name = sheet_name  # 用例集
        self.faicase = faicase  # 失败的用例
        self.blocase = blocase  # 阻塞的用例
        self.sc = sc  # success case
        self.fc = fc  # false case
        self.bc = bc  # block case
        self.tc = tc  # total  case
        self.plan_name = plan_name  # 如： LanTu_api_test

    def report_title(self):
        # 飞书群发消息时，需要以下内容，目前只有岚图，后期可能会有其他项目，做个判断，
        if 'LanTu' in self.plan_name:
            self.pr_name = '岚图'
        else:
            self.pr_name = '名称格式报错'
        if 'api' in self.plan_name:
            self.apiorui = '接口'
        elif 'ui' in self.plan_name:
            self.apiorui = 'UI'
        else:
            self.apiorui = '类型格式报错'
        if 'test' in self.plan_name:
            self.env = '测试环境'
        elif 'pro' in self.plan_name:
            self.env = '生产环境'
        else:
            self.env = '环境格式报错'

    # 获取tenant_access_token
    def get_ten_acc_token(self):
        url_token = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        headers_token = {
            'Content-Type': 'application/json; charset=utf-8',
        }
        data_token = {
            'app_id': 'cli_a40d6db44c7c100d',
            'app_secret': 'Tyc7UJULt9MBBuzaJVtrBcJclwUcbko1'
        }
        response = requests.request('POST', url_token, headers=headers_token, json=data_token)
        self.ten_acc_token = json.loads(response.text)['tenant_access_token']
        # print('this is acc_token', self.ten_acc_token)

    # 上传文件到飞书空间的文件夹下
    def send_file(self):
        self.file_name = report.md_file_name
        file_path = os.path.abspath(report.md_file_path)
        file_size = os.path.getsize(file_path)
        self.parent_node = 'DKlUfFqNalkEzTd5EJpcGT75nQh'  # 文件夹token，抓包可以看到
        url_upload = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"

        payload = {'file_name': self.file_name,
                   'parent_type': 'explorer',
                   'parent_node': self.parent_node,
                   'size': file_size}
        files = [
            ('file', (self.file_name, open(file_path, 'rb'), 'application/json'))
        ]
        headers_upload = {
            'Authorization': f'Bearer {self.ten_acc_token}'
        }

        response = requests.request("POST", url_upload, headers=headers_upload, data=payload, files=files)

        # 获取上传到飞书文件夹的文件url
        file_url_feishu = (f'https://open.feishu.cn/open-apis/drive/v1/files?direction=DESC&folder_token='
                           f'{self.parent_node}&order_by=CreatedTime')
        headers_upload = {
            'Authorization': f'Bearer {self.ten_acc_token}'
        }

        response = requests.request("GET", file_url_feishu, headers=headers_upload, data=payload)
        all_info = json.loads(response.text)
        self.files = all_info['data']['files']
        for i in self.files:
            if self.file_name in i['name']:
                self.file_url = i['url']

    def delete_file(self):
        # 删除 创建时间>=30天 的文件

        # 获取文件夹下的清单
        # 删除的接口是按创建时间升序排序  查询url的接口是按创建时间降序排序
        file_url_feishu = (f'https://open.feishu.cn/open-apis/drive/v1/files?direction=ASC&folder_token='
                           f'{self.parent_node}&order_by=CreatedTime')
        headers_upload = {
            'Authorization': f'Bearer {self.ten_acc_token}'
        }

        response = requests.request("GET", file_url_feishu, headers=headers_upload)
        all_info = json.loads(response.text)
        files = all_info['data']['files']

        current_timestamp = int(time.time())  # 当前时间戳 10位
        threshold_days = 30  # 超过30天
        file_token_list = []  # 文件token列表
        for file in files:
            if (current_timestamp - int(file['created_time'])) > (threshold_days * 24 * 60 * 60):
                file_token_list.append(file['token'])

        for file_token in file_token_list:
            url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}?type=file"  # 删除文件/文件夹
            payload = ''
            headers_del = {
                'Authorization': f'Bearer {self.ten_acc_token}'
            }
            response = requests.request("DELETE", url, headers=headers_del, data=payload)
        return all_info['data']['has_more']

    def has_more(self):
        # 当飞书文件夹下的has_more：True时，执行：查询文件夹下清单-->删除超过30天的文件
        # 当飞书文件夹下的has_more：False时，不执行
        while True:
            has_more = self.delete_file()
            if not has_more:
                break

        pass

    def sendmessage_feishu(self):
        # 发送卡片类型的消息到飞书群聊中的机器人

        # sheet_name 有多个时，发送到飞书群由 ['data1'、'data2'、'data3']  变成  data1、data2、data3
        if type(self.sheet_name) is list:
            self.sheet_name = '、'.join(self.sheet_name)
        if type(self.faicase) is list:
            self.faicase = '、'.join(self.faicase)
        if type(self.blocase) is list:
            self.blocase = '、'.join(self.blocase)

        headers = {'content-type': "application/json"}
        # url = "https://open.feishu.cn/open-apis/bot/v2/hook/3c1da9e7-aaca-45f4-92da-2a9ff06db8e9" #自动化用例执行结果
        # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/0720c99f-d3d3-4c69-9b98-63c7887d7030'  #飞书-岚图汽车-灵活数采
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/e25eba9a-76fa-412b-a476-06c46293b765'  # 飞书助手

        if self.code == 0 and self.bc == 0:
            result = "测试通过"
            content = {
                "msg_type": "interactive",
                "card": {
                    "elements": [{
                        "tag": "div",
                        "text": {
                            "content": f'功能模块：{self.sheet_name}\n成功总数：  {self.sc}\t条\n失败总数：  {self.fc}\t条\n'
                                       f'用例名称：  {self.faicase}\n阻塞总数：  {self.bc}\t条\n用例名称：  {self.blocase}\n'
                                       f'用例总数：  {self.tc}\t条\n\n测试结果：<font color="green"> **{result}** </font> ',
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
                                "url": self.file_url,
                                "type": "default",
                                "value": {}
                            }
                        ],
                        "tag": "action"
                    }],
                    "header": {
                        "title": {
                            "content": f'{self.pr_name}_{self.apiorui}_{self.env}',
                            "tag": "plain_text"
                        }
                    }
                }
            }
            requests.post(url=url, data=json.dumps(content), headers=headers)
        elif self.code == 0 and self.bc != 0:
            content = {
                "msg_type": "interactive",
                "card": {
                    "elements": [{
                        "tag": "div",
                        "text": {
                            "content": f'功能模块：{self.sheet_name}\n成功总数：  {self.sc}\t条\n失败总数：  {self.fc}\t条\n'
                                       f'用例名称：  {self.faicase}\n阻塞总数：  {self.bc}\t条\n用例名称：  {self.blocase}\n'
                                       f'用例总数：  {self.tc}\t条\n\n测试结果：<font color="grey"> **有用例阻塞，请注意** </font> ',
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
                                "url": self.file_url,
                                "type": "default",
                                "value": {}
                            }],
                        "tag": "action"
                    }],
                    "header": {
                        "title": {
                            "content": f'{self.pr_name}_{self.apiorui}_{self.env}',
                            "tag": "plain_text"
                        }
                    }
                }
            }
            requests.post(url=url, data=json.dumps(content), headers=headers)
        else:
            content = {
                "msg_type": "interactive",
                "card": {
                    "elements": [{
                        "tag": "div",
                        "text": {
                            "content": f'功能模块：{self.sheet_name}\n成功总数：  {self.sc}\t条\n失败总数：  {self.fc}\t条\n'
                                       f'用例名称：  {self.faicase}\n阻塞总数：  {self.bc}\t条\n用例名称：  {self.blocase}\n'
                                       f'用例总数：  {self.tc}\t条\n\n测试结果：<font color="red"> **测试失败** </font> ',
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
                                "url": self.file_url,
                                "type": "default",
                                "value": {}
                            }
                        ],
                        "tag": "action"
                    }],
                    "header": {
                        "title": {
                            "content": f'{self.pr_name}_{self.apiorui}_{self.env}',
                            "tag": "plain_text"
                        }
                    }
                }
            }
            requests.post(url=url, data=json.dumps(content), headers=headers)

    def run(self):
        self.report_title()
        self.get_ten_acc_token()
        self.send_file()
        self.sendmessage_feishu()


class SendQiwei:
    def __init__(self):
        pass

    def sendmessage(code, name, sheet_name):
        headers = {'content-type': "application/json"}
        url = "https://open.feishu.cn/open-apis/bot/v2/hook/3c1da9e7-aaca-45f4-92da-2a9ff06db8e9"  # 自动化用例执行结果
        # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/204c7253-0602-4177-aa28-28d50ae476bf'  # 飞书助手

        if code == 0:
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

    '''
    企微机器人模版
        if code == 1:
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


class send_dingding:
    def __init__(self):
        pass


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
