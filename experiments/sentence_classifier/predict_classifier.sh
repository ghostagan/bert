
export BERT_BASE_DIR=/data/machenglong/experiments/data/chinese_L-12_H-768_A-12
export GLUE_DIR=/data/machenglong/experiments/data
export TRAINED_CLASSIFIER=/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/model.ckpt-6234

CUDA_VISIBLE_DEVICES=1 /data/machenglong/anaconda3/envs/tensorflow1.12/bin/python /data/machenglong/experiments/bert_pycharm/run_sentence_classifier.py \
  --task_name=sc \
  --do_predict=true \
  --data_dir=$GLUE_DIR/sc \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=128 \
  --output_dir=/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/