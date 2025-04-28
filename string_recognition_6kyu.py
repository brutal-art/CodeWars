"""
Pine's grandma is hearing impaired: whatever you say to her, she responds with 
"HUH?!  SPEAK UP, SONNY!", unless you shout it (type in all capitals).

If you shout, she can hear you (or at least she thinks so) and yells back, 
"NO, NOT SINCE 1938!" You can't stop talking to grandma until you shout "BYE".

When you shout "BYE", grandma shouts back "OK, BYE!" and end the conversation.

Your input is an array with a list of strings with all the words/sentences you say in order
You can expect there is aways a "BYE", 
although it is not necessarily the last word in the list
Your output is an array with a list of strings and every sentence Pine's grandma replies
Words/sentences are always a string

"""

def deaf_grandma(you):

    grandma = ['HUH?! SPEAK UP, SONNY!', 'NO, NOT SINCE 1938!', 'OK, BYE!']
    answer = []

    for question in you:
        if question == "BYE":
            answer.append(grandma[2])
            return answer
        elif question == question.upper():
            answer.append(grandma[1])
        else:
            answer.append(grandma[0])
    return answer

if __name__ == '__main__':
    arr = ["good morning", "NICE TO SEE YOU", "BYE", "oh, I forgot", "nevermind", "see you"]
    print(deaf_grandma(arr))
    print(["HUH?! SPEAK UP, SONNY!", "NO, NOT SINCE 1938!", "OK, BYE!"])