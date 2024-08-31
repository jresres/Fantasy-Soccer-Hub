from fasthtml.common import *
from LeaderboardPage import LeaderboardSection
from NavigationBar import NavBarSection

# Loading tailwind and daisyui
tlink = Script(src="https://cdn.tailwindcss.com"),
dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")

app = FastHTML(hdrs=(tlink, dlink, picolink))

@app.get("/")
def homepage():
    title = "Fantasy Soccer Hub"

    return (
            Title(title), 
            Main(
                NavBarSection(),
                LeaderboardSection()
            )
            )

serve()