MODEL=gpt-3.5-turbo-0125

dataname=wnut17
datamode=test

FEW_SHOT_SETTING=pool
DEMO_RETRIEVAL_METHOD=GPTEmbDvrsKNN
diverseKNN_sampling=Sc
diverseKNN_number=50
self_annotate_tag=std_c5
demo_datamode=train
FEW_SHOT_NUMBER=20
START_TIME="TIME_STAMP"

# # ----- two-stage majority voting
demo_select_method=std_c5
DEMO_SIZE=500
#python code/self_consistent_annotation/GeneratePrompts_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/AskGPT_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --demo_datamode $demo_datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/ComputeMetric_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/GeneratePrompts_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/AskGPT_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --demo_datamode $demo_datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/ComputeMetric_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/GeneratePrompts_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/AskGPT_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --demo_datamode $demo_datamode \
#    --model $MODEL \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag
#
#python code/self_consistent_annotation/ComputeMetric_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag

#python code/self_consistent_annotation/ComputeMetric_multi-stages_trf.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag \
#    --compute_self_consistency_threshold 4

for ((i = 1; i < 10; i++)); do
python code/self_consistent_annotation/ComputeMetric_multi-stages_trf-all.py \
    --dataname $dataname \
    --datamode $datamode \
    --model $MODEL \
    --demo_datamode $demo_datamode \
    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
    --demo_select_method $demo_select_method \
    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
    --few_shot_number $FEW_SHOT_NUMBER \
    --start_time $START_TIME \
    --self_annotate_tag $self_annotate_tag \
    --compute_self_consistency_threshold $i
done

#for ((i = 1; i < 9; i++)); do
#python code/self_consistent_annotation/ComputeMetric_multi-stages.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag \
#    --compute_self_consistency_threshold $i \
##    --ES 1
#done

#python code/self_consistent_annotation/ComputeMetric.py \
#    --dataname $dataname \
#    --datamode $datamode \
#    --model $MODEL \
#    --demo_datamode $demo_datamode \
#    --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#    --demo_select_method $demo_select_method \
#    --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#    --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#    --few_shot_number $FEW_SHOT_NUMBER \
#    --start_time $START_TIME \
#    --self_annotate_tag $self_annotate_tag \
#    --compute_self_consistency_threshold 1

# -----------------------------------------------------------
# # # ----- entity-level threshold filtering
# demo_select_method=std_c5_th_ent_4.0
# DEMO_SIZE=500
# python code/self_consistent_annotation/GeneratePrompts.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --model $MODEL \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --self_annotate_tag $self_annotate_tag

# python code/self_consistent_annotation/AskGPT.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --demo_datamode $demo_datamode \
#     --model $MODEL \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --start_time $START_TIME \
#     --self_annotate_tag $self_annotate_tag

# python code/self_consistent_annotation/ComputeMetric.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --model $MODEL \
#     --demo_datamode $demo_datamode \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --start_time $START_TIME \
#     --self_annotate_tag $self_annotate_tag


# -----------------------------------------------------------
# # ----- sample-level threshold filtering
# demo_select_method=std_c5_all_th_spl_4.0
# DEMO_SIZE=296
# python code/self_consistent_annotation/GeneratePrompts.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --model $MODEL \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE --demo_datamode $demo_datamode \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --self_annotate_tag $self_annotate_tag

# python code/self_consistent_annotation/AskGPT.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --demo_datamode $demo_datamode \
#     --model $MODEL \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --start_time $START_TIME \
#     --self_annotate_tag $self_annotate_tag

# python code/self_consistent_annotation/ComputeMetric.py \
#     --dataname $dataname \
#     --datamode $datamode \
#     --model $MODEL \
#     --demo_datamode $demo_datamode \
#     --few_shot_setting $FEW_SHOT_SETTING --demo_size $DEMO_SIZE \
#     --demo_select_method $demo_select_method \
#     --demo_retrieval_method $DEMO_RETRIEVAL_METHOD \
#     --diverseKNN_number $diverseKNN_number --diverseKNN_sampling $diverseKNN_sampling \
#     --few_shot_number $FEW_SHOT_NUMBER \
#     --start_time $START_TIME \
#     --self_annotate_tag $self_annotate_tag
