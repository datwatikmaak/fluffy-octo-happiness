def generate_affiliation_link(url):
    aff_link = url.split("/")
    http = aff_link[0].replace("https", "http")
    num = aff_link[5]
    return f"{http}//www.amazon.com/dp/{num}/?tag=pyb0f-20"
