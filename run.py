from sys import argv

from chat import start_server

if __name__ == '__main__':
    try:
        HOST, PORT = argv[1:]

        start_server(HOST, PORT)

    except ValueError as e:
        if len(argv[1:]) < 2:
            print('Please provide the Host and Port value')
            print('e.g python3 run.py localhost 1234')

    except OSError as e:
        if 'Errno 98' in str(e):
            print(f'Port {PORT} in use!')

    except KeyboardInterrupt:
        print('Server Stopped!')

    except Exception as e:
        print(__name__, e)
