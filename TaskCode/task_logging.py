# coding:utf-8
import logging

__author__ = 'YangJun'


# 普通logging控制台输出和文件日志输出格式及调用
# logger = logging.getLogger('Clarence')
# logger.setLevel(logging.INFO)
# # logging.basicConfig(level=logging.INFO,
# #                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 控制台日志输出日志格式
#
# Format = logging.Formatter(fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh = logging.FileHandler("test.log")
# fh.setLevel(logging.DEBUG)
# fh.setFormatter(Format)
# logger.addHandler(fh)
#
# sh = logging.StreamHandler()
# sh.setLevel(logging.INFO)
# sh.format(Format)
# logger.addHandler(sh)


# 重新封装logging中控制台和文件日志输出，当项目中存在多处日志打印时，可封装日志模块
class Logger:
    def __init__(self, name, sh_level, ft_level, path):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        Format = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        sh = logging.StreamHandler()
        sh.setLevel(sh_level)
        sh.setFormatter(Format)
        fh = logging.FileHandler(path)
        fh.setLevel(ft_level)
        fh.setFormatter(Format)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def logging_info(self, message):
        self.logger.info(message)

    def logging_debug(self, message):
        self.logger.debug(message)

    def logging_warning(self, message):
        self.logger.warning(message)

    def logging_error(self, message):
        self.logger.error(message)

    def logging_critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    test_log = Logger("clarence", logging.INFO, logging.DEBUG, 'test.log')
    test_log.logging_error("just test")
