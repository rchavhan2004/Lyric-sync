import time

def print_lyrics():
    lines = [
        "So I'ma love you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you",
        "If the party was over",
        "And our time on earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to YOU !!",
    ]

    delays = [0.02, 0.04, 0.4, 2.6, 1.0, 3.3, 1.4, 1.8, 0.9, 1.2]

    for i, line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
        time.sleep(delays[i])


print_lyrics()
