def echo():
    received = yield "Ready to receive"
    while True:
        received = yield f"Received: {received}"

gen = echo()
print(next(gen))
print(gen.send("Hello"))
print(gen.send("World"))