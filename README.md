# UrlAndStructureCrawler_Grupi11
Zhvillimi i nje GUI aplikacioni i cili mundeson URL dhe structure crawling


## Web Crawling

&nbsp;&nbsp;Një Crawler është një program kompjuterik që automatikisht kërkon dokumente në Web. Crawlers janë programuar kryesisht për veprime të përsëritura në mënyrë që shfletimi të automatizohet. Search engines përdorin crawlers më shpesh për të shfletuar internetin dhe për të ndërtuar një indeks. Crawlers të tjerë kërkojnë lloje të ndryshme informacioni siç janë burimet RSS dhe adresat e postës elektronike. Termi crawler vjen nga Search Engine i parë në internet: Web Crawler. Sinonimet janë gjithashtu "Bot" ose "Spider". Web Crawler më i njohur në internet është Googlebot.

### Parakushtet

&nbsp;&nbsp;Për ekzekutimin e programit, paraprakisht duhet të kemi instaluar libraritë Pillow, bs4, requests, validators. Për instalimin e këtyre librarive duhet të hapni terminalin në direktoriumin e projektit dhe të ekzekutoni komandat si në vijim:
</br>
</br>![Screenshot_4](https://user-images.githubusercontent.com/58752918/107848820-df42a000-6df6-11eb-8907-b345f6afdd45.png)
</br>![Screenshot_5](https://user-images.githubusercontent.com/58752918/107848821-dfdb3680-6df6-11eb-8e23-025481023bf6.png)
</br>![Screenshot_6](https://user-images.githubusercontent.com/58752918/107848822-e073cd00-6df6-11eb-959d-67a4ec8fa3e0.png)
</br>![Screenshot_7](https://user-images.githubusercontent.com/58752918/107848823-e073cd00-6df6-11eb-97a9-f74180f78449.png)


### Ekzekutimi

&nbsp;&nbsp;Programi mund të ekzekutohet duke hapur terminalin ne direktotriumin e projektit dhe duke shkruajtur komandën si në vijim:
</br>
![Screenshot_16](https://user-images.githubusercontent.com/58752918/107850470-0901c400-6e03-11eb-8a3a-a783b3d38dd3.png)
</br>
Poashtu ekzekutimi mund të bëhet edhe duke e bërë run projektin në njërin nga editor-ët që vendosni të përdorni, në rastin e mëposhtëm është përdorur PyCharm:</br>
![Screenshot_17](https://user-images.githubusercontent.com/58752918/107850964-a90d1c80-6e06-11eb-95f4-f43583a418d7.png)


## Testimi i programit

&nbsp;&nbsp;Pas ekzekutimit të programit, do të na shfaqet një dritare e cila do t'i mundësojë përdoruesit të jap një URL dhe të ekzekutojë procesin e Crawling, në vijim janë të paraqitura fotot:
</br>
![Screenshot_9](https://user-images.githubusercontent.com/58752918/107848833-f08bac80-6df6-11eb-821d-5f2d50a9ddca.png)
</br>
Aplikacioni përmban një menubar dhe disa opsione për zgjedhje:
</br>
![Screenshot_11](https://user-images.githubusercontent.com/58752918/107848827-eec1e900-6df6-11eb-8476-a520381a1b56.png)
</br>
Opsioni Scrape paraqet faqen kryesore e cila hapet në momentin e ekzekutimit të programit, opsioni Exit është për daljen mbylljen e dritares.
</br>
Opsioni Help përmban About, në momentin që klikohet About na shfaqet një dritare e cila përmban sqarime rreth Web Crawling.
</br>
![Screenshot_12](https://user-images.githubusercontent.com/58752918/107848828-ef5a7f80-6df6-11eb-9c6b-e07bcfddd8aa.png)
</br>
![Screenshot_13](https://user-images.githubusercontent.com/58752918/107848829-ef5a7f80-6df6-11eb-8d9e-056e90d9af8f.png)
</br>
Në dritaren kryesore nëse tentojmë të lëmë të zbrazët hapsirën ku kërkohet URL-ja na shfaqet një dritare tjetër si më poshtë:
</br>
![Screenshot_18](https://user-images.githubusercontent.com/58752918/107851469-79f8aa00-6e0a-11eb-80a6-6f7097a1dc43.png)</br>
Në rastin kur tentohet të shkruhet dicka që nuk është ne formatin e URL-së përsëri na shfaqet dritarja e mësipërme:
</br>
![Screenshot_20](https://user-images.githubusercontent.com/58752918/107851698-238c6b00-6e0c-11eb-99a8-44165cf659e8.png)
</br>
</br>
Dhe në fund kemi funksionimin e aplikacionit në rastin kur është dhënë një URL valide:
</br>
1. Në rastin e parë është bërë crawl URL-ja https://telegrafi.com/
![Screenshot_15](https://user-images.githubusercontent.com/58752918/107848831-eff31600-6df6-11eb-9066-b7e8c3ca9367.png)</br>
2. Në rastin e dytë është bërë crawl URL-ja http://www.trusti.org/sq/
![Screenshot_14](https://user-images.githubusercontent.com/58752918/107848830-eff31600-6df6-11eb-8ed7-207480507342.png)

## Teknologjia e përdorur

* [Python](https://www.python.org/) - Gjuha programuese
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE

## Referencat

* [Web Crawler](https://www.sciencedaily.com/terms/web_crawler.htm#:~:text=A%20web%20crawler%20(also%20known,up%2Dto%2Ddate%20data. )
* [Python Web Crawlers](https://opensource.com/resources/python/web-scraper-crawler)
* [Python GUI Programming](https://www.tutorialspoint.com/python/python_gui_programming.htm#:~:text=Tkinter%20is%20the%20standard%20GUI,to%20the%20Tk%20GUI%20toolkit.&text=Import%20the%20Tkinter%20module.)
* [Python Tutorials](https://pythonspot.com/)




