import sys
import nation

nation_list = []

if len(sys.argv) < 2:
    print('Please specify the parameter.')
    sys.exit()

print('sys.argv[1]      : ', sys.argv[1])

if sys.argv[1][0] == 'i':
    for i in range(int(sys.argv[1][1:])):
        nation_list.append(nation.Nation())
        print('Nation ' + str(i + 1) + ' has been created.')
        print('Nation name is ' + nation_list[i].name + '.')
        print('Nation population is ' + str(nation_list[i].pop) + '.')
    print('Initilized.')
    print('Nation has been created ' + sys.argv[1][1:] + ' times.')

