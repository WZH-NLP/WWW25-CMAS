"""
@Time       : 2024/5/8 20:53
@File       : read_json.py
@Description: 
"""
import json

path = "prompts/self_consistent_annotate/wikigold/self_supervision/train_shuffle_42/fs_pool_std_c5_500_GPTEmbDvrsKNN_50_Sc/st_std_c5_test_prompts__16_code.json"
with open(path, 'r') as f:
    data = json.load(f)

for obj in data:
    label = eval(obj['label'])
    for item in label.items():
        if item[1] == 'Miscellaneous':
            print(item[0])
    # print("label:", obj['label'])

# todo
"""
definition of MISC:
This includes adjectives, like Italian, and events, like 1000 Lakes Rally, making it a very diverse category
"""
