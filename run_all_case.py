import unittest, os, yagmail
from tools import HTMLTestRunner
current_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(current_path, "case")

report_path = os.path.join(current_path, 'report')
report = os.path.join(report_path, 'report.html')

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    return discover

def send(user, password, receiver):
    yag = yagmail.SMTP(user=user,
                       password=password,
                       host='smtp.exmail.qq.com')

    contents = ['测试报告']
    try:
        yag.send(to=receiver,
                 subject='subject',
                 contents=contents,
                 attachments="D:\\xyt_code\\report\\report.html")

    except Exception as e:
        print("Error: 抱歉发送邮件失败", e)

    yag.close()

if __name__ == '__main__':
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title='来画系统项目测试报告',
        description='来画工作台测试报告'
    )
    runner.run(all_case())
    fb.close()

    send("xieyingtao@laihua.com", "nt5a6Y9wbEgj8bmj",
         "xieyingtao@laihua.com")
