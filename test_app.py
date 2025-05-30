import unittest
from transformers import pipeline
import torch

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

    def test_summarization(self):
        # Test with a simple input text
        test_text = """
        Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence 
        displayed by animals including humans. AI research has been defined as the field of study of intelligent 
        agents, which refers to any system that perceives its environment and takes actions that maximize its 
        chance of achieving its goals. The term "artificial intelligence" had previously been used to describe 
        machines that mimic and display "human" cognitive skills that are associated with the human mind, such 
        as "learning" and "problem-solving".
        """
        
        # Generate summary
        summary = self.summarizer(test_text, max_length=130, min_length=30, do_sample=False)
        
        # Basic assertions
        self.assertIsInstance(summary, list)
        self.assertGreater(len(summary), 0)
        self.assertIn('summary_text', summary[0])
        self.assertIsInstance(summary[0]['summary_text'], str)
        self.assertGreater(len(summary[0]['summary_text']), 0)

if __name__ == '__main__':
    unittest.main() 