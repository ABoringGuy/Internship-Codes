import ast
import pprint
code = '''
def greet(name):
    print("Hello, " + name + "!")

greet("John")
'''
tree = ast.parse(code)
pprint.pprint(ast.dump(tree, indent=2))