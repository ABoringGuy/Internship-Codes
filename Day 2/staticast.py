import ast

class FunctionCallVisitor(ast.NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            args = [arg for arg in node.args if isinstance(arg, ast.Str)]
            if args:
                print("Detected print statements with string literals:")
                for arg in args:
                    print(arg.s)  # Print the string literal directly
        self.generic_visit(node)

def perform_static_analysis(code):
    tree = ast.parse(code)
    visitor = FunctionCallVisitor()
    visitor.visit(tree)


def main():
    code = '''
def calculate_average(numbers):
        total = sum(numbers)
        average = total / len(numbers)
        print("Average:", average)

data = [1, 2, 3, 4, 5]
calculate_average(data)
print("End of program")
    '''
    perform_static_analysis(code)

main()