!pip install transformers==3.0.0 nlp==0.2.0
!git clone https://github.com/patil-suraj/question_generation.git

%cd question_generation

!python prepare_data.py \
    --task qg \
    --model_type t5 \
    --dataset_path data/squad_multitask/ \
    --qg_format highlight_qg_format \
    --max_source_length 512 \
    --max_target_length 32 \
    --train_file_name train_data_qg_hl_t5.pt \
    --valid_file_name valid_data_qg_hl_t5.pt \
