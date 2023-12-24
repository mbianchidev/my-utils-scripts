import time
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(f'Time left: {timer}', end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    while True:
        clear_screen()
        print("Pomodoro Timer")
        print("1. Start Pomodoro (25 minutes)")
        print("2. Start Short Break (5 minutes)")
        print("3. Start Long Break (15 minutes)")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            pomodoro_timer(25)
        elif choice == '2':
            pomodoro_timer(5)
        elif choice == '3':
            pomodoro_timer(15)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
