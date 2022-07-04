from collections import Counter
from responses import responses, blank_spot
from support_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load("en_core_web_lg")

exit_commands = ("quit", "goodbye,", "exit", "no", "I need to leave")

class ChatBot:
    
    def make_exit(self, user_message):
        for item in exit_commands:
            if item in user_message:
                print("Okay, have a good one.")
                return True
            return False

    def chat(self):
        user_message = input("Hi there.  I can see that you aren't from Earth, do you have any questions about our animals?\n")
        while not self.make_exit(user_message) == True:
            user_message = self.respond(user_message)

    def find_intent_match(self, responses, user_message):
        bow_user_message = Counter(preprocess(user_message))
        processed_responses = [Counter(preprocess(response)) for response in responses]
        similarity_list = [compare_overlap(response, bow_user_message) for response in processed_responses]
        response_index = similarity_list.index(max(similarity_list))
        return responses[response_index]

    def find_entities(self, user_message):
        processed_message = preprocess(user_message)
        tagged_user_message = pos_tag(processed_message)
        message_nouns = extract_nouns(tagged_user_message)
        tokens = word2vec(" ".join(message_nouns))
        category = word2vec(blank_spot)
        word2vec_result = compute_similarity(tokens, category)
        word2vec_result.sort(key = lambda x: x[2])
        if len(word2vec_result) < 1:
            return False
        else:
            return word2vec_result[-1][0]

    def respond(self, user_message):
        best_response = self.find_intent_match(responses, user_message)
        entity = self.find_entities(user_message)
        print(best_response.format(entity))
        input_message = input("Do you have any more questions about animals?\n")
        return input_message


chatboy = ChatBot()
chatboy.chat()



        
