def space():
    print()

def even (start, end):
    num = []

    for i in range(start, end + 1):
        if i % 2 == 0:
            num.append(i)
            
    return num

def odd (start, end):
    num = []

    for i in range(start, end + 1):
        if i % 2 != 0:
            num.append(i)
            
    return num

def save_history (history, start, end, choose, result):
    history.append({
        "start": start,
        "end": end,
        "type": choose,
        "result": result
    })

def show_history(history):
    if not history:
        print("No previous information saved")
        return

    for i, item in enumerate (history, start = 1):
        print(f"{i} Range: {item["start"]} - {item["end"]}")
        print(f" Type: {item["type"]}")
        print(f" Result: {item["result"]}")