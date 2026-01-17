# Add the following test init command and import a test file
from EmotionDetection.emotion_detection import emotion_detector
import unittest
# Create a unit test class in the file test_emotion_detection.py
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for Joy emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1["dominant_emotion"]["name"], 'joy')

        # Test case for Anger emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2["dominant_emotion"]["name"], 'anger')

        # Test case for Disgust emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3["dominant_emotion"]["name"], 'disgust')

        # Test case for Sadness emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4["dominant_emotion"]["name"], 'sadness')

        # Test case for Fear emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5["dominant_emotion"]["name"], 'fear')

if __name__ == "__main__":
		
    unittest.main()