
export BERT_BASE_DIR=/data/machenglong/experiments/data/chinese_L-12_H-768_A-12
export GLUE_DIR=/data/machenglong/experiments/data

CUDA_VISIBLE_DEVICES=1 /data/machenglong/anaconda3/envs/tensorflow1.12/bin/python /data/machenglong/experiments/bert_pycharm/run_sentence_classifier.py \
  --task_name=sc \
  --do_train=true \
  --do_eval=true \
  --data_dir=$GLUE_DIR/sc \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=1.0 \
  --output_dir=/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/