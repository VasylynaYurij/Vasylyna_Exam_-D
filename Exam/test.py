from main import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0
    assert round(celsius_to_fahrenheit(37), 2) == 98.6
    print("Все пройшло ура")

test_celsius_to_fahrenheit()
