import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


fname = '../NGSIM-Data/NGSIM-Data/trajectories-0400pm-0415pm_editted.csv'

input_zones = [102, 101, 123, 103, 106, 112]

side_inputs = [112, 106, 103]
front_input = [101]
turn_front_inputs = [123, 102]

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
    print(np.mean(totals))
    print(np.std(totals))
    plt.hist(totals, bins=bins)


def inter_arrival_time(orgs, metric='Epoch_ms', bins=None):
    iats = []

    for org in orgs:
        df_iso = df_unq[df_unq['Org_Zone'] == org]

        for i in range(len(df_iso[metric].values[1:]) - 1):
            iat = max(1, df_iso[metric].values[i+1] - df_iso[metric].values[i]) / 1000
            iats.append(iat)
    iats = np.array(iats)
    # print(np.mean(iats))

    loc, scale = scipy.stats.expon.fit(iats, floc=0)
    print("Beta", scale)

    plt.subplot(131)
    plt.title("Actual Distribution")
    plt.hist(iats, bins=bins)

    plt.subplot(132)
    plt.title("Fitted Exponential Distribution (PDF)")
    x = np.linspace(scipy.stats.expon.ppf(0.001, scale=scale), scipy.stats.expon.ppf(0.9999, scale=scale), 100)
    plt.plot(x, scipy.stats.expon.pdf(x, scale=scale), 'r-', lw=3, alpha=0.6)

    plt.subplot(133)
    plt.title("Sampling from Fitted Distribution")
    r = np.random.exponential(scale, 1000)
    plt.hist(r, bins=bins)


def average_speed():
    df_trim = pandas.DataFrame(df, columns=['Veh_Velocity'])
    print(np.mean(df_trim.values))


def destinations(org):
    df_iso = df_unq[df_unq['Org_Zone'] == org]
    df_rel = df_iso[df_iso['Dest_Zone'].isin(output_zones)]

    bins = {
        215: 1,
        214: 1,
        213: 1,
        212: 1,
        206: 1,
        221: 1,
        222: 1,
        203: 1
    }

    count = 8

    for dp in df_rel['Dest_Zone'].values:
        bins[dp] += 1
        count += 1

    for key in bins.keys():
        bins[key] /= count

    keys = []
    probs = []

    for key, val in bins.items():
        keys.append(key)
        probs.append(val)

    print(keys, probs)


def main():
    # average_speed()

    # for i in range(1, 9):
    #     plt.subplot(2, 3, i)
    #     plt.title(input_zones[i-1])
    #     inter_arrival_time([input_zones[i-1]])
    # plt.show()

    # plt.title('Input Distribution')
    # inter_arrival_time(front_input, bins=50)
    # plt.show()
    #
    # plt.title('Input Distribution')
    # inter_arrival_time(side_inputs, bins=50)
    # plt.show()
    #
    # plt.title('Input Distribution')
    # inter_arrival_time(turn_front_inputs, bins=50)
    # plt.show()

    # plt.title('Time to Destination')
    # total_time(bins=22)
    # plt.show()

    # for org in input_zones:
    #     print(org, end='\t')
    #     destinations(org)

    pass

if __name__ == '__main__':
    main()
