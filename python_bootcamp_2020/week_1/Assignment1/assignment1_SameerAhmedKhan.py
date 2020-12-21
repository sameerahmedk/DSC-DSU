def diagonal():
    name: str = (input("Name is: "))

    # diagonal print
    print('Diagonally, it becomes: ')
    for i in range(len(name)):
        print(' ' * i + name[i])

    print()
    # reverse diagonal print
    print('Reverse diagonally, it becomes: ')
    for i in range(len(name)):
        print(' ' * i + name[-i - 1])


def student_rec():
    student_record = {
                         "roll_num": [],
                         "name": [],
                         "age": [],
                         "marks": []
                     }, \
                     {
                         "roll_num": [],
                         "name": [],
                         "age": [],
                         "marks": []
                     }, \
                     {
                         "roll_num": [],
                         "name": [],
                         "age": [],
                         "marks": []
                     }, \
                     {
                         "roll_num": [],
                         "name": [],
                         "age": [],
                         "marks": []
                     }, \
                     {
                         "roll_num": [],
                         "name": [],
                         "age": [],
                         "marks": []
                     }
    highest = 0
    lowest = 100
    total = 0
    for i in range(5):
        student_record[i]["roll_num"] = (input("Enter roll number of Student %d: " % i))
        student_record[i]["name"] = (input("Enter name of Student %d: " % i))
        student_record[i]["age"] = (input("Enter age of Student %d: " % i))
        student_record[i]["marks"] = (input("Enter marks of Student %d: " % i))
        total = + int(student_record[i]["marks"])
        if int(student_record[i]["marks"]) > highest:
            highest = int(student_record[i]["marks"])
        if int(student_record[i]["marks"]) < lowest:
            lowest = int(student_record[i]["marks"])

    print('Class average is: ', total / 5)
    print('Class highest is: ', highest)
    print('Class lowest is: ', lowest)


def lyrics():
    song = '''
    Najaane kab se
    Umeedain kuch baqi hain
    Mujhe phir bhi teri yaad
    Kyun ati hai?
    Najaane kab se
    Durr jitna bhi tum mujhse
    Paas tere main
    Ab toh aadat si hai mujhko aise jeene main
    Zindagi se koi shikva bhi nahi hai
    Ab toh zinda hun main iss neele asmaan main
    Chaahat aisi hai yeh teri
    Barhti jaye
    Aahat aise hai yeh teri mujhko sataye
    Yaadain gehri hain itni
    Dil doob jaye
    Aur aankhon main yeh ghum num ban jaye
    Ab toh aadat si hai mujhko aise jeene main
    Yeh jo raatain hain
    Yeh jo baatain hain
    Sabhi raatain hain
    Bhula do unhain
    Mitta do unhain
    Ab toh aadat si hai mujhko'''

    import time
    a = song.split('\n')
    for x in range(len(a)):
        print(a[x])
        time.sleep(1)


def main():
    diagonal()
    student_rec()
    lyrics()


if __name__ == '__main__':
    main()
