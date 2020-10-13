from flask import Flask, render_template, jsonify,request
import os
from config import conf_directory
from pathlib import Path

app = Flask(__name__)


@app.route("/data", methods=["GET"])
def data():
    directory = conf_directory
    if request.method == "GET":
        if os.path.exists(directory):
            files = os.listdir(directory)
            f_dict = {"data": []}
            for file in files:
                if Path(directory).is_file():
                    filename = os.path.splitext(file)[0]
                    file_ext = os.path.splitext(file)[1]
                    full_list = [os.path.join(directory, i) for i in files]
                    time_sorted_file = sorted(full_list, key=os.path.getctime)
                    f_dict["data"].append({
                        "name": filename,
                        "type": file_ext,
                        "time": time_sorted_file,
                    })
            return jsonify(array=f_dict)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

