import Server.MServer as MS
import Client.MClient as MC

def main():
  ms = MS()
  print(ms.test())
  mc = MC()
  print(mc.test())
  

if __name__=="__main__":
  main()
