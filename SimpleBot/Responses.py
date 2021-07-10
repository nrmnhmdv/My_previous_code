from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"

    if user_message in ("how are you?"):
        return "I am feeling good"

    if user_message in ("who are you", "who are you?"):
        return "I am bot Madish!! "

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("what are you doing?"):
        return "I am doing my job Ser. "

    return "I don't understand you. "
