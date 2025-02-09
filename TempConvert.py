#TempConvert.py
#Name: Brandon Jergensen
#Date: 2/9/25
#Assignment: TempConvert.py


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = int(float(input("What is the temperature in Fahrenheit?:")))

  tempC = round((tempF - 32) * 5 / 9)


  

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
