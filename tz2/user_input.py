import sys


def proccess_command(userInput):
    userInput = userInput.replace(' ', '')
    if len(userInput) >= 1:
        if userInput[0].isdigit():
            result = process_range(userInput)
        else:
            process_action(userInput)
            result = None
    else:
        result = None

    return result


def process_range(userInput):
    userInput = userInput.split(',')
    result = []
    for i in userInput:
        if '-' in i:
            start, end = i.split('-')
            start = int(start)
            end = int(end)
            if start > end:
                raise ValueError
            else:
                for r in range(start, end+1):
                    result.append(r)
        else:
            result.append(i)

    return list(set(result))


def process_action(userInput):
    if userInput == 'exit' or userInput == 'quit':
        sys.exit()
    elif userInput == 'next':
        # go and download next page
        pass
