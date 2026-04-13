# Pahinga’t Gawa: Productivity App 🥔⏲️

## Project Description
The *Pahinga’t Gawa: Productivity App* is a simple yet effective time management tool inspired by and using the Pomodoro Technique.
It helps users stay focused by dividing work into manageable intervals, followed by short breaks.
This project includes:
- Customizable timer
- Built-in task list

## How to Run the Program
1. Make sure Python is installed on your computer.
2. If it is not yet installed, download and install it from the official Python website.
3. Go to the GitHub page and download the timer.py file to your computer.
4. Open command prompt. In Windows, win + R, and type type cmd and press Enter.
5. Navigate to the folder where timer.py is saved.
6. Use the cd command. For example: 
cd Downloads
or any place you placed the file
7. Run the Python Script. To run, type "python timer.py". If the command does not work, type "python3 timer.py"
8. If you get an error like “python is not recognized”
It means Python isn’t added to your system PATH. You’ll need to reinstall Python and make sure to check “Add Python to PATH” during installation.

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

### Integrated Task List:
* A built-in task area where users can:
  * Add, edit, or remove tasks.
  * Check off completed tasks during or after sessions.
* Task list remains visible while the timer is running.

## Example Output 
**Task List:**
- [x] Finish homework
- [x] Review notes
- [ ] Read chapter 34–64

**Enter work duration:** 25 minutes
**Enter break duration:** 5 minutes

Starting **#1 Work Session** (25 min)...  
Time Remaining: 24:59 ...  
Start | Pause | Skip | Reset

Work done!

Starting **#1 Rest Session** (5 min)...  
Time Remaining: 04:59  
Start | Pause | Skip | Reset

Break done!  

_If there is an error, it will display:_
> Whoops! The Rest Timer is greater than the Work Timer! Please try again.

## Contributors
* Febby Cadalso (Initial Draft, Flowchart)
* Christian Bagaindoc (Initial Draft, GitHub)





