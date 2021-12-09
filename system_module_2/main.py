import json
from flask import Flask, render_template, request, Response
from google.cloud import datastore

datastore_client = datastore.Client()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def queryData():  # put application's code here
    """Retrieves data from Datastore using the limit url param"""
    limit = request.args.get('limit', default=100, type=int)
    titles = fetch_titles(limit)
    return render_template('index.html', titles=titles)

def fetch_titles(limit):
    query = datastore_client.query(kind='Title')
    titles = query.fetch(limit=limit)
    return titles


@app.route('/titles', methods=['POST'])
def postDataHandler():
    if not request.data:
        # Can't send GET request to this endpoint
        return Response(status=405)
    if not request.is_json:
        return Response(status=400)
    # Parse posted data into list of dict
    content = request.get_json()
    data = json.loads(content)
    # Store the data in Datastore
    store_title(data)
    # Return success status
    status_code = Response(status=200)
    return status_code

def store_title(titles):
    """Creates a batch job to put the data in google cloud datastore"""
    batch = datastore_client.batch()
    batch.begin()
    for title in titles:
        entity = datastore.Entity(key=datastore_client.key('Title'))
        entity.update(title)
        batch.put(entity)
    batch.commit()


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
