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


# add the unique title to that page

def entitle_base(page_title):

    # Read in the base template header and footer page elements
    base = open("templates/base.html").read()
    
    entitled_base = base.replace("{{title}}", page_title)
    return entitled_base



# smush the content in between the base page header and footer 

def content_sandwich(entitled_base, content_html, output_page):

    # Read in the base template header and footer page elements
    base_page = entitled_base

    content = open(content_html).read()

    # Use the string replace 
    full_page = base_page.replace("{{content}}", content)
    
    print("writing file", content_html)
    return open(output_page, "w+").write(full_page)




def main():
    # main function
    print("Hello, your static site generator is runnin'")


    # Get the page elements from the new list using a loop
    for page in pages:

        title = page["title"]
       
        content = page["filename"]

        print('Getting', title, 'file...', content, '...')
        
        entitled_base = entitle_base(title)
        content_sandwich(entitled_base, content, page["output"])


    print("hey, I ran successfully up to the end")
    
main()
