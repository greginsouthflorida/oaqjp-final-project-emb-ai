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

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Extracting sentiment label and score from the response
        scores = formatted_response['emotionPredictions'][0]['emotion']

        # Determine highest score using max function
        emotion = max(scores, key=scores.get)
        dominant_emotion = scores[emotion]

        # Build the output string
        # output = {   # Use this line to print test results
        dom_emot_dic = {	
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

        dom_emot_rtn = emotion
        return dom_emot_rtn, dom_emot_dic

    # If the response status code is 400, empty text field, set dominant_emotion to None
    elif response.status_code == 400:
        dom_emot_rtn = None

        dom_emot_dic = {	
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
        return dom_emot_rtn, dom_emot_dic

    # If the response status code is anything else, set dominant_emotion to Error
    else:
        dom_emot_rtn = 'Error'

        dom_emot_dic = {	
            'anger': 'Error',
            'disgust': 'Error',
            'fear': 'Error',
            'joy': 'Error',
            'sadness': 'Error',
            'dominant_emotion': 'There is an error in the app'
        }
        
        return dom_emot_rtn, dom_emot_dic

    # print(output) # Use this line when displaying test data