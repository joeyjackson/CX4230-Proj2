import pandas
import matplotlib.pyplot as plt
import numpy as np


fname = '../NGSIM-Data/NGSIM-Data/trajectories-0400pm-0415pm_editted.csv'

input_zones = [102, 101, 123, 103, 106, 112]
output_zones = [215, 214, 213, 212, 206, 221, 222, 203]

columns = ['Vehicle_ID', 'Lane_ID', 'Epoch_ms', 'Org_Zone', 'Dest_Zone']

df = pandas.read_csv(fname)
df_trim = pandas.DataFrame(df, columns=columns)
df_unq = df_trim.drop_duplicates(subset='Vehicle_ID', keep='first')


def total_time(bins=None):
    df_rel = df_trim[
        df_trim['Org_Zone'].isin([101, 102, 123]) &
        df_trim['Dest_Zone'].isin([213, 214, 215])
    ]

    df_first = df_rel.drop_duplicates(subset='Vehicle_ID', keep='first')
    df_last = df_rel.drop_duplicates(subset='Vehicle_ID', keep='last')

    df_start = pandas.DataFrame(df_first, columns=['Vehicle_ID', 'Epoch_ms'])
    df_start.rename(columns={'Epoch_ms': 'start'}, inplace=True)
    df_end = pandas.DataFrame(df_last, columns=['Vehicle_ID', 'Epoch_ms'])
    df_end.rename(columns={'Epoch_ms': 'end'}, inplace=True)
    df_both = df_start.merge(df_end)
    totals = (df_both['end'] - df_both['start']) / 1000
    plt.hist(totals, bins=bins)


def inter_arrival_time(orgs, metric='Epoch_ms', bins=None):
    iats = []

    for org in orgs:
        df_iso = df_unq[df_unq['Org_Zone'] == org]

        for i in range(len(df_iso[metric].values[1:]) - 1):
            iat = max(1, df_iso[metric].values[i+1] - df_iso[metric].values[i]) / 1000
            iats.append(iat)
    iats = np.array(iats)
    # print(iats)
    print(np.mean(iats))
    plt.hist(iats, bins=bins)


def average_speed():
    df_trim = pandas.DataFrame(df, columns=['Veh_Velocity'])
    print(np.mean(df_trim.values))


def main():

    # average_speed()

    # plt.title('Time to Destination')
    # total_time(bins=22)
    # plt.show()

    # for i in range(1, 7):
    #     plt.subplot(2, 3, i)
    #     plt.title(input_zones[i-1])
    #     inter_arrival_time([input_zones[i-1]])
    # plt.show()

    # plt.title('Input Distribution')
    # inter_arrival_time(input_zones, bins=50)
    # plt.show()

    pass

if __name__ == '__main__':
    main()
