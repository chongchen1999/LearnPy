import pickle

with open("data/data", "wb") as f:
    o1 = "hello world"
    o2 = 4567890
    o3 = [1, 2, 3]
    pickle.dump(o1, f)
    pickle.dump(o2, f)
    pickle.dump(o3, f)

with open("data/data", "rb") as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))