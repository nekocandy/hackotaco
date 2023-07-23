from st_pages import Page, Section, show_pages, add_page_title

add_page_title("GG!")

show_pages(
    [
        Page("./pages/home.py", "Home", "🏠"),
        Page("./pages/hello.py", "Hello", "👋"),
        Page("./pages/user_data.py", "User Data", "👽"),
        Page("./pages/display.py", "View", "📊"),
        Page("./pages/mkd.py", "Editor", "📝"),
        Section("Teams"),
        Page("./pages/teams/create.py", "Create", "👨‍💻"),
        Page("./pages/teams/list.py", "List", "👨‍💻"),
        Page("./pages/bento.py", "AltProf", "👤"),
        Page("./pages/vd.py", "Educational Resources", "💻"),
    ]
)
