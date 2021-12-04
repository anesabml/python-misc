def doubleitt(fn):
    def func(*args):
        return fn(*args) + ', ' + fn(*args)
    return func

# @documenter("DOH!")
@doubleitt
@doubleitt
def homer():
    return "D'oh"

def main():
    print homer()

if __name__ == "__main__":
    main()