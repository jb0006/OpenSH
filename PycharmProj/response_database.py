from response_structure import *

all = [
    Command(["joe mama", "what is 1 + 1"], "good question",
            [ParameterNode(["hot"],
                           "NOT FUNNY, DIDN'T LAUGH", code_to_run="print('lmfao')")]),
    Command(["you suck"], "no, please do not say that"),
    Command(["lights", "turn lights", "turn the lights"], "turning the lights, what? on or off?",
            [ParameterNode(["on"],
                           "Turning the lights on!",
                           code_to_run="print('--executed command to turn lights on--')"),
             ParameterNode(["off"],
                           "Turning the lights off!",
                           code_to_run="print('--executed command to turn lights off--')")]),
    Command(["say something funny"], "something funny"),
    Command(["say hi"], "hi to who?",
            [ParameterNode(["audience"],
                           "Hello, audience!"),
             ParameterNode(["presenters"],
                           "Hello Juan, Chris, Aiden, Antonio, Derek, and Jackie"),
             ParameterNode(["teacher"],
                           "Hello, Mr. Rajewich!")])
]