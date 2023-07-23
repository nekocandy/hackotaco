from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title("GG!")

show_pages(
    [
        Page("./pages/home.py", "Home", "🏠"),
        Page("./pages/bento.py", "Hello", "👋"),
        Page("./pages/user_data.py", "User Data", "👽"),
        Page("./pages/display.py", "View", "📊"),
        Page("./pages/mkd.py", "Emergency MD Editor", "📝"),
        Page("./pages/vd.py", "Educational Resources", "💻"),
        Page("./pages/mentors.py", "Mentor", "👨‍🏫"),
        Section("Teams"),
        Page("./pages/teams/create.py", "Create", "👨‍💻"),
        Page("./pages/teams/join.py", "Join", "👨‍💻"),
        Page("./pages/teams/list.py", "List", "👨‍💻"),
        Page("./pages/teams/project.py", "Project", "👨‍💻"),
    ]
)

hide_pages(["Project"])
