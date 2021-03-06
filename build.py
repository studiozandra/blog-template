# importing the date class datetime module
from datetime import date

#import modules to access content directory files
import glob
import os

pages = [
    # {
    #     "filename": "content/about.html",
    #     "output": "docs/about.html",
    #     "title": "About",
    # },
    # {
    #     "filename": "content/design.html",
    #     "output": "docs/design.html",
    #     "title": "Design",
    # },
    # {
    #     "filename": "content/blog.html",
    #     "output": "docs/blog.html",
    #     "title": "Blog",
    # },
    # {
    #     "filename": "content/index.html",
    #     "output": "docs/index.html",
    #     "title": "Home",
    # },
    # {
    #     "filename": "content/contact.html",
    #     "output": "docs/contact.html",
    #     "title": "Contact",
    # },

]


blog_posts = [

    {
        "filename": "blog/1.html",
        "date": "September 3rd, 2020",
        "title": "Another post",
        "output": "docs/1.html",
    },
    {
        "filename": "blog/2.html",
        "date": "November 10th, 2020",
        "title": "Yet Another post",
        "output": "docs/2.html",
    },
    {
        "filename": "blog/3.html",
        "date": "December 14th, 2020",
        "title": "Razer 15 review",
        "output": "docs/3.html",
    },
    

]
# get list of all html files in 'content' folder
all_html_files = glob.glob("content/*.html")



# get list of files in 'blog' folder
blog_folder_files = os.listdir("blog/")



# list up just the above page filenames
page_filename_list = ''

for page in pages:
    page_filename_list += page['filename']




# list up just the above blog post filenames
posts_filename_list = ''

for post in blog_posts:
    posts_filename_list += post['filename']


# using angle brackets as starting point, strip the tags and return only the title text
# (passing in the line which contains the header class)

def strip_title_tags(html_ele):
    clean_title = ''
    started = False
    for char in html_ele:
        if (char == ">" and started == False):
            started = True
        if (char == "<" and started == True):
            started = False
        if (started == True and (char not in ["<",">","/","\n"])):
            clean_title += char
    return clean_title    



# check if any new pages exist in the content folder that are not hardcoded in above list
def check_for_new_pages():
    print("checking for new content...")
    for page in all_html_files:
        if (page in page_filename_list):
            print ("page Exists", page)
        else:
            print("it's new content, dawg", page)
            file_path = page
            file_name = os.path.basename(file_path)
            print(file_name, "file_name")
            name_only, extension = os.path.splitext(file_name)
            print(name_only, "name_only")
            file = open(page)
            for line in file:
                if ("display-4" in line):
                    tagline = strip_title_tags(line)
                    pages.append({ "filename": "content/" + file_name, "output": "docs/" + file_name, "title": name_only, "tagline": tagline  })





# check if any new blog posts exist in the blog folder that are not listed above
def check_for_new_posts():
    for b_file in blog_folder_files:
        if (b_file in posts_filename_list):
            print ("Element Exists", b_file)
        else:
            print("issa new post, dawg", b_file)
            file = open("blog/" + b_file)
            for line in file:
                if ("blog-post-title" in line):
                    new_title = strip_title_tags(line)
                    blog_posts.append({ "filename": "blog/" + b_file, "date": "today", "title": new_title, "output": "docs/" + b_file })




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

    if len(content_html) > 300:
        content = content_html
    else:
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




# generate blog post archive links list (aside on content/blog.html and blg base template)

def auto_blog_post_links(title):

    # Read in the base page
    if title == 'blog':
        blog_base = open("content/blog.html").read()
    else:
        blog_base = auto_links(title, 'post', 'posts')

    blog_links_html = ''
    

    for post in blog_posts:
        blog_links_html += '<li><a href="'
        # remove old path by replacing the first instance of the directory path "blog" with empty string
        blog_links_html += post['filename'].replace("blog/", "", 1)
        blog_links_html += '"'
        blog_links_html += '>'
        blog_links_html += post['title']
        blog_links_html += '</a></li>'
        archive_added_base = blog_base.replace('{{blog-links}}', blog_links_html)
        
    
    # return content to be sandwiched
    return archive_added_base
    



# generate nav links automatically 
# if param 1 == pages[filename], + inline styling of pages[title] to show active link
# if param 2 (items) == posts , func works for blog posts. if param 2 == pages 

def auto_links(current_page_title, item, items):

    # Read in the base template header and footer page elements
    if items == 'posts':
        base = open("templates/blog_base.html").read()
    else:
        base = open("templates/base.html").read()


    nav_links_html = ''

    for page in pages:
        nav_links_html = nav_links_html + '<a class="p-2 text-muted" href="'

        # remove old path by replacing the first instance of the directory path "content" with empty string
        nav_links_html += page['filename'].replace("content/", "", 1)
        nav_links_html += '"'

        # if the current 'main' loop iteration page matches the auto links loop, change link color
        if current_page_title == page['title']:
            nav_links_html += 'style="text-decoration: none;background-color: #4a4864;"'
        nav_links_html += '>'

        # make navigation links lowercase
        nav_links_html += page['title'].lower()
        nav_links_html += '</a>'
        nav_added_base = base.replace('{{navlinks}}', nav_links_html)

    return nav_added_base




def build_blog_posts():
    # main function
    print("Building blog posts")


    # Get the page elements from the new list using a loop
    for post in blog_posts:

        title = post["title"]
       
        content = post["filename"]

        print('Getting', title, 'file...', content, '...')

        # add navbar links
        nav_added_base = auto_blog_post_links(title)
        
        # call the function to write in the page title
        entitled_base = entitle_base(title, nav_added_base)

        # call the function to write in the copyright year
        copyrighted_base = copyright_year(entitled_base)

        #call the func to write in the main content
        write_output_file(copyrighted_base, content, post["output"])



def main():
    # main function
    print("Hello, your static site generator is runnin'")

    check_for_new_pages()

    check_for_new_posts()

    build_blog_posts()

    # Get the page elements from the new list using a loop
    for page in pages:

        title = page["title"]

        content = page["filename"]

        print('Getting', title, 'file...', content, '...')

        # add navbar links
        nav_added_base = auto_links(title, 'page', 'pages')
        
        # call the function to write in the page title
        entitled_base = entitle_base(title, nav_added_base)

        # call the function to write in the copyright year
        copyrighted_base = copyright_year(entitled_base)

        # call the func to generate and add the blog links sidebar

        if page["title"] == "blog":
            content = auto_blog_post_links(page["title"])


        #call the func to write in the main content
        write_output_file(copyrighted_base, content, page["output"])


    print("hey, I ran successfully up to the end")



# invoke the main function, avoid conflicts with other modules called "main"
    
if __name__ == "__main__":
    main()
