
# 安装

### 机器
机器 66


### Build environment
python3.10 -m venv venv
source venv/bin/activate

如果涉及到AI 使用GPU，一般需要再 requirements.txt 第一行添加 
--extra-index-url https://download.pytorch.org/whl/cu118

pip install -r requirements.txt 

### mmlab packages
```bash
pip install --no-cache-dir -U openmim 
mim install mmengine 
mim install "mmcv>=2.0.1" 
mim install "mmdet>=3.1.0" 
mim install "mmpose>=1.1.0" 
```