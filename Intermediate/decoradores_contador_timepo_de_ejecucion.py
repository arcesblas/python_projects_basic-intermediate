from datetime import datetime

def execution_time(func):
    def wrapper():
        inital_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - inital_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_fuc():
    lista = [x for x in range(1,1000000) if x % 2 == 0]
    print(lista)

        
if __name__ == '__main__':
    random_fuc()

