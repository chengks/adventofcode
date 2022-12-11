import re
import sys;print(sys.version)
import math

class Monkey:
    def __init__(self, _id, _items, __divisible_nr, _operation, _operation_nr,  _monkeys):
        self.id = _id
        self.items = _items
        self.divisible_nr = __divisible_nr
        self.operation = _operation
        self.operation_nr = _operation_nr
        self.monkeys = _monkeys
        self.inspect_counter = 0

def convertInput():
    monkey_regex = re.compile(r'^Monkey\s([0-9]*):$', flags=re.IGNORECASE)
    items_regex = re.compile(r'^\s\sStarting\sItems:\s([0-9,\s]+)$', flags=re.IGNORECASE)
    operation_regex = re.compile(r'^\s\sOperation:\snew\s=\sold\s([+|-|*|])\s([0-9|old]+)$')
    divisible_regex = re.compile(r'^\s\sTest:\sdivisible\sby\s([0-9]+)$')
    monkey_throw_regex = re.compile(r'^\s\s\s\sIf\s(true|false):\sthrow\sto\smonkey\s([0-9]+)$')
    m = []
    with open("input.txt") as file:
        while (line := file.readline()):
            monkey_id = monkey_regex.findall(line.rstrip())[0]
            if monkey_id:
                items = [int(i) for i in items_regex.findall(file.readline().rstrip())[0].replace(' ','').split(',')]
                operation_formula = operation_regex.findall(file.readline().rstrip())[0]
                operation = operation_formula[0]
                operation_nr = int(operation_formula[1]) if operation_formula[1] != 'old' else operation_formula[1]
                divisible_nr = divisible_regex.findall(file.readline().rstrip())[0]
                m1 = monkey_throw_regex.findall(file.readline().rstrip())[0]
                monkey1 = (True if m1[0] == 'true' else False, int(m1[1]))
                m2 = monkey_throw_regex.findall(file.readline().rstrip())[0]
                monkey2 = (True if m2[0] == 'true' else False, int(m2[1]))
                m.append(Monkey(int(monkey_id), items, int(divisible_nr), operation, operation_nr, [monkey1, monkey2]))
                file.readline().rstrip()
    return m

def calculate(symbol, item, operation_nr):
    if operation_nr ==  'old': return item * item   
    if symbol ==  '+': return item + operation_nr
    if symbol ==  '-': return item - operation_nr
    if symbol ==  '*': return item * operation_nr 
        
    return item

def main():
    print("main execute")
    monkeys = convertInput()
    round = 1
    mod = math.prod([monkey.divisible_nr for monkey in monkeys])
    while round <= 10000:
        for m in monkeys:
            while len(m.items) > 0:
                m.inspect_counter += 1
                worry_level = m.items.pop(0)
                new_worry_level = calculate(m.operation, worry_level, m.operation_nr)
                new_worry_level %= mod
                divisible = new_worry_level % m.divisible_nr
                
                if divisible == 0:
                    throw_to_monkey = [mt for mt in monkeys if mt.id == m.monkeys[0][1]][0]
                    throw_to_monkey.items.append(new_worry_level)                
                else:
                    throw_to_monkey = [mt for mt in monkeys if mt.id == m.monkeys[1][1]][0]
                    throw_to_monkey.items.append(new_worry_level)
        round += 1
            
    sorted_monkeys = sorted(monkeys, key=lambda x: x.inspect_counter, reverse=True)
    
    print(sorted_monkeys[0].inspect_counter * sorted_monkeys[1].inspect_counter)
    
if __name__  == "__main__":
    main()