from response_structure import *
import webbrowser

ip = "192.168.43.193"

def EvaluateSpeech(query: str) -> str:
    response = "You said: " + query + ", but I did not understand that."
    if "lights" in query:
        if get_boolean(query) in "on":
            response = "turning the lights on"

            webbrowser.open(ip + "/?r255g255b255&")

        elif get_boolean(query) in "off":
            response = "turning the lights off"

            webbrowser.open(ip + "/?r0g0b0&")

        elif get_boolean(query) in "red":
            response = "changing lights to red"

            webbrowser.open(ip + "/?r255g0b0&")

        elif get_boolean(query) in "green":
            response = "changing lights to green"

            webbrowser.open(ip + "/?r0g255b0&")

        elif get_boolean(query) in "blue":
            response = "changing lights to blue"

            webbrowser.open(ip + "/?r0g0b255&")

        elif get_boolean(query) in "purple":
            response = "changing lights to purple"

            webbrowser.open(ip + "/?r255g0b255&")

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
