x = """{
  "tests": [
    {
      "name": "Test1",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "Ana",
      "output": "'Ana' comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    },
    {
      "name": "Test2",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "árbol",
      "output": "'árbol' comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    },
    {
      "name": "Test3",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "Berenjena",
      "output": "'Berenjena' no comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    },
    {
      "name": "Test4",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "Árbol",
      "output": "'Árbol' comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    },
    {
      "name": "Test5",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "androide",
      "output": "'androide' comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    },
    {
      "name": "Test7",
      "setup": "",
      "run": "LANG=en_US.utf8 timeout 3m python3 comienza_con_a.py",
      "input": "123",
      "output": "'123' no comienza con 'A'",
      "comparison": "included",
      "timeout": 1,
      "points": 1
    }
  ]
}
"""
print(len(x))
print(x[930:950])
