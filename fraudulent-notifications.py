from statistics import median

sample_data = ([10, 20, 30, 40, 50], 3)

# TOO SLOW: need counting sort
def activity_notifications(expenditure, d):
    notifications = 0
    for index in range(d, len(expenditure)):
        prior_days = expenditure[index - d: index]
        if median(prior_days) * 2 <= expenditure[index]:
            notifications += 1
    return notifications


print(activity_notifications(sample_data[0], sample_data[1]))
