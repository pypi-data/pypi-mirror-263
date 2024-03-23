from snakenest import Snake


@Snake(name='memory_results_manager')
class ResultsManager(object):

    def __init__(self):
        super().__init__()
        self.__step_results = {}

    def get_result_steps(self, identifier) -> list:
        """
        Returns a COPY list of dictionaries with the result of the workflow steps
        :return: List of COPY dictionaries with the result of the workflow steps
        """
        if identifier in self.__step_results:
            return self.__step_results[identifier]

        return []

    def add_result_step(self, identifier, step):

        if identifier not in self.__step_results:
            self.__step_results[identifier] = []

        self.__step_results[identifier].append(step)
