from flask import Flask  # Import flask
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='')  # Setup the Flask app by creating an instance of Flask

@app.route('/<string:user_id>')
def home(user_id):
    title = 'title_' + user_id
    description = 'description_' + user_id
    banner = 'http://banner/' + user_id + '.png'
    
    HtmlFile = open('static/index.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 

    soup = BeautifulSoup(source_code)
    
    # title
    metatag = soup.new_tag('title')
    metatag.append(title)
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'title'
    metatag.attrs['content'] = title
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'og:title'
    metatag.attrs['content'] = title
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'twitter:title'
    metatag.attrs['content'] = title
    soup.head.append(metatag)
    
    # description
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'description'
    metatag.attrs['content'] = description
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'og:description'
    metatag.attrs['content'] = description
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'twitter:description'
    metatag.attrs['content'] = description
    soup.head.append(metatag)
    
    # image
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'og:image'
    metatag.attrs['content'] = banner
    soup.head.append(metatag)
    
    metatag = soup.new_tag('meta')
    metatag.attrs['property'] = 'twitter:image'
    metatag.attrs['content'] = banner
    soup.head.append(metatag)
    
    print(soup.prettify())
    
    return soup.prettify()

if __name__ == '__main__':  # If the script that was run is this script (we have not been imported)
    app.run()  # Start the server