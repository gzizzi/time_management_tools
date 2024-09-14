#! /usr/bin/env python3

#
# timer.py: a simple timer for work and study (and the necessary rest)
#

#
# to do:
#
# - put in a git repo (time_manage_tools, together with some future org mode setting or elisp package)
# - implement a pomodoro timer (now it is a separate script, maybe merge the two) --pomodoro work_time rest_time
# - use a tasklist (--todo option, to extract and process FOCUS@T@task lines)
# - --only for the current use
#

# Ctrl-z to pause the timer
# then fg to resume it

import time
import argparse
import sys

def countdown_timer(task, time_limit):
    """Countdown timer that prints the remaining time for the task."""
    total_seconds = time_limit * 60  # Convert minutes to seconds
    Time_expired = False

    if total_seconds > 0 : 
        try:
            while total_seconds:
                mins, secs = divmod(total_seconds, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(f"\r{task}: {timer}", end="")
                time.sleep(1)
                total_seconds -= 1

            print(f"\nTime's up for the task: {task}!")
            Time_expired = True

            while True:
                total_seconds += 1
                mins, secs = divmod(total_seconds, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(f"\r{task}: delay {timer}", end="")
                time.sleep(1)

        except KeyboardInterrupt:
            if Time_expired: 
                total_time_spent = time_limit * 60 + total_seconds
            else:
                total_time_spent = time_limit * 60 - total_seconds

            mins, secs = divmod(total_time_spent, 60)
            timer_time_spent = '{:02d}:{:02d}'.format(mins, secs)
            print(f"\nTimer interrupted! Task '{task}' was stopped. Total time spent '{timer_time_spent}'")
            # print(f"Total time spent '{timer_time_spent}'")
            
    elif total_seconds == 0 :
        try:
            while True:
                    total_seconds += 1
                    mins, secs = divmod(total_seconds, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(f"\rtime spent on {task}: {timer}", end="")
                    time.sleep(1)

        except KeyboardInterrupt:
            print(f"\nTimer interrupted! Task '{task}' was stopped. Total time spent '{timer}'")
            # print(f"Total time spent '{timer}'")
    else :
        print(f"Error! Negative time? Are you joking?")
        
def main():
    parser = argparse.ArgumentParser(description="A CLI Timer for tasks.")
    
    # Add arguments for the task and time limit
    parser.add_argument("task", type=str, help="The task you want to time.")
    # nargs='?' is necessary for default=0
    parser.add_argument("time_limit", nargs='?', default=0, type=int, help="The time limit for the task in minutes.")
    
    args = parser.parse_args()
    
    # Start the countdown/timer
    countdown_timer(args.task, args.time_limit)

if __name__ == "__main__":
    main()
