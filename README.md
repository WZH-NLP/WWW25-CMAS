# A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition

Source code for our paper accepted at the ACM WWW conference: [A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition](https://dl.acm.org/doi/pdf/10.1145/3696410.3714923), our implementation is base on [Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models](https://github.com/Emma1066/Self-Improve-Zero-Shot-NER). 

## Prepare the data
See data/README.md

Run the followings commands to Extract trf and embedding
```shell
python extract_trf.py --dataset_name <dataset_name>
python get_trf_embd.py
```

## Run
### 1. Set your <api-key> and <base-url> in code/const.py

### 2. Run the followings commands

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

