import motor
import questions
import calculations

def run():
    interval, steps = calculations.duration(questions.duration(), calculations.distance(questions.movement()))

    ready_list = ["yes", "y", "ok", "yup", "oki", "k"]
    ready = input("Ready to start?")
    if ready.lower() in ready_list:
        motor.motor(interval, steps)
        print(interval, "\n", steps)
        print("yes")

        if input("Do you want to go again?") in ready_list:
            run()

    

