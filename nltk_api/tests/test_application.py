import unittest
from nltk_api.application import app


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def testDefinitionEndpoint(self):
        # check happy path for not specific definition lookup
        response = self.app.get('/definition/cat')
        self.assertEqual(response.status, '200 OK')
        self.assertIn(b'"word": "cat"', response.data)
        self.assertIn(b'"partOfSpeech": "noun"', response.data)
        self.assertIn(b'"definition": "Feline', response.data)

        # check happy path for specific definition lookup
        response = self.app.get('/definition/cat/verb')
        self.assertEqual(response.status, '200 OK')
        self.assertIn(b'"word": "cat"', response.data)
        self.assertIn(b'"partOfSpeech": "verb"', response.data)
        self.assertIn(b'"definition": "Beat with a cat-o\'-nine-tails', response.data)

        # should send HTTP 400 on wrongly provided part of speech
        response = self.app.get('/definition/cat/this_part_of_speech_doesnt_exist')
        self.assertEqual(response.status, '400 BAD REQUEST')

    def testSimilarEndpoint(self):
        # check happy path for not specific similar lookup
        response = self.app.get('/similar/pig')
        self.assertEqual(response.status, '200 OK')
        self.assertIn(b'"definition": "Domestic swine"', response.data)
        self.assertIn(b'"partOfSpeech": "noun"', response.data)
        self.assertIn(b'"word": "hog', response.data)

        # check happy path for specific similar lookup
        response = self.app.get('/similar/pig/verb')
        self.assertEqual(response.status, '200 OK')
        self.assertIn(b'"definition": "Eat greedily"', response.data)
        self.assertIn(b'"partOfSpeech": "verb"', response.data)
        self.assertIn(b'"word": "devour', response.data)

        # should send HTTP 400 on wrongly provided part of speech
        response = self.app.get('/similar/pig/this_part_of_speech_doesnt_exist')
        self.assertEqual(response.status, '400 BAD REQUEST')

    def testLemmaEndpoint(self):
        # Check happy path
        post_payload = '[{"word": "jogging", "partOfSpeech": "verb"}]'
        result = self.app.post('/lemma', headers={'Content-Type': 'application/json'}, data=post_payload)
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'"lemma": "jog"', result.data)

        # Check if sends HTTP 400 on malformed request body
        post_corrupted_payload = 'asdasdasd'
        result = self.app.post('/lemma', headers={'Content-Type': 'application/json'}, data=post_corrupted_payload)
        self.assertEqual(result.status, '400 BAD REQUEST')

        post_wrong_format_payload = '[{"missing": "jogging", "keys": "verb"}]'
        result = self.app.post('/lemma', headers={'Content-Type': 'application/json'}, data=post_wrong_format_payload)
        self.assertEqual(result.status, '400 BAD REQUEST')

    def testSentenceTaggerEndpoint(self):
        post_payload = '["I walk towards the sun", "He is happy today!"]'
        result = self.app.post('/tagger', headers={'Content-Type': 'application/json'}, data=post_payload)

        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'"item": "I"', result.data)
        self.assertIn(b'"item": "today"', result.data)

        # Check if sends HTTP 400 on malformed request body
        post_corrupted_payload = 'asdasdasd'
        result = self.app.post('/tagger', headers={'Content-Type': 'application/json'}, data=post_corrupted_payload)
        self.assertEqual(result.status, '400 BAD REQUEST')

    def testSentenceTaggerWithDifferentSentences(self):
        post_payload = """
        ["Should we start class now, or should we wait for everyone to get here?","She did not cheat on the test, for it was not the right thing to do.","I would have gotten the promotion, but my attendance wasn’t good enough.","I really want to go to work, but I am too sick to drive.","She advised him to come back at once.","The lake is a long way from here.","A glittering gem is not enough.","Lets all be unique together until we realise we are all the same.","If you like tuna and tomato sauce- try combining the two. It’s really not as bad as it sounds.","I often see the time 11:11 or 12:34 on clocks."]
        """
        result = self.app.post('/tagger', headers={'Content-Type': 'application/json'}, data=post_payload)
        self.assertEqual(result.status, '200 OK')
