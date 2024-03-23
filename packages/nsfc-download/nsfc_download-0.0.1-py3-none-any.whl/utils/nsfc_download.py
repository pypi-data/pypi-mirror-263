import os
import re
import sys
from utils import get_data, img_pdf

def main():
    current_path = os.getcwd()
    # 判断是否有参数
    if len(sys.argv) < 2:
        print("请输入链接！")
        return
    # 获取第一个参数
    pdf_name = sys.argv[1]
    # 判断是符合https://kd.nsfc.cn/finalDetails?id=709232d7be43f7cad6fba63a5fb38b63
    pattern = re.compile(r'^https://kd.nsfc.cn/finalDetails\?id=\w{32}$')
    if pattern.match(pdf_name):
        # 获取id
        id = pdf_name.split('=')[-1]
        # 实例化
        nsfc = get_data.NSFC(id)
        # 创建文件夹 nsfc.projectName
        if not os.path.exists(nsfc.projectName):
            os.makedirs(nsfc.projectName)
        print("数据保存路径：", os.path.join(current_path, nsfc.projectName))
        # 下载
        path_lists = nsfc.download()
        # 转换PDF
        img_pdf.img_change_pdf(path_lists,
                               os.path.join(current_path, os.path.join(nsfc.projectName, f'{nsfc.projectName}.pdf')))
    else:
        # 提示出错
        print("请输入正确的链接！")

if __name__ == '__main__':
    main()