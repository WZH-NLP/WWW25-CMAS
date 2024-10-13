"""
@Time       : 2024/5/24 16:36
@File       : show_results.py
@Description: 
"""
import json
import ast

file_dict = {
    "CODE": "TIME_STAMP_st_std_c5_test__16_response_code.json",
    "NATURAL LANGUAGE": "TIME_STAMP_st_std_c5_test__16_response.json"
}

# print(file_dict.keys())
name1 = list(file_dict.keys())[0]
name2 = list(file_dict.keys())[1]
path1 = file_dict[name1]
path2 = file_dict[name2]
with open(path1, 'r', encoding='utf-8') as file:
    data1 = json.load(file)
with open(path2, 'r', encoding='utf-8') as file:
    data2 = json.load(file)
a = ast.literal_eval(data2[0]['prediction'])

for d1, d2 in zip(data1, data2):
    print('sentence:', d1['sentence'])
    print('label', d1['label'])
    label = d1['label']
    pred_d1 = ast.literal_eval(d1['prediction'])
    pred_d2 = ast.literal_eval(d2['prediction'])
    print('-'*50)
    # d1 right prediction
    info = f'{name1} right prediction:'
    print(info)
    for item in pred_d1.items():
        if item in label.items():
            print(item)
    print('-'*50)
    # d1 wrong prediction
    info = f'{name1} wrong prediction:'
    print(info)
    for item in pred_d1.items():
        if item not in label.items():
            print( item)
    print('-'*50)
    # d2 right prediction
    info = f'{name2} right prediction:'
    print(info)
    for item in pred_d2.items():
        if item in label.items():
            print( item)
    print('-'*50)
    # d2 wrong prediction
    info = f'{name2} wrong prediction:'
    print(info)
    for item in pred_d2.items():
        if item not in label.items():
            print( item)
    print('-'*50)

    # d1 predicts not d1 not
    info = f'{name1} predicts but {name2} not:'
    print(info)
    for item in pred_d1.items():
        if item in label.items() and item not in pred_d2.items():
            print( item)
    print('-'*50)
    # d2 predicts not d1 not
    info = f'{name2} predicts but {name1} not:'
    print(info)
    for item in pred_d2.items():
        if item in label.items() and item not in pred_d1.items():
            print(item)
    print()
    print("#" * 50)
