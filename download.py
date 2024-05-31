
from HFUtils.HFUtilDownload import HFUtilDownload

import requests,os
from tqdm import tqdm


def download_file(url, local_filename=None):
    """
    下载文件并显示进度条
    
    :param url: 文件的URL
    :param local_filename: 本地保存的文件名，如果不提供则从URL中提取
    """
    if local_filename is None:
        local_filename = url.split('/')[-1]
    # 确保保存目录存在
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # 确保请求成功
        total_size = int(r.headers.get('content-length', 0))  # 获取文件总大小
        with open(local_filename, 'wb') as f, tqdm(
                desc=local_filename,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:  # 过滤掉keep-alive新行
                    f.write(chunk)
                    bar.update(len(chunk))

downLoadUtil = HFUtilDownload()


url = "https://download.openmmlab.com/mmdetection/v2.0/yolox/yolox_l_8x8_300e_coco/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth"
localFilePath = "./dwpose/yolox_l_8x8_300e_coco.pth"
download_file(url, localFilePath)



repo_id="TMElyralab/MusePose"
folder_name="MusePose"
local_dir="./pretrained_weights"
downLoadUtil.download_folder_from_repo(repo_id=repo_id, 
                                         folder_name=folder_name, 
                                         local_dir=local_dir)

repo_id="lambdalabs/sd-image-variations-diffusers"
downLoadUtil.download_folder_from_repo(repo_id=repo_id, 
                                         local_dir=local_dir)

repo_id="stabilityai/sd-vae-ft-mse"
downLoadUtil.download_folder_from_repo(repo_id=repo_id, 
                                         local_dir=local_dir)

repo_id="yzd-v/DWPose"
downLoadUtil.download_folder_from_repo(repo_id=repo_id, 
                                         local_dir=local_dir)


repo_id="lambdalabs/sd-image-variations-diffusers"
downLoadUtil.download_folder_from_repo(repo_id=repo_id, 
                                         local_dir=local_dir)



