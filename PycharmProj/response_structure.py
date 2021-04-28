
class ParameterNode:
    def __init__(self, keywords, response):
        self.keywords = keywords
        self.response = response

class Command:

    def __init__(self, keywords: [str], base_response, parameters: [ParameterNode]):
        self.keywords = keywords
        self.response = base_response
        self.parameters = parameters

    def Procedure(self, input_string) -> str:
        queued_response = ""
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
                        break

        return queued_response


