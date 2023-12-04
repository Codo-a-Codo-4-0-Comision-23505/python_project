import time

def hacelo_varias_veces(func):
    def wrapper_varias_veces():
        for x in range(10):
            func()
    return wrapper_varias_veces

def debuging_time_of_execution(func):
    def wrapper_debuging_time():
        # el tiempo actual
        start_time = time.time()
        func()
        elapsed_time = time.time() - start_time
        # el tiempo actual menos el anterior define cuanto tardo la funcion
        print("Tardo en ms: " + str(elapsed_time))
    return wrapper_debuging_time

@debuging_time_of_execution
@hacelo_varias_veces
def saltar():
    print("Estoy saltando")


saltar() # cuantas veces salta? 1
