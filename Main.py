import Server.MServer as MS
import Client.MClient as MC

def main():
  print("main called")
  ms = MS.MServer()
  print(ms.test())
  mc = MC.MClient()
  print(mc.test())
  

if __name__=="__main__":
  main()
