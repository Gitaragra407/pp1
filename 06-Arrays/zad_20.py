array = [15, 38, 7, 23, 14]
def occurs(number,array):
    for i in range(len(array)):
        if array[i] == number:
            return 'does'
    return "doesn't"

usrNumber = int(input())
print(f'The number {usrNumber} {occurs(usrNumber,array)} appear in the array.')