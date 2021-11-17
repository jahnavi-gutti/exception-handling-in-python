try:
    n=input()
    num=int(n)
    n=input()
    den=int(n)
    k=num/den
except:
    print("error")
else:
    print(k)
finally:
    print("this divion reslt")
"""
4
2
2.0
this divion reslt"""
"""
5
0
error
this divion reslt"""
