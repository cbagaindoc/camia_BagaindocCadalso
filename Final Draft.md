# Pahinga’t Gawa: Productivity App 🥔⏲️

## Problem Statement:
In our daily lives, it’s common to feel overwhelmed by the number of tasks we need to accomplish. This sense of overload often leads to procrastination or distraction, decreasing overall productivity. Many people avoid starting tasks because they seem too time-consuming or stressful. [^1] 

To address this issue, we aim to develop a solution based on the Pomodoro Technique, a proven time management method developed by Francesco Cirillo that helps users stay focused and reduce burnout. [^2]

## Project Objectives:
Our project’s main goal is to help users increase productivity and manage time more effectively. 
Through **Pahinga’t Gawa** application, we aim to:
* Build a simple, user-friendly productivity app in Python within the project deadline.
* Help users break tasks into manageable work/rest intervals to reduce overload.
* Provide a clear, strict countdown timer to improve focus and time-awareness.
* Include an organized task list to help users track and prioritize their work.

## Planned Features:
### Customizable Pomodoro Timer:
* Users can set their own work and break durations.
* The timer automatically cycles between:
  * A Work Session (e.g., 25 minutes)
  * A Break Session (e.g., 5 minutes)
  * Break Session must always be shorter than Work Session.
* User can also:
  * Pause & Unpause the timer
  * Skip timer sessions
  * Reset timer 
### Integrated Task List: 
* A built-in task area where users can:
  * Add, edit, or remove tasks.
  * Check off completed tasks during or after sessions.
* Task list remains visible while the timer is running.

 ## Flowchart / Pseudocode:
For our base flowchart, please see our [Process Flow Diagram](https://github.com/cbagaindoc/camia_BagaindocCadalso/blob/main/Process%20Flow%20Diagram%20(PFD).md) in our repository on GitHub


## Planned Inputs and Outputs
### Input Type
| Feature              | Description                                 | User Input Method                       |
|----------------------|---------------------------------------------|-------------------------------------------|
| Start / Pause / Stop | User can start, pause, and stop the timer   | Button clicks, keyboard shortcuts         |
| Skip Command         | User can skip the current timer session early | Button clicks, keyboard shortcuts       |
| Length of the Timer  | User sets duration for work & rest intervals | User-entered values, settings adjustment |
| To-Do List           | User manages a checklist of tasks           | Typing to add tasks, edit/delete actions  |
| Priority List        | User sets work priorities.                   | Typing to add a priority level |
| Settings             | A configuration option that allows users to configure the time intervals and color for the priority list        | Configuring in settings                      |



### Output Type
| Feature                   | Description                                                    | Output Type                |
|---------------------------|----------------------------------------------------------------|-----------------------------|
| Countdown Timer Display   | Remaining time for current session (Work or Rest)             | On-screen digital timer (e.g., MM:SS) |
| Session Classification        | Current session count (e.g., “Work Session”)                     | On-screen text              |
| To-do list                | To-do list (e.g., • Read ch. 67)                               | On-screen text              |
| Buzzer Alarm              | Will sound an alarm if rest/work timer reaches 00:00           | Sound                       |
| Settings             | A configuration option       | On-screen                       |
[^1]: Lillis, C. (2025, April 24). [What is task paralysis?](https://www.medicalnewstoday.com/articles/task-paralysis#:~:text=Task%20paralysis%20is%20when%20someone,rapid%20changes%20in%20mood)
[^2]: Cirillo, Francesco, [The Pomodoro Technique](https://web.archive.org/web/20230331051358/https://francescocirillo.com/products/the-pomodoro-technique), archived from [the original](https://francescocirillo.com/products/the-pomodoro-technique) on 31 March 2023
