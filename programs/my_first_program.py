from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))

    # Perform some creative computation
    sum_ints = my_int1 + my_int2
    product_ints = my_int1 * my_int2
    complex_computation = sum_ints * my_int3 + product_ints - my_int2

    return [Output(complex_computation, "my_output", party1)]