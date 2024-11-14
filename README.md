Some tests of kdtree.

[Test Description](./task.md)

To check a program with small tests, run:

```sh
chmod +x test_small.sh
chmod +x test_medium.sh
./test_small.sh A 2000
./test_medium.sh A 200
```

To compare two programs:

```sh
chmod +x gen_max_random.py
python time_compare.py A B -C gen_max_random.py (or any other executable generator) [-T] [-OP]
```