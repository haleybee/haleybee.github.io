domain = 'http://walsbr.com/'
pages = ['about', 'blog', 'pedagogy', 'projects', 'cv']
domain_names = []


for thing in pages:
        url = domain + thing
        domain_names.append(url)

print(domain_names)

#Comprehension version:
#url = [domain + page for page in pages]
