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

VERBS = [
    "bop",
    "twist",
    "pull",
    "flick",
    "spin",
]
UNUSUAL_VERBS = [
    "lick",
    "kick",
    "punch",
    "behold",
    "ignore",
    "dismiss",
    "foresee",
    "forget",
    "forgive",
    "forsake",
    "abide",
    "accept",
    "withhold",
    "withstand",
    "perplex",
]
VERY_UNUSUAL_VERBS = [
    "genuflect",
    "overthrow",
    "incite",
    "beknight",
    "betray",
    "bewitch",
    "aggregate",
    "debase",
    "devastate",
    "deface",
    "unlink",
    "unhook",
    "polyphonize",
    "hypothesize",
    "anthropomorphize",
    "demythologize",
    "disenfranchise",
    "internationalize",
    "polyploidize",
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
    time_limit = 3 # s
    score = 0
    fully_unusual = 40

    while True:
        if score < 50:
            if random.random() < score / fully_unusual:
                option = random.choice(UNUSUAL_VERBS)
            else:
                option = random.choice(VERBS)
        else:
            if random.random() < 0.1:
                option = random.choice(VERBS)
            else:
                option = random.choice(VERY_UNUSUAL_VERBS)

        response = input_with_timeout(f"{score}: {option} it!\n", time_limit)
        if response != option:
            print()
            print(random.choice(ON_LOSE).format(score))
            break
        score += 1
        print()

def main():
    print("Welcome to Bop It!")
    print("Press Enter to start")
    input()
    game()

if __name__ == '__main__':
    main()