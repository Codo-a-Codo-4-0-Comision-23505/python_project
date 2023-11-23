import datetime

def hacelo_varias_veces(func):
    def wrapper_varias_veces():
        for x in range(10):
            func()
    return wrapper_varias_veces

def debuging_time_of_execution(func):
    def wrapper_debuging_time():
        # el tiempo actual
        time = datetime.datetime.now()
        func()
        totalTime = datetime.datetime.now() - time
        # el tiempo actual menos el anterior define cuanto tardo la funcion
        print("Tardo en ms: " + str(time))
    return wrapper_debuging_time

@debuging_time_of_execution
@hacelo_varias_veces
def saltar():
    print("Estoy saltando")


saltar() # cuantas veces salta? 1
