import pickle

with open('8872_tor.pickle', 'rb') as f:
    info = pickle.load(f)
    print(len(info), len(info[0]))
    print(info[0])
