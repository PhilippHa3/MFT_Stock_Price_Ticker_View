from flask import Flask, Response
import json, time, random
import multiprocessing as mp


def stock_price_gen_process(delay, id, name, shared_queue, start_val):
    """
        defines the process to update a stock price and pushes it to a shared queue
    """
    stock_price_model = {
        'id': id,
        'name': name,
        'val': start_val,
        'diff': 0.0, 
        'timestamp': time.time()
    }

    while True:
        # randomly get difference
        difference = random.gauss(0, 3)
        stock_price_model['diff'] = difference
        stock_price_model['val'] = stock_price_model['val'] + difference
        stock_price_model['timestamp'] = time.time()
        try:
            shared_queue.put(stock_price_model)
        except:
            pass

        time.sleep(delay)

def init_app(shared_queue):
    """
        initalizes the flask app with the shared queue
    """
    app = Flask(__name__)

    @app.route('/pub')
    def stream_data():
        def event_stream():
            # takes data from the shared queue
            while True:
                data = shared_queue.get()
                yield f"{json.dumps(data)}\n\n"
        
        return Response(event_stream())#, mimetype='text/event_stream')

    return app

if __name__ == '__main__':

    shared_queue = mp.Queue(maxsize=10)

    # define + start worker processes
    processes = [
        mp.Process(target=stock_price_gen_process, args=(2, 0, "Google", shared_queue, 750.0)),
        mp.Process(target=stock_price_gen_process, args=(1, 1, "Nvidia", shared_queue, 500.0)),
        mp.Process(target=stock_price_gen_process, args=(1.5, 2, "Apple", shared_queue, 250.0))
    ]

    for p in processes:
        p.start()

    # start app
    try:
        app = init_app(shared_queue)
        app.run(debug=False, port=5000)
    except KeyboardInterrupt:
        print("Stop Backend!")
    finally:
        for p in processes:
            if p.is_alive():
                p.terminate()
                p.join()