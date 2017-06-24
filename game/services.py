from .models import Question, Answer

def get_judgement(form_data):
    karma = get_karma(form_data)
    if karma < -300:
        karma = f"You collected {karma} karma."
        judgement = "You're a truly horrible person."

    elif karma < 0:
        karma = f"You collected {karma} karma."
        judgement = "Almost there, but not quite. Better luck next time."

    elif karma > 0 and karma < 1000:
        karma = f"You collected {karma} karma."
        judgement = "Very good, you win at life!"

    elif karma == 1000:
        karma = f"You collected {karma} karma."
        judgement = "Perfect score! Who are you?...Ghandi."

    else:
        karma = f"You collected {karma} karma."
        judgement = "Joe called, he wants his average back."

    final_judgement = karma + '\n' + judgement
    return final_judgement

def get_karma(form_data):
    karma = 0
    answers = form_data.values()
    for answer in answers:
        karma += answer.karma
        add_vote(answer)
    return karma

def add_vote(answer):
    a = answer
    a.votes += 1
    a.save()
