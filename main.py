from subprocess import Popen

subprocesses = []

for i in range(10):
    subprocesses.append(Popen(
        ["venv/Scripts/python.exe", f"send.py", f"{i}"]
    ))
for el in subprocesses:
    el.wait()
