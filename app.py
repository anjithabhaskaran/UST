from configs.config import app
from apis import api

## Initialize the 'api' with the 'app' instance to integrate it with your Flask application.
api.init_app(app)

# Start the Flask application 
if __name__ == '__main__':

    app.run(debug=True)