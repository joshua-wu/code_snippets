#coding=utf-8
import os
import pickle


def process_display(now, total, prefix='', gap=1000):
    """display a process in number"""
    if now % gap == 0:
        # print ""
        print(prefix, "{:0.2f}%".format(now / total * 100), end='\r')


def vec_to_string(ids, sep=" "):
    return sep.join([str(x) for x in ids])


def test_or_create_dir(file_name):
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))


def save_var(var, out_path):
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
    file = open(out_path, "wb")
    pickle.dump(var, file)
    file.close()


def load_var(in_path):
    if os.path.exists(in_path):
        file = open(in_path, "rb")
        var = pickle.load(file)
        file.close()
        return var
    else:
        return None
