try:
  import sympy as sp, numpy as np, math
except Exception as e:
  print(f"E in module. '?>sympy<, numpy, math'\n{e}")

def calc(inp):
  x = sp.symbols('x')
  result = eval(inp, {'sp': sp, 'np': np, 'math': math})
  if isinstance(result, (sp.Expr, np.ndarray)):
    return result
  else:
    return print(f"Hasil: {result}")

def func_main():
  while True:
    try:
      math_commands = input("calc\033[36m > \033[0m").replace('\\ln', '\n').replace('exit()', '')
      if "exit" in math_commands:
        break
      else:
        calc(math_commands)
    except KeyboardInterrupt:
      print("\nExit."); break
    except EOFError:
      print("\nExit."); break
    except Exception as e:
      print(f"ERROR cacl!\n\033[31m{e}\033[0m"); continue

func_main()