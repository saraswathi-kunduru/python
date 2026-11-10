def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    x = input("Enter text: ")
    print(convert(x))

main()