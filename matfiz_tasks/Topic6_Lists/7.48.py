vector_a = list(map(float, input("Vector A: ").split()))
vector_b = list(map(float, input("Vector B: ").split()))

vector_a, vector_b = vector_b, vector_a

print("\n" + '-'*50 + "\nModified:")
print("Vector A:", vector_a)
print("Vector B:", vector_b)

# - task 2
print("\n" + '='*50)
print("Vector A before:", vector_a)
vector_a = vector_a[::-1]
print("Vector A after:", vector_a)
