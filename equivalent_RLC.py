#Equivalent Impedance Calculator

import string
import json
from decimal import *

def two_parallel(value_list):

    value_list = value_list[0].split(",")

    parallel_list = {}

    i = 0
    j = 0

    for i in range(len(value_list)):
        j = i + 1

        for j in range(i, len(value_list)):
                    parallel_calculation = (Decimal(value_list[i])*Decimal(value_list[j]))/(Decimal(value_list[i])+Decimal(value_list[j]))

                    if parallel_calculation >= 1000000:
                            parallel_calculation = parallel_calculation/1000000

                            equivalent_value = str(parallel_calculation) + " M"
                    else:
                        if parallel_calculation >= 1000:
                            parallel_calculation = parallel_calculation/1000

                            equivalent_value = str(round(parallel_calculation, 3)) + " k"
                        else:
                            equivalent_value = str(round(parallel_calculation, 3)) + " " 

                    if i != j:
                        combination_name = str(value_list[i]) + "||" + str(value_list[j]) + " or " + str(value_list[j]) + "||" + str(value_list[i])
                    else:
                        combination_name = str(value_list[i]) + "||" + str(value_list[j])
                    
                    parallel_list[combination_name] = equivalent_value

    parallel_list = json.dumps(parallel_list, indent=4, separators=(",\n", ": "), ensure_ascii=False)

    file = codecs.open(r"C:\Users\Jacob\Desktop\parallel-combinatorials.odt", "w+", "utf-8")
    file.write(parallel_list)
    file.close()

    print(parallel_list)

    return parallel_list

def n_parallel(value_list):
    print(value_list)

    value_list = value_list[0].split(",")

    inverse_resistance_sum = 0
    for i in range(len(value_list)):
        inverse_resistance_sum = inverse_resistance_sum + 1/int(value_list[i])

    nParallel_equiv_resist = round(1/inverse_resistance_sum, 3)
    return nParallel_equiv_resist