import math
from decimal import Decimal

class RateMonotonic:

    def isFactive(self, listObj):
        for elem in reversed(listObj):
            if elem is not listObj[0]:
                last_response_time = elem.executionTime
                for x in range(0, len(listObj)-1):
                    response = self.calculate_response(last_response_time, listObj, elem.executionTime)
                    if response == int(last_response_time) or response <= int(elem.deadline):
                        return True
                    if response > int(elem.deadline):
                        return False
                    else:
                        last_response_time = response

    @staticmethod
    def calculate_response(last_response_time, listObj, custo):
        response_time = 0
        for i in listObj:
            response_time += (float(last_response_time) / float(i.periodo)) * float(i.executionTime)
            response_time = math.ceil(response_time)
        response_time = int(response_time) + int(custo)
        return response_time
