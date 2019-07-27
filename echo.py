import socket

HOST = ''
PORT = 80

def listen():

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  s.listen(1)
  
  while True:
    conn, addr = s.accept()

    try:
      print 'Connected by', addr
      while True: 
        data = conn.recv(2048)
        if not data:
          break
        conn.sendall(data)

    finally:
      conn.close() 

listen()
