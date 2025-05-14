# A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition

Source code for our paper accepted at the ACM WWW conference: [A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition](https://dl.acm.org/doi/pdf/10.1145/3696410.3714923). Our implementation is base on [Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models](https://github.com/Emma1066/Self-Improve-Zero-Shot-NER). 

## Introduction
Inspired by the demonstrated complex problem-solving capabilities of multi-agent approaches, in this paper, we present a framework, named the <ins>C</ins>ooperative <ins>M</ins>ulti-<ins>A</ins>gent <ins>S</ins>ystem (CMAS) for zero-shot NER, harnessing the collective intelligence of LLM-based agents.

![image](framework.png)

CMAS aims to address two challenging problems:

- Challenge 1: Overlooking correlations between contexts surrounding entities.
- Challenge 2: Indiscriminate use of task demonstrations.

To tackle the first issue, we propose redefining the traditional NER task into two subtasks: recognizing named entities and identifying entity type-related features (TRFs, i.e., tokens strongly associated with entity types). To address the second problem, we incorporate a self-reflection mechanism, enabling LLMs to reflect on the helpfulness of retrieved demonstrations and selectively learn from them.
 
## Prepare the data
1. See data/README.md

2. Run the followings commands to Extract trf and embedding:
```shell
python extract_trf.py --dataset_name <dataset_name>
python get_trf_embd.py
```

## Run
1. Set your <api-key> and <base-url> in code/const.py

2. Run the followings commands:

```shell
# Self-annotator for unlabelled data
sh scripts/wikigold_1_self_annotate_TSMV.sh
sh scripts/wikigold_2_entity_level_sel.sh
sh scripts/wikigold_2_sample_level_sel.sh
# Helpfulness-based prediction
sh scripts/wikigold_3_test_inference_helpfulness.sh
# Trf-based prediction
sh scripts/wikigold_3_test_inference_trf.sh
# Get performance on overall prediction
sh scripts/wikigold_3_test_get_results.sh
```

## Citations
```
@inproceedings{wang2025cooperative,
  title={A cooperative multi-agent framework for zero-shot named entity recognition},
  author={Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
  booktitle={Proceedings of the ACM on Web Conference 2025},
  pages={4183--4195},
  year={2025}
}

@inproceedings{wang2023generalizing,
  title={Generalizing Few-Shot Named Entity Recognizers to Unseen Domains with Type-Related Features},
  author={Wang, Zihan and Zhao, Ziqi and Chen, Zhumin and Ren, Pengjie and de Rijke, Maarten and Ren, Zhaochun},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
  pages={2228--2240},
  year={2023}
}

```
