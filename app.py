from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# noinspection PyUnresolvedReferences
@app.route('/')
def web_route():
    return render_template('home.html')


@app.route('/create_event', methods=['POST'])
def create_event():
    title = request.form['title']
    description = request.form['description']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    with open(file='database.json', encoding='utf-8', mode='a') as file:
        file.write(
            f'{title}\n{description}\n{start_date}\n{end_date}'
        )
    return jsonify({'success': True})


@app.route('/get_events', methods=['GET'])
def get_events():
    # load from database
    events = []
    formatted_events = []
    for event in events:
        formatted_event = {
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'color': event.color
        }
        formatted_events.append(formatted_event)
        # I am not sure if this will work
    return jsonify(formatted_events)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
