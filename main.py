from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title("GG!")

show_pages(
    [
        Page("./page/home.py", "Home", "🏠"),
        Page("./page/bento.py", "Hello", "👋"),
        Page("./page/user_data.py", "User Data", "👽"),
        Page("./page/display.py", "View", "📊"),
        Page("./page/vd.py", "Educational Resources", "💻"),
        Page("./page/mentors.py", "Mentor", "👨‍🏫"),
        Section("Teams", icon="👨‍💻"),
        Page("./page/teams/create.py", "Create", "👨‍💻"),
        Page("./page/teams/join.py", "Join", "👨‍💻"),
        Page("./page/teams/list.py", "List", "👨‍💻"),
        Page("./page/teams/project.py", "Project", "👨‍💻"),
        Page("./page/mkd.py", "Emergency MD Editor", "📝", in_section=False),
    ]
)

hide_pages(["Project"])
