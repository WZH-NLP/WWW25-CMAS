"""
@Time       : 2024/8/8 17:37
@File       : extract_trf.py
@Description: extract type-related-features
"""
import argparse

import ast

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mutual_info_score
import json
from transformers import AutoTokenizer


def group_data_by_tag(ori_data: pd.DataFrame, ner_types) -> pd.DataFrame:
    """
    group the data by their tags
    :param ori_data:
    :return: grouped_dataset( pd.DataFrame(columns=['tokens', 'tags', 'class', 'sentence']) )
    """
    new_data = pd.DataFrame(columns=['tokens', 'tags', 'class', 'sentence'])
    for i in range(0, ori_data.shape[0]):
        tokens = ori_data.loc[i]['tokens']
        tags = ori_data.loc[i]['tags']
        class_list = []
        for entity_type in ner_types.items():
            if entity_type[1] in tags:
                class_list.append(entity_type[0])
                new_data.loc[len(new_data)] = [tokens, tags, entity_type[0], ' '.join(tokens)]
    print(f"new_data:\n{new_data}")
    return new_data


def mutual_information(grouped_data, num_per_domain, total_class_num, drf_save_path, ckpt, rho) -> dict:
    """
    extract drf by mutual information
    :param rho: 3
    :param drf_save_path: save path
    :param total_class_num: 4
    :param grouped_data: pd.DataFrame(columns=['tokens', 'tags', 'class', 'sentence'])
    :param num_per_domain: nums of DRF
    :return: drf words per domain
    """
    #  get the counts of each words
    if "roberta" in ckpt.lower():
        tokenizer = AutoTokenizer.from_pretrained(ckpt, add_prefix_space=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(ckpt)
    drf_id_list = []
    docs_per_class = grouped_data[['class', 'sentence']].groupby(['class'], as_index=False).agg({'sentence': ' '.join})
    print(docs_per_class.info())
    count_vector = CountVectorizer(lowercase=False)
    count_fit = count_vector.fit_transform(docs_per_class['sentence'])
    count_vector_array = count_fit.toarray()
    # print(count_vector_array.shape)
    count_sum = count_vector_array.sum(axis=0)
    # print(count_vector.vocabulary_['the'])

    # get the total CountVectorizer all sentences * all words
    total_vector = CountVectorizer(binary=True, stop_words='english', lowercase=False)
    total_array = total_vector.fit_transform(grouped_data['sentence']).toarray()

    # drf dict of each class
    words_per_domain = {}
    for class_id in range(0, total_class_num):
        drfs_in_one_class = []  # drf in this class
        src_class_name = docs_per_class['class'][class_id]
        print("Now extracting DRF of class by MI:", src_class_name)
        mi_vector_of_src = []
        for i in range(0, grouped_data.shape[0]):
            if grouped_data.loc[i]['class'] == src_class_name:
                mi_vector_of_src.append(1)
            else:
                mi_vector_of_src.append(0)
        MI = {}
        for i in range(0, total_array.shape[1]):
            temp = mutual_info_score(total_array[:, i], mi_vector_of_src)
            MI[i] = temp
        # print(MI)
        MIs = sorted(MI.items(), key=lambda x: x[1], reverse=True)
        # print(MIs)
        for word_info in MIs:
            word_name = total_vector.get_feature_names_out()[word_info[0]]
            count_word_id = count_vector.vocabulary_[word_name]
            if len(drfs_in_one_class) == num_per_domain:
                break
            if count_vector_array[class_id][count_word_id] == 0 or any(ch.isdigit() for ch in word_name):
                continue
            if count_sum[count_word_id] / count_vector_array[class_id][count_word_id] < rho:
                word_id = tokenizer(word_name)["input_ids"][1]
                if word_id not in drf_id_list:
                    drf_id_list.append(word_id)
                    drfs_in_one_class.append(word_name)
        words_per_domain[src_class_name] = drfs_in_one_class
    print(words_per_domain)
    file_name = drf_save_path
    print("writing to", file_name, "...")
    with open(file_name, 'w') as f:
        f.write(json.dumps(words_per_domain))
    return words_per_domain


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset_name', type=str, default='wikigold', help="Name of the dataset")
    parser.add_argument('--num_per_domain', type=int, default=10, help="Number of trf per domain")
    parser.add_argument('--rho', type=int, default=3, help="Parameter for mutual information")

    args = parser.parse_args()

    with open(f'{args.dataset_name}/train.json', 'r') as file:
        data = json.load(file)

    with open(f'{args.dataset_name}/abb2labelname.json', 'r') as file:
        ner_types = json.load(file)

    all_tokens = []
    all_tags = []

    for entry in data:
        sentence = entry['sentence']
        if not isinstance(entry['label'], dict):
            labels = ast.literal_eval(entry['label'])
        else:
            labels = entry['label']
        tokens = sentence.split()
        tags = ['O'] * len(tokens)

        for entity, label in labels.items():
            entity_tokens = entity.split()
            for i in range(len(tokens) - len(entity_tokens) + 1):
                if tokens[i:i + len(entity_tokens)] == entity_tokens:
                    tags[i] = label
                    for j in range(1, len(entity_tokens)):
                        tags[i + j] = label

        assert len(tokens) == len(tags)
        all_tokens.append(tokens)
        all_tags.append(tags)

    df = pd.DataFrame({'tokens': all_tokens, 'tags': all_tags})

    group_data = group_data_by_tag(df, ner_types)
    trfs = mutual_information(group_data, args.num_per_domain, len(ner_types), f'{args.dataset_name}/trf.json',
                              'bert-base-cased', args.rho)
    print(trfs)


if __name__ == "__main__":
    main()
