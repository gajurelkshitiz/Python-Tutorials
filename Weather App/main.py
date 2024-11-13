import sys
from PyQt5.QtWidgets import (QApplication, QLineEdit, QPushButton, QWidget,
                             QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt
import requests


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Show Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.setStyleSheet("""
                        QLabel, QPushButton{
                            font-family : calibri;
                        }
                        QLabel#city_label{
                            font-size : 50px;
                        }    
                        QLineEdit#city_input{
                            font-size : 35px;
                        }
                        QPushButton#get_weather_button{
                            background-color : hsl(191, 59%, 86%);
                            font-size : 25px;
                            font-weight : bold;
                            border-radius : 20px;
                        }
                        QLabel#temperature_label{
                            font-size : 50px;
                        } 
                        QLabel#emoji_label{
                            font-size : 80px;
                            font-family : segoe UI emoji;
                        } 
                        QLabel#description_label{
                            font-size : 40px;
                        }   
                        
                    """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        api_key = "f6a83cd085bc600410bf18484ba8028e"
        city = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        try: 
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data['cod'] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError:
            value = 5
            match value:
                case 1:
                    pass
                case 2:
                    pass
                
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized\nInvalid API Key.")
                case 403:
                    self.display_error("Forbidden\nAccess is Denied.")
                case 404:
                    self.display_error("Not Found\nCity Not Found.")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later.")
                case 501:
                    self.display_error("Bad Gateway\nInvalid Response from the server.")
                case 503:
                    self.display_error("Service Unavailable\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout\nNo response from server.")
                case _:
                    self.display_error(f"HTTP Error: {response.status_code}")
        
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error.\nCheck your internet connection.")
        
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error.\nThe request timed out.")
        
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects.\nCheck the URL.")
        
        except requests.exceptions.RequestException as req_error:            # exception due to network problems, invalid urls...
            self.display_error(f"Request Error\n{req_error}")
            
        
        
        
        
    
    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("font-size : 25px;"
                                             "color : red;")
        self.emoji_label.clear()
        self.description_label.clear()
    
    def display_weather(self, data):
        print(data)
        self.temperature_label.setStyleSheet("font-size : 50px;")
        
        temp_kelvin = data['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['main']
        
        
        self.temperature_label.setText(f"{temp_celcius:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
      
    @staticmethod  
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return"⛈️"
        elif 300 <= weather_id <= 321:
            return "⛅"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "🌥️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
