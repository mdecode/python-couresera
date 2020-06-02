import random, time , logging

logging.basicConfig(filename = 'logging.txt', level=logging.DEBUG)

while True:
    logging.debug(random.choice(['hello' , 'hi', 'howdy']))
    time.sleep(1)
