#coding:utf8
import codecs
import numpy as np


def compare_predict_golden():
    predict_file = '/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/test_results.tsv'
    golden_file = '/data/machenglong/experiments/data/sc/test.tsv'
    lables_file = '/data/machenglong/experiments/data/sc/labels.tsv'

    label_index = []
    with codecs.open(lables_file, 'r', 'utf8') as lables_file:
        for eachline in lables_file:
            eachline = eachline.strip()
            label_index.append(eachline)

    golden_example_list = []
    with codecs.open(golden_file, 'r', 'utf8') as golden_file:
        for eachline in golden_file:
            eachline = eachline.strip()
            golden_example_list.append(eachline.split('\t'))

    print('line\tpredict_label\tpredict_probability'.format())
    with codecs.open(predict_file, 'r', 'utf8') as predict_file:
        line_index = 0
        for eachline in predict_file:
            eachline = eachline.strip()
            items = eachline.split('\t')
            array = np.asarray(items, dtype=float)
            predict_lable = label_index[np.argmax(array)]
            predict_probability = array[np.argmax(array)]

            if predict_lable != golden_example_list[line_index][2] or (predict_lable == golden_example_list[line_index][2] and predict_probability < 0.9):
                print('{}\t{}\t{}'.format(golden_example_list[line_index], predict_lable, predict_probability))
            line_index = line_index + 1


if __name__ == '__main__':
    compare_predict_golden()