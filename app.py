from __future__ import unicode_literals
import os
from flask import Flask, render_template, jsonify, request
# import json
# import requests

# import time
# import atexit

# from Adafruit_MotorHAT import Adafruit_MotorHAT


RESULTS_PER_PAGE = 10
# configuration
DEBUG = True

# import Robot
LEFT_TRIM   = 0
RIGHT_TRIM  = 0


# # Create an instance of the robot with the specified trim values.
# # Not shown are other optional parameters:
# #  - addr: The I2C address of the motor HAT, default is 0x60.
# #  - left_id: The ID of the left motor, default is 1.
# #  - right_id: The ID of the right motor, default is 2.
# robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
# ROBOT_FUNCTIONS = {
#     'up': robot.forward,
#     'down': robot.backward,
#     'left': robot.left,
#     'right': robot.right,
#     'stop': robot.stop
# }

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    speed = data['speed'].lower()
    direction = data['direction'].lower()
    speeds = {'fast': 250, 'slow': 125}
    speed_num = speeds[speed]
    print speed_num, direction
    # ROBOT_FUNCTIONS[direction](speed_num)
    return jsonify({'response': 'OK'})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", '0.0.0.0')
    app.run(host=host, port=port)
