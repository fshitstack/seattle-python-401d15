import root
from package_a import module_a_a, module_a_b
from package_b import module_b_a, module_b_b

bio = "I am module a in package a"

if __name__ == "__main__":
    print(bio)
    print(root.bio)
    print(module_a_a.bio)
    print(module_a_b.bio)
    print(module_b_a.bio)
    print(module_b_b.bio)
