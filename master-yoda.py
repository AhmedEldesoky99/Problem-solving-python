"""
 MASTER YODA: Given a sentence, return a sentence with the words reversed

    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda (sentence : str):
    result = sentence.split()
    print(" ".join(result[::-1]))

master_yoda('We are ready')