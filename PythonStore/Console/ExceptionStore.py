"""
Overview:
    - Utility using for raised customizing exception.
Author:
    - Le Anh Tu
Information:
    - letuss004@gmail.com
    - 0336407556
Note:
    - If there is any issue, contact me as above
"""


class ParameterInputException(Exception):
    """Exception raised for errors in the input argument.

    Attributes:
        :parameter: message -- explanation of the error

    Note:
        :parameter: message can be customize
    """

    def __init__(self, message="Parameter was incorrect according to the request of method."):
        self.message = message
        super().__init__(self.message)
