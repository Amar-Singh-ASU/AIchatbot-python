import re
import random


def unknown():
    response = ["Could you please re-phrase that? ",
                "Processing...",
                "Sorry to hear your issue, we will be with you shortly",
                "What can I help you with?"][
        random.randrange(4)]
    return response

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello, GenericBusiness Chatbot would be happy to assist you, wait one moment please', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you for using GenericBusiness Customer Service, have a wonderful rest of your day :D!', ['that','is','all'], required_words=['that', 'all'])
    response('I am very sorry to hear that. We take your issues very seriously and will work on it!',['bad','horrible','terrible'],single_response=True)
    response('Yes we are happy to assist you!', ['ready'],single_response=True)
    response('We are very sorry your product was late, that should not have happened', ['late'],single_response=True)
    response('Yes absolutely, would you like in app credits or a refund to your origional payment method?', ['compensate', 'compensated', 'compensation', 'owe'],single_response=True)
    response('Alright we are sending the credits to the GenericBusiness app, please be patient as the transfer may take up to 4 minutes', ['credit', 'credits','cred'],single_response=True)
    response('Absolutely! We are sending the money back to the to the origional payment method, please be patient as the transfer may take up to 24 hours', ['mulla','money','cash','payment','method'],single_response=True)
    response('We see that you are upset and understand your frustration, we REALLY do, how can we make things better :(', ['angry', 'grumpy','anger','mad','upset','unhappy'],single_response=True)
    


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('Customer: ')))