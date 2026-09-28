import os
import time
import sys

# Кадры анимации танцующего человечка
frames = [
    r"""
      \o/
       |
      / \
    """,
    r"""
      _o_
       |
      / \
    """,
    r"""
      \o/
      /|
       >
    """,
    r"""
      _o_
       |\
       <
    """,
    r"""
       o
      /|\
      / \
    """,
    r"""
      \o/
       |\
       <
    """,
    r"""
      _o_
       |/
       >
    """,
    r"""
      \o_
       |
      / \
    """,
]

def clear():
    """Очистка консоли (кроссплатформенно)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def dance(cycles=10, delay=0.2):
    try:
        for _ in range(cycles):
            for frame in frames:
                clear()
                # Красивое обрамление
                print("=" * 30)
                print("🎵  T A N C E   T I M E  🎵".center(30))
                print("=" * 30)
                print(frame)
                print("=" * 30)
                sys.stdout.flush()
                time.sleep(delay)
    except KeyboardInterrupt:
        clear()
        print("Танец окончен! 💃🕺")

if __name__ == "__main__":
    dance(cycles=20, delay=0.15)