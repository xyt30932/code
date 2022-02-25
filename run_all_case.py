import unittest, os,time
from tools import HTMLTestRunner
current_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(current_path, "script")

report_path = os.path.join(current_path, 'report')
report = os.path.join(report_path, 'report-{}.html'.format(time.strftime("%Y-%m-%d-%H-%M-%S")))


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    return discover


if __name__ == '__main__':
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title='来画系统项目测试报告',
        description='来画工作台测试报告'
    )
    runner.run(all_case())