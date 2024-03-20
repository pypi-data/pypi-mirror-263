import multiprocessing

import send
from autotest import Autotest

code_counts = multiprocessing.Manager().dict()
plan_name = 'LanTu_ui_1'
sheet_names = ['data1', 'data2', 'data3', 'data4']
# sheet_names = ['data1']


def run(sheet_name):

    desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'headless': True}
    server_url = ''
    sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)
    sweet.plan()
    send.sendMessage(sweet.code, plan_name, sheet_name)
    if sweet.code == 0:
        with code_counts.get_lock():
            code_counts[sweet.code] = code_counts.get(sweet.code,0)+1
    elif sweet.code == 1:
        with code_counts.get_lock():
            code_counts[sweet.code] = code_counts.get(sweet.code, 1) + 1
    else:
        print('未知的code:',sweet.code)
    if sweet.code:
        with code_counts.get_lock():
            code_counts[sweet.code] = code_counts.get(sweet.code, 2) + 1


    # send.sendFile_fs(os.path.basename(sweet.report_excel))


data = {
    "oid": "58d45cdf-ab05-4a77-99f0-fbb1dcff7ba1",
    "code": 200,
    "data": {
        "value": {
            "_id": "65547471328db62ad50e1f7e",
            "team": "6004f4c73dcc2495ce57e594",
            "version_id": "65547471328db62ad50e1f8b",
            "version_identifier": 1,
            "principal_id": "65547471328db62ad50e1f7e",
            "is_latest_version": 1,
            "title": "状态监控",
            "important_level": '',
            "maintenance_uid": "f49b9d78c6524230921378885a666f4d",
            "test_library_id": "64c86fb7771a90595a744c61",
            "type": "5f0c152f3342df1eff78bdb9",
            "test_type": 1,
            "estimated_workload": '',
            "suite_id": "65547376328db62ad50e1e5c",
            "precondition": "<p style=\"text-align: left;\">部署状态页有数据时查看按钮变成可点击，无数据时查看时按钮置灰不可点击</p>",
            "participants": [
                {
                    "id": "f49b9d78c6524230921378885a666f4d",
                    "type": 1,
                    "subscription": 40
                }
            ],
            "steps": [
                {
                    "description": "部署状态：下发成功",
                    "expected_value": "1、对应的状态描述：下发EMQ成功算法;\n（说明：下发EMQ成功）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "step_id": "65547471328db62ad50e1f7f"
                },
                {
                    "step_id": "65547471328db62ad50e1f80",
                    "is_group": 0,
                    "description": "部署状态：下发失败",
                    "expected_value": "1、对应的状态描述：\n1：发布mqtt失败\n2：客户机未连接\n3：转码异常\n（说明：算法下发EMQ失败  ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f81",
                    "is_group": 0,
                    "description": "部署状态：运行成功",
                    "expected_value": "1、对应的状态描述：运行成功；\n（说明：收到上传数据/收到运行成功消息  ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f82",
                    "is_group": 0,
                    "description": "部署状态：运行失败",
                    "expected_value": "1、对应的状态描述：运行失败；\n（说明：收到运行失败消息  ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f83",
                    "is_group": 0,
                    "description": "部署状态：停止成功",
                    "expected_value": "1、对应的状态描述：停止成功；\n（说明：收到停止成功消息  ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f84",
                    "is_group": 0,
                    "description": "部署状态：停止失败",
                    "expected_value": "1、对应的状态描述：停止失败；\n（说明：收到停止失败消息 ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f85",
                    "is_group": 0,
                    "description": "部署状态：停止中",
                    "expected_value": "1、对应的状态描述：停止中；\n（说明：停止算法下发EMQ成功 ）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f86",
                    "is_group": 0,
                    "description": "部署状态：停止下发失败",
                    "expected_value": "1、对应的状态描述：\n1：发布mqtt失败\n2：客户机未连接\n3：转码异常\n（说明：停止算法下发EMQ失败 ）；\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f87",
                    "is_group": 0,
                    "description": "部署状态：已部署",
                    "expected_value": "1、对应的状态描述：审批通过；\n（说明：下发了，审批通过(主页、审批页有)）\n2、可执行的单车操作：重试、停止、查看；\n3、可执行的多车操作：重试、停止",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f88",
                    "is_group": 0,
                    "description": "部署状态：待审批",
                    "expected_value": "1、对应的状态描述：等待审批；\n（说明：创建了，还未审批(主页、审批页有)）\n 车辆部署页面 禁止重试、停止操作",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f89",
                    "is_group": 0,
                    "description": "部署状态：已驳回",
                    "expected_value": "1、对应的状态描述：驳回；\n（说明：下发被驳回(主页、审批页有)）\n车辆部署页面 禁止重试、停止操作",
                    "group_id": ''
                },
                {
                    "step_id": "65547471328db62ad50e1f8a",
                    "is_group": 0,
                    "description": "部署状态：未部署（事件列表页面展示）",
                    "expected_value": "1、对应的状态描述：保存未部署；\n（说明：只保存未点部署）",
                    "group_id": ''
                }
            ],
            "description": "",
            "identifier": 328,
            "state_id": "64f182bf7cd193fa0f05bc07",
            "state_type": 1,
            "properties": {
                "workload_ss_armh": 0,
                "workload_ss_emh": 0,
                "workload_ss_ermh": 0,
                "workload_ss_pbr": 0
            },
            "position": 21495808,
            "suite_position": 131072,
            "assignee": "f49b9d78c6524230921378885a666f4d",
            "assignor": "f49b9d78c6524230921378885a666f4d",
            "assign_at": 1700033649,
            "created_at": 1700033649,
            "created_by": "f49b9d78c6524230921378885a666f4d",
            "updated_at": 1700033649,
            "updated_by": "f49b9d78c6524230921378885a666f4d",
            "is_deleted": 0,
            "is_archived": 0,
            "back_log_ids": [],
            "relation_page_count": 0,
            "relation_idea_count": 0,
            "comment_count": 0,
            "attachments": [],
            "attachment_count": 0,
            "link_count": 0,
            "comments": [
                ''
            ],
            "backup_review_state_id": "5ec4b4b8f6a585911b267868",
            "backup_review_state_type": 1,
            "review_result_state": 1,
            "suite_ids": [
                "64c870ce079e90f05ba0cd8a",
                "65545e1e91d3e4aa71c46d1b",
                "655463e2328db62ad50e0617",
                "65547376328db62ad50e1e5c"
            ],
            "is_link": 0,
            "whole_identifier": "JL-328",
            "latest_test_run": '',
            "global_permissions": "00",
            "permissions": "1111111110111111111111100000000111111111111000",
            "latest_version": {
                "_id": "65547471328db62ad50e1f8b",
                "name": "v1",
                "description": "初始化创建",
                "identifier": 1
            },
            "version_name": "v1",
            "version_description": "初始化创建",
            "principal_version": "v1",
            "principal_version_count": 1,
            "version_count": 1,
            "definition_id": "6004f4c75f4983170492bc7a",
            "test_run_history_count": 0,
            "review_history_count": 0,
            "relation_counts": {
                "work_item_backlog_group": 0,
                "work_item_defect_group": 0,
                "idea": 0,
                "page": 0
            },
            "in_snapshot_count": 0
        },
        "references": {
            "library": {
                "_id": "64c86fb7771a90595a744c61",
                "name": "吉利GEEA3.0架构项目",
                "description": "",
                "color": "#56ABFB",
                "identifier": "JL",
                "is_sample": 0,
                "name_pinyin": "jlGEEA30jgxm,jiliGEEA30jiagouxiangmu",
                "user_group_ids": [],
                "scope_type": 1,
                "visibility": 2,
                "members": [
                    {
                        "uid": "61235fc18bb9417da97c99992ee4a415",
                        "role_ids": [
                            "100000000000000000000001"
                        ]
                    },
                    {
                        "uid": "c17104589df44e5fb756d4bc0ce2eaf6",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 1
                    },
                    {
                        "uid": "0645fb23917c4eeeb7feb05b7beb8072",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 2
                    },
                    {
                        "uid": "865756ad18f14a3a8726f762d1c6b597",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 3
                    },
                    {
                        "uid": "dcdac3bfa1ad44a89ccbce73a7293cc6",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 4
                    },
                    {
                        "uid": "10e618bc58aa47478e1c6f787f5f7ec9",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 5
                    },
                    {
                        "uid": "8dfd40119fd047c8a7f7259c5ce6e81f",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 6
                    },
                    {
                        "uid": "fed44bcc61694972b1587151aecd5d66",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 7
                    },
                    {
                        "uid": "7568138b410a493aaa1b08cb69ab0ab0",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 8
                    },
                    {
                        "uid": "bdd833edcf4b4f12b10767f23b6195e8",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 9
                    },
                    {
                        "uid": "a2e1aded7836470c8d22b905c36e3081",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 10
                    },
                    {
                        "uid": "564432114b5d4bdab2ac06a95594cd65",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 11
                    },
                    {
                        "uid": "26b691e5b08c46698ef744e1fbe245c5",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 12
                    },
                    {
                        "uid": "f12cd2fbea794ec2a12c98f35430d4ca",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 13
                    },
                    {
                        "uid": "5b021bdac3354af9a78f71e31f4243c3",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 14
                    },
                    {
                        "uid": "3c90e45d747f443bbb805fce9afce876",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 15
                    },
                    {
                        "uid": "e8feebe53140456c9f4492a991f474fb",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 16
                    },
                    {
                        "uid": "aa1cbde6e258491181f3407807800a95",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 17
                    },
                    {
                        "uid": "f49b9d78c6524230921378885a666f4d",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 18
                    },
                    {
                        "uid": "a3f015c4b9dc4a0ab378e40306dcc039",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 19
                    },
                    {
                        "uid": "93e8e341f1cc40f5824626cf05517783",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 20
                    },
                    {
                        "uid": "7a6866e56d91457ebfbaab893686e99d",
                        "role_ids": [
                            "100000000000000000000002"
                        ],
                        "position": 21
                    }
                ],
                "created_at": 1690857399,
                "created_by": "61235fc18bb9417da97c99992ee4a415",
                "updated_at": 1708925744,
                "updated_by": "61235fc18bb9417da97c99992ee4a415",
                "is_deleted": 0,
                "is_archived": 0,
                "team": "6004f4c73dcc2495ce57e594",
                "type": 1,
                "members_be_user_group": []
            },
            "members": [
                {
                    "_id": "6237f2cc1964f81615117e70",
                    "uid": "f49b9d78c6524230921378885a666f4d",
                    "display_name": "吴皖靖",
                    "email": "",
                    "mobile": "15800795212",
                    "avatar": "default.png",
                    "name": "15800795212"
                }
            ],
            "suites": [
                {
                    "_id": "64c870ce079e90f05ba0cd8a",
                    "name": "vcloud",
                    "parent_id": '',
                    "emoji_icon": ''
                },
                {
                    "_id": "65545e1e91d3e4aa71c46d1b",
                    "name": "事件采集模块",
                    "parent_id": "64c870ce079e90f05ba0cd8a",
                    "emoji_icon": ''
                },
                {
                    "_id": "65547376328db62ad50e1e5c",
                    "name": "状态监控",
                    "parent_id": "655463e2328db62ad50e0617",
                    "emoji_icon": ''
                },
                {
                    "_id": "655463e2328db62ad50e0617",
                    "name": "部署状态页面-二级页面",
                    "parent_id": "65545e1e91d3e4aa71c46d1b",
                    "emoji_icon": ''
                }
            ],
            "states": [
                {
                    "_id": "64f182bf7cd193fa0f05bc07",
                    "type": 1,
                    "name": "设计",
                    "color": "#6698ff",
                    "selectable": 1,
                    "is_disable": 0
                },
                {
                    "_id": "64f182ee7cd193fa0f05bc09",
                    "type": 3,
                    "name": "就绪",
                    "color": "#73D897",
                    "selectable": 1,
                    "is_disable": 0
                },
                {
                    "_id": "64f183647cd193fa0f05bc0a",
                    "type": 4,
                    "name": "废弃",
                    "color": "#aaaaaa",
                    "selectable": 1,
                    "is_disable": 0
                }
            ],
            "types": [
                {
                    "_id": "5f0c152f3342df1eff78bdb9",
                    "text": "功能测试"
                },
                {
                    "_id": "5f0c15353342df1eff78bdba",
                    "text": "性能测试"
                },
                {
                    "_id": "5f0c153d3342df1eff78bdbb",
                    "text": "配置相关"
                },
                {
                    "_id": "5f0c15433342df1eff78bdbc",
                    "text": "安装部署"
                },
                {
                    "_id": "5f0c15493342df1eff78bdbd",
                    "text": "接口测试"
                },
                {
                    "_id": "5f0c15de3342df1eff78bdbe",
                    "text": "安全相关"
                },
                {
                    "_id": "5f0c16203342df1eff78bdbf",
                    "text": "兼容性测试"
                },
                {
                    "_id": "5f0c162c3342df1eff78bdc0",
                    "text": "UI测试"
                },
                {
                    "_id": "5f0c16333342df1eff78bdc1",
                    "text": "其他"
                }
            ],
            "properties": [
                {
                    "_id": "5f0c16653342df1eff78bdc2",
                    "name": "前置条件",
                    "key": "precondition",
                    "raw_key": "precondition",
                    "type": 2,
                    "property_key": "precondition",
                    "value_path": "precondition",
                    "from": 1,
                    "layout": 1,
                    "export_required": 0,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0
                    },
                    "icon": "multiline-text"
                },
                {
                    "_id": "5f0c172c3342df1eff78bdc4",
                    "name": "用例步骤",
                    "key": "steps",
                    "raw_key": "steps",
                    "type": 23,
                    "property_key": "steps",
                    "value_path": "steps",
                    "from": 1,
                    "layout": 1,
                    "export_required": 1,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0
                    },
                    "icon": "list-ordered"
                },
                {
                    "_id": "5f0c16ed3342df1eff78bdc3",
                    "name": "备注",
                    "key": "description",
                    "raw_key": "description",
                    "type": 2,
                    "property_key": "description",
                    "value_path": "description",
                    "from": 1,
                    "layout": 1,
                    "export_required": 0,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0
                    },
                    "icon": "multiline-text"
                },
                {
                    "_id": "62ff3b9d38663cd5a863eed3",
                    "name": "测试类型",
                    "key": "test_type",
                    "raw_key": "test_type",
                    "type": 6,
                    "property_key": "test_type",
                    "options": [
                        {
                            "_id": 1,
                            "text": "手动",
                            "bg_color": "#6698ff"
                        },
                        {
                            "_id": 2,
                            "text": "自动",
                            "bg_color": "#73D897"
                        }
                    ],
                    "value_path": "test_type",
                    "from": 1,
                    "option_style": 3,
                    "layout": 2,
                    "export_required": 0,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0,
                        "config_validator_required": 0,
                        "config_placeholder": 0,
                        "config_default_value": 0
                    },
                    "icon": "check-circle"
                },
                {
                    "_id": "63e074633a9ea5e44d2515c6",
                    "name": "维护人",
                    "key": "maintenance_uid",
                    "raw_key": "maintenance_uid",
                    "type": 9,
                    "property_key": "maintenance_uid",
                    "value_path": "maintenance_uid",
                    "from": 1,
                    "layout": 3,
                    "export_required": 0,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0,
                        "config_validator_required": 0,
                        "config_placeholder": 0,
                        "config_default_value": 0
                    },
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "_id": "63e074633a9ea5e44d2515c8",
                    "name": "状态",
                    "key": "state_id",
                    "raw_key": "state_id",
                    "type": 14,
                    "property_key": "state_id",
                    "value_path": "state_id",
                    "from": 1,
                    "layout": 3,
                    "export_required": 0,
                    "lookup": "states",
                    "icon": "clock-circle-moment"
                },
                {
                    "_id": "6004f4c75f4983bd8e92bc79",
                    "name": "用例类型",
                    "key": "type",
                    "raw_key": "type",
                    "type": 6,
                    "property_key": "type",
                    "options": [
                        {
                            "_id": "5f0c152f3342df1eff78bdb9",
                            "text": "功能测试"
                        },
                        {
                            "_id": "5f0c15353342df1eff78bdba",
                            "text": "性能测试"
                        },
                        {
                            "_id": "5f0c153d3342df1eff78bdbb",
                            "text": "配置相关"
                        },
                        {
                            "_id": "5f0c15433342df1eff78bdbc",
                            "text": "安装部署"
                        },
                        {
                            "_id": "5f0c15493342df1eff78bdbd",
                            "text": "接口测试"
                        },
                        {
                            "_id": "5f0c15de3342df1eff78bdbe",
                            "text": "安全相关"
                        },
                        {
                            "_id": "5f0c16203342df1eff78bdbf",
                            "text": "兼容性测试"
                        },
                        {
                            "_id": "5f0c162c3342df1eff78bdc0",
                            "text": "UI测试"
                        },
                        {
                            "_id": "5f0c16333342df1eff78bdc1",
                            "text": "其他"
                        }
                    ],
                    "value_path": "type",
                    "from": 1,
                    "layout": 3,
                    "lookup": "types",
                    "icon": "check-circle"
                },
                {
                    "_id": "63e074633a9ea5e44d2515c7",
                    "name": "重要程度",
                    "key": "important_level",
                    "raw_key": "important_level",
                    "type": 6,
                    "property_key": "important_level",
                    "options": [
                        {
                            "_id": 1,
                            "text": "P0",
                            "color": "#FF7575",
                            "bg_color": "#FF7575"
                        },
                        {
                            "_id": 2,
                            "text": "P1",
                            "color": "#FF9F73",
                            "bg_color": "#FF9F73"
                        },
                        {
                            "_id": 3,
                            "text": "P2",
                            "color": "#F6C659",
                            "bg_color": "#F6C659"
                        },
                        {
                            "_id": 4,
                            "text": "P3",
                            "color": "#5DCFFF",
                            "bg_color": "#5DCFFF"
                        },
                        {
                            "_id": 5,
                            "text": "P4",
                            "color": "#73D897",
                            "bg_color": "#73D897"
                        }
                    ],
                    "value_path": "important_level",
                    "from": 1,
                    "option_style": 2,
                    "layout": 3,
                    "export_required": 0,
                    "icon": "importance"
                },
                {
                    "key": "identifier",
                    "name": "编号",
                    "from": 1,
                    "type": 3,
                    "export_required": 0,
                    "value_path": "identifier",
                    "raw_key": "identifier",
                    "property_key": "identifier",
                    "icon": "version"
                },
                {
                    "_id": "65a0ccc9c60ec328ad06d054",
                    "key": "title",
                    "name": "标题",
                    "from": 1,
                    "type": 1,
                    "export_required": 1,
                    "value_path": "title",
                    "raw_key": "title",
                    "property_key": "title",
                    "icon": "font"
                },
                {
                    "_id": "65a0ccc9c60ec328ad06d057",
                    "key": "suite_id",
                    "name": "模块",
                    "type": 1,
                    "from": 1,
                    "export_required": 0,
                    "value_path": "suite_id",
                    "raw_key": "suite_id",
                    "property_key": "suite_id",
                    "lookup": "suites",
                    "icon": "test-case-type"
                },
                {
                    "key": "review_result_state",
                    "name": "评审结果",
                    "from": 1,
                    "type": 32,
                    "is_system": 1,
                    "icon": "review",
                    "permissions": {
                        "name_editable": 0,
                        "data_editable": 0
                    },
                    "value_path": "review_result_state",
                    "raw_key": "review_result_state",
                    "property_key": "review_result_state"
                },
                {
                    "key": "principal_version",
                    "name": "版本",
                    "from": 1,
                    "type": 28,
                    "is_system": 1,
                    "icon": "version-circle",
                    "permissions": {
                        "name_editable": 0,
                        "data_editable": 0
                    },
                    "value_path": "principal_version",
                    "raw_key": "principal_version",
                    "property_key": "principal_version"
                },
                {
                    "_id": "65a0ccc9c60ec328ad06d056",
                    "key": "test_library_id",
                    "name": "测试库",
                    "from": 1,
                    "type": 6,
                    "export_required": 0,
                    "value_path": "test_library_id",
                    "raw_key": "test_library_id",
                    "property_key": "test_library_id",
                    "lookup": "pilots",
                    "icon": "test-lib"
                },
                {
                    "_id": "62ff3c3938663cd5a863eed5",
                    "key": "version_identifier",
                    "name": "版本号",
                    "from": 1,
                    "type": 3,
                    "export_required": 0,
                    "permissions": {
                        "sortable": 1,
                        "removable": 0,
                        "name_editable": 0,
                        "data_editable": 0,
                        "movable": 0,
                        "config_validator_required": 0,
                        "config_placeholder": 0,
                        "config_default_value": 0
                    },
                    "value_path": "version_identifier",
                    "raw_key": "version_identifier",
                    "property_key": "version_identifier",
                    "icon": "hashtag"
                },
                {
                    "_id": "65a0ccc9c60ec328ad06d055",
                    "key": "attachments",
                    "name": "附件",
                    "from": 1,
                    "type": 18,
                    "export_required": 0,
                    "value_path": "attachments",
                    "raw_key": "attachments",
                    "property_key": "attachments",
                    "lookup": "attachments"
                },
                {
                    "key": "comments",
                    "name": "评论",
                    "from": 1,
                    "type": 18,
                    "export_required": 0,
                    "value_path": "comments",
                    "raw_key": "comments",
                    "property_key": "comments"
                },
                {
                    "_id": "65a0ccc9c60ec328ad06d058",
                    "key": "participants",
                    "name": "关注人",
                    "from": 1,
                    "type": 10,
                    "export_required": 0,
                    "value_path": "participants",
                    "raw_key": "participants",
                    "property_key": "participants",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "status",
                    "name": "执行结果",
                    "from": 1,
                    "type": 14,
                    "export_required": 0,
                    "options": [
                        {
                            "_id": 1,
                            "text": "通过",
                            "color": "#73D897",
                            "icon": "check-circle-fill"
                        },
                        {
                            "_id": 2,
                            "text": "受阻",
                            "color": "#FFCD5D",
                            "icon": "minus-circle-fill"
                        },
                        {
                            "_id": 3,
                            "text": "失败",
                            "color": "#FF7575",
                            "icon": "close-circle-fill"
                        },
                        {
                            "_id": 4,
                            "text": "跳过",
                            "color": "#5DCFFF",
                            "icon": "arrow-right-circle-fill"
                        },
                        {
                            "_id": 5,
                            "text": "未测",
                            "color": "#DDDDDD",
                            "bg_color": "#CACACA",
                            "icon": "question-circle-fill"
                        }
                    ],
                    "value_path": "status",
                    "raw_key": "status",
                    "property_key": "status",
                    "icon": "result"
                },
                {
                    "key": "executed_at",
                    "name": "执行时间",
                    "from": 1,
                    "type": 4,
                    "export_required": 0,
                    "value_path": "executed_at",
                    "raw_key": "executed_at",
                    "property_key": "executed_at",
                    "icon": "calendar"
                },
                {
                    "key": "executor_uid",
                    "name": "执行人",
                    "from": 1,
                    "type": 9,
                    "export_required": 0,
                    "value_path": "executor_uid",
                    "raw_key": "executor_uid",
                    "property_key": "executor_uid",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "executed_time",
                    "name": "执行次数",
                    "from": 1,
                    "type": 3,
                    "export_required": 0,
                    "value_path": "executed_time",
                    "raw_key": "executed_time",
                    "property_key": "executed_time",
                    "icon": "hashtag"
                },
                {
                    "key": "priority",
                    "name": "优先级",
                    "from": 1,
                    "type": 6,
                    "export_required": 0,
                    "options": [
                        {
                            "_id": 1,
                            "text": "高",
                            "color": "#FF7575"
                        },
                        {
                            "_id": 2,
                            "text": "中",
                            "color": "#F6C659"
                        },
                        {
                            "_id": 3,
                            "text": "低",
                            "color": "#73D897"
                        },
                        {
                            "_id": 4,
                            "text": ""
                        }
                    ],
                    "value_path": "priority",
                    "raw_key": "priority",
                    "property_key": "priority",
                    "icon": "exclamation-three"
                },
                {
                    "key": "created_at",
                    "name": "创建时间",
                    "from": 1,
                    "type": 4,
                    "export_required": 0,
                    "value_path": "created_at",
                    "raw_key": "created_at",
                    "property_key": "created_at",
                    "icon": "calendar"
                },
                {
                    "key": "created_by",
                    "name": "创建人",
                    "from": 1,
                    "type": 9,
                    "export_required": 0,
                    "value_path": "created_by",
                    "raw_key": "created_by",
                    "property_key": "created_by",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "deleted_at",
                    "name": "删除时间",
                    "from": 1,
                    "type": 4,
                    "export_required": 0,
                    "value_path": "deleted_at",
                    "raw_key": "deleted_at",
                    "property_key": "deleted_at",
                    "icon": "calendar"
                },
                {
                    "key": "deleted_by",
                    "name": "删除人",
                    "from": 1,
                    "type": 9,
                    "export_required": 0,
                    "value_path": "deleted_by",
                    "raw_key": "deleted_by",
                    "property_key": "deleted_by",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "archived_at",
                    "name": "归档时间",
                    "from": 1,
                    "type": 4,
                    "export_required": 0,
                    "value_path": "archived_at",
                    "raw_key": "archived_at",
                    "property_key": "archived_at",
                    "icon": "calendar"
                },
                {
                    "key": "archived_by",
                    "name": "归档人",
                    "from": 1,
                    "type": 9,
                    "export_required": 0,
                    "value_path": "archived_by",
                    "raw_key": "archived_by",
                    "property_key": "archived_by",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "updated_at",
                    "name": "更新时间",
                    "from": 1,
                    "type": 4,
                    "export_required": 0,
                    "value_path": "updated_at",
                    "raw_key": "updated_at",
                    "property_key": "updated_at",
                    "icon": "calendar"
                },
                {
                    "key": "updated_by",
                    "name": "更新人",
                    "from": 1,
                    "type": 9,
                    "export_required": 0,
                    "value_path": "updated_by",
                    "raw_key": "updated_by",
                    "property_key": "updated_by",
                    "lookup": "members",
                    "icon": "user-bold"
                },
                {
                    "key": "suite_position",
                    "name": "模块顺序",
                    "from": 1,
                    "type": 3,
                    "export_required": 0,
                    "value_path": "suite_position",
                    "raw_key": "suite_position",
                    "property_key": "suite_position",
                    "icon": "hashtag"
                },
                {
                    "key": "estimated_workload",
                    "raw_key": "estimated_workload",
                    "name": "预估工时",
                    "from": 2,
                    "type": 3,
                    "icon": "hashtag",
                    "is_system": 1,
                    "value_path": "properties.estimated_workload",
                    "permissions": {},
                    "property_key": "estimated_workload",
                    "custom_config": {
                        "enable_sum_with_descendants": 0
                    },
                    "ref_properties": {
                        "workload_s_semh": {
                            "key": "workload_s_semh",
                            "raw_key": "workload_s_semh",
                            "name": "预估工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.estimated_workload",
                            "is_system": 1
                        },
                        "workload_ss_emh": {
                            "key": "workload_ss_emh",
                            "raw_key": "workload_ss_emh",
                            "name": "总预估工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.workload_ss_emh",
                            "is_system": 1
                        }
                    }
                },
                {
                    "key": "reported_workload",
                    "raw_key": "reported_workload",
                    "name": "登记工时",
                    "from": 2,
                    "type": 3,
                    "icon": "hashtag",
                    "is_system": 1,
                    "value_path": "properties.reported_workload",
                    "permissions": {},
                    "property_key": "reported_workload",
                    "custom_config": {
                        "enable_sum_with_descendants": 0
                    },
                    "ref_properties": {
                        "workload_s_armh": {
                            "key": "workload_s_armh",
                            "raw_key": "workload_s_armh",
                            "name": "登记工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.reported_workload",
                            "is_system": 1
                        },
                        "workload_ss_armh": {
                            "key": "workload_ss_armh",
                            "raw_key": "workload_ss_armh",
                            "name": "总登记工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.workload_ss_armh",
                            "is_system": 1
                        }
                    }
                },
                {
                    "key": "remaining_workload",
                    "raw_key": "remaining_workload",
                    "name": "剩余工时",
                    "from": 2,
                    "type": 3,
                    "icon": "hashtag",
                    "is_system": 1,
                    "value_path": "properties.remaining_workload",
                    "permissions": {},
                    "property_key": "remaining_workload",
                    "custom_config": {
                        "enable_sum_with_descendants": 0
                    },
                    "ref_properties": {
                        "workload_s_sermh": {
                            "key": "workload_s_sermh",
                            "raw_key": "workload_s_sermh",
                            "name": "剩余工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.remaining_workload",
                            "is_system": 1
                        },
                        "workload_ss_ermh": {
                            "key": "workload_ss_ermh",
                            "raw_key": "workload_ss_ermh",
                            "name": "总剩余工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.workload_ss_ermh",
                            "is_system": 1
                        }
                    }
                },
                {
                    "key": "progress_by_remaining",
                    "raw_key": "progress_by_remaining",
                    "name": "工时进度",
                    "from": 2,
                    "type": 15,
                    "icon": "progress",
                    "is_system": 1,
                    "value_path": "properties.progress_by_remaining",
                    "property_key": "progress_by_remaining",
                    "custom_config": {
                        "enable_sum_with_descendants": 0
                    },
                    "ref_properties": {
                        "workload_s_spbr": {
                            "key": "workload_s_spbr",
                            "raw_key": "workload_s_spbr",
                            "name": "工时进度",
                            "from": 2,
                            "type": 15,
                            "icon": "progress",
                            "value_path": "properties.progress_by_remaining",
                            "is_system": 1
                        },
                        "workload_ss_pbr": {
                            "key": "workload_ss_pbr",
                            "raw_key": "workload_ss_pbr",
                            "name": "总工时进度",
                            "from": 2,
                            "type": 15,
                            "icon": "progress",
                            "value_path": "properties.workload_ss_pbr",
                            "is_system": 1
                        },
                        "workload_s_sermh": {
                            "key": "workload_s_sermh",
                            "raw_key": "workload_s_sermh",
                            "name": "剩余工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.remaining_workload",
                            "is_system": 1
                        },
                        "workload_ss_ermh": {
                            "key": "workload_ss_ermh",
                            "raw_key": "workload_ss_ermh",
                            "name": "总剩余工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.workload_ss_ermh",
                            "is_system": 1
                        },
                        "workload_s_armh": {
                            "key": "workload_s_armh",
                            "raw_key": "workload_s_armh",
                            "name": "登记工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.reported_workload",
                            "is_system": 1
                        },
                        "workload_ss_armh": {
                            "key": "workload_ss_armh",
                            "raw_key": "workload_ss_armh",
                            "name": "总登记工时",
                            "from": 2,
                            "type": 3,
                            "icon": "hashtag",
                            "value_path": "properties.workload_ss_armh",
                            "is_system": 1
                        }
                    }
                }
            ],
            "property_bindings": [
                {
                    "property_key": "precondition",
                    "from": 1
                },
                {
                    "property_key": "steps",
                    "from": 1
                },
                {
                    "property_key": "description",
                    "from": 1
                },
                {
                    "property_key": "test_type",
                    "from": 1,
                    "layout": 2,
                    "group_id": "5cb9466afda1ce4ca0000001"
                },
                {
                    "property_key": "maintenance_uid",
                    "from": 1,
                    "layout": 3
                },
                {
                    "property_key": "state_id",
                    "from": 1,
                    "layout": 3
                },
                {
                    "property_key": "type",
                    "from": 1,
                    "layout": 3
                },
                {
                    "property_key": "important_level",
                    "from": 1,
                    "layout": 3
                }
            ],
            "property_groups": [
                {
                    "_id": "5cb9466afda1ce4ca0000001",
                    "name": "属性"
                }
            ]
        }
    }
}
print(data['data']['value']['participants'])

# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#
#     with multiprocessing.Pool(processes=5) as pool:
#         for sheet_name in sheet_names:
#             pool.apply_async(run, args=(sheet_name,))
#             time.sleep(2)
#
#         pool.close()
#         pool.join()
    # print('失败数：',code_counts.get(0,0))
    # print('成功数：',code_counts.get(1,0))
    # print('总数：',code_counts.get(2,0))

