#coding:utf8
import codecs
import numpy as np
from sklearn.metrics import f1_score


def compare_predict_golden():
    predict_file = '/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/test_results.tsv'
    golden_file  = '/data/machenglong/experiments/data/sc/test.tsv'
    lables_file  = '/data/machenglong/experiments/data/sc/labels.tsv'
    result_file  = '/data/machenglong/experiments/bert_pycharm/experiments/sentence_classifier/output/result_analysis.tsv'

    label_index = []
    y_true = []
    y_pred = []
    with codecs.open(lables_file, 'r', 'utf8') as lables_file:
        for eachline in lables_file:
            eachline = eachline.strip()
            label_index.append(eachline)

    golden_example_list = []
    with codecs.open(golden_file, 'r', 'utf8') as golden_file:
        for eachline in golden_file:
            eachline = eachline.strip()
            golden_example_list.append(eachline.split('\t'))
            y_true.append(eachline.split('\t')[-1])

    with codecs.open(result_file, 'w', 'utf8') as output_file:

        print('line\tpredict_label\tpredict_probability'.format())
        output_file.write('line\tpredict_label\tpredict_probability\n')
        with codecs.open(predict_file, 'r', 'utf8') as predict_file:
            line_index = 0
            for eachline in predict_file:
                eachline = eachline.strip()
                items = eachline.split('\t')
                array = np.asarray(items, dtype=float)
                predict_lable = label_index[np.argmax(array)]
                y_pred.append(predict_lable)
                predict_probability = array[np.argmax(array)]

                if predict_lable != golden_example_list[line_index][2] or (predict_lable == golden_example_list[line_index][2] and predict_probability < 0.9):
                    print('{}\t{}\t{}'.format(golden_example_list[line_index], predict_lable, predict_probability))
                    output_file.write('{}\t{}\t{}\n'.format(golden_example_list[line_index], predict_lable, predict_probability))
                line_index = line_index + 1

        print('labels: {}'.format(label_index))
        output_file.write('labels: {}\n'.format(label_index))
        print('F1: {}'.format(f1_score(y_true, y_pred, labels=label_index, average=None)))
        output_file.write('F1: {}\n'.format(f1_score(y_true, y_pred, labels=label_index, average=None)))


if __name__ == '__main__':
    compare_predict_golden()
