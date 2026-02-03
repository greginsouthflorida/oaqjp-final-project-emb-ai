# Load the Flask library along with its render_template function
from flask import Flask, emotionDetector, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")    # referenced in the mywebscript.js
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Get the dominant emotion and emotion dictionary from the emotion_detector function and store the response
    dom_emot_rtn, dom_emot_dic = emotion_detector(text_to_analyze)

    # Build the formatted output string
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {dom_emot_dic['anger']}, "
        f"'disgust': {dom_emot_dic['disgust']}, "
        f"'fear': {dom_emot_dic['fear']}, "
        f"'joy': {dom_emot_dic['joy']}, "
        f"'sadness': {dom_emot_dic['sadness']}. "
        f"The dominant emotion is {dom_emot_rtn}."
    ) 
	
    return formatted_output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)