# importing the date class datetime module
from datetime import date

#import module to access content directory
import os

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


blog_posts = [

    {
        "filename": "blog/1.html","date": "September 3rd, 2020","title": "Another post",
    },
    {
        "filename": "blog/2.html","date": "November 10th, 2020","title": "Yet Another post",
    },
    {
        "filename": "blog/3.html","date": "December 14th, 2020","title": "Razer 15 review",
    },

]

new_list = os.listdir("blog/")
print(new_list)

# add the unique title to that page

def entitle_base(page_title, nav_added_base):

    # Read in the base template header and footer page elements
    base = nav_added_base
    
    entitled_base = nav_added_base.replace("{{title}}", page_title)
    return entitled_base



# smush the content in between the base page header and footer 

def write_output_file(copyrighted_base, content_html, output_page):

    # Read in the base template header and footer page elements
    base_page = copyrighted_base

    content = open(content_html).read()

    # Use the string replace 
    full_page = base_page.replace("{{content}}", content)
    
    print("writing file", content_html)
    return open(output_page, "w+").write(full_page)


# write in current copyright year

def copyright_year(entitled_base):
    # creating the date object of today's date
    current_date = date.today()
    
    copyrighted_base = entitled_base.replace("{{year}}", str(current_date.year))
    return copyrighted_base


# generate nav links automatically 
# if param === pages[filename], + inline styling of pages[title]

def auto_links(current_page_title):

    # Read in the base template header and footer page elements
    base = open("templates/base.html").read()

    nav_links_html = ''

    for page in pages:
        nav_links_html = nav_links_html + '<a class="p-2 text-muted" href="'

        # replace the first instance of the directory path "content" with empty string
        nav_links_html += page['filename'].replace("content/", "", 1)
        nav_links_html += '"'
        if current_page_title == page["title"]:
            nav_links_html += 'style="text-decoration: none;background-color: #4a4864;"'
        nav_links_html += '>'
        nav_links_html += page['title']
        nav_links_html += '</a>'
        nav_added_base = base.replace('{{navlinks}}', nav_links_html)

    return nav_added_base


def blog_posts():
    # main function
    print("Building blog posts")


    # Get the page elements from the new list using a loop
    for post in blog_posts:

        title = post["title"]
       
        content = post["filename"]

        print('Getting', title, 'file...', content, '...')

        # # add navbar links
        # nav_added_base = auto_links(title)
        
        # # call the function to write in the page title
        # entitled_base = entitle_base(title, nav_added_base)

        # # call the function to write in the copyright year
        # copyrighted_base = copyright_year(entitled_base)

        # #call the func to write in the main content
        # write_output_file(copyrighted_base, content, page["output"])



def main():
    # main function
    print("Hello, your static site generator is runnin'")


    # Get the page elements from the new list using a loop
    for page in pages:

        # TODO add blog_posts, if blog then use blog title? or, call blog func outside later?

        title = page["title"]
       
        content = page["filename"]

        print('Getting', title, 'file...', content, '...')

        # add navbar links
        nav_added_base = auto_links(title)
        
        # call the function to write in the page title
        entitled_base = entitle_base(title, nav_added_base)

        # call the function to write in the copyright year
        copyrighted_base = copyright_year(entitled_base)

        #call the func to write in the main content
        write_output_file(copyrighted_base, content, page["output"])


    print("hey, I ran successfully up to the end")
    
main()
