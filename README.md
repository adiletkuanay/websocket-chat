# Websocket Chat Application
<p align="center">
<a href="https://pypi.python.org/pypi/asgiref" rel="nofollow"><img alt="https://img.shields.io/pypi/v/asgiref.svg" src="https://pypi-camo.freetls.fastly.net/b580a7dbf8bcb1bcd74cd585a8009440b9877573/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f617367697265662e737667"></a>
<a href="https://pypi.python.org/pypi/channels" rel="nofollow"><img alt="https://img.shields.io/pypi/v/channels.svg" src="https://pypi-camo.freetls.fastly.net/b0143993a12af4e0e1e373afd2ca2b08b2eded4c/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6368616e6e656c732e737667"></a>
</p>
This is a simple websocket chat application built using Django and Channels. It allows users to join chat rooms and communicate with each other in real-time using websockets.


## 🌟 Features
- Real-time chat functionality using websockets
- Multiple chat rooms with unique URLs
- User authentication and authorization
- Simple and intuitive user interface
- Dockerized for easy deployment

## 🚀 Usage instructions
1. Clone the repository:
  ```py
git clone <repository_url>
```
2. Navigate into the project directory:
```py
cd websocketchat
```
3. Install dependencies:
```py
pip install -r requirements.txt
```
4. Apply database migrations:
```py
python manage.py migrate
```
5. Run the development server:
```py
python manage.py runserver
```
