class RateMonotonic:

    def isFactive(self, listObj):
        for elem in reversed(listObj):
            if elem is not listObj[0]:
                last_response_time = elem.executionTime
                while True:
                    response = self.calculate_response(last_response_time, listObj)
                    if response[0] == response[1]:
                        if response[0] > int(elem.deadline):
                            return False
                        else:
                            return True
                    else:
                        last_response_time = response[1]

    @staticmethod
    def calculate_response(last_response_time, listObj):
        response_time = 0
        for i in listObj:
            response_time += (int(last_response_time) / int(i.periodo)) * int(i.executionTime)
        response_time = int(response_time) + int(last_response_time)
        last_response_time = response_time
        return response_time, last_response_time
