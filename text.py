import json
import os
import openai
import openai

my_openai_api_keys = [
    {"key": "", "set_base": True,
     "api_base": ""},
]

openai.api_base = my_openai_api_keys[0]['api_base']
openai.api_key = my_openai_api_keys[0]['key']


class Conversation:
    def __init__(self, num_of_round):
        self.num_of_round = num_of_round
        self.messages = []

    def ask(self, question):
        try:
            self.messages.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=self.messages,
                temperature=1,
                max_tokens=1024 * 4,
                top_p=1,
            )
        except Exception as e:
            print(e)
            return e

        message = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": message})

        if len(self.messages) > self.num_of_round * 2 + 1:
            del self.messages[1:3]
        return message


a="Given entity label set: ['Organization', 'Person', 'Location', 'Miscellaneous'] and target sentence : '( 52.76 / 53.18 )'\nWhat entity types may be included in this sentence?\nIf not present, answer: None.\nRespond as a list, e.g. ['entity type 1', 'entity type 2', .....]\n"
b="Here provide some examples and the corresponding entity labels.\nBased on the entity types in the target sentence, please predict the helpfulness scores and give reasons of each sentence, which indicates the degree to which providing the current example can aid in extracting named entities from the target_sentence. The score ranges from 1 to 5, with 1 being the least helpful and 5 being the most helpful.\nProvide answer in the following JSON format: [{\"Example id\": \"helpfulness score\"},{\"Reason id\": \"reasons\"}]Sentence: 1. Ilke Wyludda ( Germany ) 66.60 metres\nAnswer: [{'Ilke Wyludda': 'Person'}, {'Germany': 'Location'}]\nSentence: OAKLAND 65 72 .474 12 1/2\nAnswer: [{'OAKLAND': 'Location'}]\nSentence: Riley ( Australia ) 64 71 , Carl Mason 69 66 , Barry Lane\nAnswer: [{'Riley': 'Person'}, {'Australia': 'Location'}, {'Carl Mason': 'Person'}, {'Barry Lane': 'Person'}]\nSentence: 6. Chandra Sturrup ( Bahamas ) 11.26\nAnswer: [{'Chandra Sturrup': 'Person'}, {'Bahamas': 'Location'}]\nSentence: Allensbach Aug 21 37.2 32.8 8.0 13.0 5.6\nAnswer: [{'Allensbach': 'Location'}]\nSentence: 23. Poland 8.12\nAnswer: [{'Poland': 'Location'}]\nSentence: SEATTLE 70 64 .522 6\nAnswer: [{'SEATTLE': 'Location'}]\nSentence: KANSAS CITY 58 70 .453 18 1/2\nAnswer: [{'KANSAS CITY': 'Location'}]\nSentence: 9. Jason Rouser ( U.S. ) 46.11\nAnswer: [{'Jason Rouser': 'Person'}, {'U.S.': 'Location'}]\nSentence: The Nasdaq composite index closed 3.53 points lower Friday at 1,141.50 .\nAnswer: [{'Nasdaq': 'Organization'}]\nSentence: 26. Finland 8.09\nAnswer: [{'Finland': 'Location'}]\nSentence: 1. Virna De Angeli ( Italy ) 55.66\nAnswer: [{'Virna De Angeli': 'Person'}, {'Italy': 'Location'}]\nSentence: CALIFORNIA 58 68 .460 14 1/2\nAnswer: [{'CALIFORNIA': 'Location'}]\nSentence: HOUSTON 69 61 .531 -\nAnswer: [{'HOUSTON': 'Location'}]\nSentence: 35. Hungary 7.98\nAnswer: [{'Hungary': 'Location'}]\nSentence: 2. Anthony Washington ( U.S. ) 68.44\nAnswer: [{'Anthony Washington': 'Person'}, {'U.S.': 'Location'}]\n"
c="Given entity label set: ['Organization', 'Person', 'Location', 'Miscellaneous'] and target sentence : '( 52.76 / 53.18 )'\nConsider the above helpfulness scores, recognize the named entities for the target sentence.\nProvide answer in the following JSON format: [{\\\"Entity Name\\\": \\\"Entity Label\\\"}]. If there is no entity in the text, return the following empty list: []\n\nSentence: 1. Ilke Wyludda ( Germany ) 66.60 metres\nAnswer: [{'Ilke Wyludda': 'Person'}, {'Germany': 'Location'}]\nSentence: OAKLAND 65 72 .474 12 1/2\nAnswer: [{'OAKLAND': 'Location'}]\nSentence: Riley ( Australia ) 64 71 , Carl Mason 69 66 , Barry Lane\nAnswer: [{'Riley': 'Person'}, {'Australia': 'Location'}, {'Carl Mason': 'Person'}, {'Barry Lane': 'Person'}]\nSentence: 6. Chandra Sturrup ( Bahamas ) 11.26\nAnswer: [{'Chandra Sturrup': 'Person'}, {'Bahamas': 'Location'}]\nSentence: Allensbach Aug 21 37.2 32.8 8.0 13.0 5.6\nAnswer: [{'Allensbach': 'Location'}]\nSentence: 23. Poland 8.12\nAnswer: [{'Poland': 'Location'}]\nSentence: SEATTLE 70 64 .522 6\nAnswer: [{'SEATTLE': 'Location'}]\nSentence: KANSAS CITY 58 70 .453 18 1/2\nAnswer: [{'KANSAS CITY': 'Location'}]\nSentence: 9. Jason Rouser ( U.S. ) 46.11\nAnswer: [{'Jason Rouser': 'Person'}, {'U.S.': 'Location'}]\nSentence: The Nasdaq composite index closed 3.53 points lower Friday at 1,141.50 .\nAnswer: [{'Nasdaq': 'Organization'}]\nSentence: 26. Finland 8.09\nAnswer: [{'Finland': 'Location'}]\nSentence: 1. Virna De Angeli ( Italy ) 55.66\nAnswer: [{'Virna De Angeli': 'Person'}, {'Italy': 'Location'}]\nSentence: CALIFORNIA 58 68 .460 14 1/2\nAnswer: [{'CALIFORNIA': 'Location'}]\nSentence: HOUSTON 69 61 .531 -\nAnswer: [{'HOUSTON': 'Location'}]\nSentence: 35. Hungary 7.98\nAnswer: [{'Hungary': 'Location'}]\nSentence: 2. Anthony Washington ( U.S. ) 68.44\nAnswer: [{'Anthony Washington': 'Person'}, {'U.S.': 'Location'}]\nSentence: ( 52.76 / 53.18 )\nAnswer:\n"
print(a)
print(b)
print(c)