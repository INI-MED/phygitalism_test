from datetime import datetime
from flask import Flask, render_template, jsonify
import os
from config import conf_directory
from pathlib import Path

app = Flask(__name__)


def convert_time(timestamp: float) -> str:
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_file_type(file: str, show_ext=False) -> str:
    if Path(file).is_file():
        if show_ext:
            splitted = file.split('.')
            return '.' + splitted[1] if len(splitted) > 1 else splitted[0]
        else:
            return 'file'
    else:
        return 'folder'


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/api/meta", methods=["GET"])
def api():
    directory = conf_directory
    f_dict = {"data": []}
    if os.path.exists(directory):
        files = os.listdir(directory)
        sorted_files = sorted(files)
        for file in sorted_files:
            file_type = get_file_type(file, True)
            file_time = convert_time(os.path.getctime(file))
            f_dict["data"].append({
                "name": file,
                "type": file_type,
                "time": file_time,
            })
    return jsonify(f_dict)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
