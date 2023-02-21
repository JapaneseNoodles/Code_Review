""""
I have chosen the resistor network option and I have effectively utilised a recursive function that will allow for the
total sum of resistors in a given circuit.

The script will test the data type of each item in the given data, if the data type is a number, the script will return
said number however if there is a list or a tuple the script will create a new instance of the function, iterate through
that list/tuple. The process will repeat itself until all lists/tuples have been iterated through and summed together

The worst case time complexity would be O(n)
"""


def resistance(circuit):
    total_ohms = eval(circuit)

    if type(total_ohms) == int or type(total_ohms) == float:
        return round(total_ohms, 1)   # if the data being passes is a single digit then there is only one resistor

    if type(total_ohms) == tuple:  # if the resistance is in series
        ohm = sum(resistance(repr(i)) for i in total_ohms)   # recursively adds all values in the series resistors
        return round(ohm, 1)

    if type(total_ohms) == list:  # if the resistance is in parallel
        ohm = 1 / sum(1 / resistance(repr(j)) for j in total_ohms)  # recursively adds values in the series parallel
        return round(ohm, 1)


def test(circuit, ans):
    check = resistance(circuit)
    if check != ans:
        return "Test Failed"
    else:
        return "Test Passed"


print(test("(10, [20, 30])", 22.0))
print(test("[10, (20, 30)]", 8.3))
print(test("([10, 20], (30, 40))", 76.7))
print(test("(1, [12, 4, (1, [10, (2, 8)])])", 3.0))
print(test("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])", 10.0))
print(test("(25, 10, [(8, 3), 5], 9)", 47.4))
