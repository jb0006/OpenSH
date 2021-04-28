from response_structure import *

all = [
    Command(["joe mama", "what is 1 + 1"], "good question",
            [ParameterNode(["hot"],
                           "NOT FUNNY, DIDN'T LAUGH")]),
    Command(["you suck"], "no, please do not say that", []),
    Command(["turn lights", "turn the lights"], "turning the lights, what? on or off?",
            [ParameterNode(["on"],
                           "Turning the lights on!"),
             ParameterNode(["off"],
                           "Turning the lights off!")]),
    Command(["lock"], "lock what? your mom?",
            [ParameterNode(["back door"],
                           "locking the back door, if there even is one. haha!")]),
    Command(["will smith"], "will smith is an actor",
            [ParameterNode(["trying to eat soybeans in my bed"],
                           "Will smith is trying to eat soybeeeaaaans in my bed.")]),

]