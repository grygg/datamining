import pandas as pd
import numpy as np
import scipy.stats as stats
import pylab
import matplotlib.pyplot as plt


def string2num():
    f1 = open('./data/horse-colic.data.txt', 'r')
    f2 = open('./data/train.txt', 'w')
    s = f1.read()
    s = s.replace('?', '-100')
    f2.write(s)



if __name__ == '__main__':
    # loading data
    # string2num()
    # df = pd.read_csv('./data/train.txt', sep=' ')
    npdata = np.loadtxt('./data/train.txt')
    df = pd.DataFrame(npdata)

    attrname = ['surgery', 'Age', 'Hospital_Number', 'rectal_temperature', 'pulse', 'respiratory_rate',
                'temperature_of_extremities', 'peripheral_pulse', 'mucous_membranes', 'capillary_refill_time', 'pain',
                'peristalsis', 'abdominal_distension', 'nasogastric_tube', 'nasogastric_reflux',
                'nasogastric_reflux_PH', 'rectal_examination', 'abdomen', 'packed_cell_volume', 'total_protein',
                'abdominocentesis_appearance', 'abdomcentesis_total_protein', 'outcome', 'surgical_lesion', '#1_lesion',
                '#2_lesion', '#3_lesion', 'cp_data']
    labelattr = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 21, 23, 24, 25, 26, 27, 28]
    valueattr = [4, 5, 6, 16, 19, 20, 22]
    # print(df)
    # for attrid in labelattr:
    #     print(df[attrid-1].value_counts())
    #     print()

    # for attrid in valueattr:
    #     print(attrname[attrid - 1])
    #     series = df[attrid - 1].apply(pd.to_numeric, errors='coerce')
    #     series = series[series.notnull()]
    #     print('min:', series.min())
    #     print('1/4 quantile:', series.quantile(0.25))
    #     print('mean:', series.mean())
    #     print('median:', series.median())
    #     print('3/4 quantile:', series.quantile(0.75))
    #     print('max:', series.max())
    #     print()

    for attrid in valueattr:
        print(attrname[attrid - 1])
        x = npdata[attrid - 1]
        print(x)
        bins = np.arange(-100, 100, 5)
        plt.hist(x, bins = bins, alpha=0.5)
        plt.xlabel(attrname[attrid - 1])
        plt.ylabel('value')
        plt.title('Histogram')
        plt.grid(True)
        plt.show()

    for attrid in valueattr:
        print(attrname[attrid - 1])
        series = df[attrname[attrid - 1]]
        series = series[series != '?'].apply(pd.to_numeric, errors='coerce')
        _ = stats.probplot(series, dist="norm", plot=pylab)

    for attrid in valueattr:
        print(attrname[attrid - 1])
        series = df[attrname[attrid - 1]]
        series = series[series != '?'].apply(pd.to_numeric, errors='coerce')
        _ = pd.DataFrame(series).boxplot()









