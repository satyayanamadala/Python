name = "Satya"
full_name = 'YANAMADALA SATYANARAYA'
about_Me = '''I’m currently pursuing my B.Tech in Computer Science and
 Engineering with a specialization in Artificial Intelligence and Machine Learning at 
 SRM Institute of Science and Technology. I have great ambition in the field of AI and technology, 
 using data to help innovate and solve real-world problems.
'''
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5])    Here the string index is out of range
print("I'am",name)
print(full_name)
print(about_Me)

#STRING SLICING
color = "yellow"
color1 = "light,blue"
print(len(color))  #calculate the length of the str -6
print(color[:])  #prints -yellow
print(color1[:6]) #prints -light,
print(color1[:-1]) #prints -light,blu
print(color[-3:-1]) #prints -lo
print(color[-1:-3]) #there will be no output

# Iterable vs Iterator
nums = [1, 2, 3]        # iterable
it = iter(nums)         # iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
