import sys
def main():
    verbose = False
    try:
        user = sys.argv[1]
        try:
            verbose = True if sys.argv[2] else False
        except IndexError:
            pass
    except IndexError:
        user = 'root'
    print(user, verbose)

main()
