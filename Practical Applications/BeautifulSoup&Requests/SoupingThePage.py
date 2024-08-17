from bs4 import BeautifulSoup as bs  # importing the required libraries
import requests

# Extract the title from the webpage

url = 'https://parthasarathy27.github.io/frontend-development-tutorial/Event%20Management%20HTML%20Project/starter/event.html'
req = requests.get(url)

soup = bs(req.content, 'html.parser')
print(soup)

# Extract all the URLs within a webpage

for link in soup.find_all('a'):
    print(f'Link from the webside : {link.get('href')}')
  
# output:

'''
<!DOCTYPE html>

<html>
<head>
<title>Events</title>
<link href="img/date.png" rel="icon"/>
</head>
<body bgcolor="#020111" style="color: white;">
<center>
<h1>Upcoming Events📅</h1>
<p>
                Don't miss any of your important events. Stay Updated
            </p>
</center>
<hr/>
<p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex cum mollitia, libero vitae reiciendis commodi velit minima laboriosam alias voluptatem omnis? Quae unde beatae officia sint ex in ratione. Laborum nemo praesentium cum dignissimos culpa, voluptatibus inventore expedita. Repellat pariatur aut placeat et velit vero, soluta excepturi! Aliquid, incidunt velit dolorum quam impedit delectus deleniti voluptatem quisquam eos pariatur. Recusandae itaque sit temporibus aspernatur! Rem delectus recusandae sapiente, maxime repellendus sit explicabo est illo ex consequatur nostrum quos, laudantium sed. Debitis vero enim vel dolore repellendus eaque! Reiciendis explicabo cupiditate nemo ipsum exercitationem ad odio quam laboriosam corrupti, nisi ipsam!
        </p>
<center>
<img alt="event1.png" src="img/event1.png"/>
<h1>Photo Gallery</h1>
<h2>Free Entry | Free Food | Pets are Not allowed</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore minus saepe numquam placeat officiis adipisci tempore, aliquam, dolorem accusantium nam pariatur dolores neque rem quaerat iste consequatur ullam sint aliquid, doloribus nisi aut molestias reprehenderit? Eius excepturi laudantium veritatis cum odit. Quae itaque rerum adipisci consequuntur fuga deserunt? Quasi, quo?</p>
</center>
<center>
<img src="img/event2.png"/>
<h1>
<button>
<a href="https://www.myntra.com/">Fashion Store</a>
</button>
</h1>
<h2>Free Entry | Free Food | Pets are Not allowed</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore minus saepe numquam placeat officiis adipisci tempore, aliquam, dolorem accusantium nam pariatur dolores neque rem quaerat iste consequatur ullam sint aliquid, doloribus nisi aut molestias reprehenderit? Eius excepturi laudantium veritatis cum odit. Quae itaque rerum adipisci consequuntur fuga deserunt? Quasi, quo?</p>
</center>
<hr/>
<center>
<h1>Contact</h1>
<h2>+91 9871984399 | Event@gamil.com</h2>
<p> 9th rajabakery street, chennai - 11</p>
</center>
</body>
</html>
Link from the webside : https://www.myntra.com/
'''
