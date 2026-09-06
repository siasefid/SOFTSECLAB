import ast
import operator


class Calculator:
    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def calc(self, expression: str) -> str:
        try:
            tree = ast.parse(expression, mode="eval")
            result = self._evaluate(tree.body)
            return str(result)
        except Exception as exc:
            raise ValueError("Invalid expression") from exc

    def _evaluate(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numbers are allowed")

        if isinstance(node, ast.BinOp):
            operation = self.OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Operator not allowed")

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            return operation(left, right)

        raise ValueError("Expression not allowed")