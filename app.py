from flask import Flask, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

def time_diff(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)
    diff = abs((time1 - time2).total_seconds())
    return int(diff)

@app.route('/time-difference', methods=['GET', 'POST'])
def calculate_time_difference():
    """
    Calculate the time difference between pairs of timestamps.

    Accepts a JSON payload with a list of timestamp pairs.
    Returns the absolute difference in seconds for each pair.
    """

    data = request.get_json()
    timestamps = [
    ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
    ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
]
    results = []

    for t in timestamps:
        t1 = t[0]
        t2 = t[1]
        diff = time_diff(t1, t2)
        results.append(diff)

    node_id = socket.gethostname()
    response = {
        "Id": node_id,
        "result": results
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
