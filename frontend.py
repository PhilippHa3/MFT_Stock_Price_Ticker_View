import requests, json, time

def display_stocks(stocks:dict):
    # clean display + move display top left
    print("\033[2J")
    print("\033[H")

    # display all given stocks
    print("Stock   |   Value   |   Difference  |  Working ")
    print("---------------------------------------------")
    for v in stocks.values():
        # set working = False, if no update comes within 3 seconds
        working = time.time() - v['timestamp'] < 3
        print(f"{v['name']} \t   {v['val']:.2f}$\t {v['diff']:.2f}$\t\t {working}")

def start():
    url = 'http://127.0.0.1:5000/pub'

    # save stocks for displaying
    stocks = {}

    while True:
        try: 
            # read and decode stream
            with requests.get(url, stream=True) as data:
                for line in data.iter_lines():
                    decoded_line = line.decode('utf-8')
                    try:
                        # save and display stocks
                        t = json.loads(decoded_line)
                        stocks[t['id']] = t
                        display_stocks(stocks)
                    except:
                        pass
        except KeyboardInterrupt:
            print("Disconnected.")
            break

if __name__ == '__main__':
    start()