def beer(bottles):
    if bottles == 0:
      print( "No more Bottles")
      return 
    sentence = f"{bottles} bottles on the wall, take one down, {bottles - 1} bottles on the wall"
    print(sentence)
    beer(bottles - 1)
    return 

print(beer(4))