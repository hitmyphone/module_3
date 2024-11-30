calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    print(len(string))
    print(tuple_)
    count_calls()
def is_contains(stroka,spisok):
    count_calls()
    spisok1 = []
    for i in spisok:
        i = i.upper()
        spisok1.append(i)
    if stroka.upper() in spisok1:
        print(True)
    else:
        print(False)

string_info("derevo")
is_contains("LeArnInG", ["I", "am", "learning"])
string_info("overed")
is_contains("Am", ["I", "am", "learning"])
print(calls)

