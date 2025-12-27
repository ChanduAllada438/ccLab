html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello from Python</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>This HTML file was generated using Python.</p>
</body>
</html>
"""

# create / overwrite the file
with open("hello.html", "w") as file:
    file.write(html_content)

print("HTML file created: hello.html")
