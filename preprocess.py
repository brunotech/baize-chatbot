import pickle
import json
import sys
import os

data_name = str(sys.argv[1])

if not os.path.exists("data"):
    os.makedirs("data")

data = []
for i in range(100):
    try:
        temp = pickle.load(open(f"collected_data/{data_name}_chat_{i}.pkl", "rb"))
    except:
        continue
    for topic in temp:
        x = temp[topic]
        x = x.split("[Human]")[1:-1]
        if len(x) != 0:
            s = ""
            for y in x:
                if "[AI]" not in y:
                    break
                y = y.split("[AI]")
                if len(y) == 2:
                    s += f"[|Human|] {y[0].strip()}" + "\n" + "[|AI|] " + y[1].strip() + "\n"
                else:
                    break
            if s != "":
                prompt = "The conversation between human and AI assistant.\n"
                s = prompt + s + "[|Human|] "

                data.append({"topic": topic, "input": s})

json.dump(data, open(f"data/{data_name}_chat_data.json", "w"))
