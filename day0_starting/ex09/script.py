from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0

# pip uninstall ft_package
# rm -rf dist build ft_package.egg-info
# python3 -m build
# pip install ./dist/ft_package-0.0.1-py3-none-any.whl