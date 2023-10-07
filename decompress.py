def main():
    code = ""
    text = ""
    pos = None
    length = None
    symbol = None
    codes = []
    j=0
    while j<100:
     code = input()
     if code=='':
         break
     codes.append(code)
     i = 0
     while i<len(code):
          if code[i-1]=='<':
             pos = code[i]
             if code[i+1]==',':
                length = code[i+2]
          if code[i]=='>':
             if ord(code[i-1])>=0 and ord(code[i-1])<=9:
                 length = code[i-1]
             else:
                 symbol = code[i-1]
          i += 1
     if pos=='0':
         text+=symbol
     else:
         y = len(text)
         x=y-int(pos)
         for i in range (x,x+int(length)):
           text+= text[i]
         if symbol!= 'l':
             text+=symbol
     j += 1
    print(text)




if __name__ == "__main__":
    main()
