��          �      <      �     �  �  �    �  7   �  2     6   ?  �   v     H     U     ]     a  
   m     x     �     �     �     �  �  �  )   L  �  v  `  _  r   �  j   3  j   �  ;  	     E     X     s  #   v     �     �  
   �  #   �  #   �                                                          
                          	                      Advanced options Between 0.1 and 99.0. This field is supported by some search engines and defines the delay between successive crawler accesses in seconds. If the crawler rate is a problem for your server, you can set the delay up to 5 or 10 or a comfortable value for your server, but it's suggested to start with small values (0.5-1), and increase as needed to an acceptable value for your server. Larger delay values add more delay between successive crawl accesses and decrease the maximum crawl rate to your web server. Case-sensitive. A missing trailing slash does also match to files which start with the name of the pattern, e.g., '/admin' matches /admin.html too. Some major search engines allow an asterisk (*) as a wildcard and a dollar sign ($) to match the end of the URL, e.g., '/*.jpg$'. Please specify at least one allowed or dissallowed URL. The URLs which are allowed to be accessed by bots. The URLs which are not allowed to be accessed by bots. This should be a user agent string like 'Googlebot'. Enter an asterisk (*) for all user agents. For a full list look at the <a target=_blank href='http://www.robotstxt.org/db.html'> database of Web Robots</a>. URL patterns allowed and crawl delay disallowed pattern robot rule rules url Project-Id-Version: django-robots
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2011-02-08 12:09+0100
PO-Revision-Date: 2011-12-07 13:14+0000
Last-Translator: Jannis <jannis@leidel.info>
Language-Team: LANGUAGE <LL@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: ru
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)
 Расширенные настройки Введите значение между 0.1 и 99.0. Этот параметр поддерживается некоторыми поисковыми системами и определяет задержку в секундах до следующего запроса робота. Если робот обнаруживает проблемы на вашем сервер, вы можите установить задержку от 5, 10 или более подходяще значение для вашего сервера, но лучше начинать с небольших значений (0.5-1), и постепенно увеличивать до достижения оптимальных значений для вашего сервера.  Большие значения увеличивают время выгрузки роботом вашего сайта и могут отрицательно влиять на ваш рейтинг в данной системе. Внимание: учитывается регистр!<br />Если в конце пропущен слэш, то под шаблон попадут все файлы, путь к которым начинается с таких же символов. Например: под шаблон "/admin" так же попадет "/admin.html".<br />Часть поисковых систем понимают звездочку (*) как произвольное количество любых символов и знак доллара ($) как символ конца URL. Например: "/*.jpg$" Укажите как минимум один URL-адрес (неважно разрешенный или нет) URL адреса разрешенные для индексации поисковыми роботами. URL-адреса запрещенные для индексации поисковыми роботами. Название робота (User agent). Введите звездочку (*) для применения правил ко всем роботов. Полный список можно посмотреть в <a target=_blank href='http://www.robotstxt.org/db.html'>базе данных веб-ботов</a>. Шаблоны URL разрешенные URL и частота обновления запрещенные URL шаблон робот правило индексации правила индексации URL-адрес 