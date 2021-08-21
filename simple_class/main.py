"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for simple_class.

TODO(dduclayan): DO NOT SUBMIT without a detailed description of simple_class.
"""


class Animal:

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight


class Cat(Animal):

  def __init__(self, name, weight, color):
    super().__init__(name, weight)
    self.color = color


def whos_heavier(animal1, animal2):
  if animal1.weight > animal2.weight:
    return animal1.name
  else:
    return animal2.name


def print_stats(animal):
  print('My name is ' + animal.name)
  print('My weight is ' + str(animal.weight) + ' lbs.')
  try:
    print('My color is ' + animal.color)
  except AttributeError:
    pass


def main():
  dog = Animal('dog', 23)
  yellow_cat = Cat('cat', 15, 'yellow')

  print(whos_heavier(dog, yellow_cat))
  print_stats(dog)
  print_stats(yellow_cat)

if __name__ == '__main__':
  main()
