print("Hello from inside a file!")


def hello():
   print( "Hello Welcome to Python!")

hello()

def pack(doritos, locos, tacos):
    return [doritos, locos, tacos]

print(pack("hello", "again", "friend"))

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for food in range(len(list)):
      if food == 0:
        print(f"First I eat {list[0]}")
      else:
        print(f"Next I eat {list[food]}")


eat_lunch(["doritos","tacos"])
eat_lunch([])
eat_lunch(["doritos"])