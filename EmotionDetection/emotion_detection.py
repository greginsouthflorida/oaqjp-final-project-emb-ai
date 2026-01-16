import requests
import json

def emotion_detector(text_to_analyze):    # function to analyze emotion of text input

    # Emotion library input connection link
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers	
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    scores = formatted_response['emotionPredictions'][0]['emotion']

    # Determine highest score using max function
    emotion = max(scores, key=scores.get)
    dominant_emotion = scores[emotion]

    # Build the output dictionary
    output = {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': {
            'name': emotion,
            'score': dominant_emotion
        }
    }

    print(output)