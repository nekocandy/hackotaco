from st_pages import Page, show_pages, add_page_title

add_page_title("GG!")

show_pages(
    [
        Page("./page/home.py", "Home", "🏠"),
        Page("./page/hello.py", "Hello", "👋"),
        Page("./page/user_data.py", "User Data", "👤"),
    ]
)
