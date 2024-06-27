def printer(index):
    try:
        return "Hello"
    except:
        return "Fail"
    finally:
        return print(printer(index+1))

print(printer(0))

