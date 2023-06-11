# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo


def make_repeater(n):
    def repeater(string):
        assert type(string) == str,"Solo puedes usar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater(5)
    print(repeat_5("Hola"))

if __name__ == "__main__":
    run()