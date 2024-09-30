def convert_temperature(temperature, unit):
  """Converts a temperature from one unit to the others.

  Args:
    temperature: The temperature value to convert.
    unit: The original unit of measurement ('C', 'F', or 'K').

  Returns:
    A dictionary containing the converted temperatures in Celsius, Fahrenheit, and Kelvin.
  """

  if unit == 'C':
    celsius = temperature
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
  elif unit == 'F':
    fahrenheit = temperature
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (celsius * 9/5) + 32 + 273.15
  elif unit == 'K':
    kelvin = temperature
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
  else:
    raise ValueError("Invalid unit of measurement")

  return {'C': celsius, 'F': fahrenheit, 'K': kelvin}

def main():
  while True:
    temperature = float(input("Enter a temperature value: "))
    unit = input("Enter the original unit of measurement (C, F, or K): ").upper()

    converted_temperatures = convert_temperature(temperature, unit)

    print("Converted temperatures:")
    print("Celsius:", converted_temperatures['C'])
    print("Fahrenheit:", converted_temperatures['F'])
    print("Kelvin:", converted_temperatures['K'])

    if input("Do you want to convert another temperature? (y/n): ").lower() != 'y':
      break

if __name__ == '__main__':
  main()