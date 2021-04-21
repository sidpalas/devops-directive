import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import time

NUM_NAMESPACES = 1
TOTAL_GOAL_PODS = 10001
GOAL_PODS = TOTAL_GOAL_PODS/NUM_NAMESPACES


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
time_elapsed_text = ax2.text(0.1, 0.25, '', fontsize=15) 
running_pods_text = ax2.text(0.1, 0.5, '', fontsize=15)
completion_estimate_text = ax2.text(0.1, 0.75, '', fontsize=15)

def animate(i):
  df = pd.read_csv('./progress.csv')
  df.columns = df.columns.str.replace(' ', '')
  df['relative-timestamp'] = df['timestamp'] - df['timestamp'].min()
  df.drop('timestamp', axis='columns', inplace=True)
  df.set_index('relative-timestamp', inplace=True)
  ax1.clear()
  ax1.plot(df)
  ax1.legend(df.columns, loc='upper left')
  ax1.set_title(f'Progress Towards 10k!')
  ax1.set_xlabel('Time Elapsed (s)')
  ax1.set_ylabel('Count')


  # Calculate estimated time
  minutes_elapsed = df.last_valid_index()/60

  current_running_pods = df['running-pods'].max()
  portion_complete = current_running_pods/GOAL_PODS

  estimated_completion_minutes = minutes_elapsed / portion_complete

  time_elapsed_str = f'Minutes elapsed: {"{0:.2f}".format(minutes_elapsed)} minutes'
  time_elapsed_text.set_text(time_elapsed_str)

  running_pods_str = f'Number of running pods: {current_running_pods}'
  running_pods_text.set_text(running_pods_str)

  completion_estimate_str = f'Estimated completion time: {"{0:.2f}".format(estimated_completion_minutes)} minutes'
  completion_estimate_text.set_text(completion_estimate_str)

ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()