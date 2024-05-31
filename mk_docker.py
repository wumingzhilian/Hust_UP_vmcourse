import os
import shutil
import random
import re
from pathlib import Path

def rename_files():
    src_directory = 'drill'
    # 确保目录存在
    if not os.path.exists(src_directory):
        print(f"Directory {src_directory} does not exist.")
        return

    # 遍历 drill 目录中的所有文件
    for file in os.listdir(src_directory):
        file_path = os.path.join(src_directory, file)
        if os.path.isfile(file_path):
            # 分离文件名和扩展名
            base_name, extension = os.path.splitext(file)
            
            # 去除扩展名中的点号
            new_extension = extension.replace('.', '')

            # 重新组合文件名
            new_filename = base_name + new_extension

            # 构建新的文件路径
            new_file_path = os.path.join(src_directory, new_filename)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed '{file}' to '{new_filename}'")


def copy_and_replace(template_path, target_path, filename, port, name):
    # 创建目标目录的路径
    os.makedirs(target_path, exist_ok=True)
    
    # 遍历模板目录并复制文件
    for root, dirs, files in os.walk(template_path):
        relative_path = root[len(template_path):].lstrip(os.sep)
        dest_path = os.path.join(target_path, relative_path)
        os.makedirs(dest_path, exist_ok=True)
        
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_path, file)
            shutil.copy(src_file, dst_file)
            
            # 如果文件是文本格式，替换占位符
            if dst_file.endswith('.yml') or dst_file.endswith('.sh') or dst_file.endswith('Dockerfile') or  dst_file.endswith('.xinetd'):
                with open(dst_file, 'r', encoding='utf8') as f:
                    content = f.read()
                content = content.replace('{port}', str(port))
                content = content.replace('{name}', name)
                with open(dst_file, 'w', encoding='utf8') as f:
                    f.write(content)

def main():
    src_directory = 'drill'
    template_directory = 'template'
    base_port = 2000

    # 遍历 drill 目录中的所有文件
    for file in os.listdir(src_directory):
        file_path = os.path.join(src_directory, file)
        if os.path.isfile(file_path):
            # 文件名（不包含后缀）作为目录名
            name = Path(file).stem
            new_directory = os.path.join('output', name)
            new_ctf_directory = os.path.join(new_directory, 'ctf')
            os.makedirs(new_ctf_directory, exist_ok=True)
            
            # 随机分配一个端口
            port = random.randint(base_port, 3000)
            
            # 拷贝 template 到新目录并替换内容
            copy_and_replace(template_directory, new_directory, file, port, name)
            
            # 移动文件到新的 ctf 目录下
            shutil.copy(file_path, os.path.join(new_ctf_directory, file))

if __name__ == "__main__":
    main ()# 生成新的目录
    #rename_files () # 重命名文件