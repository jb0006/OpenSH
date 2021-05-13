
class Action:
    def __init__(self, keywords, ):



class ParameterNode:
    def __init__(self, keywords, response, code_to_run=None):
        self.keywords = keywords
        self.response = response
        self.run = code_to_run


class Command:

    def __init__(self, keywords: [str], base_response, parameters: [ParameterNode] = []):
        self.keywords = keywords
        self.response = base_response
        self.parameters = parameters

    def Procedure(self, input_string) -> (str, str):
        queued_response = ""
        parameter_exec = ""
        found_key = False
        for key in self.keywords:
            if key in input_string:
                found_key = True
                queued_response = self.response
                break

        selected_parameter: ParameterNode
        if found_key and self.parameters is not None:

            for parameter in self.parameters:

                for keyword in parameter.keywords:

                    if keyword in input_string:

                        selected_parameter = parameter
                        queued_response = selected_parameter.response
                        parameter_exec = selected_parameter.run
                        break

        return queued_response, parameter_exec


