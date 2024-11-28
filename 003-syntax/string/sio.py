import io
s = "0123456789"

sio = io.StringIO(s)
print(sio)
print(sio.getvalue())
sio.seek(3)
sio.write("abc")
print(sio.getvalue())