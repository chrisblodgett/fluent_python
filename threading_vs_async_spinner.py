import itertools
import time
from threading import Event, Thread


def spin(msg: str, done_event: Event, speed: float) -> None:
    status = ''
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done_event.wait(speed):
            break
    blanks = ' ' * len(status)
    print(
        f'\r{blanks}\r', end=''
    )  # causes the line to be overwritten by usign \r to go to the
    # beginning then printing blanks the lenfgth of the string and finally resetting the cursor


def slow(delay: int) -> int:
    time.sleep(
        delay
    )  # this will block the main thread but will let the spin thread proceed
    return 42


# thread supervisor
def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking', done, 0.5))
    spinner.start()
    result = slow(5)
    done.set()  # set to treu to cause the done to stop
    spinner.join()  # wait for spinner thread to finish
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
