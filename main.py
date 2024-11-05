import flet as ft
from urllib.parse import urlparse, parse_qs

def main(page):
    # Настройка страницы
    page.title = "Mobile Web App"
    page.scroll = "adaptive"
    
    # Извлечение данных пользователя из URL
    url_data = urlparse(page.url)
    query_params = parse_qs(url_data.query)
    telegram_user_id = query_params.get("user_id", ["Неизвестно"])[0]
    telegram_username = query_params.get("username", ["Неизвестно"])[0]

    # Если данных нет, перенаправляем на страницу интеграции Telegram
    if telegram_user_id == "Неизвестно" or telegram_username == "Неизвестно":
        page.launch_url("/telegram_integration.html")
        return  # Завершаем выполнение, пока пользователь не вернется с данными

    # Функция для навигации по страницам
    def navigate_to(page_name):
        if page_name == "home":
            page.views.clear()
            page.views.append(home_page())
        elif page_name == "income":
            page.views.clear()
            page.views.append(income_page())
        elif page_name == "friends":
            page.views.clear()
            page.views.append(friends_page())
        elif page_name == "wallet":
            page.views.clear()
            page.views.append(wallet_page())
        page.update()

    # Создание навигационной панели
    def navigation_bar():
        return ft.Row(
            [
                ft.TextButton("Главная", on_click=lambda _: navigate_to("home")),
                ft.TextButton("Доход", on_click=lambda _: navigate_to("income")),
                ft.TextButton("Друзья", on_click=lambda _: navigate_to("friends")),
                ft.TextButton("Кошелёк", on_click=lambda _: navigate_to("wallet")),
            ],
            alignment="center",
            expand=True,
        )

    # Главная страница
    def home_page():
        return ft.View(
            controls=[
                ft.CircleAvatar(avatar_url="user_avatar_url", radius=50),
                ft.Text(f"Username: {telegram_username}"),
                ft.Text(f"User ID: {telegram_user_id}"),
                ft.Text("Баланс: Капля"),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Валюта: Ведро"),
                            ft.Button("Играть"),
                        ]
                    ),
                    bgcolor="#E0E0E0",
                    height=100,
                    alignment="center",
                ),
                navigation_bar(),
            ]
        )

    # Страница "Доход"
    def income_page():
        return ft.View(
            controls=[
                ft.Text("Список заданий"),
                navigation_bar(),
            ]
        )

    # Страница "Друзья"
    def friends_page():
        return ft.View(
            controls=[
                ft.Icon(ft.icons.GROUP),
                ft.Text("Приглашай друзей"),
                ft.Text("Капли от друзей"),
                ft.Button("Собрать капли"),
                ft.Text("Получай 10% от друзей и 2,5% от их рефералов"),
                ft.Button("Пригласить друга"),
                navigation_bar(),
            ]
        )

    # Страница "Кошелёк"
    def wallet_page():
        return ft.View(
            controls=[
                ft.Button("Подключить кошелёк"),
                navigation_bar(),
            ]
        )

    # Запуск с главной страницы
    page.views.append(home_page())

# Запуск приложения Flet
ft.app(target=main, view="web_browser", port=8550)
