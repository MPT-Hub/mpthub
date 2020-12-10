import pandas as pd
import numpy as np
from timeit import default_timer as timer

print("Importing files")
app_init = timer()

file_path = "D:/OneDrive/Pessoal/Acadêmico/FEUP/2019-2020-PDISS_DISS/"
file_path += "_research/Results/20200218/ImageJ/561_Mucus_200ul/"
name_list = ["561_D2_Mucus_200ul_Series001.csv",
             "561_D2_Mucus_200ul_Series002.csv",
             "561_D2_Mucus_200ul_Series003.csv",
             "561_D2_Mucus_200ul_Series004.csv",
             "561_D2_Mucus_200ul_Series005.csv",
             "561_D2_Mucus_200ul_Series006.csv"]


full_data = pd.DataFrame()
for name in name_list:
    file_data = pd.read_csv(f"{file_path}{name}",
                            usecols=['Trajectory', 'Frame', 'x', 'y'])
    file_data.insert(0, "File", name, allow_duplicates=True)
    full_data = full_data.append(file_data)

end = timer()
print(f"Importing files took {(end - app_init):.3f} seconds\n")

print("Defining configuration")
init = timer()
frame_count = 606
frame_filter = 590
fps = 30
width_px = 512
width_si = 160
p_size = 200

# frame_count = 540
# frame_filter = 500
# fps = 25
# width_px = 512
# width_si = 128
# p_size = 100

end = timer()
print(f"Defining configuration took {(end - init):.3f} seconds\n")

print("Summarizing")
init = timer()

grouped = full_data.groupby(['File', 'Trajectory'], as_index=False).count()[
    ['File', 'Trajectory', 'Frame']]

# print("Gets trajectories per file")
trajectories_per_file = grouped.groupby(['File'], as_index=False).count()[
    ['File', 'Trajectory']]
# print(trajectories_per_file)

# print("Gets valid trajectories per file")
summary_valid = grouped[grouped['Frame'] > frame_filter].groupby(
    ['File'], as_index=False).count()[
        ['File', 'Trajectory']].rename(columns={'Trajectory': 'Valid'})
# print(summary_valid)

# print("Final trajectory table")
summary = trajectories_per_file.merge(summary_valid, how='left').fillna(0)
summary[['Trajectory', 'Valid']] = summary[['Trajectory', 'Valid']].astype(int)
# print(summary)

# print("Trajectory table with total")
summary_total = pd.DataFrame(summary.sum()).transpose()
summary_total['File'] = 'Total'
summary_total = summary.append(summary_total)
print(summary)

end = timer()
print(f"Summarizing took {(end - init):.3f} seconds\n")
# print(summary_total)

print("Grouping valid trajectories")
init = timer()

valid_per_file = grouped[grouped['Frame'] > frame_filter].groupby(
    ['File', 'Trajectory'], as_index=False).count()

valid_per_file = list(
    zip(valid_per_file['File'], valid_per_file['Trajectory']))

full_valid_data = full_data[
    [x in valid_per_file for x in list(
        zip(full_data['File'], full_data['Trajectory']))]]

time_step = 1 / fps
max_time = frame_count / fps
tau = np.linspace(time_step, max_time, frame_count)

trajectories_group = full_valid_data.groupby(
    ['File', 'Trajectory'], as_index=False)

end = timer()
print(f"Grouping valid trajectories took {(end - init):.3f} seconds\n")

print("Computing MSD")
init = timer()

i = 0
msd = pd.DataFrame()
for (file, trajectory), trajectory_data in trajectories_group:
    init_msd = timer()

    pixel_size = width_px / width_si
    frames = len(trajectory_data)
    t = tau[:frames]
    xy = trajectory_data.values

    position = pd.DataFrame({"t": t, "x": xy[:, -2], "y": xy[:, -1]})
    shifts = position["t"].index.values + 1

    msdp = np.zeros(shifts.size)
    for k, shift in enumerate(shifts):
        diffs_x = position['x'] - position['x'].shift(-shift)
        diffs_y = position['y'] - position['y'].shift(-shift)
        square_sum = np.square(diffs_x) + np.square(diffs_y)
        msdp[k] = square_sum.mean()

    msdm = msdp * (1 / (pixel_size ** 2))
    msdm = msdm[:frame_filter]
    msd[i] = msdm

    i += 1

    end_msd = timer()
    print(
        f"Computing MSD_{i:03} for {file}, {trajectory:3} took {(end_msd - init_msd):.3f} seconds")

tau = tau[:frame_filter]

msd.insert(0, "tau", tau, True)
msd = msd[msd[msd.columns[0]] < 10]

msd.name = "MSD"
msd.set_index('tau', inplace=True)
msd.index.name = f'Timescale ({chr(120591)}) (s)'
msd['mean'] = msd.mean(axis=1)

end = timer()
print(f"Computing MSD took {(end - init):.3f} seconds\n")

print(f"Full proccess took {(end - app_init):.3f} seconds\n")

print(msd.describe())
