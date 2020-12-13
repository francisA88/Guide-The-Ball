from distutils.core import setup, Extension

def main():
    setup(name="main",
          version="1.0.0",
          description="Guide The Ball shared library compiled",
          author="Francis Ali",
          author_email="francisali693@gmail.com",
          ext_modules=[Extension("main", ["main.c"]), Extension("dbOps", ["dbOps.c"]), Extension("gamelogic",['gamelogic.c'])],
    )

if __name__ == "__main__":
    main()