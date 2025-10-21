# Lambda Function VS Normal Function

# Normal func
def sum(x,y):
    print(x+y)

sum(10,5)

# lambda i like an annonymous function
sum = lambda x,y:x+y
print(sum(20,20))

# Maximum of two numbers : Check which number is bigger
max = lambda x,y : x if x > y else y
print("Max",max(10, 14))

# Reversed string with lambda
rev = lambda x: x[::-1]
print("Reversed string:",rev("Python"))


# Working with pre defined function:
# Map
# Question 1
def sum(x):
    return x * x

sum_result = list(map(sum, [1,2,3,4,5]))
print(sum_result)

# With lambda
sum_result_With_lambda = list(map(lambda x:x+x, [2,4,6,8,10]))
print(sum_result_With_lambda)


# Question 2
names = ["Ali Khan", "Sara Ahmed", "Bilal Qureshi", "Hina Fatima", "Ahmed Raza"]
# Without lambda
def modify(n):
    splited = n.split(' ')
    return f'{splited[0][0]}.{splited[1][0]}'
        
newNames = list(map(modify,names))
print(newNames)

# With lambda
newNames = list(map(lambda n:n.split(' ')[0][0] + "."+ n.split(' ')[1][0],names))
print(newNames)


# Question 3
names = ["  ali khan ", "sara   ahmed", "  bilal qureshi", "hina FATIMA  ", "  ahmed  raza "]
# with lambda 
cleaned = list(map(lambda x:x.strip().title(),names))
print(cleaned)



