from livereload import Server, shell

server = Server()

BUILD_COMMAND = "jupyter-book build ."
OUTPUT_PATH = "_build/html"
CHAPTERS_PATH = "chapters/"

WATCHED_PATHS = ["*.bib", "*.yml", "*.ipynb", "*.md", f"{CHAPTERS_PATH}/*"]

for filetype in WATCHED_PATHS:
    server.watch(filetype, shell(BUILD_COMMAND))

print("Running initial build...")
shell(BUILD_COMMAND)()

server.serve(root=OUTPUT_PATH)
