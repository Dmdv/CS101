__author__ = 'Dyachkov'

#Define a procedure, add_to_index,
#that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already
#in the index, add the url
#to the list of urls associated
#with that keyword.

#If the keyword is not in the index,
#add an entry to the index: [keyword,[url]]

#Define a procedure, lookup,
#that takes two inputs:

#   - an index
#   - keyword

#The output should be a list
#of the urls associated
#with the keyword. If the keyword
#is not in the index, the output
#should be an empty list.

#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.

#lookup(index,'udacity') => ['http://udacity.com','http://npr.org']
#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

from Unit3.webcrawler2 import get_all_links, get_page, union
from Unit4.ListExt import removeEmpty

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
index = []

def lookup(index, keyword):
    """
    Returns url by keyword
    """
    for pair in index:
        if pair[0] == keyword:
            return pair[1]
    return []

def add_to_index2(index, keyword, url):
    """
    This adds url to index
    """
    for pair in index:
        if pair[0] == keyword:
            array = pair[1]
            array.append(url)
            return
    index.append([keyword, [url]])

def add_to_index(index, keyword, url):
    """
    This adds url only if urls doesn't exist.
    """
    for entry in index:
        if entry[0] == keyword:
            if not url in entry[1]:
                entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])


def add_page_to_index(index,url,content):
    """
    Indexes page
    """
    strings = content.split()
    for word in strings:
        add_to_index(index, word, url)

def crawl_web(seed):
    """
    Returns index
    """
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop() # this is url
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            links = get_all_links(content)
            union(tocrawl, links)
            crawled.append(page)
    return index

def split_string(source,splitlist):
    """
    Split strings, less optimal
    """
    array = source.split(splitlist[0])
    array = removeEmpty(array)

    output = array

    for i in range(1, len(splitlist)):
        out = []

        for str in output:

            value = str.split(splitlist[i])
            value = removeEmpty(value)

            for item in value:
                out.append(item)

        output = out

    return output

def split_string2(source, splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print (index) # => [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

out = split_string("This is a test-of the,string separation-code!", " ,!-")
print(out)
out = split_string2("This is a test-of the,string separation-code!", " ,!-")
print(out)
out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
out = split_string2("After  the flood   ...  all the colors came out.", " .")
print(out)