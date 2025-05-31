from bs4 import BeautifulSoup


with open("home.html", "r") as f:
    content = f.read()

    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all("div", class_="card") 
    courses = [{"title": course.h5.text, "desc": course.p.text, "price": course.a.text.split()[-1]} for course in course_cards]
    
    for course in courses:
        print(f"{course["title"]}: {course["price"]}")