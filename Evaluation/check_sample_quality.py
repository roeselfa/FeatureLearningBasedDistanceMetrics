import numpy as np
import pandas as pd
import sys


# returned die Ergebnisse als Liste statt sie rauszuschreiben
def check_sample_quality(input_eventlog, input_sample, delimiter):
    # print results to console as well?
    # 0 = no || 1 = yes
    also_print_to_console = 0

    # set custom na values (exludes "NA" to keep lines with Case ID "NA")
    custom_na_values = ['-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN', '#N/A', 'N/A', '#NA', 'NULL', 'NaN', '-NaN', 'nan',
                        '-nan']
    event_log = pd.read_csv(input_eventlog, delimiter=delimiter, keep_default_na=False, na_values=custom_na_values)
    sample_log = pd.read_csv(input_sample, delimiter=";", keep_default_na=False, na_values=custom_na_values)

    # reduce columns to Case IDs and Activities, group by case ID
    caseIDs = pd.Series(event_log['Case ID'].unique())
    activities = pd.Series(event_log['Activity'].unique())
    act_list = activities.tolist()
    col_list = ['Case ID', 'Activity']
    small_event_log = event_log[col_list]
    small_sample = sample_log[col_list]

    ##directly follows matrices
    ##count total occurrences of behaviours
    elog_matrix = np.zeros((activities.size, activities.size), dtype=np.int)
    sample_matrix = np.zeros((activities.size, activities.size), dtype=np.int)

    traces_elog = 0
    traces_sample = 0
    last_caseID = ""
    last_activity = ""

    # parsing original event log
    for index, row in small_event_log.iterrows():
        current_caseID = row['Case ID']
        current_activity = row['Activity']

        if last_caseID == current_caseID:
            index_a = act_list.index(last_activity)
            index_b = act_list.index(current_activity)
            elog_matrix[index_a][index_b] = elog_matrix[index_a][index_b] + 1
            last_activity = current_activity

        else:
            traces_elog = traces_elog + 1
            last_caseID = current_caseID
            last_activity = current_activity

    # parsing sample event log
    last_caseID = ""
    last_activity = ""

    for index, row in small_sample.iterrows():
        current_caseID = row['Case ID']
        current_activity = row['Activity']

        if last_caseID == current_caseID:
            index_a = act_list.index(last_activity)
            index_b = act_list.index(current_activity)
            sample_matrix[index_a][index_b] = sample_matrix[index_a][index_b] + 1
            last_activity = current_activity

        else:
            traces_sample = traces_sample + 1
            last_caseID = current_caseID
            last_activity = current_activity

    expected_sample_ratio = traces_sample / traces_elog
    #num_of_behaviours_elog = np.sum(elog_matrix)
    #num_of_behaviours_sample = np.sum(sample_matrix)

    ##unsampled behaviours
    unique_behaviours_elog = np.count_nonzero(elog_matrix)
    unique_behaviours_sample = np.count_nonzero(sample_matrix)
    unsampled = (unique_behaviours_elog - unique_behaviours_sample) / unique_behaviours_elog * 100

    # create sample ratio matrix, non-behaviours are NaN
    sample_ratio_matrix = np.zeros((activities.size, activities.size), dtype=np.float64)
    for x in range(0, activities.size):
        for y in range(0, activities.size):
            if elog_matrix[x, y] != 0:
                sample_ratio_matrix[x, y] = sample_matrix[x, y] / elog_matrix[x, y]
            else:
                sample_ratio_matrix[x, y] = np.nan

    # calculating mu and sigma
    mean = np.nanmean(sample_ratio_matrix, dtype=np.float64)
    std_dev = np.nanstd(sample_ratio_matrix, dtype=np.float64)

    # count total number of over- under- un- and truly sampled behaviours
    count_truly_sampled = 0
    # count_under_sampled = 0
    # count_over_sampled = 0

    for x in range(0, activities.size):
        for y in range(0, activities.size):
            if elog_matrix[x, y] != 0:
                # if sample_ratio_matrix[x,y] < expected_sample_ratio - std_dev or sample_ratio_matrix[x,y]== 0:
                # count_under_sampled = count_under_sampled +1
                # if sample_ratio_matrix[x,y] > expected_sample_ratio + std_dev:
                # count_over_sampled = count_over_sampled +1
                if expected_sample_ratio - std_dev <= sample_ratio_matrix[x, y] <= expected_sample_ratio + std_dev and \
                        sample_ratio_matrix[x, y] != 0:
                    count_truly_sampled = count_truly_sampled + 1

    truly_sampled_percent = count_truly_sampled / unique_behaviours_elog * 100
    # under_sampled_percent = count_under_sampled / unique_behaviours_elog * 100
    # over_sampled_percent = count_over_sampled / unique_behaviours_elog * 100

    ##print to console
    if also_print_to_console == 1:
        print("\n")
        print(input_eventlog, "          |", input_sample)
        print("-----------------------------")
        print("expec. sample ratio  : %1.2f" % (expected_sample_ratio))
        print("mean sample ratio    : %1.2f" % (mean))
        print("std deviation        : %1.2f" % (std_dev))

        print("truly sampled        : %2d" % (truly_sampled_percent), "%")
        # print("Oversampled          : %2d" %(over_sampled_percent),"%")
        # print("Undersampled         : %2d" %(under_sampled_percent),"%")
        print("Unsampled            : %2d" % (unsampled), "%")

    ##output the results to a list
    # am besten erst Tupel der Werte und ihrer Bezeichner erstellen und diese Tupel dann in eine Liste hängen
    output = truly_sampled_percent
    # output.append(("expec. sample ratio", expected_sample_ratio))
    # output.append(("mean sample ratio", mean))
    # output.append(("std deviation", std_dev))
    # output.append(("Oversampled", over_sampled_percent))
    # output.append(("Undersampled", under_sampled_percent))
    # output.append(("Unsampled", unsampled))
    print(input_sample)
    return output


"""
	out_file = open(output_results, 'w+')
	print(input_eventlog,"          |",input_sample,file=out_file)
	print("-----------------------------",file=out_file)
	print("expec. sample ratio  : %1.2f" %(expected_sample_ratio),file=out_file)
	print("mean sample ratio    : %1.2f"%(mean),file=out_file)
	print("std deviation        : %1.2f" %(std_dev),file=out_file)

	print("truly sampled        : %2d" %(truly_sampled_percent),"%",file=out_file)
	print("Oversampled          : %2d" %(over_sampled_percent),"%",file=out_file)
	print("Undersampled         : %2d" %(under_sampled_percent),"%",file=out_file)
	print("Unsampled            : %2d" %(unsampled),"%",file=out_file)
	out_file.close()
	
	"""
