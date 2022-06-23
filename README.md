# Python Bazel
- Very simple repository

* How to run:

1. Clone the repository:
    - git clone https://github.com/victor-s-santos/very_simple_python_bazel.git

2. Make sure you have bazel installed, if not, just run:
    - npm -g @bazel/bazelisk

3. Test the Calculator methods:
    - bazel test projects/calculator/...

4. Run flask server:
    - bazel run projects/python_app/...

5. Build the entery project:
    - bazel build //...