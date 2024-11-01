import os
import shutil
import yaml
def setup_directory(directory_path):
    """如果存在目录，则删除并重新创建"""
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
    os.makedirs(directory_path)

def load_config():
    # 加载YAML文件
    with open('./config.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config