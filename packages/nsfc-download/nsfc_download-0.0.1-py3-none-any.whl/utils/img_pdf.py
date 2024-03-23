import os

import img2pdf

def img_change_pdf(imgs_pathlist, output_name):
    # 创建一个PDF文件 并以二进制方式写入
    with open(output_name, "wb") as f:
        # convert函数 用来转PDF
        write_content = img2pdf.convert(imgs_pathlist)
        f.write(write_content)  # 写入文件
    print("转换成功！")  # 提示语
    print("当前路径为：", output_name)
    os.startfile(output_name)  # 打开文件