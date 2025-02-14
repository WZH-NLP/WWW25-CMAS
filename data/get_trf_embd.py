"""
@Time       : 2024/8/12 20:36
@File       : get_trf_embd.py
@Description: 
"""
import json
import pickle

import numpy as np
import openai

from openai.embeddings_utils import get_embedding

dataset_name = 'wnut17'


def main():
    my_openai_api_keys = {"key": "<api-key>", "set_base": True,
                          "api_base": "<base-url>"}

    openai.api_key = my_openai_api_keys["key"]
    openai.api_base = my_openai_api_keys["api_base"]
    with open(f'{dataset_name}/trf.json', 'r') as file:
        trfs = json.load(file)
    trf2embd = {}
    for trf_list in trfs.values():
        for trf in trf_list:
            print(trf)
            embd = get_embedding(trf, engine="text-embedding-ada-002")
            # print(embd)
            trf2embd[trf] = embd
    print(trf2embd)
    with open(f'{dataset_name}/trf_embd.pkl', 'wb') as f:
        pickle.dump(trf2embd, f)

main()
# with open(f'{dataset_name}/trf_embd.pkl', 'rb') as f:
#     data = pickle.load(f)
# print(len(data['village']))
