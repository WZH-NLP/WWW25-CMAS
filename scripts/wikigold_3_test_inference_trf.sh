MODEL=gpt-3.5-turbo-0125

dataname=wikigold
datamode=test

FEW_SHOT_SETTING=pool
DEMO_RETRIEVAL_METHOD=GPTEmbDvrsKNN
diverseKNN_sampling=Sc
diverseKNN_number=50
self_annotate_tag=std_c5
demo_datamode=train_shuffle_42
FEW_SHOT_NUMBER=16
START_TIME="TIME_STAMP"

# # ----- two-stage majority voting
demo_select_method=std_c5
DEMO_SIZE=500
python code/self_consistent_annotation/GeneratePrompts_trf.py \
    --dataname $dataname \
    --datamode $datamode \
    --model $MODEL \
    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
    --demo_select_method $demo_select_method \
    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
    --few_shot_number $FEW_SHOT_NUMBER \
    --self_annotate_tag $self_annotate_tag

python code/self_consistent_annotation/AskGPT_trf.py \
    --dataname $dataname \
    --datamode $datamode \
    --demo_datamode $demo_datamode \
    --model $MODEL \
    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
    --demo_select_method $demo_select_method \
    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
    --few_shot_number $FEW_SHOT_NUMBER \
    --start_time $START_TIME \
    --self_annotate_tag $self_annotate_tag
