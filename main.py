from st_pages import Page, Section, hide_pages, show_pages

show_pages(
    [
        Page("./pages/landing.py", "Landing", "🏠"),
        Page("./pages/bento.py", "Hello", "👋"),
        Page("./pages/user_data.py", "User Data", "👽"),
        Page("./pages/vd.py", "Educational Resources", "💻"),
        Page("./pages/mentors.py", "Mentor", "👨‍🏫"),
        Section("Teams", icon="👨‍💻"),
        Page("./pages/teams/create.py", "Create", "👨‍💻"),
        Page("./pages/teams/join.py", "Join", "👨‍💻"),
        Page("./pages/teams/list.py", "List", "👨‍💻"),
        Page("./pages/teams/project.py", "Project", "👨‍💻"),
        Page("./pages/display.py", "View", "📊", in_section=False),
        Page("./pages/mkd.py", "Emergency MD Editor", "📝"),
    ]
)

hide_pages(["Project"])
