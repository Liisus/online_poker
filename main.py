#! python
import eventlet
eventlet.monkey_patch()

from dotenv import load_dotenv
load_dotenv()

import argparse

from website import create_app

app, socketio = create_app()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Online poker flask app')

    parser.add_argument('--port', type=int, default=5000,
                        help='Server port number (default: 5000)')

    parser.add_argument('--host', default='localhost',
                        help='Server host address (default: localhost)')

    parser.add_argument('--debug', action='store_true',
                        help='Pretty self explanatory')

    args = parser.parse_args()

    socketio.run(app, debug=args.debug, host=args.host, port=args.port)
