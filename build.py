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

def content_sandwich(name_of_page, output_page):

    # Read in the base template header and footer page elements
    base = open("templates/base.html").read()

    content = open(name_of_page).read()

    # Use the string replace 
    full_page = base.replace("{{content}}", content)
    
    print("writing file", name_of_page)
    return open(output_page, "w+").write(full_page)



def main():
    # main function
    print("Hello, your static site generator is runnin'")


    # Get the page elements from the new list using a loop
    for page in pages:

        print('Gettin\'', page["title"], 'file...', page["filename"], '...')
       
        content = page["filename"]

        # # Use the string replace 
        # full_page = base.replace("{{content}}", content)
        
        # print("writing file", page["output"])
        # open(page["output"], "w+").write(full_page)
        content_sandwich(content, page["output"])
        


    print("hey, I ran successfully up to the end")
    
main()
