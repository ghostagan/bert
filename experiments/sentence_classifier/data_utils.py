#coding:utf8

import xlrd, xlwt
import codecs
import csv

excel_file = 'D:/temp/desktop/nlu_data_part2_fin_review(2).xls'
txt_file = 'D:/temp/desktop/nlu_data_part2_fin.txt'

def read_excel():
    file_out = codecs.open(txt_file, 'w', 'utf8')
    excel = xlrd.open_workbook(filename=excel_file)#打开文件

    label_txt_statistics = dict()

    for sheet_index in range(7):
        sheet_name = 'data{}'.format(sheet_index)
        index = 2
        sheet = excel.sheet_by_name(sheet_name)
        for row_index in range(sheet.nrows):
            text = sheet.cell_value(row_index, 0)
            if text == u'文本':
                continue
            label = sheet.cell_value(row_index, 1)
            if len(label) == 0 or label == 'x' or label == 'y' or label == 'z':
                label = 'other'
            file_out.write('{}_{}\t{}\t{}\n'.format(sheet_name, index, text, label))
            index = index + 1
            if label_txt_statistics.__contains__(label):
                label_txt_statistics[label] = label_txt_statistics[label] + 1
            else:
                label_txt_statistics[label] = 1

    print('{}'.format(label_txt_statistics))

    # sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    # sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    # print(sheet1,sheet2)
    # print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #
    # rows = sheet1.row_values(2)#获取行内容
    # cols = sheet1.col_values(3)#获取列内容
    # print(rows)
    # print(cols)
    #
    # print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)


def cola():
    tsv_array = ['D:/temp/desktop/glue_data/CoLA/train.tsv', 'D:/temp/desktop/glue_data/CoLA/dev.tsv', 'D:/temp/desktop/glue_data/CoLA/test.tsv']

    file_out = codecs.open('D:/temp/desktop/glue_data/sc/test.tsv', 'w', 'utf8')
    reader = csv.reader(codecs.open('D:/temp/desktop/glue_data/CoLA/test.tsv', 'r', 'utf8'), delimiter="\t", quotechar=None)
    for line in reader:
        print(line)
        # file_out.write(line[0] + '\t' + line[3] + '\t' + line[1] + '\n')
        file_out.write(line[0] + '\t' + line[1] + '\t' + line[0] + '\n')


def extract_news_data_by_corpus():
    intentions = ['query_news', 'close_news', 'open_news', 'pause_news', 'continue_news']
    entities = ['channel', 'date', 'area', 'keyword']

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')

    worksheet.write(0, 0, 'text')
    worksheet.write(0, 1, 'intention')
    worksheet.write(0, 2, 'channel')
    worksheet.write(0, 3, 'date')
    worksheet.write(0, 4, 'area')
    worksheet.write(0, 5, 'keyword')

    excel_in = xlrd.open_workbook(filename=excel_file)  # 打开文件
    index = 1
    for sheet_index in range(7):
        sheet_name = 'data{}'.format(sheet_index)
        sheet = excel_in.sheet_by_name(sheet_name)
        for row_index in range(sheet.nrows):
            text = sheet.cell_value(row_index, 0)
            if text == u'文本':
                continue
            label = sheet.cell_value(row_index, 1)
            if label in intentions:
                worksheet.write(index, 0, text)
                worksheet.write(index, 1, label)
                index = index + 1

    workbook.save('D:/temp/desktop/news.xls')


def extract_stock_data_by_corpus():
    intentions = ['query_stock', 'query_stockmarket']
    entities = ['stock_name', 'date']

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')

    worksheet.write(0, 0, 'text')
    worksheet.write(0, 1, 'intention')
    for i in range(len(entities)):
        worksheet.write(0, i+2, entities[i])

    excel_in = xlrd.open_workbook(filename=excel_file)  # 打开文件
    index = 1
    for sheet_index in range(7):
        sheet_name = 'data{}'.format(sheet_index)
        sheet = excel_in.sheet_by_name(sheet_name)
        for row_index in range(sheet.nrows):
            text = sheet.cell_value(row_index, 0)
            if text == u'文本':
                continue
            label = sheet.cell_value(row_index, 1)
            if label in intentions:
                worksheet.write(index, 0, text)
                worksheet.write(index, 1, label)
                index = index + 1

    workbook.save('D:/temp/desktop/stock.xls')


if __name__ == '__main__':
    # read_excel()
    # extract_news_data_by_corpus()
    extract_stock_data_by_corpus()