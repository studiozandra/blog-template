print("Hello, your static site generator is runnin'")



# Combining page elements header (top), content (middle) and footer (bottom)
top = open("templates/top.html").read()
middle = open("content/index.html").read()
bottom = open("templates/bottom.html").read()
full_index = top + middle + bottom
open("docs/index.html", "w+").write(full_index)

top_about = open("templates/top_about.html").read()
middle_about = open("content/about.html").read()
full_about = top_about + middle_about + bottom
open("docs/about.html", "w+").write(full_about)

top_contact = open("templates/top_contact.html").read()
middle_contact = open("content/contact.html").read()
full_contact = top_contact + middle_contact + bottom
open("docs/contact.html", "w+").write(full_contact)

top_design = open("templates/top_design.html").read()
middle_design = open("content/design.html").read()
full_design = top_design + middle_design + bottom
open("docs/design.html", "w+").write(full_design)

top_technology = open("templates/top_technology.html").read()
middle_technology = open("content/technology.html").read()
full_technology = top_technology + middle_technology + bottom
open("docs/technology.html", "w+").write(full_technology)

print("hey, I ran successfully up to the end")