import cv2
import numpy as np

def load_image(image_path):
    try:
        image = cv2.imread(image_path)
        return image
    except Exception as e:
        print("Ошибка при загрузке изображения:", e)
        return None

def getNumber():
    while True:
        getNumber = input("Ввод: ")
        if getNumber.isdigit():
            return getNumber
        else:
            print("Некорректный выбор. Попробуйте снова.")

def display_image(image, window_name):
    cv2.imshow(window_name, image)

def show_channel(image, channel):
    b, g, r = cv2.split(image)
    if channel == 'red':
        channel_image = r
    elif channel == 'green':
        channel_image = g
    elif channel == 'blue':
        channel_image = b
    display_image(channel_image, 'Channel Image')

def add_border(image, border_size):
    bordered_image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    display_image(bordered_image, 'Bordered Image')

def gray_scale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray_image, 'Gray Image')

def draw_line(image, start_point, end_point, thickness):
    line_color = (0, 255, 0)
    line_image = cv2.line(image, start_point, end_point, line_color, thickness)
    display_image(line_image, 'Line Image')


def capture_from_webcam():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cap.release()
        return frame


def main_menu():
    print("Выберите действие:")
    print("1. Загрузить изображение")
    print("2. Сделать снимок с веб-камеры")
    choice = getNumber()
    return choice

def uniq_menu():
    print("Выберите действие:")
    print("1. Добавить границы")
    print("2. Получить изображение в оттенках серого")
    print("3. Нарисовать линию на изображении зелёным цветом")
    choice = getNumber()
    return choice


while True:
    choice = main_menu()

    if choice == '1':
        while True:
            image_path = input("Введите название изображения: ")
            image = load_image(image_path)
            if image is not None:
                print("Изображение найдено")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
        

    elif choice == '2':
        image = capture_from_webcam()

    else:
        print("Некорректный выбор. Попробуйте снова.")

    if image is not None:
        display_image(image, 'Loaded Image')
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

        while True:
            choice = input("Введите канал (r/g/b): ")
            if choice == 'r':
                show_channel(image, 'red')
                cv2.waitKey(3000)
                break
            elif choice == 'g':
                show_channel(image, 'green')
                cv2.waitKey(3000)
                break
            elif choice == 'b':
                show_channel(image, 'blue')
                cv2.waitKey(3000)
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
        cv2.destroyAllWindows()
        while True:
            choice = uniq_menu()
            if choice == '1':
                print("Введите размер рамки. ")
                border_size = int(getNumber())
                add_border(image, border_size)
                cv2.waitKey(3000)
                cv2.destroyAllWindows()
            elif choice == '2':
                gray_scale(image)
                cv2.waitKey(3000)
                cv2.destroyAllWindows()
            elif choice == '3':
                print("Введите x координату 1 точки: ")
                x1 = int(getNumber())
                print("Введите y координату 1 точки: ")
                y1 = int(getNumber())
                print("Введите x координату 2 точки: ")
                x2 = int(getNumber())
                print("Введите y координату 2 точки: ")
                y2 = int(getNumber())
                start_point = (x1, y1)
                end_point = (x2, y2)
                print("Введите толщину линии: ")
                thickness = int(getNumber())
                draw_line(image, start_point, end_point, thickness)
                cv2.waitKey(3000)
                cv2.destroyAllWindows()
            else:
                print("Некорректный выбор. Попробуйте снова.")
