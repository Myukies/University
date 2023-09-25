def project_along(b, a):
    sigma = (b*a)/(a*a) if a*a > 1e-20 else 0
    return(sigma * a)

def project_orthogonal(b, a):
    return b - project_along(b, a)

a = int(input("Enter Value: "))
b = int(input("Enter Value: "))

print(project_along(a,b))
print(project_orthogonal(a,b))
