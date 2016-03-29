import operator
import time
from socket import gethostname
__author__ = 'braydenrw'


class ApocCount:
    def __init__(self):
        self.wordcount = {}
        self.sorted_words = {}
        self.n = 37

    @staticmethod
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return ApocCount().fib(n-1) + ApocCount().fib(n-2)

    def main(self):
        start_time = time.time()
        f = open("/Users/braydenrw/PycharmProjects/WordCount/apoc.txt", "r+")
        for word in f.read().split():
            if word not in self.wordcount:
                self.wordcount[word] = 1
            else:
                self.wordcount[word] += 1
        f.close()

        ApocCount().fib(self.n)

        self.sorted_words = sorted(self.wordcount.items(), key=operator.itemgetter(1), reverse=True)

        # f = open("log.txt", "a")
        print "Apoc with fib 37 on " + gethostname()
        i = 0
        for item in self.sorted_words:
            s = str(item)
            s = s.replace('(', '')
            print s.replace(')', '')
            i += 1
            if i == 10:
                break
        print "--- %s seconds ---\n" % (time.time() - start_time)
        # f.close()

if __name__ == '__main__':
    ApocCount().main()
