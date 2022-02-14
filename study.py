#Number 1
def fizzbuzz(n):
  number = 1
  while number <= n:
    if number % 3 == 0:
      print ('fizz')
    elif number % 5 == 0:
      print ('buzz')
    elif number % 3 == 0 and number % 5 == 0:
      print ('fizzbuzz')
    else:
      print (number)
    number = number + 1

#Number 2
def pal(n):
    m = n
    while m:
        n, m = n * 10 + m % 10, m // 10
    return n

#Number 3
def make_zipper(f1, f2, sequence):
    zipper = lambda x: x
    helper = lambda f, g: lambda x: f(g(x))
    while sequence > 0:
        if sequence % 10 == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)
        sequence = sequence // 10
    return zipper

#Number 4
def sum_digits(x):
    sum = 0
    while x > 0:
        sum = sum + x % 10
        x = x // 10
    return sum

#Number 4
from operator import mul
def falling(n, k):
    total, stop = 1, n - k
    while n > stop:
        total, n = total * n, n - 1
    return total

#Number 5
def double_eights(n):
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False

#Number 6
def wears_jacket_with_if(temp, raining):
    if temp <= 60 or raining == True:
        return True
    else:
        return False

#Number 7
def wears_jacket(temp, raining):
    return temp <= 60 or raining == True

#Number 8
def is_prime(n):
    def prime_helper(k):
        if k == n:
            return True
        elif n % k == 0 or n == 1:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper (2)


#Number 9
from operator import add, sub
def a_plus_abs_b(a, b):
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)

#Number 10
def two_of_three(x, y, z):
    return min(x*x + y*y, x*x + z*z, y*y + z*z)

#Number 11
def largest_factor(x):
    i = x - 1
    while i >0:
        if x%i == 0:
            return i
        i -= 1

#Number 12
def with_if_statement():
    if c():
        return t()
    else:
        return f()
def with_if_function():
    return if_function(c(), t(), f())
def c():
    return False
def t():
    print(5)
def f():
    print(6)

#Number 13
def hailstone(n):
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n

#Number 14
from operator import add, mul, sub
square = lambda x: x * x
identity = lambda x: x
def summation(n, f):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + f(i)
        i += 1
    return sum

def product(n, f):
    i = 1
    product = 1
    while i <= n:
        product = product * f(i)
        i += 1
    return product

#Number 15
def accumulate(combiner, base, n, f):
    result = base
    i = 1
    while i <= n:
        result = combiner(result, f(i))
        i += 1
    return result

#Number 16
def summation_using_accumulate(n, f):
    return accumulate(add, 0, n, f)
def product_using_accumulate(n, f):
    return accumulate(mul, 1, n, f)

#Number 17
def compose1(h, g):
    def f(x):
        return h(g(x))
    return f
def make_repeater(h, n):
    def helper(x):
        i = 0
        while i < n:
            x = h(x)
            i += 1
        return x
    return helper

#Number 18
from operator import add, mul, mod
def lambda_curry2(func):
    return lambda x: lambda y: func(x, y)

#Number 19
def count_cond(condition):
    def helper(x):
        k = 1
        count = 0
        while k <= x:
            if condition(x, k):
                count += 1
            k += 1
        return count
    return helper

#Number 20
def both_paths(sofar= 'S'):
    print (sofar)
    def left():
        return both_paths(sofar + "L")
    def right():
        return both_paths(sofar + "R")
    return left, right

#Number 21
def compose(f, g):
    return lambda x: f(g(x))
def composite_identity(f, g):
    def helper(x):
        return compose(f, g)(x) == compose(g, f)(x)
    return helper


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest = ', ' + repr(self.rest)
        else:
            rest =''
        return 'Link(' +repr(self.first)+rest+')'
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ''
            self = self.rest
        return string + str(self.first) + '>'

#Number 22
def cycle(f1, f2, f3):
    def helper1(n):
        def helper2(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return helper2
    return helper1

#Number 23
def keep_ints(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print (i)
        i += 1

#Number 24
def make_keeper(n):
    def helper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print (i)
            i += 1
    return helper

#Number 25
def print_delayed(x):
    def delay_print(y):
        print (x)
        return print_delayed(y)
    return delay_print

#Number 26
def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print

#Number 27
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

#Number 28
def count_matches(n, m):
    count = 0
    while n > 0  or m > 0:
        if n % 10 == m % 10:
            count += 1
        n, m = n // 10, m // 10
    return count

#Number 29
def make_skipper(n):
    def helper(x):
        for i in range(x + 1):
            if i % n != 0 :
                print (i)
    return helper

#Number 30
def ordered_digits(x):
    while x > 0:
        last_digit = x % 10
        last = last_digit
        if last_digit < last:
            return True
        return False
        x = x // 10

#Number 31
def is_palindrome(n):
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

#Number 32
def same_digits(a, b):
    assert a > 0 and b > 0
    while a and b:
        if a % 10 == b % 10:
            end = a % 10
            while a % 10 == end:
                a = a // 10
            while b % 10 == end:
                b = b //10
        else:
            return False
    return a == b

#Number 33
def search(f, x):
    while not f(x):
        x += 1
    return x
def no_repeats(a):
    return search(lambda b: same_digits(a, b), 1)

#Number 34
def unique_largest(n):
    assert n > 0
    top = 0
    while n:
        n, d = n // 10, n % 10
        if d > top:
            top, unique = d, True
        elif d == top:
            unique = False
    return unique

#Number 35
def transitive(p):
    abc = 0
    while abc < 100:
        a, b, c = abc // 100, (abc // 10) % 10 ,  abc %  10
        if p(a,b) and p(b,c) and not p(b,c):
            return False
        abc = abc +  1
    return True

#Number 36
def compose(n):
    assert n >0
    if n == 1:
        return lambda f: f
    def call(f):
        def on(g):
            return compose(n-1)(lambda x: f(g(x)))
        return on
    return call

#Number 37
def num_sevens(x):
    if x % 10 == 7:
        return 1 + num_sevens(x // 10)
    elif x < 10:
        return 0
    else:
        return num_sevens(x // 10)

#Number 38
def pingpong(n):
    def helper(result, i, step):
        if i == n:
            return result
        elif i % 7 == 0 or num_sevens(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)

#Number 39
def count_change(total):
    def constrained_count(total, smallest_coin):
        if total == 0:
            return 1
        if smallest_coin > total:
            return 0
        without_coin = constrained_count(total, smallest_coin * 2)
        with_coin = constrained_count(total - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(total, 1)

#Number 40
def missing_digits(n):
    last = n % 10
    rest = n // 10
    if n < 10:
        return n
    elif last == rest % 10:
        return missing_digits(rest)
    elif last != ((rest) % 10 + 1):
        return last - (rest) % 10 -1 + missing_digits(rest)
    return missing_digits(rest)

#Number 41
def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

#Number 42
def merge(n1, n2):
    n1_last, n2_last = n1 % 10, n2 % 10
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1_last < n2_last:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

#Number 43
def make_func_repeater(f, x):
    def repeat(k):
        if k == 0:
            return x
        else:
            return f(repeat(k-1))
    return repeat

#Number 44
def skip_add(n):
    if n <= 0:
        return 0
    return n + skip_add(n - 2)

#Number 45
def summation(n, term):
    assert n >= 1
    if n == 1:
        return term(n)
    return term(n) + summation(n - 1, term)

#Number 46
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

#Number 47
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)

#Number 48
def max_subseq(n, l):
    if n == 0 or l == 0:
        return 0
    with_last = max_subseq(n // 10, l - 1) * 10 + n % 10
    without_last = max_subseq(n // 10, l)
    return max(with_last, without_last)

#Number 49
def can_win(number):
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new = number - action
        if not can_win(new):
            return True
        action += 1
    return False

#Number 50
def pal(n):
    m = n
    while m:
        n, m = n * 10 + m % 10, m // 10
    return n

#nUmber 51
def contains(a, b):
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)

#Number 52
def clear_negatives(lst):
    if not lst:
        return []
    elif lst[0] < 0:
        return clear_negatives(lst[-lst[0]:])
    else:
        return [lst[0]] + clear_negatives(lst[1:])

#Number 53
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

#Number 54
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total

#Number 55
def even_weighted(s):
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

#Number 56
def max_product(s):
    if s == []:
        return 1
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))

#Number 57
def check_hole_number(n):
    if n // 10 == 0:
        return True
    return ((n // 10) % 10) < (n % 10) and ((n // 10) % 10) < ((n // 100) % 10) and check_hole_number(n // 100)

#Number 58
def check_mountain_number(n):
    def helper(x, is_increasing):
        if x // 10 == 0:
            return True
        if is_increasing and (x % 10) < ((x // 10) % 10):
            return helper(x // 10, is_increasing)
        return (x % 10) > ((x // 10) % 10) and helper(x // 10, False)
    return helper(n, True)

#Number 59
def map_mut(f, L):
    for i in range(len(L)):
        L[i] = f(L[i])

#Number 60
def merge_list(s1, s2):
    if s2 == []:
        return s1
    elif s1 == []:
        return s2
    elif s1[0] < s2[0]:
        return merge_list(s1[0] + merge(s1[1:], s2))
    else:
        return merge_list(s2[0] + merge(s1, s2[1:]))

#Number 61
def mario_number(level):
    def ways(n):
        if n == len(level) - 1:
            return 1
        if n >= len(level) or level[n] == 'P':
            return ways(n + 1) + ways(n + 2)
    return ways(0)

#Number 62
def couple(lst1, lst2):
    assert len(lst1) == len(lst2)
    return [[lst1[i], lst2[i]] for i in range(0, len(lst1))]

#Number 63
def add_this_many(x, el, lst):
    i = 0
    for element in lst:
        if element == x:
            i += 1
    while i > 0:
        lst.append(el)
        i -= 1

#Number 64
def group_by(s, fn):
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped:
            grouped[key].append(e)
        else:
            grouped[key] = [e]
        return grouped

#Number 65
def partition_options(total, biggest):
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total - biggest, biggest)
        without_biggest = partition_options(total, biggest - 1)
        with_biggest = [[biggest] + elem for elem in with_biggest]
        return with_biggest + without_biggest

def minimum(s, key):
    if not s:
        return None
    m = s[0]
    for v in s[1:]:
        if key(v) < key(m):
            m = v
    return m

def tightest(bounds, t):
    return minimum([b for b in bounds if t > b(0) and t < b(1)], lambda b: [abs(t - x) for x in b][0])

#Number 66
def make_adder_inc(n):
    def make_helper(x):
        nonlocal n
        value = n + x
        n += 1
        return value
    return make_helper

#Number 67
def make_fib():
    x = 0
    y = 1
    def fib_helper():
        nonlocal x, y
        next_value = x
        x, y = y, x + y
        return next_value
    return fib_helper

#Number 68
def make_sassy_function(f, msg):
    sassy = True
    def helper(x):
        nonlocal sassy
        sassy = not sassy
        if sassy:
            return msg
        return f(x)
    return helper

#Number 69
def sentence_buffer():
    sentence = ''
    def sentence_helper(x):
        nonlocal sentence
        sentence += x + ' '
        if x[-1] == '.':
            result, sentence = sentence, ''
            return result.strip()
    return sentence_helper

#Number 70
def scale(it, multiplier):
    for i in it:
        i = i * multiplier
        yield i

#Number 71
def memory(n):
    def mem(f):
        nonlocal n
        n = f(n)
        return n
    return mem

#Number 72
def nonlocalist():
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i -1)
    return prepend, lambda x: get(x)

#Number 73
def merge(a, b):
    first_a, first_b = next(a), next(b)
    while True:
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)
def sequence(start, step):
    while True:
        yield start
        start += step

#Number 74
def generate_subsets():
    subset = [[]]
    n = 1
    while True:
        yield subset
        subset = subset + [s + [n] for s in subsets]
        n += 1

#Number 75
def sum_paths_gen(t):
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for s in sum_paths_gen(b):
            yield s + label(t)

#Number76
def collect_words(t):
    if is_leaf(t):
        return [label(t)]
    words = []
    for b in branches(t):
        words += [label(t) + word for word in collect_words(b)]
    return words

#Number 77
def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
        return True

#Number 78
def largest_product_path(tree):
    if tree == None:
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        for t in branches(tree):
            paths = [largest_product_path(t)]
            return label(tree) * max(paths)

#Number 79
def max_tree(t):
    if is_leaf(t):
        return tree(root(t))
    else:
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max([root(t)] + [root(s) for s in new_branches])
        return tree(new_label, new_branches)

#number 80
def level_order(tree):
    if not tree:
        return []
    curr, next = [label(tree)], [tree]
    while next:
        find_next = []
        for b in next:
            find_next.extend(branches(b))
        next = find_next
        curr.extend([label(t) for t in next])
    return curr

#Number 81
def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        paths =[]
        for b in branches(t):
            for path in all_paths(b):
                paths = paths.append([label(t)] + path)
        return paths

#Number 82
def make_max_finder():
    finder = 0
    def function(list):
        nonlocal finder
        if max(list) > finder:
            finder = max(list)
        return finder
    return function

#Number 83
def generate_constant(x):
    while True:
        yield x
#Number 84
def black_hole(seq, trap):
    for i in seq:
        if i == trap:
            yield from generate_constant(trap)
        yield i

#Number 84
def gen_inf(lst):
    while True:
        for i in lst:
            yield i

#Number 85
def naturals():
    i = 1
    while True:
        yield i
        i += 1
def filter(iterable, fn):
    for i in iterable:
        if fn(i):
            yield i

#Number 86
def tree_sequence(t):
    yield label(t)
    for b in branches(t):
        for value in tree_sequence(b):
            yield value

#Number 87
def make_digit_getter(n):
    total = 0
    def get_next():
        nonlocal n, total
        if n == 0:
            return total
        i = n % 10
        n //= 10
        total += i
        return i
    return get_next

#number 88
class VendingMachine:
    def __init__(self, name, balance, price):
        self.name = name
        self.balance = 0
        self.price = price
        self.stock = 0
    def add_funds(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}'.format(amount)
        else:
            self.balance += amount
            return 'Current balance: {0}'.format(self.balance)
    def restock(self, amount):
        self.stock += amount
        return 'Current {0} stock: {1}'.format(self.name, self.stock)
    def vend(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. '
        difference = self.price - self.balance
        if difference > 0:
            return 'You must add ${0} more funds. '.format(difference)
        message = 'Here is your {0}.format(self.name)'
        if difference != 0:
            message += ' and ${0} change'.format(-difference)
        self.balance = 0
        self.stock -= 1
        return message + '.'

#Number 89
def preorder(t):
    if is_leaf(t):
        return [label(t)]
    tree = []
    for b in branches(t):
        tree += preorder(b)
    return [label(t)] + tree

#Number 90
def store_digits(n):
    result = Link.empty
    while n > 0:
        result = Link(n % 10, result)
        n //= 10
    return result

#Number 91
def tops(t):
    if t.is_leaf():
        yield t.label
    else:
        for b in t.branches:
            if t.label < b.label:
                yield from tops(b)
#Number 92
def generate(t, value):
    if t.label == value:
        yield [value]
    for b in branches(t):
        for val in generate(b, value):
            yield [t.label] + val

#Number 93
class Mint:
    current_year = 2020
    def __init__(self):
        self.update()
    def create(self, kind):
        return kind(self.year)
    def update(self):
        self.year = Mint.current_year
class Coin:
    def __init__(self, year):
        self.year = year
    def worth(self):
        return self.cents + max(0, Mint.current_year - self.year - 50)
class Nickel(Coin):
    cents = 5
class Dime(Coin):
    cents = 10

#Number 94
def remove_all(link, value):
    if link is Link.empty or link.rest is Link.empty:
        return
    if link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    else:
        remove_all(link.rest, value)

#Number 95
def deep_map(f, link):
    if link is Link.empty:
        return link
    if isinstance(link.first, Link):
        first = deep_map(f, link.first)
    else:
        first = f(link.first)
    return Link(first, deep_map(f, link.rest))

#Number 96
class Card(object):
    cardtype = 'Staff'
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    def power(self, other_card):
        return self.attack - self.defense / 2
class Player(object):
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]
    def draw(self):
        assert not self.deck.is_empty()
        self.hand.append(self.deck.draw())
    def play(self, card_index):
        return self.hand.pop(card_index)

#Number 97
def link_to_list(link):
    new_list = []
    while link is not Link.empty:
        new_list.append(link.first)
        link = link.rest
    return new_list

def link_to_list(link):
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

#Number 98
def cummulative_mul(t):
    for b in branches(t):
        cummulative_mul(b)
    total = t.label
    for b in branches(t):
        total *= b.label
    t.label = total

#Number 99
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
class Server:
    def __init__(self):
        self.clients = {}
    def send(self, email):
        client = self.clients(email.recipient_name)
        client.receive(email)
    def register_client(self, client, client_name):
        self.clients[client_name] = client
class Client:
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        self.server.register_client(self, self.name)
    def compose(self, msg, recipient_name):
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)
    def receive(self, email):
        self.inbox.append(email)

#Number 100
def sum_nums(lnk):
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

#number 101
def multiply_lnks(lst_of_lnks):
    multiply = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rest))

#Number 102
def filter_link(link, f):
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

#Number 103
def filter_no_iter(link, f):
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)

#Number 104
class User:
    def __init__(self, identifier):
        self.identifier = identifier
    def attend(self, meeting):
        if self.identifier in [meeting.waiting, meeting.enlisted]:
            print(self.identifier, 'is already attending')
        else:
            users = meeting.waiting
            if self.identifier == meeting.host:
                users = meetings.enlisted.append(self.identifier)
            users.append(self.identifier)
    def __repr__(self):
        return 'User(' + repr(self.identifier) +')'
class Meeting:
    def __init__(self, host):
        self.waiting = []
        self.enlisted = []
        self.host = host
    def admit(self, f):
        for x in self.waiting:
            if f(x):
                self.enlisted.append(x)
        self.waiting = self.waiting.remove(self.identifier)

#Number 105
def mystery(t):
    def e(r, y):
        assert type(r.label) == int
        myst = [e(b, max(y, r.label)) for b in r.branches]
        if r.label > y:
            myst.append(r.label)
        return sum(myst)
    return e(t, 0)
#Number 106
def multiples(k, n):
    if k < n:
        for jay in multiples(k, n - k):
            yield n
        yield k
