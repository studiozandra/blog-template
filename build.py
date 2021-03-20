pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About",
    },
    {
        "filename": "content/design.html",
        "output": "docs/design.html",
        "title": "Design",
    },
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Blog",
    },
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact",
    },
]
# loop through this list and pull out differnt things at diff times


def main():
    # main function
    print("Hello, your static site generator is runnin'")


    # Read in the base template header and footer page elements
    base = open("templates/base.html").read()

    

    # Get the page elements from the new list using a loop
    for page in pages:

        print('Gettin\'', page["title"], 'file...', page["filename"], '...')
       
        content = open(page["filename"]).read()

        # Use the string replace 
        full_page = base.replace("{{content}}", content)
        
        print("writing file", page["output"])
        open(page["output"], "w+").write(full_page)
        


    print("hey, I ran successfully up to the end")
    
main()
