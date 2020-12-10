# Read in the data with Pandas
import modin.pandas as mpd
import pandas as pd
import time


if __name__ == '__main__':
    s = time.time()

    df = pd.read_csv(
        'D:/OneDrive/Pessoal/Acadêmico/FEUP/2019-2020-PDISS_DISS/_research/Results/20200218/ImageJ/561_H2O_200ul/561_D2_H2O_200ul_Series001_RAW_ch00.csv')

    e = time.time()
    print("Pandas Loading Time = {}".format(e-s))

    # Read in the data with Modin

    s = time.time()
    df = mpd.read_csv(
        'D:/OneDrive/Pessoal/Acadêmico/FEUP/2019-2020-PDISS_DISS/_research/Results/20200218/ImageJ/561_H2O_200ul/561_D2_H2O_200ul_Series001_RAW_ch00.csv')
    e = time.time()
    print("Modin Loading Time = {}".format(e-s))
