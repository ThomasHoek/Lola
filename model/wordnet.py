from typing import IO, Any
import os


# load data
dir_path: str = os.path.dirname(os.path.realpath(__file__))

# convert dict
wn_s_file: IO[Any] = open(f"{dir_path}/../WNProlog/wn_s.pl", encoding="utf-8")
wn_s: list[str] = [x.rstrip() for x in wn_s_file.readlines()]
wn_s_dict: dict[str, str] = dict()
for x in wn_s:
    wn_s_dict[x.split("'")[1]] = x.split("'")[3]
wn_s_file.close()

for i in ["wn_ant", "wn_der", "wn_hyp", "wn_sim"]:
    wn_read_file: IO[Any] = open(f"{dir_path}/../WNProlog/{i}.pl", encoding="utf-8")
    read_str: list[str] = [x.rstrip() for x in wn_read_file.readlines()]
    wn_data: list[tuple[str, str]] = [(x.split("'")[1], x.split("'")[3]) for x in read_str]
    wn_read_file.close()

    wn_file_write: IO[Any] = open(f"{dir_path}/../WNtxt/{i}.txt", encoding="utf-8", mode="w+")
    word1: str
    word2: str
    for line in wn_data:
        word1, word2 = line
        wn_file_write.write(f"{wn_s_dict[word1]} , {wn_s_dict[word2]}\n")
    wn_file_write.close()
