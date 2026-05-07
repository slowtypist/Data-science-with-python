r = open("lakshman.txt", 'x')
r.write("mai laksham")
r.close() #here in the second run it gives error as x is only exeecuted once and creates le only once and then doesnt do anything in the existing file 