# Genome Inversions Calculator 🧬
🇷🇺 Этот файл на русском языке. For English version see [README_EN.md](./README_EN.md)

Genome Inversions Calculator это веб-приложение на Python/Flask для вычисления минимального количества инверсий между перестроенными хромосомами разных организмов. Вдохновлено ранее доступным GRIMM (TEsler, G. GRIMM: Genome Rearrangements Web Server. Bioinformatics 2002, 18, 492–493). Инструмент прошел государственную регистрацию как результат моей интеллектуальной деятельности и зарегистрирован под номером №2021688591 в Федеральной службе по интеллектуальной собственности.

## 🚀 Как запустить локально?
#### 1. Клонируйте репозиторий
```bash
git clone https://github.com/janesable/gic.git
cd gic
```
#### 2. Установите зависимости
```bash
pip install -r requirements.txt
```
#### 3. Запустите приложение
```bash
python app.py
```
#### 4. Откройте в браузере
http://127.0.0.1:5000

## 💻 Как пользоваться?
#### 1. Введите названия и последовательности синтенных блоков геномов (в виде простых чисел, например: 1 -3 2 5 4). Отрицательное число будет означать, что синтенный блок имеет обратный порядок генов.
#### 2. Нажмите Count.
#### 3. Приложение отобразит все шаги инверсий и минимальное количество преобразований.
#### 4. Можно добавлять/удалять геномы по кнопке, если хотите проследить изменения более чем у двух видов.

## 📁 Структура проекта
```bash
genomic-inversion-calculator/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Web-интерфейс
├── ├── static/
│   └── style.css           # Стили
├── requirements.txt        # Список библиотек
└── README.md               # Этот файл
```

## 🧠 О проекте
Разработано с научной любовью ❤️ для анализа структурных перестроек в геномах (в моем случае геномах малярийных комаров).
Если вы используете инструмент в своей статье — будет приятно, если упомянете автора 😌

## 📬 Обратная связь
Если нашли баг или хотите предложить фичу — пишите в тг @janesable или как взрослые на почту: jane.sable.me@gmail.com
