import os
import re

import tqdm
import sys

sys.path.insert(0, '../../../')
from gxl_ai_utils.utils import utils_file


def do_remove_punctuation(text):
    # 使用正则表达式去除标点符号，只保留汉字、英文和数字
    return re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)


def make_shard():
    """"""
    utils_file.logging_print('先确认一下音频是否都转移成功到nfs, 确认过了,好些没转移成功')
    source_dir = "/home/node36_data/xlgeng/asr_data_from_pachong/gxl_output"
    # target_dir = "/home/work_nfs14/xlgeng/asr_data_from_pachong"
    target_dir = "/home/work_nfs14/xlgeng/asr_data_shard/pachong_data"
    dataname_list = ["ximalaya_lishi_10T-1", "ximalaya_lishi_10T", "ximalaya_redian_2T"]
    # for dataname in dataname_list:
    #     temp_source_dir = os.path.join(source_dir, dataname)
    #     temp_target_dir = os.path.join(target_dir, dataname)
    #     wav_scp_path = os.path.join(source_dir, dataname, "all_wav.scp")
    #     wav_dict = utils_file.load_dict_from_scp(wav_scp_path)
    #     new_wav_dict = {}
    #     for k, v in tqdm.tqdm(wav_dict.items(), total=len(wav_dict)):
    #         wav_name = os.path.basename(v)
    #         new_path = os.path.join(temp_target_dir, wav_name)
    #         if not os.path.exists(new_path):
    #             utils_file.logging_print(f"文件{new_path}不存在")
    #             continue
    #         new_wav_dict[k] = os.path.join(temp_target_dir, wav_name)
    #     utils_file.write_dict_to_scp(new_wav_dict, os.path.join(temp_source_dir, "wav_all.scp"))

    utils_file.logging_print('开始清理text, 清理完毕')
    # for dataname in dataname_list:
    #     temp_source_dir = os.path.join(source_dir, dataname)
    #     temp_target_dir = os.path.join(target_dir, dataname)
    #     wav_scp_path = os.path.join(source_dir, dataname, "all.text")
    #     wav_dict = utils_file.load_dict_from_scp(wav_scp_path)
    #     new_wav_dict = {}
    #     for k, v in tqdm.tqdm(wav_dict.items(), total=len(wav_dict)):
    #         v = do_remove_punctuation(v)
    #         new_wav_dict[k] = v
    #     utils_file.write_dict_to_scp(new_wav_dict, os.path.join(temp_source_dir, "all_2.text"))
    utils_file.logging_print("开始打包")
    # if len(sys.argv) > 1:
    #     index = int(sys.argv[1])
    # else:
    #     index = 0
    # utils_file.logging_print('开始处理第{}个数据集'.format(index))
    # dataname = dataname_list[index]
    # temp_source_dir = os.path.join(source_dir, dataname)
    # text_path = os.path.join(temp_source_dir, "all_2.text")
    # wav_path = os.path.join(temp_source_dir, "all_wav.scp")
    # temp_target_dir = os.path.join(target_dir, dataname)
    # utils_file.makedir_sil(temp_target_dir)
    # utils_file.do_make_shard_file(wav_path,text_path,temp_target_dir, num_threads=50)

    utils_file.logging_print('开始合并')
    all_list = []
    for dataname in dataname_list:
        temp_dir = os.path.join(target_dir, dataname)
        shards_list_path = os.path.join(temp_dir, "shards_list.txt")
        temp_shard_list = utils_file.load_list_file_clean(shards_list_path)
        all_list.extend(temp_shard_list)
    utils_file.write_list_to_file(all_list, os.path.join(target_dir, "all_shards_list.txt"))
if __name__ == '__main__':
    make_shard()
