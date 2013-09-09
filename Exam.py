__author__ = 'dmitrijdackov'

def unique(a, b, c):
    return a != b and a != c and b != c

print (unique(1, 2, 3))

print (unique(1, 0, 1))

print (unique(7, 7, 7))

#Prefix Removal

#Define a procedure, remove_prefix, that takes as input a string, and returns a
#string that is the part of the string following the first hyphen -. If the input string does
#not contain any hyphen -, remove_prefix should return the full input string.

def remove_prefix(s):
    index = s.find('-')
    if index == -1:
        return s
    return s[index + 1:]

print (remove_prefix('super-udacity'))
#>>> 'udacity'

print (remove_prefix('counter-counter-intelligence'))
#>>> 'counter-intelligence'

print (remove_prefix('antigravity'))
#>>> 'antigravity'

#Collatz Returns!

#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz_steps(n):
    count = 0

    if n == 1:
        return count

    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

        count += 1
    return count

#For example,

print (collatz_steps(1))
#>>> 0

print (collatz_steps(2))
#>>> 1

print (collatz_steps(6))
#>>> 8

print (collatz_steps(101))
#>>> 25

#List Explosion

#Define a procedure, explode_list, that takes as inputs a list and a number, n.
#It should return a list which contains each of the elements of the input list,
#in the original order, but repeated n times.

def explode_list(p, n):
    list = []
    if not n:
        return list
    for num in p:
        for idx in range(n):
            list.append(num)
    return list

#For example,

print (explode_list([1, 2, 3], 2))
#>>> [1, 1, 2, 2, 3, 3]

print (explode_list([1, 0, 1], 0))
#>>> []

print (explode_list(["super"], 5))
#>>> ["super", "super", "super", "super", "super"]

#Reverse Index


#Define a procedure, reverse_index, that takes as input a Dictionary, and
#returns a new Dictionary where the keys are the values in the input dictionary.
#The value associated with a key in the result is a list of all the keys in the
#input dictionary that match this value (in any order).

def reverse_index(dict):
    res = {}
    for key, value in dict.items():
        if not value in res:
            res[value] = []
        res[value].append(key)
    return res

#For example,

winners_by_year = {
    1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
    1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
    1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
    1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
    1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }

wins_by_country = reverse_index(winners_by_year)

print (wins_by_country['Brazil'])
#>>> [1958, 2002, 1970, 1994, 1962]

print (wins_by_country['England'])
#>>> [1966]

#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)

def same_structure(a, b):
    if not is_list(a) and not is_list(b):
        return True

    if not is_list(a) or not is_list(b):
        return False

    if len(a) != len(b):
        return False

    for idx in range(len(a)):
        if not same_structure(a[idx], b[idx]):
            return False

    return True

#Here are some examples:

print (same_structure(3, 7))
#>>> True

print (same_structure([1, 0, 1], [2, 1, 2]))
#>>> True

print (same_structure([1, [0], 1], [2, 5, 3]))
#>>> False

print (same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]]))
#>>> True

print (same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]]))
#>>> False

print ("Graph")

#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


def reachable(graph, node):
    graph2 = graph.copy()
    list = [node]

    if not node in graph2:
        return list

    for item in graph2[node]:
        if not item in list:
            list.append(item)

    graph2.pop(node)

    for node in list:
        lst = reachable(graph2, node)
        for item in lst:
            if not item in list:
                list.append(item)

    return list

#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print (reachable(graph, 'a'))
#>>> ['a', 'c', 'd', 'b']

print (reachable(graph, 'd'))
#>>> ['d', 'a', 'c', 'b']

print (reachable(graph, 'e'))
#>>> ['e', 'a', 'c', 'd', 'b']

#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    if not len(s):
        return len(t)
    if not len(t):
        return len(s)

    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])
    else:
        return min(
            1 + edit_distance(s[1:], t[1:]),
            1 + edit_distance(s, t[1:]),
            1 + edit_distance(s[1:], t))


#For example:

# Delete the 'a'
print (edit_distance('audacity', 'udacity'))
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print (edit_distance('audacity', 'Udacity'))
#>>> 2

# Five replacements
print (edit_distance('peter', 'sarah'))
#>>> 5

# One deletion
print (edit_distance('pete', 'peter'))
#>>> 1


#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.


def multi_lookup(index, keywords):
    if not keywords:
        return []
    activepos = lookup(index, keywords[0])
    for keyword in keywords[1:]:
        newactivepos = []
        nexturlpos = lookup(index, keyword)
        if nexturlpos:
            for pos in activepos:
                if [pos[0], pos[1] + 1] in nexturlpos:
                    newactivepos.append([pos[0], pos[1] + 1])
        activepos = newactivepos

    result = []
    for pos in activepos:
        result.append(pos[0])
    return result


def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    position = 0
    for word in words:
        add_to_index(index, word, [url, position])
        position += 1

def add_to_index(index, keyword, url_position):
    if keyword in index:
        index[keyword].append(url_position)
    else:
        index[keyword] = [url_position]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

cache = {
    'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""",
    'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""",
    'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""",
    }

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print("Page not in cache: " + url)
        return None


#Here are a few examples from the test site:

index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')

print(multi_lookup(index, ['Python']))
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print(multi_lookup(index, ['Monty', 'Python']))
#>>> ['http://www.udacity.com/cs101x/final/a.html']

print(multi_lookup(index, ['Python', 'programming', 'language']))
#>>> ['http://www.udacity.com/cs101x/final/b.html']

print(multi_lookup(index, ['Thomas', 'Jefferson']))
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print(multi_lookup(index, ['most', 'powerful', 'weapon']))
#>>> ['http://www.udacity.com/cs101x/final/a.html']




