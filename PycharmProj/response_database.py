from response_structure import *
import webbrowser

def EvaluateSpeech(query: str) -> str:
    response = "You said: " + query + ", but I did not understand that."
    if "lights" in query:
        if get_boolean(query) in "on":
            response = "turning the lights on"
        elif get_boolean(query) in "off":
            response = "turning the lights off"
        else:
            response = "turn the lights what? on or off?"
    elif "say hi to" in query or "say hello to" in query:
        response = "Hello, " + query.replace("say hi to", "")
    elif "wikipedia" in query:
        response = "Opening Wikipedia..."
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
    elif "play" in query and "youtube" in query:
        response = "Playing "
        response += query.replace("play", "").replace("in youtube", "").replace("on youtube", "")
        response += "on Youtube"

    return response
