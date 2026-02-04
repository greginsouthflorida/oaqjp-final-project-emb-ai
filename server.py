"""
Server.py for the Emotion Detector application

A text phrase entered on an index.html page is analyzed by an emotion AI API

"""
# Load the Flask library along with its render_template function
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")    # referenced in the mywebscript.js
def sent_analyzer():
    """ Get the emotion AI analysis result, format output & return output to interface """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Get dominant emotion & emotion dictionary from emotion_detector function & store the response
    dom_emot_rtn, dom_emot_dic = emotion_detector(text_to_analyze)

    if dom_emot_rtn is None:

        # Build the formatted output string
        formatted_output = 'Invalid text! Please try again!'

    else:
        # Build the formatted output string
        formatted_output = (
            f"For the given statement, the system response is "
            f"'anger': {dom_emot_dic['anger']}, "
            f"'disgust': {dom_emot_dic['disgust']}, "
            f"'fear': {dom_emot_dic['fear']}, "
            f"'joy': {dom_emot_dic['joy']}, "
            f"'sadness': {dom_emot_dic['sadness']}."
            f"The dominant emotion is {dom_emot_rtn}."
        )

    return formatted_output

@app.route("/")
def render_index_page():
    """ Send output to index.html on server port 5000 """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
