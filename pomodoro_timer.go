package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func clearScreen() {
	cmd := exec.Command("clear")
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func pomodoroTimer(minutes int) {
	seconds := minutes * 60
	for seconds > 0 {
		mins := seconds / 60
		secs := seconds % 60
		fmt.Printf("\rTime left: %02d:%02d", mins, secs)
		time.Sleep(1 * time.Second)
		seconds--
	}
	fmt.Println("\nTime's up!")
}

func main() {
	for {
		clearScreen()
		fmt.Println("Pomodoro Timer")
		fmt.Println("1. Start Pomodoro (25 minutes)")
		fmt.Println("2. Start Short Break (5 minutes)")
		fmt.Println("3. Start Long Break (15 minutes)")
		fmt.Println("4. Exit")

		var choice string
		fmt.Print("Select an option: ")
		fmt.Scanln(&choice)

		switch choice {
		case "1":
			pomodoroTimer(25)
		case "2":
			pomodoroTimer(5)
		case "3":
			pomodoroTimer(15)
		case "4":
			os.Exit(0)
		default:
			fmt.Println("Invalid choice. Please select a valid option.")
			time.Sleep(2 * time.Second)
		}
	}
}
