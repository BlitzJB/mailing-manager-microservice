from application import app

import json
config = json.load(open('./config.json'))


if __name__ == '__main__':
    app.run(
        debug=True if not config['production'] else False, 
        host=config['host'], 
        port=config['port']
    )