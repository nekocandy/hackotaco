from st_pages import Page, show_pages, add_page_title

add_page_title("GG!")

show_pages(
    [
        Page("./pages/home.py", "Home", "🏠"),
        Page("./pages/hello.py", "Hello", "👋"),
        Page("./pages/user_data.py", "User Data", "👽"),
        Page("./pages/display.py", "View", "📊"),
    ]
)
