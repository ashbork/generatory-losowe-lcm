from livereload import Server, shell

server = Server()


filetypes = ["*.bib", "*.yml", "*.ipynb"]

for filetype in filetypes:
    server.watch(filetype, shell("jupyter-book build ."))

server.serve(root="_build/html")
