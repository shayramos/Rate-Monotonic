import math
from decimal import Decimal

class RateMonotonic:

    def isFactive(self, listObj):
        for elem in reversed(listObj):
            response_time = 0
            if elem is not listObj[0]:
                last_response_time = int(elem.executionTime)
                for x in range(0, len(listObj)-1):
                    response = self.calculate_response(response_time, last_response_time, listObj, elem.executionTime)
                    if response == int(last_response_time):
                        if response > int(elem.deadline):
                            return False
                        else: #or response <= int(elem.deadline)
                            return True
                    else:
                        last_response_time = response

    @staticmethod
    def calculate_response(response_time, last_response_time, listObj, custo):
        while int(response_time) is not int(last_response_time):
            if int(response_time) is not 0:
                last_response_time = int(response_time)
            for i in listObj:
                response_time += math.ceil(float(last_response_time) / float(i.periodo)) * float(i.executionTime)
                #response_time = math.ceil(response_time)
        response_time = int(response_time) + int(custo)
        return response_time
