import multiprocessing
import send
from autotest import Autotest
import time

plan_name = 'LanTu_ui_1'
# sheet_names = ['data1', 'data2', 'data3', 'data4', 'data5']
sheet_names = ['data5']

def run(sheet_name, code_counts):
    desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'headless': True}
    server_url = ''
    sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)
    sweet.plan()
    code_counts[sweet.code] = code_counts.get(sweet.code, 0) + 1
    send.sendMessage(sweet.code, plan_name, sheet_name)

if __name__ == '__main__':
    # 创建共享字典
    manager = multiprocessing.Manager()
    code_counts = manager.dict()

    with multiprocessing.Pool(processes=5) as pool:
        for sheet_name in sheet_names:
            pool.apply_async(run, args=(sheet_name, code_counts))
            time.sleep(2)
        pool.close()
        pool.join()

    # 输出统计结果
    print("Code Counts:", code_counts)
