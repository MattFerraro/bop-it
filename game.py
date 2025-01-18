import random 
import signal

class TimeoutExpired(Exception):
    pass

def alarm_handler(signum, frame):
    raise TimeoutExpired

def input_with_timeout(prompt, timeout):
    # Set signal handler
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)  # Produce SIGALRM in `timeout` seconds

    try:
        return input(prompt)
    except TimeoutExpired:
        return None
    finally:
        signal.alarm(0)  # Cancel the alarm

OPTIONS = [
    {"msg": "bop it!", "response": "bop"},
    {"msg": "twist it!", "response": "twist"},
    {"msg": "pull it!", "response": "pull"},
    {"msg": "flick it!", "response": "flick"},
    {"msg": "spin it!", "response": "spin"},
]
ON_LOSE = [
    "Game Over! Your score was: {}",
    "You lose! Your score was: {}",
    "Oh boy! Score: {}",
    "I remember my first time playing Bop It. Score: {}",
    "You could do better. Score: {}",
    "You're not very good at this, are you? Score: {}",
    "Do it the same but...uh...better. Score: {}",
    "Next time, try typing with both hands! Score: {}",
]

def game():
    time_limit = 2 # s
    score = 0
    while True:
        option = random.choice(OPTIONS)
        response = input_with_timeout(option["msg"] + "\n", time_limit)
        if response != option["response"]:
            print(random.choice(ON_LOSE).format(score))
            break
        score += 1
        print("")

def main():
    print("Welcome to Bop It!")
    print("Press Enter to start")
    input()
    game()

if __name__ == '__main__':
    main()