# Task1
import re


def solution(message, K):
    """Given a message and integer number K crop the message considering K limit and spliting words

    Args:
        message ([string]): [a message]
        K ([int]): [maximum length for the output message]

    Returns:
        [string]: [cropped message]
    """
    matches = [(m.group(0), (m.start(), m.end()-1)) for m in re.finditer(r'\S+', message)]
    print("matches", matches)
    last_index=0
    for item in matches:
        print("item", item[1][1])
        if(item[1][1]>=K):
            break
        else:
            last_index=item[1][1]
            print("last_index", last_index)
    message_out=""
    if(last_index!=0):
        message_out=message[:last_index+1]
    print("message_out", message_out)
    
        
    return message_out

print(solution("To crop or not to crop",21))
