import streamlit as st
import time
import datetime
import calendar
import matplotlib.pyplot as plt

st.set_page_config()

st.title('Ela stize u Hrvatsku za:')
st.balloons()


import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def main():
    dates, data = generate_data()
    fig, ax = plt.subplots(figsize=(6, 10))
    calendar_heatmap(ax, dates, data)
    st.pyplot(fig)

def generate_data():
    
    start = dt.datetime(2022, 6, 14, 8, 30, 0)
    difference =  dt.datetime(2022, 7, 27, 8, 30, 0) - start
    num = difference.days
    present = dt.datetime.now()
    done = present-start
    togo=num-done.days
    data = np.concatenate((np.ones(done.days),np.zeros(togo)),axis=None)
    dates = [start + dt.timedelta(days=i) for i in range(difference.days)]
    return dates, data

def calendar_array(dates, data):
    i, j = zip(*[d.isocalendar()[1:] for d in dates])
    i = np.array(i) - min(i)
    j = np.array(j) - 1
    ni = max(i) + 1

    calendar = np.nan * np.zeros((ni, 7))
    calendar[i, j] = data
    return i, j, calendar


def calendar_heatmap(ax, dates, data):
    i, j, calendar = calendar_array(dates, data)
    im = ax.imshow(calendar, interpolation='none', cmap='RdYlGn')
    label_days(ax, dates, i, j, calendar)
    label_months(ax, dates, i, j, calendar)

def label_days(ax, dates, i, j, calendar):
    ni, nj = calendar.shape
    day_of_month = np.nan * np.zeros((ni, 7))
    day_of_month[i, j] = [d.day for d in dates]

    for (i, j), day in np.ndenumerate(day_of_month):
        if np.isfinite(day):
            ax.text(j, i, int(day), ha='center', va='center')

    ax.set(xticks=np.arange(7), 
           xticklabels=['Pon', 'Uto', 'Sri', 'Cet', 'Pet', 'Sub', 'Ned'])
    ax.xaxis.tick_top()

def label_months(ax, dates, i, j, calendar):
    month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Lipanj', 'Srpanj',
                             'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    months = np.array([d.month for d in dates])
    uniq_months = sorted(set(months))
    yticks = [i[months == m].mean() for m in uniq_months]
    labels = [month_labels[m - 1] for m in uniq_months]
    ax.set(yticks=yticks)
    ax.set_yticklabels(labels, rotation=90)

main()

ph = st.empty()
N = 10000000000000000000
# for secs in range(N,0,-1):
#     mm, ss = secs//60, secs%60
#     ph.metric("", f"{mm:02d}:{ss:02d}")
#     time.sleep(1)

for secs in range(N,0,-1):
    present = datetime.datetime.now()
    future = datetime.datetime(2022, 7, 27, 8, 30, 0)
    difference = future - present
    count_hours, rem = divmod(difference.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    mm, ss = secs//60, secs%60
    ph.metric("", f"""  {difference.days:02d} dan      &       
                        {count_hours:02d}:{count_minutes:02d}:{count_seconds:02d}""")
    time.sleep(1)