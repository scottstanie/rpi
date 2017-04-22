from __future__ import unicode_literals
import os
from flask import Flask, render_template, jsonify, request
from playsound import playsound

import time
import atexit

# from Adafruit_MotorHAT import Adafruit_MotorHAT
from examples import Robot


from boto3 import Session
# from botocore.exceptions import ClientError

# configuration
DEBUG = True

# import Robot
LEFT_TRIM = 0
RIGHT_TRIM = 0


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
ROBOT_FUNCTIONS = {
    'up': robot.forward,
    'down': robot.backward,
    'left': robot.left,
    'right': robot.right,
    'stop': robot.stop
}

app = Flask(__name__)
app.config.from_object(__name__)


session = Session(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1',
)
polly = session.client("polly")


def _synth_speech(input_text, voice='Amy'):
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=input_text,
        TextType='text',
        VoiceId=voice
    )
    return response['AudioStream']


def create_mp3(message, filepath="message.mp3"):
    speech_stream = _synth_speech(message)
    with open(filepath, 'w') as f:
        f.write(speech_stream.read())


@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    message = data['message'].lower()
    try:
        filepath = "message.mp3"
        # Convert the mp3 with Polly and save as file
        create_mp3(message, filepath)
        # Play the mp3 from saved file
        playsound('message.mp3')
        return jsonify({"OK": True})
    except Exception as e:
        return jsonify({"OK": False, "exception": e})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    speed = data['speed'].lower()
    direction = data['direction'].lower()
    # Max duration is 5 seconds
    duration = float(data.get('duration', 5))
    speeds = {'fast': 250, 'slow': 125}
    speed_num = speeds[speed]
    print "speed:", speed_num, "direction:", direction, "duration:", duration
    ROBOT_FUNCTIONS[direction](speed_num, duration)
    return jsonify({'direction': direction, 'speed': speed})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", '0.0.0.0')
    app.run(host=host, port=port)
