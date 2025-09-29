import os, time, pathlib
from datetime import datetime, timedelta

def message_loop(get_message: str, get_count: int):
    print(f'Starting to print message - {get_count} times...')
    for i in range(1, get_count + 1):
        print(f'[{str(datetime.utcnow()+timedelta(hours=8))[:19]}] [{i}/{get_count}] {get_message}')
        time.sleep(1)
    print('Done & Container is exiting.')

if __name__ == "__main__":
    message = os.getenv('MESSAGE', 'Hello, World! From Docker Compose!')
    count = int(os.getenv('COUNT', 3))
    message_loop(message, count)